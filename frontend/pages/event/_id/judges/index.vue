
<template>
    <div>
        <!-- <EventNavBar/> -->
        
        <h4>judges info</h4>
        <nuxt-link :to= "`/event/${event.id}`"> back </nuxt-link>

    </div>
</template> 


<script>
//import EventNavBar from '@/components/EventNavBar.vue'
//import EventNavBar from '@/pages/event/_id/EventNavBar.vue'
export default {
        components: {
            //EventNavBar
        },
        props: ['event'],
        
}
</script>

<style lang="scss" scoped>

</style>