<template>
    <button @click="$emit('getFruits', month.id)" class="w-100 btn btn-outline-secondary" :class="month.id == activeMonth ? 'active' : ''">
        {{ month.abbreviation }}
    </button>
</template>

<script>
export default {

    name : 'MonthButton',

    props : {
        month : Object,
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