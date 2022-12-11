<template>
    <div>
        <div>
            <router-link to="/home">Home</router-link>
            <router-link to="/addItem">Add Item</router-link>
            <router-link to="/signUp">Signup</router-link>
            <router-link to="/login">Login</router-link>
            <router-view/>                   <!--Shows the component when a router-link is clicked-->
        </div>
        <h1>All Items</h1>
        <!-- <Header></Header> -->
        <label>Search: </label>
        <input type="text" v-model="search">
        
    </div>
    <div v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
        <div v-if="search!=''">
            <div v-if="((item.item_title.toLowerCase().search(search.toLowerCase()))!=-1 || (item.item_description.toLowerCase().search(search.toLowerCase()))!=-1)">
                ID:{{item.id}}<br/>
                Title:{{item.item_title}}<br/>
                Description:{{item.item_description}}<br/>
                Price: {{item.item_sprice}}<br/>
                Picture: {{item.item_picture}}<br/>
                Auction Finish: {{item.item_auctionfinish}}<br/><br/>
            </div>
        </div>
        <div v-else>
            ID:{{item.id}}<br/>
            Title:{{item.item_title}}<br/>
            Description:{{item.item_description}}<br/>
            Price: {{item.item_sprice}}<br/>
            Picture: {{item.item_picture}}<br/>
            Auction Finish: {{item.item_auctionfinish}}<br/><br/>
        </div>
    </div>
    <!-- <div>
        <a href="./views/AddItem.vue">
            <button type="button">Add Item Here</button>
        </a>
        <button @click="createNewUser">Add New User</button>
    </div> -->


</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
import Header from './components/Header.vue'

    export default{
    data() {
        return {
            items: [] as any[],
            search: '' as any
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://localhost:8000/api/addItems/");       //GET request
            let data = await response.json();
            this.items = data;
        },

    },
    mounted(){
      this.fetchItems()
    },
    // components: {
    //     Header,
    // },

    // setup(){
    //     const router = useRouter()
    // }
}

</script>