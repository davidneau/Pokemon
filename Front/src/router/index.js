import { createRouter, createWebHashHistory } from 'vue-router'
import CalendarHome from '../views/Home.vue'
import StatistiquesPokemon from '../views/Statistiques.vue'
import PokemonSD from '../views/pokemonSD.vue'
import Pokedex from '../views/pokedex.vue'
import Music from '@/views/Music.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: CalendarHome
  },
  {
    path: '/about',
    name: 'Statistiques',
    component: StatistiquesPokemon
  },
  {
    path: '/pokemonSD',
    name: 'pokemonSD',
    component: PokemonSD
  },
  {
    path: '/pokedex',
    name: 'pokedex',
    component: Pokedex
  },
  {
    path: '/music',
    name: 'Music',
    component: Music
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
