from fastapi import FastAPI, HTTPException 
import uvicorn
from database import engine, SessionLocal 
from models import Base, User, Game 
from schemas import UserCreate, UserOut,UserLogin
from sqlalchemy.orm import Session 
from fastapi import Depends
import uuid
import json

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



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
