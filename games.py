from database import SessionLocal
from models import Game

db = SessionLocal()

games = [
    { "gameid": 1, "gamename": "Runescape Old School", "isdaily": False },
    { "gameid": 2, "gamename": "Arc Raider", "isdaily": False },
    { "gameid": 3, "gamename": "Hogwarts", "isdaily": False },
    { "gameid": 4, "gamename": "Stardew Valley", "isdaily": False },
    { "gameid": 5, "gamename": "Undertale", "isdaily": False },
    { "gameid": 6, "gamename": "Hollow Knight Silksong", "isdaily": False },
    { "gameid": 7, "gamename": "God of War Ragnarok", "isdaily": False },
    { "gameid": 8, "gamename": "Arknights: Endfield", "isdaily": True },
    { "gameid": 9, "gamename": "Warframe", "isdaily": True },
    { "gameid": 10, "gamename": "Dead by Daylight", "isdaily": True }
]

for g in games:
    game = Game(
        gameid=g["gameid"],
        gamename=g["gamename"],
        isdaily=g["isdaily"]
    )
    db.add(game)

db.commit()
db.close()

print("Jogos inseridos com sucesso!")
