<template>
  <NavBar/>
  <router-view/>
</template>

<style>
@font-face {
  font-family: "FiraSans";
  src: local("FiraSans"), 
    url(./assets/fonts/FiraSans/FiraSans-Regular.ttf) format("truetype");
}

#app {
  font-family: "FiraSans", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1a150c;
  --base: #6c6a61;
  --secondary: #E7E7E7;
  --muted: #6c6a61;
  --accent: #c0c0c0;
}
</style>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: 'HomeView',
  components: {
    NavBar
  }
}
</script>
