from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Session
from database import Base, SessionLocal
from fastapi import Depends
import json

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    userid = Column(String(36), unique=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    passencrypt = Column(String, nullable=False)
    currentxp = Column(Integer, nullable=False)
    currentlvl = Column(Integer, nullable=False)

    quests = relationship("UserQuest", back_populates="user")


class Game(Base):
    __tablename__ = "game"

    gameid = Column(Integer, primary_key=True)
    gamename = Column(String, nullable=False)

    quests = relationship("UserQuest", back_populates="game")


class Quest(Base):
    __tablename__ = "quest"

    questid = Column(Integer, primary_key=True)
    questname = Column(String, nullable=False)
    questdescription = Column(String, nullable=False)
    requirements = Column(String)
    howtodoit = Column(String, nullable=False)
    rewards = Column(String, nullable=False)
    expireswhen = Column(DateTime)
    isdaily = Column(Boolean, nullable=False)

    users = relationship("UserQuest", back_populates="quest")

class UserQuest(Base):
    __tablename__ = "user_quests"

    userid = Column(
        String(36),
        ForeignKey("user.userid"),
        primary_key=True
    )
    questid = Column(
        Integer,
        ForeignKey("quest.questid"),
        primary_key=True
    )
    gameid = Column(
        Integer,
        ForeignKey("game.gameid"),
        nullable=False
    )
    completedwhen = Column(String, nullable=False)

    user = relationship("User", back_populates="quests")
    quest = relationship("Quest", back_populates="users")
    game = relationship("Game", back_populates="quests")



