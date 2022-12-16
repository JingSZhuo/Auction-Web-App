<template>
    <div>
        <button type="button" class="btn btn-primary" @click="showModal">Q&A</button>
        <transition name="fade" appear>
            <div class="modal-overlay" v-if="showModal" @click="showModal = false"></div>
        </transition>
        <div class="modal">
            <h3>Q&A</h3>
            <input>
            <button class="button" @click="showModal = false">Close</button>

        </div>
    </div>

</template>

<script>
export default{
    showModal: true //used to toggle modal
}
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    font-family: sans-serif;
}

.button{
    appearance: none;
    outline: none;
    border: none;
    background: none;
    cursor: pointer;

    display: inline-block;
    padding: 15px 25px;
    background-image: linear-gradient(to right, #CC2E5D, #FF5858);
    border-radius: 8px;

    color: #FFF;
    font-size: 18px;
    font-weight: 700;
}

.modal-overlay{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 98;
    background-color: rgba(0, 0, 0, 0.3);
}





</style>