from database import SessionLocal
from models import Quest

osrs_quests = [
    {
        "questname": "Cook's Assistant[F2P]",
        "questdescription": "Ajuda o cozinheiro do castelo.",
        "requirements": "Nenhum",
        "howtodoit": "Recolhe os ingredientes e entrega ao cozinheiro.",
        "rewards": "1 Quest Point",
        "isdaily": False,
        "gameid": 1
    },
    {
        "questname": "Sheep Shearer[F2P]",
        "questdescription": "Ajuda o fazendeiro a obter lã.",
        "requirements": "Tesoura",
        "howtodoit": "Corta lã das ovelhas e entrega ao fazendeiro.",
        "rewards": "60 XP Crafting",
        "isdaily": False,
        "gameid": 1
    },
    {
        "questname": "Romeo & Juliet[F2P]",
        "questdescription": "Ajuda Romeo a encontrar Juliet.",
        "requirements": "Nenhum",
        "howtodoit": "Segue a história e entrega as mensagens.",
        "rewards": "5 Quest Points",
        "isdaily": False,
        "gameid": 1
    }
]
arc_raider_quests = [
    {
        "questname": "Primeiro Encontro",
        "questdescription": "Sobrevive ao primeiro ataque ARC.",
        "requirements": "Nenhum",
        "howtodoit": "Completa o tutorial inicial.",
        "rewards": "50 XP",
        "isdaily": False,
        "gameid": 2
    },
    {
        "questname": "Recolher Recursos",
        "questdescription": "Obtém materiais para o acampamento.",
        "requirements": "Inventário livre",
        "howtodoit": "Explora a zona e recolhe 10 recursos.",
        "rewards": "30 XP",
        "isdaily": False,
        "gameid": 2
    },
    {
        "questname": "Destruir Drone",
        "questdescription": "Elimina um drone ARC.",
        "requirements": "Arma equipada",
        "howtodoit": "Localiza um drone e destrói-o.",
        "rewards": "70 XP",
        "isdaily": False,
        "gameid": 2
    }
]
hogwarts_quests = [
    {
        "questname": "Aprender Expelliarmus",
        "questdescription": "Domina o feitiço Expelliarmus.",
        "requirements": "Nenhum",
        "howtodoit": "Completa a aula de Defesa Contra as Artes das Trevas.",
        "rewards": "50 XP",
        "isdaily": False,
        "gameid": 3
    },
    {
        "questname": "Explorar Hogsmeade",
        "questdescription": "Visita as principais lojas de Hogsmeade.",
        "requirements": "Nível 1",
        "howtodoit": "Viaja até Hogsmeade e entra em 3 lojas.",
        "rewards": "30 XP",
        "isdaily": False,
        "gameid": 3
    },
    {
        "questname": "Derrotar um Troll",
        "questdescription": "Enfrenta um troll nas montanhas.",
        "requirements": "Varinha equipada",
        "howtodoit": "Segue o marcador no mapa e derrota o troll.",
        "rewards": "100 XP",
        "isdaily": False,
        "gameid": 3
    }
]
stardew_quests = [
    {
        "questname": "Plantar 15 sementes",
        "questdescription": "Começa a tua quinta plantando sementes.",
        "requirements": "Sementes no inventário",
        "howtodoit": "Planta 15 sementes no campo.",
        "rewards": "25 XP",
        "isdaily": False,
        "gameid": 4
    },
    {
        "questname": "Pescar um peixe",
        "questdescription": "Aprende a pescar.",
        "requirements": "Vara de pesca",
        "howtodoit": "Vai ao rio e apanha um peixe.",
        "rewards": "30 XP",
        "isdaily": False,
        "gameid": 4
    },
    {
        "questname": "Visitar a mina",
        "questdescription": "Explora o primeiro nível da mina.",
        "requirements": "Pickaxe",
        "howtodoit": "Entra na mina e derrota um monstro.",
        "rewards": "50 XP",
        "isdaily": False,
        "gameid": 4
    }
]
undertale_quests = [
    {
        "questname": "Falar com Toriel",
        "questdescription": "Conhece Toriel nas Ruínas.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho inicial até encontrares Toriel.",
        "rewards": "10 XP",
        "isdaily": False,
        "gameid": 5
    },
    {
        "questname": "Resolver puzzles das Ruínas",
        "questdescription": "Completa os puzzles iniciais.",
        "requirements": "Nenhum",
        "howtodoit": "Segue as instruções de Toriel e ativa as placas.",
        "rewards": "20 XP",
        "isdaily": False,
        "gameid": 5
    },
    {
        "questname": "Derrotar Napstablook",
        "questdescription": "Enfrenta o fantasma Napstablook.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho até ao encontro e vence a batalha.",
        "rewards": "40 XP",
        "isdaily": False,
        "gameid": 5
    }
]
silksong_quests = [
    {
        "questname": "Primeiro Combate",
        "questdescription": "Derrota o primeiro inimigo.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o caminho inicial e enfrenta o inimigo.",
        "rewards": "20 XP",
        "isdaily": False,
        "gameid": 6
    },
    {
        "questname": "Explorar a Cidade",
        "questdescription": "Descobre a primeira cidade.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o mapa até à cidade principal.",
        "rewards": "40 XP",
        "isdaily": False,
        "gameid": 6
    },
    {
        "questname": "Derrotar Mini-Chefe",
        "questdescription": "Enfrenta um mini-chefe inicial.",
        "requirements": "Arma equipada",
        "howtodoit": "Segue o caminho até ao boss e derrota-o.",
        "rewards": "100 XP",
        "isdaily": False,
        "gameid": 6
    }
]
gow_quests = [
    {
        "questname": "Primeiro Combate",
        "questdescription": "Derrota os primeiros inimigos.",
        "requirements": "Machado Leviathan",
        "howtodoit": "Segue o caminho inicial e derrota os inimigos.",
        "rewards": "50 XP",
        "isdaily": False,
        "gameid": 7
    },
    {
        "questname": "Explorar Midgard",
        "questdescription": "Explora a área inicial.",
        "requirements": "Nenhum",
        "howtodoit": "Segue o mapa e descobre 3 locais.",
        "rewards": "30 XP",
        "isdaily": False,
        "gameid": 7
    },
    {
        "questname": "Derrotar Troll",
        "questdescription": "Enfrenta um troll gigante.",
        "requirements": "Machado equipado",
        "howtodoit": "Segue o marcador e derrota o troll.",
        "rewards": "120 XP",
        "isdaily": False,
        "gameid": 7
    }
]

endfield_daily = [
    {
        "questname": "Recolher Materiais",
        "questdescription": "Obtém 5 materiais básicos.",
        "requirements": "Nenhum",
        "howtodoit": "Completa missões rápidas e recolhe materiais.",
        "rewards": "20 XP",
        "isdaily": True,
        "gameid": 8
    },
    {
        "questname": "Derrotar 10 Inimigos",
        "questdescription": "Elimina inimigos em qualquer missão.",
        "requirements": "Arma equipada",
        "howtodoit": "Joga qualquer missão e derrota 10 inimigos.",
        "rewards": "30 XP",
        "isdaily": True,
        "gameid": 8
    },
    {
        "questname": "Completar 1 Missão",
        "questdescription": "Conclui uma missão de qualquer tipo.",
        "requirements": "Nenhum",
        "howtodoit": "Seleciona uma missão rápida e completa-a.",
        "rewards": "15 XP",
        "isdaily": True,
        "gameid": 8
    }
]
warframe_daily = [
    {
        "questname": "Completar 1 Missão",
        "questdescription": "Termina qualquer missão rápida.",
        "requirements": "Nenhum",
        "howtodoit": "Seleciona uma missão no mapa e conclui-a.",
        "rewards": "20 XP",
        "isdaily": True,
        "gameid": 9
    },
    {
        "questname": "Derrotar 15 Inimigos",
        "questdescription": "Elimina inimigos em qualquer planeta.",
        "requirements": "Arma equipada",
        "howtodoit": "Joga uma missão de extermínio ou sobrevivência.",
        "rewards": "35 XP",
        "isdaily": True,
        "gameid": 9
    },
    {
        "questname": "Recolher 3 Recursos",
        "questdescription": "Obtém recursos de qualquer missão.",
        "requirements": "Nenhum",
        "howtodoit": "Explora o mapa e recolhe recursos deixados por inimigos.",
        "rewards": "15 XP",
        "isdaily": True,
        "gameid": 9
    }
]
dbd_daily = [
    {
        "questname": "Curar 1 Sobrevivente",
        "questdescription": "Ajuda um aliado ferido.",
        "requirements": "Kit médico (opcional)",
        "howtodoit": "Durante uma partida, cura um sobrevivente.",
        "rewards": "20 XP",
        "isdaily": True,
        "gameid": 10
    },
    {
        "questname": "Escapar 1 Vez",
        "questdescription": "Sobrevive a uma partida.",
        "requirements": "Nenhum",
        "howtodoit": "Completa geradores e escapa pela porta ou alçapão.",
        "rewards": "40 XP",
        "isdaily": True,
        "gameid": 10
    },
    {
        "questname": "Atingir 2 Sobreviventes",
        "questdescription": "Como killer, acerta dois golpes.",
        "requirements": "Jogar como Killer",
        "howtodoit": "Entra numa partida como killer e acerta dois hits.",
        "rewards": "30 XP",
        "isdaily": True,
        "gameid": 10
    }
]

db = SessionLocal()

all_quests = (
    osrs_quests +
    arc_raider_quests +
    hogwarts_quests +
    stardew_quests +
    undertale_quests +
    silksong_quests +      
    gow_quests +
    endfield_daily +
    warframe_daily +
    dbd_daily
)



for q in all_quests:
    quest = Quest(
        questname=q["questname"],
        questdescription=q["questdescription"],
        requirements=q["requirements"],
        howtodoit=q["howtodoit"],
        rewards=q["rewards"],
        expireswhen=None,
        isdaily=q["isdaily"],
        gameid=q["gameid"]
    )
    db.add(quest)

db.commit()
db.close()

print("Quests inseridas com sucesso!")
