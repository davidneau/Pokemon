<template>
  <v-app>
    <v-main>
      <AppNavigation></AppNavigation>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import AppNavigation from '@/components/AppNavigation'

export default {
  name: 'App',
  components: {
    AppNavigation,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
body, html {
  padding: 0;
  margin: 0;
}
</style>