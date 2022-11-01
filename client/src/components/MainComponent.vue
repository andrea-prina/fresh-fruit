<template>
    <main>
        <div class="container">
            <img src="../assets/fresh_fruit_logo.png" alt="" class="logo">
            <div class="row g-3 my-4">
                <div class="col-4 col-md-2 col-lg-1" v-for="month in months" :key="month.id">
                    <MonthButton :month="month" :activeMonth="activeMonth" @getFruits="getFreshFruits"/>
                </div>
            </div>
            <div v-if="activeMonth == null" class="text-center fw-bold">Select a month to see what seasonal fruits are fresh</div>
            <div class="row g-5">
                <div class="col-4 col-md-2 col-lg-2" v-for="fruit in freshFruits" :key="fruit.id">
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
            activeMonth : null,
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

        getFreshFruits : function(selectedMonth){

            if(this.activeMonth == selectedMonth){
                this.freshFruits = [];
                this.activeMonth = null;
            } else {
                this.setActiveMonth(selectedMonth);
                axios.get(`http://127.0.0.1:5000/fruits?month=${selectedMonth}`)
                .then((result) => {
                    this.freshFruits = result.data.data.fruits;
                })
                .catch((err) => {
                    console.warn(err);
                })
            }

        },

        setActiveMonth : function(selectedMonth){
            this.activeMonth = selectedMonth;
        }

    },

    created(){
        this.getMonths();
    }

}

</script>

<style lang="scss" scoped>

    .logo {
        width: 100%;
        max-width: 250px;
    }

</style>