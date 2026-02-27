from fastapi import FastAPI, HTTPException, Depends
import uvicorn
from database import engine, SessionLocal
from models import Base, User, Game, Quest, UserQuest
from schemas import (
    UserCreate,
    UserOut,
    UserLogin,
    QuestOut,
    QuestOutDaily,
    GameOut,
    CompletedQuest,
    CompletedGame,
    ChangeUsername, 
    ChangeEmail, 
    ChangePassword,
    DeleteUserRequest
)
from sqlalchemy.orm import Session
import uuid
from utils import add_xp_and_update_level, remove_xp_and_update_level
from datetime import datetime
from passlib.context import CryptContext
from auth import create_access_token, get_current_user
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from fastapi.middleware.cors import CORSMiddleware

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "API Working"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registro")
def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    user_exist = db.query(User).filter(User.email == user.email).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="Email já está registado")

    username_exist = db.query(User).filter(User.username == user.username).first()
    if username_exist:
        raise HTTPException(status_code=400, detail="Username já está usado")

    novo_user = User(
        userid=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        passencrypt=hash_password(user.password),
        currentxp=0,
        currentlvl=0
    )

    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)

    token = create_access_token(
        data={"sub": novo_user.userid}
    )

    return {
        "message": "Usuário registado com sucesso",
        "token": token,
        "token_type": "bearer",
        "userid": novo_user.userid,
        "username": novo_user.username,
        "email": novo_user.email,
        "currentxp": novo_user.currentxp,
        "currentlvl": novo_user.currentlvl
    }



@app.get("/users/{userid}")
def get_user_by_id(userid: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.userid == userid).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {
        "userid": user.userid,
        "username": user.username,
        "email": user.email,
        "currentxp": user.currentxp,
        "currentlvl": user.currentlvl
    }


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Email/Password Incorretos")

    if not verify_password(user.password, db_user.passencrypt):
        raise HTTPException(status_code=400, detail="Email/Password Incorretos")

    token = create_access_token(
        data={"sub": db_user.userid}
    )

    return {
        "message": "Login efetuado com sucesso",
        "token": token,
        "token_type": "bearer",
        "userid": db_user.userid,
        "username": db_user.username,
        "email": db_user.email,
        "currentxp": db_user.currentxp,
        "currentlvl": db_user.currentlvl
    }


@app.get("/games", response_model=list[GameOut])
def listar_games(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    return games

@app.get("/quests/disponiveis/{userid}", response_model=list[QuestOut])
def quests_disponiveis(userid: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")
    completed_ids = db.query(UserQuest.questid).filter(UserQuest.userid == userid).all()
    completed_ids = [q[0] for q in completed_ids]
    quests = db.query(Quest).filter(
        Quest.questid.not_in(completed_ids),
        Quest.isdaily == False
    ).all()

    result = []
    for q in quests:
        result.append({
            "questid": q.questid,
            "questname": q.questname,
            "questdescription": q.questdescription,
            "requirements": q.requirements,
            "howtodoit": q.howtodoit,
            "rewards": q.rewards,
            "isdaily": q.isdaily,
            "gameid": q.gameid,
            "gamename": q.game.gamename
        })
    return result

@app.get("/quests/daily/{userid}", response_model=list[QuestOutDaily])
def quests_daily(userid: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    quests = db.query(Quest).filter(
        Quest.isdaily == True
    ).all()

    result = []
    for q in quests:
        result.append({
            "questid": q.questid,
            "questname": q.questname,
            "howtodoit": q.howtodoit,
            "rewards": q.rewards,
            "isdaily": q.isdaily,
            "gameid": q.gameid,
            "gamename": q.game.gamename
        })

    return result

XP_REWARD = 10

@app.patch("/quests/check/{userid}/{questid}")
def check_quest(
    userid: str,
    questid: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User não encontrado")

    quest = db.query(Quest).filter(Quest.questid == questid).first()
    if not quest:
        raise HTTPException(status_code=404, detail="Quest não encontrada")

    if not quest.isdaily:
        already = db.query(UserQuest).filter(
            UserQuest.userid == userid,
            UserQuest.questid == questid
        ).first()

        if already:
            raise HTTPException(status_code=400, detail="Quest já foi completada")

    if quest.isdaily:
        completed = db.query(UserQuest).filter(
            UserQuest.userid == userid,
            UserQuest.questid == questid
        ).first()

        if completed:
            last_date = datetime.fromisoformat(completed.completedwhen).date()
            today = datetime.now().date()

            if last_date == today:
                raise HTTPException(status_code=400, detail="Daily quest já foi completada hoje")
            else:
                db.delete(completed)
                db.commit()

    user_quest = UserQuest(
        userid=userid,
        questid=questid,
        gameid=1,
        completedwhen=str(datetime.now())
    )

    db.add(user_quest)
    add_xp_and_update_level(user, XP_REWARD)

    db.commit()
    db.refresh(user)

    return {
        "message": "Quest marcada como concluída",
        "xp_ganho": XP_REWARD,
        "currentxp": user.currentxp,
        "currentlvl": user.currentlvl
    }

@app.patch("/quests/uncheck/{userid}/{questid}")
def unmark_quest(userid: str, questid: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first()  

    completed_quest = db.query(UserQuest).filter(
        UserQuest.userid == userid,
        UserQuest.questid == questid
    ).first()

    if not completed_quest:
        raise HTTPException(status_code=400, detail="Esta quest ainda não foi marcada como concluída")

    db.delete(completed_quest)
    remove_xp_and_update_level(user, XP_REWARD)

    db.commit()
    db.refresh(user)

    return {
        "message": "Quest desmarcada com sucesso",
        "xp_removido": XP_REWARD,
        "currentxp": user.currentxp,
        "currentlvl": user.currentlvl
    }

@app.get("/quests/completas/{userid}", response_model=list[CompletedGame])
def quests_completas(userid: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    completed = db.query(UserQuest).filter(UserQuest.userid == userid).all()

    games_dict = {}

    for uq in completed:
        quest = uq.quest
        
        if quest.isdaily:
            continue

        game = quest.game

        if game.gameid not in games_dict:
            games_dict[game.gameid] = {
                "gameid": game.gameid,
                "gamename": game.gamename,
                "quests": []
            }

        games_dict[game.gameid]["quests"].append({
            "questid": quest.questid,
            "questname": quest.questname,
            "questdescription": quest.questdescription,
            "rewards": quest.rewards
        })

    return list(games_dict.values())


@app.put("/changeuser/{userid}")
def change_username(userid: str, data: ChangeUsername, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first()
    if not verify_password(data.currentPass, user.passencrypt):
        raise HTTPException(status_code=400, detail="Password atual incorreta")

    user.username = data.new_username
    db.commit()
    db.refresh(user)

    return {"message": "Username atualizado com sucesso", "new_username": user.username}


@app.put("/changemail/{userid}")
def change_email(userid: str, data: ChangeEmail, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first()

    if not verify_password(data.currentPass, user.passencrypt):
        raise HTTPException(status_code=400, detail="Password atual incorreta")

    email_exists = db.query(User).filter(User.email == data.new_email).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email já está em uso")

    user.email = data.new_email
    db.commit()
    db.refresh(user)

    return {"message": "Email atualizado com sucesso", "new_email": user.email}


@app.put("/changepass/{userid}")
def change_password(userid: str, data: ChangePassword, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first()

    if not verify_password(data.currentPass, user.passencrypt):
        raise HTTPException(status_code=400, detail="Password atual incorreta")

    user.passencrypt = hash_password(data.new_password)
    db.commit()
    db.refresh(user)

    return {"message": "Password atualizada com sucesso"}


@app.delete("/deleteuser/{userid}")
def delete_user(userid: str, data: DeleteUserRequest, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    if userid != current_user:
        raise HTTPException(status_code=403, detail="Não autorizado")

    user = db.query(User).filter(User.userid == userid).first() 

    if not verify_password(data.currentPass, user.passencrypt):
        raise HTTPException(status_code=401, detail="Password incorreta")

    db.query(UserQuest).filter(UserQuest.userid == userid).delete()
    db.delete(user)
    db.commit()

    return {"message": "Utilizador eliminado com sucesso"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
