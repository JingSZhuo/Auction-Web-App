<template>

    <div>
        <h1 class="display-2">All Items</h1>
        <form>
            <label class="p-2"><strong>Search: </strong></label>
            <input class="p-2  border" type="text" placeholder="Search Items here" v-model="search">
        </form>        
        <br/>
    </div>

    <div class="text-bg-light">
        <table class="table border border-success mx-auto">
            <tr class="table border border-dark bg-warning">
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
                            <button @click="SeeChat()">See Chat</button>
                            <div v-if="seeChat==true">
                                text
                                <div v-for="(question, question_id) in (questions['questions' as unknown as number])" :key="question_id"> <!--loop through questions-->
                                    <div><!--loop through answers-->
                                        <div><!--Check if foreign key matches-->
                                            {{question['question_text']}}
                                            <input type="text" v-model="question_text">
                                            <button @click="postQuestions(question_text,item.id)">Post</button>
                                        </div>
                                    </div>
                                </div>
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
                    <hr/>
                    <!-- <ItemPage               
                        :keyID="item_id"
                        :itemID=" item['id' as unknown as number]"
                        :itemtitle="item['item_title' as unknown as string]"
                        :itemdescription="item['item_description' as unknown as string]"
                        :itemstartingprice="item['item_sprice' as unknown as string]"
                        :itemauctionfinishdate="item['item_auctionfinish' as unknown as any]"
                        :itemauctionhighestbidder="item['item_personHighestBid' as unknown as string]"
                    /> -->
                    <hr/>


                    <div class="d-flex flex-row p-2" id="bidding_form">
                            <h3>Bid for Item</h3>
                            <label class="w-auto m-auto">Email:</label><br>
                            <input type="text" v-model="email"><br>

                            <label class="w-auto m-auto">Bid:</label><br>
                            <input type="number" v-model="item_sprice"><br>

                            <button @click="bidItem(item_id+1,email,item_sprice)">Add my Bid</button>
                    </div>
                    <div class="d-flex flex-row p-2"  id="bidding_form">
                            <button @click="SeeChat()">See Q&A</button>
                            <div v-if="seeChat==true">
                                <div v-for="(question, question_id) in (questions['questions' as unknown as number])" :key="question_id"> <!--loop through questions-->
                                        {{question['question_text']}}
                                        <div v-for="(answer, answer_id) in (answers['answers' as unknown as number])" :key="answer_id"><!--loop through answers-->
                                            <!-- <div v-if="answer.question==question.id">Check if foreign key matches -->
                                            {{answer['answers']}} 
                                            
                                            <!-- </div> -->
                                        </div>
                                        <input type="text" v-model="answer_text">
                                        <button @click="postAnswers(answer_text,question.id)">Post Answer</button>
                                </div>
                                <input type="text" v-model="question_text">
                                <button @click="postQuestions(question_text,item.id)">Post Question</button>
                                
                            </div>
                            <!-- <input type="text" v-model="question_text">
                            <button @click="postQuestions(question_text,item.id)">Post</button> -->
                        </div>
                    </div>
                </div>
            </div>
    </div>

    
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
import Header from './components/Header.vue'
var expired:boolean
import ItemPage from './views/ItemPage.vue'
    export default{

    components: {
        ItemPage,
    }   , 
    data() {
        return {
            items: [] as any[],
            search: '' as any,
            email: '' as string,
            item_sprice: 0 as number,
            seeChat: false as boolean,
            questions: [] as any[],
            question_text: "" as string,  
            answers: [] as any[],   
            answer_text: "" as string 
        };
    },
    methods: {
        async fetchItems() {
            let response = await fetch("http://127.0.0.1:8000/api/addItems/");       //GET request
            let data = await response.json();
            this.items = data;
            console.log("data: ", this.items)
        },
        async fetchQuestion() {
            let response = await fetch("http://127.0.0.1:8000/api/addQuestions_api/");       //GET request
            let data = await response.json();
            this.questions = data;
            console.log("data: ", this.questions)
        },
        SeeChat(){
            this.seeChat= (!this.seeChat)
            this.fetchQuestion()
            this.fetchAnswer()
        },
        async fetchAnswer() {
            let response = await fetch("http://127.0.0.1:8000/api/addAnswers_api/");       //GET request
            let data = await response.json();
            this.answers = data;
            console.log("data: ", this.answers)
        },
        async postQuestions(question_text: string, itemID: number){
          //Ajax request to say that this is the new item model
          const user_form_input = {
            questionText: question_text,
            itemForeignKey: itemID,
          }
          await fetch("http://127.0.0.1:8000/api/addQuestions_api/" , {
              method: "POST",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(user_form_input),
          })
          .then((response) => response.json())
          this.fetchQuestion()
        },
        async postAnswers(answer_text: string, QuestionID: number){
          //Ajax request to say that this is the new item model
          const user_form_input = {
            answerText: answer_text,
            questionForeignKey: QuestionID,
          }
          await fetch("http://127.0.0.1:8000/api/addAnswers_api/" , {
              method: "POST",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(user_form_input),
          })
          .then((response) => response.json())
          this.fetchAnswer()
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