from fastapi import FastAPI, HTTPException, Depends 
import uvicorn
from database import engine, SessionLocal 
from models import Base, User, Game, Quest, UserQuest 
from schemas import UserCreate, UserOut,UserLogin, QuestOut
from sqlalchemy.orm import Session 
import uuid
from utils import add_xp_and_update_level

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

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
        raise HTTPException(status_code=400, detail="Email já está registrado")

    novo_user = User(
        userid=str(uuid.uuid4()), 
        username=user.username,
        email=user.email,
        passencrypt=user.password, 
        currentxp=0,
        currentlvl=0
    )

    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)

    return {"message": "Usuário registrado com sucesso", "userid": novo_user.userid}

@app.get("/users", response_model=list[UserOut])
def listar_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Email/Password Incorretos")

    if db_user.passencrypt != user.password:
        raise HTTPException(status_code=400, detail="Email/Password Incorretos")
    
    return {
        "message": "Login efetuado com sucesso",
        "userid": db_user.userid,
        "username": db_user.username,
        "email": db_user.email,
        "currentxp": db_user.currentxp,
        "currentlvl": db_user.currentlvl
    }

@app.get("/quests/disponiveis/{userid}", response_model=list[QuestOut])
def quests_disponiveis(userid: str, db: Session = Depends(get_db)):
    # Verificar se user existe
    user = db.query(User).filter(User.userid == userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User não encontrado")

    # Quests já completadas pelo user
    completed_ids = db.query(UserQuest.questid).filter(UserQuest.userid == userid).all()
    completed_ids = [q[0] for q in completed_ids]

    # Quests disponíveis = todas menos as completadas
    quests = db.query(Quest).filter(Quest.questid.not_in(completed_ids)).all()

    return quests


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
