<template>
     <h1> Item page</h1>


    <div id="bidding_form">
        <h1>Bid for Item</h1>
        <label>KeyID: {{keyID}}</label><br>
        <label>Item ID: {{itemID}}</label><br>
        <label>Item: {{itemtitle}} </label><br>
        <label>Item Description: {{itemdescription}}</label><br>
        <label>Item Starting Price: {{itemstartingprice}}</label><br>
        <label>Auction Finish Date: {{itemauctionfinishdate}}</label><br>
        <label>Highest bidder: {{itemauctionhighestbidder}}</label>
    </div> 
    <div class="d-flex flex-row p-2" id="bidding_form">
        <h3>Bid for Item</h3>
        <label class="w-auto m-auto">Email:</label><br>
        <input type="text" v-model="email"><br>

        <label class="w-auto m-auto">Bid:</label><br>
        <input type="number" v-model="item_sprice"><br>

        <button @click="bidItem(keyID+1,email,item_sprice)">Add my Bid</button>
    </div>


</template>

<script lang="ts">

export default {

    props: [ 'itemtitle', 'itemID', 'itemdescription', 'itemstartingprice', 'itemauctionfinishdate', 'itemauctionhighestbidder', 'keyID' ],
    data() {
        return {
            email: '',
            item_sprice: '' as any as number,
            itemsupdated: []
        }
    },
    methods: {
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
        },
        async fetchItems() {
            let response = await fetch("http://127.0.0.1:8000/api/addItems/");       //GET request
            let data = await response.json();
            this.itemsupdated = data;
            console.log("data: ", this.itemsupdated)
        },
    },
    mounted() {
        this.fetchItems()
    }
}

</script>


<!-- <script lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { computed, ComputedRef, defineComponent } from 'vue';
import Header from '../components/Header.vue'

import { isTemplateNode } from '@vue/compiler-core';


export default defineComponent({
    components: {Header},
    setup(){
        const router = useRoute()
        const itemId = computed(() => router.params.id) as ComputedRef<string>
            return {itemId}
        
    },

    data() {
        return {
          items: [],
          item_title: "",
          item_description: "",
          item_sprice: "",
          item_picture: "",
          item_auctionfinish: "",
          email: ""
        };
    },
    methods: {
    async bidItem(email: string, item_sprice: number){
          const updated_data = {
              updated_email: this.email,
              updated_sprice: this.item_sprice,

          }
          await fetch("http://localhost:8000/api/addItems/" , {
              method: "PUT",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(updated_data),
          })
          .then((response) => response.json())
    }
})


const bidForm = document.getElementById('bidding_form');

const currentDate = new Date()
const endDate = item_auctionfinish
// const endDate = datetime.datetime.strptime(item_auctionfinish, "%d/%m/%Y %H:%M")

if (currentDate > endDate){
    console.log("end of bid")
    //remove bid form for item 
    bidForm.style.display = 'none'
    //make last upated price of item be the final price of the item
    item_sprice = updated_sprice
    
    //send email to mf with last bid
}
  

</script> -->