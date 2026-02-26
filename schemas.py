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

class GameOut(BaseModel):
    gameid: int
    gamename: str
    isdaily: bool

    class Config:
        from_attributes = True

class QuestOut(BaseModel):
    questid: int
    questname: str
    questdescription: str
    requirements: str | None
    howtodoit: str
    rewards: str
    isdaily: bool
    gameid: int
    gamename: str  

    class Config:
        from_attributes = True

class CompletedQuest(BaseModel):
    questid: int
    questname: str
    questdescription: str
    rewards: str

class CompletedGame(BaseModel):
    gameid: int
    gamename: str
    quests: list[CompletedQuest]

class ChangeUsername(BaseModel):
    new_username: str


class ChangeEmail(BaseModel):
    new_email: EmailStr


class ChangePassword(BaseModel):
    new_password: str

class DeleteUserRequest(BaseModel):
    password: str