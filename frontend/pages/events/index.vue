<template>
    <div>
        <h4>List of events</h4>
        <EventCard 
          v-for = "(event,index) in events"
          :key="index"
          :event="event"
          :data-index="index"
          />
    </div>
</template>

<script>
import EventCard from '@/components/EventCard.vue'
import EventService from '@/services/EventService.js'
export default {
  head() {  //head function (a property of vue-meta), returns an object
    return {
      title: 'Eventlist -InMyGroove',
      meta: [ 
        {
          hid: 'description',
          name: 'description',
          content: 
              'List of events - InMyGroove'
        }
      ]
    }
  },
  async asyncData({error}) {
    try {
      const response = await EventService.getEvents()
      return {
        events: response.data
      }
    } catch (e) {
        error({statusCode:503, message: "unable to fetch event data at this point"})
    }
  },
  components: {
    EventCard
  }
}
</script>