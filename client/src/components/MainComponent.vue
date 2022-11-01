<template>
    <main>
        <div class="container">
            <div class="row g-2 mb-2">
                <div class="col-4 col-md-2 col-lg-1" v-for="month in months" :key="month[0]">
                    <button class="month-btn" @click="getFreshFruits(month[0])">{{ month[2] }}</button>
                </div>
            </div>
        </div>
        <ul>
            <li v-for="fruit in freshFruits" :key="fruit[0]">
                {{ fruit[1] }}
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

            months : [],
            freshFruits : [],
            selectedMonth : "",
        }
    },

    methods : {

        getMonths : function(){
            axios.get(`http://127.0.0.1:5000/months`)
            .then((result) => {
                this.months = result.data.data.months;
            })
            .catch((err) => {
                console.warn(err);
            })
        },

        getFreshFruits : function(selMonth){
            axios.get(`http://127.0.0.1:5000/fruits?month=${selMonth}`)
            .then((result) => {
                this.freshFruits = result.data.data.fruits;
            })
            .catch((err) => {
                console.warn(err);
            })
        },

    },

    created(){
        this.getMonths();
    }

}

</script>

<style lang="scss" scoped>

    .month-btn {
        width: 100%;
    }

</style>