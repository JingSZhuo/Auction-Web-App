<template>
    <!-- <h1> Hello i hope this works</h1>
    <h1>{{item_title}}</h1>
    <h3>{{item_description}}</h3>
    <h3>{{item_sprice}}</h3>
    <h3>{{item_auctionfinish}}</h3>
    <div>{{item_picture}}</div>

    <div id="bidding_form">
      <h1>Bid for Item</h1>
      <label>Email:</label><br>
      <input type="text" v-model="email"><br>

      <label>Bid:</label><br>
      <input type="number" v-model="item_sprice"><br>

      <button @click="bidItem">Add my Bid</button>
    </div> -->


</template>


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