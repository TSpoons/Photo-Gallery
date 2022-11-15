<template>
    <div class="col-1">
      <img class="menu" src="@/assets/icons/menu.svg"> 
    </div>

    <div class="col-1">
      <h1>Gallery</h1>
    </div>

    <nav class="col-sm-2 offset-8">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
</template>

<style>
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
