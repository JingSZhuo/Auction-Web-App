<template>
    <div>
      <h1 class="display-3">Add An Item</h1>

      <div class="p-5 border border-primary">
      <form class="d-flex justify-content-center ">
        <label class="p-2"><strong>Item Name:</strong> </label><br>
        <input type="text" v-model="item_title" placeholder="Enter Item Name"><br/>
      </form>

      <br/>
      
      <form class="d-flex justify-content-center">
        <label class="p-2"><strong>Description:</strong></label><br>
        <textarea rows="5" v-model="item_description" placeholder="Enter Description" w-75></textarea><br>
      </form>

      <br/>

      <form class="d-flex justify-content-center">
        <label class="p-2"><strong> Starting Price:</strong></label><br>
        <input type="number" v-model="item_sprice"><br>
      </form>

      
      <br/>

      <form class="d-flex justify-content-center">
        <label class="p-2"><strong> Date and Time of Auction Finish</strong></label><br/>
        <input type="datetime-local" v-model="item_auctionfinish"><br/>
      </form>
      </div>
      
      
      <br/>
      <button class="btn btn-primary btn-lg btn btn-success" @click="postItems">Add New Item</button>
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
          alert("Posted item")
        },
    }
  }

</script>