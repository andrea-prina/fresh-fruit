<template>
    <main>
        <div class="container">
            <h1>FreshFruit</h1>
            <div class="row g-2 my-4">
                <div class="col-4 col-md-2 col-lg-1" v-for="month in months" :key="month[0]">
                    <MonthButton :month="month" @getFruits="getFreshFruits"/>
                </div>
            </div>
            <div class="row g-2 mb-2">
                <div class="col-4 col-md-2 col-lg-1" v-for="fruit in freshFruits" :key="fruit[0]">
                    <FruitCard :fruit="fruit"/>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from 'axios'
import FruitCard from './FruitCard.vue'
import MonthButton from './MonthButton.vue'

export default {
    
    name : "MainComponent",

    components : {
        FruitCard,
        MonthButton
    },

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

</style>