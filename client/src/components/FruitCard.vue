<template>
    <div class="text-center w-100">
        <img class="w-100 mb-2" :src="fruit.image" :alt="fruit.name">
        <div>{{  fruit.name }}</div>
    </div>
</template>

<script>
export default {

    name : 'FruitCard',

    props : {
        fruit : Object,
    } 

}
</script>

<style>

</style>