<template>
    <div>
      <h1>Add An Item</h1>
      <label>Title:</label><br>
      <input type="text" v-model="item_title"><br>
      <label>Description:</label><br>
      <input type="textarea" v-model="item_description"><br>
      <label>Starting Price:</label><br>
      <input type="number" v-model="item_sprice"><br>
      <label>Picture:</label><br>
      <input type="text" v-model="item_picture"><br>
      <label>Date and Time of Auction Finish</label><br>
      <input type="datetime-local" v-model="item_auctionfinish"><br>
      <button @click="postItems">Add New Item</button>
    </div>
</template>


<script lang="ts">

  export default{
    props: ["title"],
    data() {
        return {
          items: [],
          item_title: "",
          item_description: "",
          item_sprice: "",
          item_picture: "",
          item_auctionfinish: "",
        };
    },
    methods: {
        async fetchItems() {
            //perorm an Ajax request to fetch the list of items
            let response = await fetch("http://127.0.0.1:8000/api/addItems/");   //Change to 127.0.0.1
            
            let data = await response.json();
            this.items = data;
            console.log(this.items);
        },
        async postItems(){
          //Ajax request to say that this is the new item model
          const user_form_input = {
              itemTitle: this.item_title,
              itemDescription: this.item_description,
              itemStartingPrice: this.item_sprice,
              itemPicture: this.item_picture,
              itemActionFinish: this.item_auctionfinish
          }
          await fetch("http://127.0.0.1:8000/api/addItems/" , {
              method: "POST",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(user_form_input),
          })
          .then((response) => response.json())
          this.fetchItems()
        },
    }
  }

</script>