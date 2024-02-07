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
            filtreFinal: "",
            urlBack: ""
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
            if(!event.target.src.includes("data:image/png;base64,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")){
                event.target.src = require('../assets/images/Shiny/0.png')
                document.getElementById(pokemon[0]).children[0].children[0].style["background-color"] = "red"
                this.noPokemon -= 1;
                axios.get(this.urlBack + "deletePoke/" + pokemon[0] + "/" + this.filtreFinal)
                .then((response) =>{
                    console.log(response)
                })
            }
            else {
                event.target.src = require(`../assets/images/${this.image_folder}/${pokemon[0]}.png`)
                document.getElementById(pokemon[0]).children[0].children[0].style["background-color"] = "green"
                this.noPokemon += 1;
                axios.get(this.urlBack + "addPoke/" + pokemon[0] + "/" + this.filtreFinal)
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
            await axios.get(this.urlBack + "getAllPokemons")
            .then((response) =>{
                this.pokemons = response.data
            })
            this.load()
        },
        async load() {
            if ((this.filtre == "shiny") || (this.filtre == "normal")) this.filtreFinal = this.filtre + this.game
            else this.filtreFinal = this.filtre
            console.log("ff : ", this.filtreFinal)
            await axios.get(this.urlBack + "getAllPokemonsData/" + this.filtreFinal)
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
        this.urlBack = this.$getURLBack();
        console.log("urlBack :", this.urlBack)
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
    