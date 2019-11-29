
<template>
    <div>
        <!-- <EventNavBar/> -->
        <!-- <nuxt-link to="about">About</nuxt-link>-->
        <h4>{{event.title}}</h4>
        
        <!--<img src="~/assets/build_it_up_more.jpg" width = "100%">-->
        <img :src="event.event_image" width = "100%">
        <p>{{ event.event_about}}</p>

        <nuxt-link :to= "`/event/${event.id}`"> back </nuxt-link>

    </div>
</template>   


<script>
//import EventNavBar from '@/pages/event/_id/EventNavBar.vue'
//import EventNavBar from '@/components/EventNavBar.vue'
export default {
    props: ['event'],

    components: {
        // EventNavBar
        
    },
    
        
        
}
</script>

<style lang="scss" scoped>
    

</style>