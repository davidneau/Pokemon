<template>
  <v-app>
    <AppNavigation></AppNavigation>
    <v-main>
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
