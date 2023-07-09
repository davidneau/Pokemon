<template>
  <div class="about">
    <div class="stats">
      <div class="search">
        <v-btn @click="previous"><v-icon>mdi-previous</v-icon></v-btn>
        <input type="text" v-model='searchstring' class="textsearch">
        <v-btn @click="search">Search</v-btn>
        <v-btn @click="next"><v-icon>mdi-next</v-icon></v-btn>
      </div>
      <div class="pokeInfo">
        <div class="num">
          {{ numpoke }}
        </div>
        <div class="nom">
          {{ nompoke }}
        </div>
      </div>
      <v-img class="image" id="image" :src=url></v-img>
      <div class="statistiques">
        <div class="labels">
          <label>PV</label>
          <label>Attaque</label>
          <label>Attaque spé</label>
          <label>Défense</label>
          <label>Défense spé</label>
          <label>Vitesse</label>
        </div>
        <div class="labels">
          <label>{{ pv }}</label>
          <label>{{ att }}</label>
          <label>{{ attspe }}</label>
          <label>{{ def }}</label>
          <label>{{ defspe }}</label>
          <label>{{ vitesse }}</label>
        </div>
        <div class="stats-divs">
          <div class="stat-pv animstarts"></div>
          <div class="stat-att animstarts"></div>
          <div class="stat-attspe animstarts"></div>
          <div class="stat-def animstarts"></div>
          <div class="stat-defspe animstarts"></div>
          <div class="stat-vitesse animstarts"></div>
        </div>
      </div>
      <div class="talents">
        talents: multiécaille
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default ({
    name: "StatistiquesPokemon",
    data() {
        return {
          pv: 0,
          att: 0,
          attspe: 0,
          def: 0,
          defspe: 0,
          vitesse: 0,
          searchstring: "Pikachu",
          numpoke: 149,
          nompoke: "Dracolosse",
          url: require("/src/assets/images/Pokemon-175px/172.jpg")
        };
    },
    methods: {
      addAnimation(){
        let backstats = [this.pv, this.att, this.attspe, this.def, this.defspe, this.vitesse]
        let count = 0
        let statdivs = document.getElementsByClassName("stats-divs")[0]
        for (let sdiv of statdivs.childNodes){
          sdiv.style = ""
          sdiv.style.setProperty('--arrive', backstats[count] + "px")
          sdiv.style.animation = 'none'
          sdiv.offsetWidth;
          sdiv.style.animation = null
          count += 1
        }
      },
      search(){
        axios.get("http://127.0.0.1:8000/pokemon/" + this.searchstring)
        .then((response) => {
          console.log(response)
          this.numpoke = response.data[0] + 1
          this.nompoke = response.data[1]
          this.pv = response.data[4]
          this.att = response.data[5]
          this.attspe = response.data[6]
          this.def = response.data[7]
          this.defspe = response.data[8]
          this.vitesse = response.data[9]
          this.addAnimation()
          this.url = require("../assets/images/Pokemon-175px/" + this.numpoke + ".png")
        })
      },
      previous(){
        this.numpoke -= 1
        this.searchstring = this.numpoke
        this.search()
      },
      next(){
        this.numpoke += 1
        console.log(this.numpoke)
        this.searchstring = this.numpoke
        this.search()
      }
    },
    mounted() {
      this.search()
    }
});
</script>

<style scopped>

.about{
  background-color: #111111;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stats{
  background-color: #EEEEEE;
  height: 90%;
  width: 40%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pokeInfo {
  display: flex;
  flex-direction: row;
  margin-top: 10px;
}

.num {
  border: 2px solid black;
}

.nom {
  border: 2px solid black;
}

.image{
  width: 175px;
}

.statistiques{
  display: flex;
  flex-direction: row;
  width: 100%;
}

.labels{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-right: 20px;
  width: 20%;
}

.stats-divs{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.stat-pv{
  height: 20px;
  background-color: #111111;
}

.stat-att{
  height: 20px;
  background-color: #111111;
}

.stat-attspe{
  height: 20px;
  background-color: #111111;
}

.stat-def{
  height: 20px;
  background-color: #111111;
}

.stat-defspe{
  height: 20px;
  background-color: #111111;
}

.stat-vitesse{
  height: 20px;
  background-color: #111111;
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

.search {
  margin-top: 10px;
  width: 45%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.textsearch{
  width: 200px;
  height: 80%;
  background-color: white;
}

</style>
