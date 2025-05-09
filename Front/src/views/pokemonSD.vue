<template>
  <div class="mainSD">
    <div class="upside">
      <div class="teamUp">
        <div class="banc"><v-img style="width:100%;" id="bu1" :src="bench.p1a.b1"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bu2" :src="bench.p1a.b2"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bu3" :src="bench.p1a.b3"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bu4" :src="bench.p1a.b4"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bu5" :src="bench.p1a.b5"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bu6" :src="bench.p1a.b6"></v-img><p></p></div>
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
              <p>{{ hp.p1a }}%</p>
              <div><div id="hp1" :style="`width: ${hp.p1a}%`"></div></div>
            </div>
            <div class="type">
              <v-img :src="urltype1.p1a" max-width="40%" height="100%" ></v-img>
              <v-img id="type2p1a" :src="urltype2.p1a" max-width="40%" height="100%" v-if="type2show.p1a"></v-img>
            </div>
            <div>
              <p>Status : {{ status.p1a }}</p>
              <p>Objet : {{ item.p1a }}</p>
            </div>
          </div>
          <div class="statistiquesSD">
            <div class="labels-stats">
              <label>HP</label>
              <label>{{ pv.p1a }}</label>
              <div id="p1apv" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Att</label>
              <label>{{ att.p1a }}</label>
              <div id="p1aatt" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Def</label>
              <label>{{ def.p1a }}</label>
              <div id="p1adef" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>SpeA</label>
              <label>{{ attspe.p1a }}</label>
              <div id="p1aattspe" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>SpeD</label>
              <label>{{ defspe.p1a }}</label>
              <div id="p1adefspe" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Spd</label>
              <label>{{ vitesse.p1a }}</label>
              <div id="p1avitesse" class="animstarts"></div>
            </div>
          </div>
          <div class="moves">
            <div v-for="move in moves.p1a" :key="move.nom">{{ move.nom }}</div>
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
              <p>{{ hp.p2a }}%</p>
              <div><div id="hp2" :style="`width: ${hp.p2a}%`"></div></div>
            </div>
            <div class="type">
              <v-img :src="urltype1.p2a" max-width="40%" height="100%" ></v-img>
              <v-img id="type2p2a" :src="urltype2.p2a" max-width="40%" height="100%" v-if="type2show.p2a"></v-img>
            </div>
            <div>
              <p>Status : {{ status.p2a }}</p>
              <p>Objet : {{ item.p2a }}</p>
            </div>
          </div>
          <div class="statistiquesSD">
            <div class="labels-stats">
              <label>HP</label>
              <label>{{ pv.p2a }}</label>
              <div id="p2apv" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Att</label>
              <label>{{ att.p2a }}</label>
              <div id="p2aatt" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Def</label>
              <label>{{ def.p2a }}</label>
              <div id="p2adef" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>SpeA</label>
              <label>{{ attspe.p2a }}</label>
              <div id="p2aattspe" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>SpeD</label>
              <label>{{ defspe.p2a }}</label>
              <div id="p2adefspe" class="animstarts"></div>
            </div>
            <div class="labels-stats">
              <label>Spd</label>
              <label>{{ vitesse.p2a }}</label>
              <div id="p2avitesse" class="animstarts"></div>
            </div>
          </div>
          <div class="moves">
            <div v-for="move in moves.p2a" :key="move.nom">{{ move.nom }}</div>
          </div>
        </div>
      </div>
      <div class="teamDown">
        <div class="banc"><v-img style="width:100%;" id="bd1" :src="bench.p2a.b1"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bd2" :src="bench.p2a.b2"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bd3" :src="bench.p2a.b3"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bd4" :src="bench.p2a.b4"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bd5" :src="bench.p2a.b5"></v-img><p></p></div>
        <div class="banc"><v-img style="width:100%;" id="bd6" :src="bench.p2a.b6"></v-img><p></p></div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import Pokemon from "../objects/pokemon"
  import axios from "axios"
  
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
          urlBack: "",
          currentBattleID: "",
          team: {"p1a": [], "p2a": []},
          bench: {
            "p1a": {
              "b1": "",
              "b2": "",
              "b3": "",
              "b4": "",
              "b5": "",
              "b6": ""
            },
            "p2a": {
              "b1": "",
              "b2": "",
              "b3": "",
              "b4": "",
              "b5": "",
              "b6": ""
            },
          },
          moves: {
            "p1a": [],
            "p2a": []
          },
          url: {"p1a": require("../assets/images/Pokemon-175px/0.png"), "p2a": require("../assets/images/Pokemon-175px/0.png")},
          urltype1: {"p1a": require("../assets/images/Type/Anglais/dark.png"), "p2a": require("../assets/images/Type/Anglais/fire.png")},
          urltype2: {"p1a": require("../assets/images/Type/Anglais/flying.png"), "p2a": require("../assets/images/Type/Anglais/ghost.png")},
          type2show: {"p1a": true, "p2a": true},
          nompoke: {"p1a": "Nom Pokémon", "p2a": "Nom Pokémon"},
          firstpoke: {"p1a": "???", "p2a": "???"},
          numpoke: {"p1a": "n° ???", "p2a": "n° ???"},
          hp: {"p1a": "100", "p2a": "100"},
          status: {"p1a": "normal", "p2a": "normal"},
          item: {"p1a": "???", "p2a": "???"},
          pokemonDataReady: false,
          battleOn: false,
          teamReady: false
        };
    },
    methods: {
      delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
      },
      projetMove(){
        // Ouvrir une nouvelle fenêtre avec Showdown
        let showdownWindow = window.open("https://play.pokemonshowdown.com", "_blank");

        // Vérifier si la fenêtre s'est bien ouverte
        if (showdownWindow) {
            let checkLoaded = setInterval(async() => {
                try {
                    await this.delay(5000)
                    // Vérifier si le document de la nouvelle fenêtre est chargé
                    console.log(showdownWindow)
                    clearInterval(checkLoaded); // Stopper l'intervalle
                    
                    // Récupérer le LocalStorage de la nouvelle fenêtre
                    let showdownStorage = showdownWindow.localStorage;
                    
                    // Afficher tout le LocalStorage dans la console
                    console.log("LocalStorage de Showdown :", showdownStorage);

                    // Exemple : Récupérer uniquement les teams
                    Object.keys(showdownStorage).forEach(key => {
                        if (key.startsWith("showdown_teams")) {
                            console.log(`Équipe trouvée : ${key}`, showdownStorage.getItem(key));
                        }
                    });
                } catch (error) {
                    console.log("Erreur d'accès au LocalStorage : ", error);
                }
            }, 5000); // Vérifier toutes les 1 seconde
        } else {
            console.log("Impossible d'ouvrir une nouvelle fenêtre. Vérifiez que les pop-ups ne sont pas bloquées.");
        }
      },
      init(){
        let thisParent = this

        // URL du serveur WebSocket
        const URI = "wss://sim3.psim.us/showdown/websocket";

        // Création de la connexion WebSocket
        const ws = new WebSocket(URI);

        ws.onopen = async function () {
          console.log("✅ Connecté au serveur Showdown");
          let cond = 1
          while (cond == 1){
            await thisParent.delay(1000);
            if(!thisParent.battleOn) {
              console.log('search battle');
              setTimeout(ws.send("|/cmd userdetails Mahotsuki"), 1000);
            }
          }
        };

        ws.onmessage = async function (event) {
          let message = event.data;
          // Chercher un ID de combat dans les messages
          let battleMatch = message.match(/battle-[a-z0-9-]+/);
          console.log(`🔹 ${event.data}`)

          if (message.includes("☆battle") && !thisParent.battleOn) {
            console.log("attempt to join ", battleMatch[0])
            ws.send(`|/join ${battleMatch[0]}`);
            console.log(`📡 Suivi du combat ${battleMatch[0]}...`);
            thisParent.battleOn = true;
          }

          if (message.includes("win") || message.includes("forfeited")){
            console.log("stop battle");
            await thisParent.delay(1000)
            thisParent.battleOn = false;
          }

          if (message.includes("-damage")){
            let messageSplitted = message.split('|')
            messageSplitted.forEach(async (element, index) => {
              if (element == "-damage") {
                let player = messageSplitted[index+1].split(":")[0]
                let poke = messageSplitted[index+1].split(":")[1].trim()
                let damage = messageSplitted[index+2]
                console.log(player)
                console.log(poke)
                console.log(damage)
                await thisParent.processDamage(player, poke, damage)
              }
            });
          }

          if (message.includes("move")){
            console.log(message)
            let messageSplitted = message.split('|')
            messageSplitted.forEach(async (element, index) => {
              if (element == "move") {
                let player = messageSplitted[index+1].split(":")[0]
                let poke = messageSplitted[index+1].split(":")[1].trim()
                let move = messageSplitted[index+2]
                await thisParent.processMove(player, poke, move)
              }
            });
          }

          if (message.includes("-status")){
            let messageSplitted = message.split('|')
            messageSplitted.forEach(async (element, index) => {
              if (element == "-status") {
                let player = messageSplitted[index+1].split(":")[0]
                let poke = messageSplitted[index+1].split(":")[1].trim()
                let status = messageSplitted[index+2]
                console.log(player)
                console.log(poke)
                console.log(status)
                await thisParent.processStatus(player, poke, status)
              }
            });  
          }
          
          if (message.includes("-heal")){
            let messageSplitted = message.split('|')
            messageSplitted.forEach(async (element, index) => {
              if (element == "-heal") {
                let player = messageSplitted[index+1].split(":")[0]
                let poke = messageSplitted[index+1].split(":")[1].trim()
                let damage = messageSplitted[index+2]
                await thisParent.processDamage(player, poke, damage)
              }
            });
          }

          if (message.includes("|teampreview")){
            let messageSplitted = message.split('|')
            messageSplitted.forEach(async (element, index) => {
              await thisParent.processPokeBench(element, index, messageSplitted)
            });
            console.log("teams", thisParent.team)
          }

          if (event.data.includes("switch")) {
            console.log("eventswitch")
            let message = event.data
            let indexSwitch = message.split("|").indexOf("switch")
            let namePokeSwitched = message.split("|")[indexSwitch + 2].split(",")[0].trim()
            let player = message.split("|")[indexSwitch + 1].split(":")[0]
            thisParent.switch(namePokeSwitched, player, thisParent)

            let indexSwitch2 = message.split("|").indexOf("switch", indexSwitch + 1)
            if (indexSwitch2 != -1){
              let namePokeSwitched2 = message.split("|")[indexSwitch2 + 2].split(",")[0].trim()
              let player2 = message.split("|")[indexSwitch2 + 1].split(":")[0]
              await thisParent.delay(500)
              thisParent.switch(namePokeSwitched2, player2, thisParent)
            }
          }
        };

        ws.onerror = function (error) {
            console.error("❌ Erreur WebSocket :", error);
        };

        ws.onclose = function () {
            console.log("🚪 Connexion fermée.");
        };
      },
      addAnimation(cat, player, stat){
        let id = player + cat
        document.getElementById(id).style.setProperty('--arrive', stat + "px")
        document.getElementById(id).style.animation = 'none'
        document.getElementById(id).offsetWidth;
        document.getElementById(id).style.animation = null
      },
      async processStatus(player, poke, status){
        this.team[player][poke].status = status
        this.hp[player] = status
      },
      async processDamage(player, poke, damage){
        let damageFormat = damage.split("/")[0].split(" ")[0]
        this.team[player][poke].hp = damageFormat
        this.hp[player] = damageFormat
        if (damageFormat == "0") {
          this.team[player][poke].ko = true
          let index = Object.keys(this.team[player]).indexOf(poke)
          if (player == "p2a") {
            document.getElementById("bd"+ (index + 1)).style.filter = "grayscale(90%)"
          }
          if (player == "p1a") { 
            document.getElementById("bu"+ (index + 1)).style.filter = "grayscale(90%)"
          }
        }
      },
      async processMove(player, poke, move){
        console.log(player)
        console.log(move)

        let alreadyExist = false
        let noMove = 0

        this.team[player][poke].moves.forEach((moveFromPoke) => {
            if (moveFromPoke.nom == move) alreadyExist = true
            if (moveFromPoke.nom != "") noMove += 1
        })
        
        if (!alreadyExist) this.team[player][poke].moves[noMove].nom = move
      },
      async processPokeBench(element, index, messageSplitted){
        if (element == "poke") {
          let poke = messageSplitted[index+2].split(",")[0]
          let player = messageSplitted[index+1] + "a"
          this.team[player].push(poke)
          if (this.team["p1a"].length == 6 && this.team["p2a"].length == 6) {
            let jsonPoke = {}
            axios.get(this.urlBack + "pokemonTeam/" + this.team["p1a"].join("_") + "_" + this.team["p2a"].join("_"))
            .then(response => {
              console.log(response)
              response.data.forEach((elementPoke, index) => {
                let pokeObject = new Pokemon(this)
                pokeObject.fillInformation2(elementPoke)
                jsonPoke[pokeObject.nomAnglais] = pokeObject
                if (index <= 5) {
                  this.bench["p1a"]["b" + (index+1)] = pokeObject.url
                  this.team["p1a"] = jsonPoke
                }
                else if (index <= 11) {
                  this.bench["p2a"]["b" + (index-5)] = pokeObject.url
                  this.team["p2a"] = jsonPoke
                }
                if (index == 5) jsonPoke = {}
              }) 

              console.log("team player", this.team)
            })
          }
        }
      },
      async switch(pokemon, player){
        console.log("switch", pokemon)
        while(typeof this.team[player][pokemon] == "string" || this.team[player][pokemon] == undefined) {
          console.log("waiting")
          await this.delay(1000)
        }
        this.fillPokemonActiv(pokemon, player)
      },
      async getUserBattles(username) {
        let url = `https://pokemonshowdown.com/users/${username}.json`;

        try {
            let response = await fetch(url);
            let data = await response.json();

            console.log("🔍 Combats en cours :", data.rooms);
        } catch (error) {
            console.error("❌ Erreur :", error);
        }
      },
      async getDataPokemon(){
      },
      fillPokemonActiv(pokemon, player){
        this.hp[player] = this.team[player][pokemon].hp
        this.status[player] = this.team[player][pokemon].status
        console.log("fillactive", this.team[player][pokemon])
        let poke = this.team[player][pokemon]
        this.url[player] = poke.url
        this.nompoke[player] = poke.nompoke
        this.numpoke[player] = poke.numpoke
        this.urltype1[player] = poke.urltype1
        if (poke.urltype2 !== "none") this.urltype2[player] = poke.urltype2
        else this.type2show[player] = false
        this.pv[player] = poke.pv
        this.att[player] = poke.att
        this.attspe[player] = poke.attspe
        this.def[player] = poke.def
        this.defspe[player] = poke.defspe
        this.vitesse[player] = poke.vitesse

        this.moves[player] = [poke.moves[0], poke.moves[1], poke.moves[2], poke.moves[3]]
        
        this.addAnimation("pv", player, poke.pv)
        this.addAnimation("att", player, poke.att)
        this.addAnimation("def", player, poke.def)
        this.addAnimation("attspe", player, poke.attspe)
        this.addAnimation("defspe", player, poke.defspe)
        this.addAnimation("vitesse", player, poke.vitesse)
      },
      async updateSDSession(){
      }
    },
    mounted() {
        this.urlBack = this.$getURLBack();
        console.log("urlBack :", this.urlBack)
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

.statistiquesSD{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 60%;
  margin-left: 10px;
  width: 50%;
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

.mainSD{
  height: 100%;
  display: flex;
  flex-direction: column;
}

.animstarts{
  animation: grow_stats 1s both;
  animation-fill-mode: forwards
}

@keyframes grow_stats {
  from {
    width: 0px;
  }
  to {
    width: var(--arrive);
  }
}
</style>
  