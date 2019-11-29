
<template>
    <div>
        <h4>{{event.title}}</h4>
        <h6>archives</h6>
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