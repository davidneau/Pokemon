import axios from "axios"

export default class Move {
    // Constructeur : initialise les propriétés de l'objet
    constructor(thisParent, nom) {
        this.thisParent = thisParent
        this.nom = nom
        this.type = "normal"
    }

    async fillInformation(nom, urlBack){
        await axios.get(urlBack + "move/" + nom)
        .then(response => {
            let data = response.data
            console.log(data)
            this.power = data[4]
            this.acc = data[6]
            this.pp = data[1] - 1
            this.ppmax = data[1]
            this.cat = data[3]
            this.prior = data[2]
            this.type = data[5]
            this.typeImg = "../assets/images/Type/Anglais/" + data[5] + ".png"
        })
    }

    // Méthode publique
    afficherInfos() {
    }
}