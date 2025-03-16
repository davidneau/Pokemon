<template>
  <div class="mainSD">
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
  /* import { toRaw } from 'vue' */
  
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
          type2show: {"p1a": true, "p2a": true},
          nompoke: {"p1a": "Nom Pokémon", "p2a": "Nom Pokémon"},
          firstpoke: {"p1a": "???", "p2a": "???"},
          numpoke: {"p1a": "n° ???", "p2a": "n° ???"},
          hp: {"p1a": "100%", "p2a": "100%"},
          item: {"p1a": "???", "p2a": "???"},
          pokemonDataReady: false,
          battleOn: false
        };
    },
    methods: {
      delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
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

          console.log(message.includes("☆battle"))
          console.log(thisParent.battleOn)

          if (message.includes("☆battle") && !thisParent.battleOn) {
            console.log("attempt to join ", battleMatch[0])
            ws.send(`|/join ${battleMatch[0]}`);
            console.log(`📡 Suivi du combat ${thisParent.currentBattleID}...`);
            thisParent.battleOn = true;
          }

          if (message.includes("win") || message.includes("forfeited")){
            console.log("stop battle");
            await thisParent.delay(1000)
            thisParent.battleOn = false;
          }

          if (event.data.includes("switch")) {
            let message = event.data
            console.log(message.split("|").indexOf("switch"))
            let indexSwitch = message.split("|").indexOf("switch")
            let namePokeSwitched = message.split("|")[indexSwitch + 2].split(",")[0].trim()
            let player = message.split("|")[indexSwitch + 1].split(":")[0]
            thisParent.switch(namePokeSwitched, player, thisParent)

            if (message.split("|").indexOf("switch", indexSwitch + 1)){
              console.log(message.split("|").indexOf("switch", indexSwitch + 1))
              let indexSwitch2 = message.split("|").indexOf("switch", indexSwitch + 1)
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
      switch(pokemon, player, thisParent){
        console.log(player, "switch on", pokemon)
        axios.get(thisParent.urlBack + "pokemon/" + pokemon)
        .then((response) => {
          console.log(response)
          console.log("numpoke", thisParent.numPoke)
          thisParent.numpoke[player] = response.data[0]
          thisParent.nompoke[player] = response.data[1]
          thisParent.url[player] = require("../assets/images/Pokemon-175px/" + response.data[0] + ".png")
          thisParent.urltype1[player] = require("../assets/images/Type/Anglais/" + response.data[2] + ".png")
          if (response.data[3] !== "none") {
            thisParent.urltype2[player] = require("../assets/images/Type/Anglais/" + response.data[3] + ".png")
            document.getElementById("type2p2a").style.display = "block"
          }  
          else document.getElementById("type2p2a").style.display = "none"
          thisParent.pv[player] = response.data[4]
          thisParent.att[player] = response.data[5]
          thisParent.attspe[player] = response.data[6]
          thisParent.def[player] = response.data[7]
          thisParent.defspe[player] = response.data[8]
          thisParent.vitesse[player] = response.data[9]
          let index = 4
          let cats = ["pv", "att", "attspe", "def", "defspe", "vitesse"]
          cats.forEach(element => {
            thisParent.addAnimation(element, player, response.data[index])
            index += 1
          });
        })
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
      fillbunch(){
      },
      async getDataPokemon(){
      },
      fillPokemonActiv(){
      },
      damage(){
      },
      itemInfo(){
      },
      dispatch(){
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
  