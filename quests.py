from database import SessionLocal
from models import Quest

hogwarts_quests = [
    {
        "questname": "Aprender Expelliarmus",
        "questdescription": "Domina o feitiço Expelliarmus.",
        "requirements": "Nenhum",
        "howtodoit": "Completa a aula de Defesa Contra as Artes das Trevas.",
        "rewards": "50 XP",
        "isdaily": False
    },
    {
        "questname": "Explorar Hogsmeade",
        "questdescription": "Visita as principais lojas de Hogsmeade.",
        "requirements": "Nível 1",
        "howtodoit": "Viaja até Hogsmeade e entra em 3 lojas.",
        "rewards": "30 XP",
        "isdaily": False
    },
    {
        "questname": "Derrotar um Troll",
        "questdescription": "Enfrenta um troll nas montanhas.",
        "requirements": "Varinha equipada",
        "howtodoit": "Segue o marcador no mapa e derrota o troll.",
        "rewards": "100 XP",
        "isdaily": False
    }
]

undertale_quests = [
    {
        "questname": "Falar com Toriel",
        "questdescription": "Conhece Toriel nas Ruínas.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho inicial até encontrares Toriel.",
        "rewards": "10 XP",
        "isdaily": False
    },
    {
        "questname": "Resolver puzzles das Ruínas",
        "questdescription": "Completa os puzzles iniciais.",
        "requirements": "Nenhum",
        "howtodoit": "Segue as instruções de Toriel e ativa as placas.",
        "rewards": "20 XP",
        "isdaily": False
    },
    {
        "questname": "Derrotar Napstablook",
        "questdescription": "Enfrenta o fantasma Napstablook.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho até ao encontro e vence a batalha.",
        "rewards": "40 XP",
        "isdaily": False
    }
]

stardew_quests = [
    {
        "questname": "Plantar 15 sementes",
        "questdescription": "Começa a tua quinta plantando sementes.",
        "requirements": "Sementes no inventário",
        "howtodoit": "Planta 15 sementes no campo.",
        "rewards": "25 XP",
        "isdaily": False
    },
    {
        "questname": "Pescar um peixe",
        "questdescription": "Aprende a pescar.",
        "requirements": "Vara de pesca",
        "howtodoit": "Vai ao rio e apanha um peixe.",
        "rewards": "30 XP",
        "isdaily": False
    },
    {
        "questname": "Visitar a mina",
        "questdescription": "Explora o primeiro nível da mina.",
        "requirements": "Pickaxe",
        "howtodoit": "Entra na mina e derrota um monstro.",
        "rewards": "50 XP",
        "isdaily": False
    }
]

osrs_quests = [
    {
        "questname": "Cook's Assistant",
        "questdescription": "Ajuda o cozinheiro do castelo.",
        "requirements": "Nenhum",
        "howtodoit": "Recolhe os ingredientes e entrega ao cozinheiro.",
        "rewards": "1 Quest Point",
        "isdaily": False
    },
    {
        "questname": "Sheep Shearer",
        "questdescription": "Ajuda o fazendeiro a obter lã.",
        "requirements": "Tesoura",
        "howtodoit": "Corta lã das ovelhas e entrega ao fazendeiro.",
        "rewards": "60 XP Crafting",
        "isdaily": False
    },
    {
        "questname": "Romeo & Juliet",
        "questdescription": "Ajuda Romeo a encontrar Juliet.",
        "requirements": "Nenhum",
        "howtodoit": "Segue a história e entrega as mensagens.",
        "rewards": "5 Quest Points",
        "isdaily": False
    }
]

arc_raider_quests = [
    {
        "questname": "Primeiro Encontro",
        "questdescription": "Sobrevive ao primeiro ataque ARC.",
        "requirements": "Nenhum",
        "howtodoit": "Completa o tutorial inicial.",
        "rewards": "50 XP",
        "isdaily": False
    },
    {
        "questname": "Recolher Recursos",
        "questdescription": "Obtém materiais para o acampamento.",
        "requirements": "Inventário livre",
        "howtodoit": "Explora a zona e recolhe 10 recursos.",
        "rewards": "30 XP",
        "isdaily": False
    },
    {
        "questname": "Destruir Drone",
        "questdescription": "Elimina um drone ARC.",
        "requirements": "Arma equipada",
        "howtodoit": "Localiza um drone e destrói-o.",
        "rewards": "70 XP",
        "isdaily": False
    }
]

silksong_quests = [
    {
        "questname": "Primeiro Combate",
        "questdescription": "Derrota o primeiro inimigo.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho inicial e enfrenta o inimigo.",
        "rewards": "20 XP",
        "isdaily": False
    },
    {
        "questname": "Explorar a Cidade",
        "questdescription": "Descobre a primeira cidade.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o mapa até à cidade principal.",
        "rewards": "40 XP",
        "isdaily": False
    },
    {
        "questname": "Derrotar Mini-Chefe",
        "questdescription": "Enfrenta um mini-chefe inicial.",
        "requirements": "Arma equipada",
        "howtodoit": "Segue o caminho até ao boss e derrota-o.",
        "rewards": "100 XP",
        "isdaily": False
    }
]

gow_quests = [
    {
        "questname": "Primeiro Combate",
        "questdescription": "Derrota os primeiros inimigos.",
        "requirements": "Machado Leviathan",
        "howtodoit": "Segue o caminho inicial e derrota os inimigos.",
        "rewards": "50 XP",
        "isdaily": False
    },
    {
        "questname": "Explorar Midgard",
        "questdescription": "Explora a área inicial.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o mapa e descobre 3 locais.",
        "rewards": "30 XP",
        "isdaily": False
    },
    {
        "questname": "Derrotar Troll",
        "questdescription": "Enfrenta um troll gigante.",
        "requirements": "Machado equipado",
        "howtodoit": "Segue o marcador e derrota o troll.",
        "rewards": "120 XP",
        "isdaily": False
    }
]

db = SessionLocal()

all_quests = (
    hogwarts_quests +
    undertale_quests +
    stardew_quests +
    osrs_quests +
    arc_raider_quests +
    silksong_quests +
    gow_quests
)

for q in all_quests:
    quest = Quest(
        questname=q["questname"],
        questdescription=q["questdescription"],
        requirements=q["requirements"],
        howtodoit=q["howtodoit"],
        rewards=q["rewards"],
        expireswhen=None,
        isdaily=q["isdaily"]
    )
    db.add(quest)

db.commit()
db.close()

print("Quests inseridas com sucesso!")
