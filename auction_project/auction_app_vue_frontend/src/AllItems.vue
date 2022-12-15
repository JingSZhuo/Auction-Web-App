<template>

    <div>
        <br/>
        <h1>All Items</h1>
        <!-- <Header></Header> -->
        <label>Search: </label>
        <input type="text" v-model="search">
        
    </div>
    <div>
        <table class="table border border-success w-100">
            <tr class="table border border-warning ">
                <th style="width: 10%;">ID</th>
                <th style="width: 10%;">Title</th>
                <th style="width: 20%;">Description</th>
                <th style="width: 10%;">Price</th>
                <th style="width: 10%;">Picture</th>
                <th style="width: 10%;">Auction-End-Date</th>
                <th style="width: 10%;">Highest Bidder</th>
            </tr>
        </table>
        <div v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
            <!-- <div v-if="CheckDateTime(item.item_auctionfinish)==true">  -->
                <div v-if="search!=''">
                    <div class="d-flex flex-column" v-if="(((item.item_title.toLowerCase().search(search.toLowerCase()))!=-1 || (item.item_description.toLowerCase().search(search.toLowerCase()))!=-1) && CheckDateTime(item.item_auctionfinish)==true)">
                        <div class="d-flex flex-row p-2">
                            <div class="mx-3"> {{item.id}}</div>
                            <div class="mx-3"> {{item.item_title}}</div>
                            <div class="mx-3"> {{item.item_description}}</div>
                            <div class="mx-3"> {{item.item_sprice}}</div>
                            <div class="mx-3"> {{item.item_picture}}</div>
                            <div class="mx-3"> {{item.item_auctionfinish}}</div>
                            <div class="mx-3"> {{item.item_personHighestBid}}</div>
                        </div>

                        <div class="d-flex flex-row p-2"  id="bidding_form">
                            <h3>Bid for Item</h3>
                            <label class="w-auto m-auto" >Email:</label><br>
                            <input type="text" v-model="email"><br>
    
                            <label class="w-auto m-auto">Bid:</label><br>
                            <input type="number" v-model="item_sprice"><br>

                            <button @click="bidItem(item_id+1,email,item_sprice)">Add my Bid</button>
                        </div>
                        <div class="d-flex flex-row p-2"  id="bidding_form">
                            <button @click="seeChat=!seeChat">See Chat</button>
                            <div v-if="seeChat">
                                <input type="text">
                                <button>Post</button>
                            </div>
                        </div>
                    </div>
                    
                </div> 
            <!-- </div> -->
                <div class="d-flex flex-column" v-else>
                    <div v-if="CheckDateTime(item.item_auctionfinish)==true">
                    <table class="table border border-success w-100">
                        
                        <tr>
                            <td style="width: 10%; word-wrap: break-word;" > {{item.id}}</td>
                            <td style="width: 10%; word-wrap: break-word;" > {{item.item_title}}</td>
                            <td style="width: 20%; word-wrap: break-word;"> {{item.item_description}}</td>
                            <td style="width: 10%; word-wrap: break-word;"> {{item.item_sprice}}</td>
                            <td style="width: 10%; word-wrap: break-word;"> {{item.item_picture}}</td>
                            <td style="width: 10%; word-wrap: break-word;"> {{item.item_auctionfinish}}</td>
                            <td style="width: 10%; word-wrap: break-word;"> {{item.item_personHighestBid}}</td>
                        </tr>
                    </table>
                    <div class="d-flex flex-row p-2" id="bidding_form">
                            <h3>Bid for Item</h3>
                            <label class="w-auto m-auto">Email:</label><br>
                            <input type="text" v-model="email"><br>

                            <label class="w-auto m-auto">Bid:</label><br>
                            <input type="number" v-model="item_sprice"><br>

                            <button @click="bidItem(item_id+1,email,item_sprice)">Add my Bid</button>
                    </div>
                    <div class="d-flex flex-row p-2"  id="bidding_form">
                            <button @click="seeChat=!seeChat">See Chat</button>
                            <div v-if="seeChat">
                                <div> <!--loop through questions-->
                                    <div><!--loop through answers-->
                                        <div><!--Check if foreign key matches-->
                                            <input type="text">
                                            <button>Post</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                </div>
        </div>
        </div>
    </div>
    <!-- <div v-for="(item, item_id) in (items['items' as unknown as number])" :key="item_id">
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
    </div> -->
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
var expired:boolean

    export default{
    data() {
        return {
            items: [] as any[],
            search: '' as any,
            email: '' as string,
            item_sprice: 0 as number,
            seeChat: false as boolean      
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://127.0.0.1:8000/api/addItems/");       //GET request
            let data = await response.json();
            this.items = data;
            console.log("data: ", this.items)
        },
        CheckDateTime(finish:Date){
            const now= new Date()
            const nowInMs= new Date(now).getTime()
            console.log(nowInMs)
            const aucFinish=new Date(finish).getTime()
            console.log(aucFinish)
            

            var flag='something'
            
            if (nowInMs < aucFinish){
                flag='true'
                console.log(flag)
                return true
            }
            else{
                flag='false'
                console.log(flag)
                return false
            }
                
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
}

</script>