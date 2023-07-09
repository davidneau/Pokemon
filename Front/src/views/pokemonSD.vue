<template>
  <div class="main">
    <div class="upside">
      <div class="teamUp">
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup1"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup2"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup3"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup4"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup5"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tupsrc.tup6"></v-img><p></p></div>
      </div>
      
      <div class="info_up">
        <div class="info_pokemon">
          <div class="pokeObjNomType">
            <div class="numnom">
              <p class="numero">{{ numpoke.p1a }}</p>
              <p class="nomPoke">{{ nompoke.p1a }}</p>
            </div>
            <v-img class="image" id="image" max-height="50%" max-width="80%" :src=url.p1a></v-img>
            <div class="containerHP">
              <p>{{ hp.p1a }}</p>
              <div><div id="hp1"></div></div>
            </div>
            <div class="type">
              <v-img :src="urltype1.p1a" max-width="40%" height="100%" ></v-img>
              <v-img id="type2p1a" :src="urltype2.p1a" max-width="40%" height="100%" v-if="type2show.p1a"></v-img>
            </div>
            <p>Objet : {{ item.p1a }}</p>
          </div>
          <div class="statistiques">
            <div class="labels-stats">
              <label>HP</label>
              <label>{{ pv.p1a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Att</label>
              <label>{{ att.p1a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Def</label>
              <label>{{ def.p1a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>SpeA</label>
              <label>{{ attspe.p1a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>SpeD</label>
              <label>{{ defspe.p1a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Spd</label>
              <label>{{ vitesse.p1a }}</label>
              <div></div>
            </div>
          </div>
        </div>
      </div>

    </div>
    <div class="downside">
      <div class="info_down">
        <div class="info_pokemon">
          <div class="pokeObjNomType">
            <div class="numnom">
              <p class="numero">{{ numpoke.p2a }}</p>
              <p class="nomPoke">{{ nompoke.p2a }}</p>
            </div>
            <v-img class="image" id="image" max-height="50%" max-width="80%" :src=url.p2a></v-img>
            <div class="containerHP">
              <p>{{ hp.p2a }}</p>
              <div><div id="hp2"></div></div>
            </div>
            <div class="type">
              <v-img :src="urltype1.p2a" max-width="40%" height="100%" ></v-img>
              <v-img id="type2p2a" :src="urltype2.p2a" max-width="40%" height="100%" v-if="type2show.p2a"></v-img>
            </div>
            <p>Objet : {{ item.p2a }}</p>
          </div>
          <div class="statistiques">
            <div class="labels-stats">
              <label>HP</label>
              <label>{{ pv.p2a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Att</label>
              <label>{{ att.p2a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Def</label>
              <label>{{ def.p2a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>SpeA</label>
              <label>{{ attspe.p2a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>SpeD</label>
              <label>{{ defspe.p2a }}</label>
              <div></div>
            </div>
            <div class="labels-stats">
              <label>Spd</label>
              <label>{{ vitesse.p2a }}</label>
              <div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="teamDown">
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn1"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn2"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn3"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn4"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn5"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" :src="tdwnsrc.tdwn6"></v-img><p></p></div>
      </div>

    </div>
  </div>
</template>
  
  <script>
  import axios from "axios"
  import { toRaw } from 'vue'
  
  export default ({
      name: "StatistiquesPokemon",
      data() {
          return {
            pokemon: {"p1a": "", "p2a": ""},
            pv: {"p1a": 0, "p2a": 0},
            att: {"p1a": 0, "p2a": 0},
            attspe: {"p1a": 0, "p2a": 0},
            def: {"p1a": 0, "p2a": 0},
            defspe: {"p1a": 0, "p2a": 0},
            vitesse: {"p1a": 0, "p2a": 0},
            team1: {},
            team2: {},
            tupsrc: {
              "tup1": "",
              "tup2": "",
              "tup3": "",
              "tup4": "",
              "tup5": "",
              "tup6": "",
            },
            tdwnsrc: {
              "tdwn1": "",
              "tdwn2": "",
              "tdwn3": "",
              "tdwn4": "",
              "tdwn5": "",
              "tdwn6": "",
            },
            url: {"p1a": require("../assets/images/Pokemon-175px/0.png"), "p2a": require("../assets/images/Pokemon-175px/0.png")},
            urltype1: {"p1a": require("../assets/images/Type/Anglais/dark.png"), "p2a": require("../assets/images/Type/Anglais/fire.png")},
            urltype2: {"p1a": require("../assets/images/Type/Anglais/flying.png"), "p2a": require("../assets/images/Type/Anglais/ghost.png")},
            type2show: {"p1a": false, "p2a": false},
            nompoke: {"p1a": "Nom Pokémon", "p2a": "Nom Pokémon"},
            firstpoke: {"p1a": "???", "p2a": "???"},
            numpoke: {"p1a": "n° ???", "p2a": "n° ???"},
            hp: {"p1a": "100%", "p2a": "100%"},
            item: {"p1a": "???", "p2a": "???"},
            pokemonDataReady: false
          };
      },
      methods: {
        init(){
            axios.get("http://127.0.0.1:8000/initSDSession")
            .then(() => {
                this.updateSDSession()
            })
        },
        fillbunch(){
          const target_1 = toRaw(this.team1);
          Object.keys(target_1).forEach(((element, index) => {
            if (target_1[element].length !== 0) {
              try {
                console.log("Chargement de l'image pour : ", element["NomAnglais"])
                let id = "tup" + (index + 1)
                console.log(id)
                this.tupsrc[id] = require('../assets/images/Pokemon-175px/' + target_1[element]["index"] + '.jpg')
                document.getElementsByClassName('banc')[index].childNodes[1].innerText = target_1[element]["NomAnglais"]
              }
              catch (error){
                console.log(error)
              }
            }
          }))
          const target_2 = toRaw(this.team2);
          console.log(target_2)
          Object.keys(target_2).forEach(((element, index) => {
            if (target_2[element].length !== 0) {
              try {
                console.log("Chargement de l'image pour : ", element["NomAnglais"])
                let id = "tdwn" + (index + 1)
                this.tdwnsrc[id] = require('../assets/images/Pokemon-175px/' + target_2[element]["index"] + '.jpg')
                document.getElementsByClassName('banc')[6 + index].childNodes[1].innerText = target_2[element]["NomAnglais"]
              }
              catch (error){
                console.log(error)
              }
            }
          }))
        },
        async getDataPokemon(){
          console.log("requete pour avoir les donnée des pokemons avec :")
          console.log(this.team1)
          console.log(this.team2)
          let list_pokemon = Array()
          Object.entries(this.team1).forEach(([key]) => {
            list_pokemon.push(key)
          });
          Object.entries(this.team2).forEach(([key]) => {
            list_pokemon.push(key)
          });
          console.log("http://127.0.0.1:8000/pokemonTeam/" + list_pokemon.join('_'))
          await axios.get("http://127.0.0.1:8000/pokemonTeam/" + list_pokemon.join('_'))
          .then((response) => {
            console.log(response.data)
            response.data.forEach((element, index) =>{
              let team = this.team1
              if (index >= 6) {team = this.team2}
              if (element !== null) {
                let pokemon = element[12].toLowerCase()
                team[pokemon]["index"] = element[0]
                team[pokemon]["Nom"] = element[1]
                team[pokemon]["Type1"] = element[2]
                team[pokemon]["Type2"] = element[3]
                team[pokemon]["PV"] = element[4]
                team[pokemon]["Att"] = element[5]
                team[pokemon]["AttSpe"] = element[6]
                team[pokemon]["Def"] = element[7]
                team[pokemon]["DefSpe"] = element[8]
                team[pokemon]["Vit"] = element[9]
                team[pokemon]["Talent1"] = element[10]
                team[pokemon]["Talent2"] = element[11]
                team[pokemon]["TalentCache"] = element[13]
                team[pokemon]["NomAnglais"] = element[12]
                team[pokemon]["Numero"] = element[14]
                team[pokemon]["HPremain"] = "100%"
                team[pokemon]["Statut"] = "OK"
                team[pokemon]["Item"] = "Unknown"
              }
            })
            this.fillbunch()
            this.fillPokemonActiv("p1a", this.firstpoke["p1a"])
            this.fillPokemonActiv("p2a", this.firstpoke["p2a"])
            this.pokemonDataReady = true
          })
        },
        fillPokemonActiv(player, pokemonChosen){
          let pokemon
          if (player == "p1a") {pokemon = toRaw(this.team1)[pokemonChosen.toLowerCase()]}
          if (player == "p2a") {pokemon = toRaw(this.team2)[pokemonChosen.toLowerCase()]}
          console.log("pokemon actif : ", pokemonChosen)
          let numplayer = parseInt(player.charAt(1)) - 1
          this.numpoke[player] = "n°" + pokemon["Numero"]
          this.nompoke[player] = pokemon["NomAnglais"]
          this.urltype1[player] = require("../assets/images/Type/Anglais/" + pokemon["Type1"] +  ".png")
          if (pokemon["Type2"] != "none"){
            this.type2show[player] = true;
            this.urltype2[player] = require("../assets/images/Type/Anglais/" + pokemon["Type2"] +  ".png")
            }
          else {this.type2show[player] = false}
          let hp = pokemon["HPremain"]
          console.log(pokemon)
          if (player == "p1a"){
            document.getElementById("hp1").style.width = hp
            this.hp[player] = hp
          }
          if (player == "p2a"){
            document.getElementById("hp2").style.width = hp
            this.hp[player] = hp
          }
          this.pv[player] = pokemon["PV"]
          this.att[player] = pokemon["Att"]
          this.attspe[player] = pokemon["AttSpe"]
          this.def[player] = pokemon["Def"]
          this.defspe[player] = pokemon["DefSpe"]
          this.vitesse[player] = pokemon["Vit"]
          this.url[player] = require("../assets/images/Pokemon-175px/" + pokemon["index"] + ".jpg") 
          let backstats = [this.pv[player], this.att[player], this.def[player], this.attspe[player], this.defspe[player], this.vitesse[player]]
          let count = 0
          let statdivs = document.getElementsByClassName("statistiques")[numplayer]
          for (let sdiv of statdivs.childNodes){
              sdiv = sdiv.childNodes[2]
              sdiv.style = ""
              sdiv.style.width = backstats[count] + "px"
              if (backstats[count] < 80) {sdiv.style.backgroundColor = "red"}
              else if(backstats[count] < 110) {sdiv.style.backgroundColor = "yellow"}
              else {{sdiv.style.backgroundColor = "green"}}
              sdiv.style.animation = 'none'
              sdiv.offsetWidth;
              sdiv.style.animation = null
              count += 1
          }
        },
        damage(player, damage, item){
          console.log(this.nompoke)
          if (item !== "" && item.split(" ")[1] == "item:"){
            item = item.split(":")[1].substring(1); 
            console.log("item :", item)
          }
          this.item[player] = item
          let hpremain = parseInt(damage.split("/")[0]) / parseInt(damage.split("/")[1])
          this.hp[player] = Math.round(hpremain * 100) + "%"
          console.log(damage.includes("fnt"))
          if (player == "p1a") {
            if (damage.includes("fnt")){
              this.hp[player] = "KO"
              document.getElementById("hp1").style.width = 0
              this.team1[this.nompoke["p1a"].toLocaleLowerCase()]["HPremain"] = "KO"
            }
            else {
              document.getElementById("hp1").style.width = Math.round(hpremain * 100) + "%";
              this.team1[this.nompoke["p1a"].toLocaleLowerCase()]["HPremain"] = Math.round(hpremain * 100) + "%"
            }
            console.log(this.team1)
          }
          if (player == "p2a") {
            console.log(this.nompoke["p2a"].toLowerCase())
            if (damage.includes("fnt")){
              this.hp[player] = "KO"
              document.getElementById("hp2").style.width = 0
              this.team2[this.nompoke["p2a"].toLocaleLowerCase()]["HPremain"] = "KO"
            }
            else {
              document.getElementById("hp2").style.width = Math.round(hpremain * 100) + "%"
              this.team2[this.nompoke["p2a"].toLocaleLowerCase()]["HPremain"] = Math.round(hpremain * 100) + "%"
            }
            console.log(this.team2)
          }
        },
        itemInfo(data){
          let jsonData = JSON.parse(data[0])
          console.log("item info : ", jsonData)
        },
        dispatch(inp_type, data){
          if (inp_type == "poke"){
            let pokemon = data[1].split(",")[0]
            let player = data[0]
            if (player == "p1"){this.team1[pokemon.toLowerCase()] = {}}
            if (player == "p2"){this.team2[pokemon.toLowerCase()] = {}}
            if (Object.keys(toRaw(this.team1)).length == 6 && Object.keys(toRaw(this.team2)).length == 6){
              console.log(Object.keys(toRaw(this.team1)).length)
              console.log(Object.keys(toRaw(this.team1)).length)
              console.log("GetDataPokemon")
              this.getDataPokemon()
            }
          }
          if (inp_type == "-damage" || inp_type == "-heal"){
            let player = data[0].split(":")[0]
            let damage = data[1]
            let item = ""
            console.log(data)
            if (data.length == 3){item = data[2]; console.log(item)}
            this.damage(player, damage, item)
          }
          if (inp_type == "switch"){
            let pokemon = data[1].split(",")[0]
            let player = data[0].split(":")[0]
            if (!this.pokemonDataReady){this.firstpoke[player] = pokemon}
            else {
              console.log(player + " switch avec " + pokemon)
              this.fillPokemonActiv(player, pokemon)
            }
          }
/*           if (inp_type == "request"){
            this.itemInfo(data)
          } */
          if (inp_type == "win"){
            this.team1 = {}
            this.team2 = {}
            console.log("match terminée, réinitialisation des teams ")
          }
        },
        async updateSDSession(){
          let a = 1
          const timeout = (ms) => new Promise(resolve => setTimeout(resolve, ms));
          while (a == 1) {
              axios.get("http://127.0.0.1:8000/getLogsSD")
                  .then((response) => {
                    if (response.data.length !== 0) {console.log(response.data)}
                    for (let i=0; i<response.data.length; i++){
                      let inp_type = response.data[i][0]
                      let data = response.data[i][1]
                      this.dispatch(inp_type, data)
                    }
                  })
              await timeout(3000)
          }
        }
      },
      mounted() {
        this.init()
      }
  });
  </script>
  
<style scopped>
.stats-divs div{
    height: 20px;
    width: 1px;
    background-color: black;
}

.statistiques{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 60%;
  margin-left: 10px;
}

.upside{
  width: 100%;
  height: 50%;
  background-color: aqua;
  border: 1px solid black;
}

.teamUp{
  max-height: 30%;
  height: 30%;
  background-color: blue;
  border: 1px solid black;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.info_up{
  height: 70%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.info_pokemon{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  width: 50%;
  height: 100%;
}

.info_down{
  height: 70%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.teamDown{
  height: 30%;
  background-color: blue;
  border: 1px solid black;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.downside{
  width: 100%;
  height: 50%;
  background-color: aqua;
  border: 1px solid black;
}

.banc {
  border: 1px solid black;
  width: 15%;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  max-height: 100%;
}

.labels-stats{
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 16.66%;
  justify-content: flex-start;
}

.labels-stats div{
  width: 1px;
  height: 80%;
  background-color: black;
}

.labels-stats label:first-child{
  position: absolute;
  left: 0;
}

.labels-stats label:nth-child(2){
  position: absolute;
  left: 20%;
}

.labels-stats div:nth-child(3){
  position: absolute;
  left: 40%;
}

.pokeObjNomType{
  border: 1px solid black; 
  height: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.numnom{
  display: flex;
  flex-direction: row;
  height: 10%;
  width: 100%;
}

.numero {
  width: 30%;
  text-align: center;
  border: 1px solid black;
}

.nomPoke {
  width: 70%;
  text-align: center;
  border: 1px solid black;
}

.type{
  width: 100%;
  height: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.containerHP{
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.containerHP div{
  background-color: red;
  width: 70%;
  height: 60%;
}

.containerHP div div{
  background-color: green;
  width: 100%;
  height: 100%;
}

.v-responsive__sizer { padding-bottom: 0% !important}

.main{
  height: 100%;
}
</style>
  