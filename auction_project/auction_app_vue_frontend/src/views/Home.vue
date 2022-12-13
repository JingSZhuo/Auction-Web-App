<template>
    <div>
        <h2> welcome to our btec ebay!</h2>
    </div>
    <div>   
            <router-link to="/allItems">List All Items</router-link>|
            <router-link to="/addItem">Add Item</router-link>|
            <button @click="logout">logout</button>
            <router-view/>                   <!--Shows the component when a router-link is clicked-->
    </div>
    
</template>

<script lang="ts">

export default {

    methods: {
        async logout () {
            await fetch('http://127.0.0.1:8000/logout/' , {
                method: 'GET',
                credentials: 'include',
            })
            window.location.replace("http://127.0.01:8000/loginPage")     //refresh when logged out 
        }
    }
}

</script>
