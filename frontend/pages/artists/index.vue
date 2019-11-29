<template>
  <div>
      <h5> artists </h5>
      <ArtistCard 
        v-for="(artist,index) in artists"
        :key="index"
        :artist="artist"
        :data-index="index"
        />

  </div>
</template>

<script>
import ArtistCard from '@/components/ArtistCard.vue';
import EventService from '@/services/EventService.js'
export default {
components: {ArtistCard},
async asyncData(){
    try {
      const output = await EventService.getArtists()
      return {
        artists: output.data
      }
    } catch (e){
        error({statusCode:503, message: "unable to fetch event data at this point"})
    }
}
    
}
</script>