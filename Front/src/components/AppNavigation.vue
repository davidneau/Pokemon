<template>
    <span>
        <v-navigation-drawer app v-model="drawer" dark style="border: solid 2px">
            <v-list>
                <v-list-item link to='/'>
                    Home
                </v-list-item>
                <v-list-item link to='/about'>
                    Informations
                </v-list-item>    
                <v-list-item link to='/pokemonSD'>
                    Pokemon Showdown
                </v-list-item> 
                <v-list-item link to='/Pokedex'>
                    Pokedex
                </v-list-item> 
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app color="blue darken-4" dark>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        </v-app-bar>    
    </span>
</template>

<script>
export default {
    name: 'AppNavigation',
    data(){
        return {
            drawer: false,
        }
    }
}
</script>

<style>
.v-toolbar{
    position: relative;
}
</style>