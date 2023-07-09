import { createRouter, createWebHashHistory } from 'vue-router'
import CalendarHome from '../views/Home.vue'
import StatistiquesPokemon from '../views/Statistiques.vue'
import PokemonSD from '../views/pokemonSD.vue'

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
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
