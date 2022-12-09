<template>
    <div>
        <h1>All Items</h1>
        <Header></Header>
        <input type="text" v-model="search">
        <button>Search</button>
    </div>
    <div v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
        <div v-if="search!=''">
            <div v-if="((item.item_title.search(search))!=-1 || (item.item_description.search(search))!=-1)">
                <!-- v-if="(search!='') && ((search) in (item.item_title) || (search) in (item.item_description)) -->
                now here
                {{item.id}}<br/>
                {{item.item_title}}<br/>
                {{item.item_description}}<br/>
                {{item.item_sprice}}<br/>
                {{item.item_picture}}<br/>
                {{item.item_auctionfinish}}
            </div>
        </div>
        <div v-else>
            I am here
            {{item.id}}<br/>
            {{item.item_title}}<br/>
            {{item.item_description}}<br/>
            {{item.item_sprice}}<br/>
            {{item.item_picture}}<br/>
            {{item.item_auctionfinish}}
        </div>
    </div>
    <div>
        <a href="./views/AddItem.vue">
            <button type="button">Add Item Here</button>
        </a>
        <button @click="createNewUser">Add New User</button>
    </div>


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
            let response = await fetch("http://localhost:8000/api/addItems/");
            let data = await response.json();
            this.items = data;
        },
        async createNewUser() {
            await fetch("http://localhost:8000/signup/", {
                method: "POST",
                credentials: "include",
            });
        }
    },
    mounted(){
      this.fetchItems()
    },

    components: {Header},

    setup(){
        const router = useRouter()




    }
}

</script>