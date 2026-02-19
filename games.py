from database import SessionLocal
from models import Game

db = SessionLocal()

games = [
    "Hogwarts",
    "Undertale",
    "Stardew Valley",
    "Runescape Old School",
    "Arc Raider",
    "Hollow Knight Silksong",
    "God of War Ragnarok"
]

for name in games:
    game = Game(gamename=name)
    db.add(game)

db.commit()
db.close()

print("Jogos inseridos com sucesso!")
