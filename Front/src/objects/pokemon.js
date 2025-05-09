import axios from "axios"
import { reactive } from 'vue';
import Move from "./move"

export default class Pokemon {
    // Constructeur : initialise les propriétés de l'objet
    constructor(thisParent) {
        this.thisParent = thisParent
        this.moves = [new Move(this, ""), new Move(this, ""), new Move(this, ""), new Move(this, "")]
    }

    async fillInformation(nom, urlBack){
        await axios.get(urlBack + "pokemon/" + nom)
        .then(response => {
            let data = response.data
            console.log("data", nom, data)
            this.numpoke = data[0]
            this.nompoke = data[1]
            this.url = require("../assets/images/Pokemon-175px/" + data[0] + ".png")
            this.type1 = data[2]
            this.type2 = data[3]
            this.urltype1 = require("../assets/images/Type/Anglais/" + data[2] + ".png")
            if (data[3] != "none") this.urltype2 = require("../assets/images/Type/Anglais/" + data[3] + ".png")
            this.pv = data[4]
            this.att = data[5]
            this.attspe = data[6]
            this.def = data[7]
            this.defspe = data[8]
            this.vitesse = data[9]
        })
    }

    async fillInformation2(data){
        console.log("data", data[1], data)
        this.numpoke = data[0]
        this.nompoke = data[1]
        this.url = require("../assets/images/Pokemon-175px/" + data[0] + ".png")
        this.type1 = data[2]
        this.type2 = data[3]
        this.urltype1 = require("../assets/images/Type/Anglais/" + data[2] + ".png")
        if (data[3] != "none") this.urltype2 = require("../assets/images/Type/Anglais/" + data[3] + ".png")
        this.pv = data[4]
        this.att = data[5]
        this.attspe = data[6]
        this.def = data[7]
        this.defspe = data[8]
        this.vitesse = data[9]
        this.nomAnglais = data[12]
        this.hp = 100
        this.status = "normal"
        this.ko = false
    }

    // Méthode publique
    afficherInfos() {
        console.log(`Nom: ${this.nompoke}, Num: ${this.numpoke}`);
        console.log(this.thisParent.pokemon)
        this.thisParent.pokemon["p1a"] = reactive({ valeur: "a" })
    }
}