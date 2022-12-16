<template>
    <div>
        <h1 class="display-1"><strong>Welcome to our BTEC Ebay!</strong></h1>
    </div>
    <nav class="navbar-expand-lg navbar-light bg-light d-flex justify-content-center ">   
        <router-link class="mx-auto" to="/allItems"><strong>List All Items</strong></router-link>|
        <router-link class="mx-auto" to="/addItem"><strong>Add Item</strong></router-link>|
        <router-link class="mx-auto" to="/profilePage"><strong>Profile</strong></router-link>
        <button class="align-items-end" @click="logout"><strong>logout</strong></button>
    </nav>
    <div>
        <br/>
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
