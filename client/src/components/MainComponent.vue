<template>
    <main>
        <div class="container">
            <div class="row">
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">JAN</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">FEB</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">MAR</div>
                </div>
            </div>
            <div class="row">
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">JAN</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">FEB</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">MAR</div>
                </div>
            </div>
            <div class="row">
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">JAN</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">FEB</div>
                </div>
                <div class="col-4 d-flex justify-content-center p-3">
                    <div class="month-card d-flex align-items-center justify-content-center">MAR</div>
                </div>
            </div>
            <div class="row">
                <div class="col-4 d-flex justify-content-center">
                    <div class="month-card d-flex align-items-center justify-content-center">JAN</div>
                </div>
                <div class="col-4 d-flex justify-content-center">
                    <div class="month-card d-flex align-items-center justify-content-center">FEB</div>
                </div>
                <div class="col-4 d-flex justify-content-center">
                    <div class="month-card d-flex align-items-center justify-content-center">MAR</div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
export default {
    
    name : "MainComponent",

}
</script>

<style lang="scss" scoped>

    .month-card {

        border: 1px solid red;
        border-radius: 5px;
        width: 25vw;
        height: 25vw;

    }

</style>