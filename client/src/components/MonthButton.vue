<template>
    <button @click="$emit('getFruits', month[0])" class="w-100">
        {{ month[2] }}
    </button>
</template>

<script>
export default {

    name : 'MonthButton',

    props : {
        month : Object,
    }

}
</script>

<style lang="scss" scoped>

</style>