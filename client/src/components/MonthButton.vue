<template>
    <button @click="$emit('getFruits', month[0])" class="w-100 btn btn-outline-secondary" :class="month[0] == activeMonth ? 'active' : ''">
        {{ month[2] }}
    </button>
</template>

<script>
export default {

    name : 'MonthButton',

    props : {
        month : Array,
        activeMonth : Number,
    }

}
</script>

<style lang="scss" scoped>

    button.active {
        background-color: #EE4033;
        color: #FFF;
    }

    button:hover {
        background-color: #EE4033;
    }

</style>