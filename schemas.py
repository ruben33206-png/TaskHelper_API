from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    userid: str
    username: str
    email: str
    currentxp: int
    currentlvl: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class QuestOut(BaseModel):
    questid: int
    questname: str
    questdescription: str
    requirements: str | None
    howtodoit: str
    rewards: str
    isdaily: bool

    class Config:
        from_attributes = True


