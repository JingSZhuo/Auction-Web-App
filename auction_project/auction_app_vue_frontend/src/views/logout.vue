<template>

<button @click="logout">Click here to Log out</button>


</template>

<script lang="ts">

export default {

    methods: {

        async logout () {
            await fetch('http://127.0.0.1:8000/logout/')
        }
    }
}

</script>