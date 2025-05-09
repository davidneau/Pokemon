import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const myPlugin = {
  install(app) {
    // Ajoutez votre fonction globale ici
    app.config.globalProperties.$getURLBack = function(){
      if (window.location.href.includes("pokemonda")){
          return "https://pokemon-1xp8.onrender.com/"
      }
      else {
          return "http://127.0.0.1:8000/"
      }
    }
  }
}

createApp(App)
  .use(router)
  .use(vuetify)
  .use(myPlugin)
  .mount('#app')