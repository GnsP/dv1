<template>
  <div id="app">
    
    <nav-bar/> <!-- did not understand this naming part -->
    <h5>The thread connecting music, movements and artists</h5>
    
    <nuxt />
    
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  components:{
    NavBar
  },

  head() {  //head function (a property of vue-meta), returns an object
    return {
      titleTemplate: '%s - InMyGroove',
      meta: [
        {
          hid: 'description', //create page overrides the description, hid helps to stop redundancy
          name: 'description',
          content: 
              'InMyGroove - The thread connecting music, movement and artists, connecting HipHop Elements'
        }
      ]
    }
  }

  
}
</script>


