<template>
    <div class="main">
        <div id="Pokedex">
            <div :id=pokemon[0] :style="{'background-color': colorGen(pokemon[0] )}" class="card" v-for="(pokemon) in pokemons.slice(0, 1024)" :key="pokemon.id" @click="change(pokemon, $event)">
                <div>
                    <div class="entry" style="text-align: center">
                        <img class="imagePoke" :src="require(`../assets/images/${image_folder}/0.png`)">
                        <p>{{ pokemon[0] }} - {{ pokemon[1] }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="Side">
            <div class="filtres">
                <h2>Filtres</h2>
                <div>
                    <h3>Jeu</h3>
                    <select name="game" id="game" @change="onChangeGame($event)">
                        <option value="Home">Home</option>
                        <option value="PoGO">Pokemon GO</option>
                    </select>
                </div>
                <div>
                    <h3>Type</h3>
                    <select name="type" id="type" @change="onChangeCat($event)">
                        <option value="shiny">Shiny</option>
                        <option value="normal">Tous</option>
                        <option v-if="this.game == 'PoGO'" value="shadow">Obscurs</option>
                        <option v-if="this.game == 'PoGO'" value="pure">Purifiés</option>
                        <option v-if="this.game == 'PoGO'" value="threeStars">3*</option>
                        <option v-if="this.game == 'PoGO'" value="perfect">Parfait</option>
                    </select>
                </div>
            </div>
            <div class="infos">
                <h2>Informations</h2>
                <p>{{noPokemon}} / 1025</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default ({
    name: "PokedexView",
    data() {
        return {
            pokemons: [],
            pokemonsData: [],
            noPokemon: 0,
            image_folder: "Shiny",
            filtre: "shiny",
            game: "Home",
            filtreFinal: ""
        };
    },
    methods: {
        colorGen(num){
            num = parseInt(num)
            if (num <= 151) return "#902D8D"
            if (num <= 251) return "#497BBB"
            if (num <= 386) return "#0AB0ED"
            if (num <= 493) return "#14A99D"
            if (num <= 649) return "#17A453"
            if (num <= 721) return "#8EC447"
            if (num <= 809) return "#FFEF2E"
            if (num <= 905) return "#F7922B"
            return "black"
        },
        change(pokemon, event){
            console.log(event.target.src)
            console.log(event.target.src.includes("0.aef45"))
            if(!event.target.src.includes("0.aef45")){
                event.target.src = require('../assets/images/Shiny/0.png')
                document.getElementById(pokemon[0]).children[0].children[0].style["background-color"] = "red"
                this.noPokemon -= 1;
                axios.get("http://127.0.0.1:8000/deletePoke/" + pokemon[0] + "/" + this.filtreFinal)
                .then((response) =>{
                    console.log(response)
                })
            }
            else {
                event.target.src = require(`../assets/images/${this.image_folder}/${pokemon[0]}.png`)
                document.getElementById(pokemon[0]).children[0].children[0].style["background-color"] = "green"
                this.noPokemon += 1;
                axios.get("http://127.0.0.1:8000/addPoke/" + pokemon[0] + "/" + this.filtreFinal)
                .then((response) =>{
                    console.log(response)
                })
            }
        },
        onChangeGame(event){
            let i = 1;
            while (i<=1024){
                document.getElementById(i).children[0].children[0].style["background-color"] = "red"
                document.getElementById(i).children[0].children[0].children[0].src = require(`../assets/images/${this.image_folder}/0.png`)
                i+=1;
            }
            this.noPokemon = 0
            this.game = event.target.value
            this.load()
        },
        onChangeCat(event){
            let i = 1;
            while (i<=1024){
                document.getElementById(i).children[0].children[0].style["background-color"] = "red"
                document.getElementById(i).children[0].children[0].children[0].src = require(`../assets/images/${this.image_folder}/0.png`)
                i+=1;
            }
            this.noPokemon = 0
            this.filtre = event.target.value
            console.log(this.filtre)
            if (this.filtre == "shiny") this.image_folder = "Shiny"
            else this.image_folder = "Pokemon-175px"
            this.load();
        },
        async init() {
            await axios.get("http://127.0.0.1:8000/getAllPokemons")
            .then((response) =>{
                this.pokemons = response.data
            })
            this.load()
        },
        async load() {
            if ((this.filtre == "shiny") || (this.filtre == "normal")) this.filtreFinal = this.filtre + this.game
            else this.filtreFinal = this.filtre
            console.log("ff : ", this.filtreFinal)
            await axios.get("http://127.0.0.1:8000/getAllPokemonsData/" + this.filtreFinal)
            .then((response) =>{
                this.pokemonsData = response.data
                this.pokemonsData.forEach(element => {
                    let card = document.getElementById(element[0])
                    let div = card.children[0].children[0]
                    div.style["background-color"] = "green"
                    let image = div.children[0]
                    this.noPokemon += 1;
                    image.src = require(`../assets/images/${this.image_folder}/${element[0]}.png`)
                });
            })
        }
    },
    mounted() {
        this.init()
    }
});
</script>
    
<style scopped>
html {
    overflow: hidden;
}

.main{
    display:flex; 
    flex-direction: row;
    justify-content: space-around; 
    align-items: center
}
#Pokedex {
    background-color: black;
    width: 1214px;
    height: 665px;
    display: flex;
    flex-wrap: wrap;
    overflow: auto;
}

.entry {
    background-color: red;
    width: 100px;
    margin-left: 10px;
    margin-right: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    color: white;
    border-radius: 10px;
    font-size: 14px;
}

.infos{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    background-color: yellow;
    border-radius: 10px;
    border: 1px solid black;
    width: 200px;
    height: 100px;
}

.filtres{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    background-color: pink;
    border-radius: 10px;
    border: 1px solid black;
    width: 200px;
}

.filtres div{
    width: 80%;
    margin-top: 10px;
    margin-bottom: 10px;
}

.filtres div select{
    background-color: white;
    width: 100%;
    padding-left: 5px;
	appearance: default;
}

.Side{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    height: 100%;
}

@media only screen and (max-width: 600px) {

    .infos{
        visibility: hidden;
        position: absolute;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        background-color: yellow;
        border-radius: 10px;
        border: 1px solid black;
        width: 200px;
        height: 100px;
    }

    .filtres{
        position: absolute;
        visibility: hidden;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        background-color: pink;
        border-radius: 10px;
        border: 1px solid black;
        width: 200px;
    }

    #Pokedex {
        background-color: black;
        width: 100%;
        height: 100%;
        display: flex;
        flex-wrap: wrap;
        overflow: auto;
    }
    
    .card {
        width: 20%;
        padding: 5px;
    }

    .entry{
        background-color: red;
        width: 100%;
        margin-left: 0px;
        margin-right: 0px;
        margin-top: 0px;
        margin-bottom: 0px;
        color: white;
        border-radius: 10px;
        font-size: 14px;
    }

    .imagePoke{
        height: 80%;
        width: 80%;
    }
}

</style>
    