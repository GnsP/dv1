<template>
  <div class="nav">
    <nuxt-link to = '/' class = "brand">
    InmyGroove</nuxt-link>  <!-- nuxt-link instead of router-link-->
    <nav>
        <nuxt-link to = '/events'>Eventlist</nuxt-link> |
        <nuxt-link to = '/artists'>Artists</nuxt-link> |
        <nuxt-link to = '/event/create'>Create</nuxt-link>
    </nav> 
  </div>
</template>

<style scoped>
.brand {
      font-family: 'Montserrat', sans-serif;
      font-weight: 200;
      font-size: 1.5em;
      color: #000000;
      text-decoration: none;
}
.nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 10px;
}
.nav .nav-item {
      box-sizing: border-box;
      margin: 0 5px;
      color: rgba(0, 0, 0, 0.5);
      text-decoration: none;
}
.nav .nav-item.router-link-exact-active {
      color: #39b982;
      border-bottom: solid 2px #39b982;
}
.nav a {
      display: inline-block;
}


</style>