from fastapi import APIRouter, Request
""" from sd import FollowerClient """
from threading import Thread
import requests
import time

router = APIRouter()



@router.get('/pokemon/{nameorid}')
def getStats(request: Request, nameorid):
    try:
        key = int(nameorid)
        request.app.cur.execute(f'SELECT * FROM public."Statistiques" where index={key}')
        print(f'SELECT * FROM public."Statistiques" where index={key}')
    except:
        key = nameorid
        request.app.cur.execute(f'SELECT * FROM public."Statistiques" where "Nom anglais"=\'{key}\'')
        print(f'SELECT * FROM public."Statistiques" where "Nom anglais"=\'{key}\'')
    resultset = request.app.cur.fetchone()
    print("result", resultset)
    return resultset

@router.get('/pokemonTeam/{team}')
def getStats(request: Request, team):
    team = team.split('_')
    print(team)
    list_of_stat = []
    for poke in team:
        print(f'SELECT * FROM public."Statistiques" where "Nom anglais"=\'{poke}\'')
        request.app.cur.execute(f'SELECT * FROM public."Statistiques" where lower("Nom anglais")=\'{poke.lower()}\'')
        resultset = request.app.cur.fetchone()
        print("result", resultset)
        list_of_stat.append(resultset)
    return list_of_stat

@router.get('/move/{nameorid}')
async def getStats(request: Request, nameorid):
    try:
        key = int(nameorid)
        request.app.cur.execute(f'SELECT * FROM public."Move" where index={key}')
    except:
        key = nameorid
        key = key.lower()
        key = key.replace(" ", "-")
        print(f'SELECT * FROM public."Move" where "name"=\'{key}\'')
        request.app.cur.execute(f'SELECT * FROM public."Move" where "name"=\'{key}\'')
    resultset = request.app.cur.fetchone()
    print("result", resultset)
    return resultset

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
    request.app.cur.execute(f'SELECT * FROM public."Statistiques" ORDER BY index')
    resultset = request.app.cur.fetchall()
    return resultset


@router.get('/customRequest')
def customRequest(request: Request):
    request.app.cur.execute('ALTER TABLE public."pokedex2" ADD COLUMN AM boolean;')
    resultset = request.app.cur.fetchall()
    return resultset

@router.get('/getAllPokemonsData/{filtre}')
def getAllPokemonsData(request: Request, filtre):
    print(f'SELECT * FROM public."pokedex2" WHERE "{filtre}"=true ORDER BY numero')
    request.app.cur.execute(f'SELECT * FROM public."pokedex2" WHERE "{filtre}"=true ORDER BY numero')
    resultset = request.app.cur.fetchall()
    return resultset

@router.get('/addPoke/{num}/{filtre}')
def addPoke(request: Request, num, filtre):
    request.app.cur.execute(f"UPDATE public.pokedex2 SET \"{filtre}\"=true	WHERE numero={num}")
    request.app.conn.commit()
    return "OK"

@router.get('/deletePoke/{num}/{filtre}')
def deletePoke(request: Request, num, filtre):
    request.app.cur.execute(f"UPDATE public.pokedex2 SET \"{filtre}\"=false WHERE numero={num}")
    request.app.conn.commit()
    return "OK"

@router.get('/update/')
def update(request: Request):
    for i in range(1025):
        print(i)
        request.app.cur.execute(f"INSERT INTO public.pokedex(numero, name, \"shinyPoGO\", game, \"shinyHome\", shadow, \"threeStars\", perfect, pure, mega, \"normalPoGO\", \"normalHome\") VALUES ("+str(i+1)+", '???', false, 'PokemonGO', false, false, false, false, false, false, true, true)")
    request.app.conn.commit()
    return "OK"


@router.get('/moveUpdate/')
def update(request: Request):
    i=2
    baseurl = "https://pokeapi.co/api/v2/move/"

    while 1==1:
        print(i)
        response = requests.get("https://pokeapi.co/api/v2/move/" + str(i))

        # Vérifier que la requête a réussi
        if response.status_code == 200:
            print("Contenu HTML récupéré avec succès :")
            res = response.json()
            name = res["name"]
            acc = res["accuracy"]
            if acc == None:
                acc = 0
            pp = res["pp"]
            power = res["power"]
            if power == None:
                power = 0
            priority = res["priority"]
            category = res["damage_class"]["name"]
            typeAtt = res["type"]["name"]
            request.app.cur.execute(f'INSERT INTO public."Move"(name, pp, priority, category, power, type, accuracy) VALUES (\'{name}\', {pp}, {priority}, \'{category}\', {power}, \'{typeAtt}\', {acc});')
            
        else:
            print(f"Erreur lors de la requête : statut {response.status_code}")
            break
        i+=1
    request.app.conn.commit()
    return "OK"