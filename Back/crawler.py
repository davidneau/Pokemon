import json
import requests
import urllib.request

base = ""

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

pokemonform = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0").text)

for i in range(888, 1280):
    pokemon = pokemonform["results"][i]["name"]
    print(pokemon)
    r = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
    print("https://pokeapi.co/api/v2/pokemon/" + str(i+1))
    data = json.loads(r.text)

    name = data["name"][0].upper() + data["name"][1:]

    talents = data["abilities"]
    talent1 = "none"
    talent2 = "none"
    talenthidden = "none"

    for t in talents:
        print(t)
        if t['slot'] == 1:
            talent1 = t['ability']['name'].replace("-", "")
        if t['slot'] == 2:
            talent2 = t['ability']['name'].replace("-", "")
        if t['is_hidden'] == True:
            talenthidden = t['ability']['name'].replace("-", "")

    type1 = "none"
    type2 = "none"

    type1 = data["types"][0]["type"]["name"]
    if len(data["types"]) == 2:
        type2 = data["types"][1]["type"]["name"]

    pv = ''
    att = ''
    attspe = ''
    defe = ''
    defespe = ''
    vit = ''

    pv = data["stats"][0]["base_stat"]
    att = data["stats"][1]["base_stat"]
    defe = data["stats"][2]["base_stat"]
    attspe = data["stats"][3]["base_stat"]
    defespe = data["stats"][4]["base_stat"]
    vit = data["stats"][5]["base_stat"]

    numero = data["species"]["url"].split('/')[-2]

    print("name", name)

    print("t1", talent1)
    print("t2", talent2)
    print("th", talenthidden)

    print("type1", type1)
    print("type2", type2)

    print("pv", pv)
    print("att", att)
    print("def", defe)
    print("attspe", attspe)
    print("defspe", defespe)
    print("vit", vit)

    print(numero)

    img_url = data['sprites']['front_default']

    print(img_url)

    base += f"INSERT INTO main.\"Statistiques\"(\
    index, \"Nom\", \"type 1\", \"type 2\", \"PV\", \"Attaque\", \"Attaque spécial\", \"Défense\", \"Défense spécial\", \"Vitesse\", \"Talent 1\", \"Talent 2\", \"Nom anglais\", \"talent_caché\", \"numero\")\
    VALUES ({i+1}, \'{name}\', \'{type1}\', \'{type2}\', {pv}, {att}, {attspe}, {defe}, {defespe}, {vit}, \'{talent1}\', \'{talent2}\', \'{name}\', \'{talenthidden}\', \'{numero}\');\n"
    #base += f"UPDATE main.\"Statistiques\" SET \"type 1\"=\'{type1}\', \"type 2\"=\'{type2}\', \"Talent 1\"=\'{talent1}\', \"Talent 2\"=\'{talent2}\', \"talent_caché\"=\'{talenthidden}\' WHERE index={i+1};\n"
    """
    try:
        download_image(img_url, 'img/', str(i+1))
    except:
        pass"""

with open("remplirbase88.txt","w", encoding="utf8") as f:
        f.write(base)