<template>
    <div>
        <h1>All Items</h1>
        <Header></Header>
    </div>
    <div>
        <table>
            <tr v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
                <th>{{item.id}}</th>
                <th>{{item.item_title}}</th>
                <th>{{item.item_description}}</th>
                <th>{{item.item_sprice}}</th>
                <th>{{item.item_picture}}</th>
                <th>{{item.item_auctionfinish}}</th>
            </tr>
        </table>
    </div>
    <div>
        <a href="./views/AddItem.vue">
            <button type="button">Add Item Here</button>
        </a>
        
    </div>


</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
import Header from './components/Header.vue'

    export default{
    data() {
        return {
            items: [] as any[]
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://localhost:8000/api/addItems/");
            let data = await response.json();
            this.items = data;
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