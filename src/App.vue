<template>
  <div class="navbar row justify-content-start">
    <NavBar/>
  </div>
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

.menu {
    width: 32px;
    height: 32px;
}

h1 {
    font-weight: bold;
    margin: 0px;
}

.navbar {
    background-color: var(--secondary);
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
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
