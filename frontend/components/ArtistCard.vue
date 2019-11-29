<template>
      <nuxt-link :to="'/artist/' + artist.id">
        <div class="-shadow">
          <img src = "~/assets/kyoka.jpg" width="20%"/><br>
          <!-- <img :id="val" width="20%" /><br> -->
          <h4 class="title">
            {{ artist.name }}
          </h4>
          <!-- <span>{{ event.attendees.length }} attending</span> -->
        </div>
      </nuxt-link>
</template>

<script>
    export default {
      name: 'ArtistCard',
      props: {
        artist: Object
      },
      
    }
</script>

<style scoped>
    div {
      padding: 20px;
      margin-bottom: 24px;
      transition: all 0.2s linear;
      cursor: pointer;
    }
    div:hover {
      transform: scale(1.01);
      box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
    }
    .title {
      margin: 0;
      color: black;
    }
    a {
      text-decoration: none;
    }
</style>
