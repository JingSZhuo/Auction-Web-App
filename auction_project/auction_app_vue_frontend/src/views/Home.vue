<template>
    <div>
        <h2> welcome to our btec ebay!</h2>
    </div>
    <div>   
            <router-link to="/allItems">List All Items</router-link>|
            <router-link to="/addItem">Add Item</router-link>|
            <router-link to="/signUp">Signup</router-link>
            
            <router-view/>                   <!--Shows the component when a router-link is clicked-->
    </div>
    
</template>