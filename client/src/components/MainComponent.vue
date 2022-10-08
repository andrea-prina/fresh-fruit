<template>
    <main>
        <input type="text" name="" id="" v-model="month" placeholder="">
        <button @click="getFreshFruits">PRESS ME</button>
        <ul>
            <li v-for="fruit in freshFruit" :key="fruit.id">
                {{ fruit[0] }}
            </li>
        </ul>
    </main>
</template>

<script>
import axios from 'axios'

export default {
    
    name : "MainComponent",

    data : function(){
        return {

            month : "",
            freshFruit : [],
        }
    },

    methods : {

        getFreshFruits : function(){
            axios.get(`http://127.0.0.1:5000/fruit?month=${this.month}`)
            .then((result) => {
                this.freshFruit = result.data.data.fruits
                console.log(this.freshFruit);
            })
            .catch((err) => {
                console.warn(err);
            })
        },

    }

}

</script>

<style lang="scss" scoped>

</style>