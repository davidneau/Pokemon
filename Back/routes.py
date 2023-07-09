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