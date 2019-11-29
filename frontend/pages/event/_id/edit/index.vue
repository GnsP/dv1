<template>
    <div>
        <h4>Editing {{ event.title}}</h4>
        <nuxt-link :to= "`/event/${event.id}`"> back </nuxt-link>
    </div>
</template>

<script>
export default {
    props: ['event']
    
}
</script>
<style lang="scss" scoped>

</style>