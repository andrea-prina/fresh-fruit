<template>
    <div class="text-center">
        <img class="w-100" :src="fruit[2]" :alt="fruit[1]">
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