from fastapi import APIRouter, Request
from sd import FollowerClient
from threading import Thread
import time
router = APIRouter()

@router.get('/pokemon/{nameorid}')
def getStats(request: Request, nameorid):
    try:
        key = int(nameorid)
        request.app.cur.execute(f'SELECT * FROM main."Statistiques" where index={key-1}')
    except:
        key = nameorid
        print(f'SELECT * FROM main."Statistiques" where "Nom anglais"=\'{key}\'')
        request.app.cur.execute(f'SELECT * FROM main."Statistiques" where "Nom anglais"=\'{key}\'')
    resultset = request.app.cur.fetchone()
    print("result", resultset)
    return resultset

@router.get('/pokemonTeam/{team}')
def getStats(request: Request, team):
    team = team.split('_')
    print(team)
    list_of_stat = []
    for poke in team:
        print(f'SELECT * FROM main."Statistiques" where "Nom anglais"=\'{poke}\'')
        request.app.cur.execute(f'SELECT * FROM main."Statistiques" where lower("Nom anglais")=\'{poke.lower()}\'')
        resultset = request.app.cur.fetchone()
        print("result", resultset)
        list_of_stat.append(resultset)
    return list_of_stat


followerClient = ""

@router.get('/initSDSession')
async def initSDSession():
    def initiation(username, password):
        global followerClient 
        followerClient= FollowerClient(name=username, password=password)
        followerClient.start()
    with open("./login.txt", "rt") as f, open("./owner.txt", "rt") as o:
        username, password = f.read().strip().splitlines()
    t = Thread(target=initiation, args=[username, password])
    t.run()

@router.get('/getLogsSD')
async def getLogsSD():
    global followerClient
    if followerClient != "":
        log = followerClient.log
        print("log :", log)
        followerClient.log = []
        print("followerClient.log vider : ", followerClient.log)
        return log
    else:
        print("followerClient actuellement non initié")

@router.get('/getAllPokemons')
def getAllPokemons(request: Request):
    request.app.cur.execute(f'SELECT * FROM main."Statistiques" ORDER BY index')
    resultset = request.app.cur.fetchall()
    return resultset


@router.get('/getAllPokemonsData/{filtre}')
def getAllPokemonsData(request: Request, filtre):
    print(f'SELECT * FROM main."pokedex" WHERE "{filtre}"=true ORDER BY numero')
    request.app.cur.execute(f'SELECT * FROM main."pokedex" WHERE "{filtre}"=true ORDER BY numero')
    resultset = request.app.cur.fetchall()
    return resultset

@router.get('/addPoke/{num}/{filtre}')
def addPoke(request: Request, num, filtre):
    request.app.cur.execute(f"UPDATE main.pokedex SET \"{filtre}\"=true	WHERE numero={num}")
    request.app.conn.commit()
    return "OK"

@router.get('/deletePoke/{num}/{filtre}')
def deletePoke(request: Request, num, filtre):
    request.app.cur.execute(f"UPDATE main.pokedex SET \"{filtre}\"=false WHERE numero={num}")
    request.app.conn.commit()
    return "OK"

@router.get('/update/')
def update(request: Request):
    for i in range(1025):
        print(i)
        request.app.cur.execute(f"INSERT INTO main.pokedex(numero, name, \"shinyPoGO\", game, \"shinyHome\", shadow, \"threeStars\", perfect, pure, mega, \"normalPoGO\", \"normalHome\") VALUES ("+str(i+1)+", '???', false, 'PokemonGO', false, false, false, false, false, false, true, true)")
    request.app.conn.commit()
    return "OK"