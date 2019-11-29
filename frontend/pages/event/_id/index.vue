<template>
    <div>
       <h2>{{event.title}}</h2>
       <nuxt-link :to= "`/event/${event.id}/about`">About</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/judges`">Judges</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/rules`">Rules</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/register`">Register</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/archive`">Archive</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/contact`">Contact</nuxt-link> |
       <nuxt-link :to= "`/event/${event.id}/edit`">Edit</nuxt-link>
        
    </div>
</template>

<script>
export default {
    props: ['event']
}
</script>

