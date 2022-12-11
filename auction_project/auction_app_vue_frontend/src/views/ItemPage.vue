<template>
    <h1> Hello i hope this works</h1>
    <h1>{{item_title}}</h1>
    <h3>{{item_description}}</h3>
    <h3>{{item_sprice}}</h3>
    <h3>{{item_auctionfinish}}</h3>
    <div>{{item_picture}}</div>

    <div>
      <h1>Bid for Item</h1>
      <label>Email:</label><br>
      <input type="text" v-model="email"><br>

      <label>Bid:</label><br>
      <input type="number" v-model="item_sprice"><br>

      <button @click="bidItem">Add my Bid</button>
    </div>
</template>


<script lang="ts">
export default ({

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
        async fetchItems() {
            //perorm an Ajax request to fetch the list of item
            let response = await fetch("http://localhost:8000/api/addItems/");
            let data = await response.json();
            this.items = data;
            console.log(this.items);
        },
        async bidItem(email: string, item_sprice: number){
            //Ajax request to say that this is the new item model
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
          this.fetchItems()
        },
    }
})
  

</script>