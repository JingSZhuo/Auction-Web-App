<template>
        <div>
        <br/>
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
                Auction Finish: {{item.item_auctionfinish}}<br/>
                Highest Bid: {{item.item_personHighestBid}}<br/>

                <div id="bidding_form">
                    <h1>Bid for Item</h1>
                    <label>Email:</label><br>
                    <input type="text" v-model="email"><br>

                    <label>Bid:</label><br>
                    <input type="number" v-model="item_sprice"><br>

                    <button @click="bidItem(item_id+1,email,item_sprice)">Add my Bid</button>
                </div>
            </div>
        </div>
        <div v-else>
            ID:{{item.id}}<br/>
            Title:{{item.item_title}}<br/>
            Description:{{item.item_description}}<br/>
            Price: {{item.item_sprice}}<br/>
            Picture: {{item.item_picture}}<br/>
            Auction Finish: {{item.item_auctionfinish}}<br/>
            Highest Bid: {{item.item_personHighestBid}}<br/>

            <div id="bidding_form">
                    <h1>Bid for Item</h1>
                    <label>Email:</label><br>
                    <input type="text" v-model="email"><br>

                    <label>Bid:</label><br>
                    <input type="number" v-model="item_sprice"><br>

                    <button @click="bidItem(item_id+1,email,item_sprice)">Add my Bid</button>
                </div>
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
            search: '' as any,
            email: '' as string,
            item_sprice: 0 as number
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://127.0.0.1:8000/api/addItems/");       //GET request
            let data = await response.json();
            this.items = data;
        },
        async bidItem(id:number,email: string, item_sprice: number){
          const updated_data = {
            item_id:id,
            updated_email: email,
            updated_sprice: item_sprice,

          }
          await fetch("http://localhost:8000/api/addItems/" , {
              method: "PUT",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(updated_data),
          })
          .then((response) => response.json())
          this.fetchItems()
    }

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