<template>
    <div>
        <nuxt-child :event="event"/>
        <!-- <h6>Home page for {{event.id}}</h6> -->
    </div>
</template>

<script>
//import EventNavBar from '@/pages/event/_id/EventNavBar.vue'
import EventService from '@/services/EventService.js'
export default {
    components: {
        //EventNavBar
    },
    head() {
        return {
            title: this.event.id,     //do not miss "this"
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'What you need to know about Event #' + this.event.title
                }
            ]
        }
    },
    async asyncData({error, params}) {
      try {
        const response = await EventService.getEvent(params.id)
        return {
        event: response.data   //event ...... NOT events here , dont miss this one..
        }
      } catch (e) {
        error({statusCode:503, message: "unable to fetch data for event#"  + params.id })
        }
    },
}

</script>
