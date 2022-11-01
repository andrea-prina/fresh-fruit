<template>
    <div class="text-center w-100">
        <img class="w-100 mb-2" :src="fruit[2]" :alt="fruit[1]">
        <div>{{  fruit[1]  }}</div>
    </div>
</template>

<script>
export default {

    name : 'FruitCard',

    props : {
        fruit : Array,
    } 

}
</script>

<style>

</style>