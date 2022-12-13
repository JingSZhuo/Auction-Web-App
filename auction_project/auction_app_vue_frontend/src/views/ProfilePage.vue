<template>
  <div v-for="(user, user_id) in (users['users' as unknown as number])" :key="user_id">
    <h1>User Profile</h1>
    <div>{{user['user_profilePicture']}}</div>
    <button @click="ChangePic=!ChangePic">Change Profile Picture</button><br>
    <div v-if="ChangePic==true">
      <input type="text" v-model="new_pic">
      <!-- <button @click="SavePic(user.id,user.new_pic)"></button> -->
    </div>
    <h3>Email</h3>
    <div>{{user['user_email']}}</div>
    <button @click="ChangeEmail=!ChangeEmail">Change Email</button><br>
    <div v-if="ChangeEmail==true">
      <input type="text" v-model="new_email">
      <button @click="SaveEmail(user.id,user.new_email)"></button>
    </div>
    <h3>Date of Birth</h3>
    <div>{{user['user_dob']}}</div>
    <button @click="ChangeDOB=!ChangeDOB">Change Date of Birth</button><br>
    <div v-if="ChangeDOB==true">
      <input type="date" v-model="new_dob">
      <button @click="SaveDOB(user.id,user.new_dob)"></button>
    </div>
  </div>
</template>

<script lang="ts">
  export default{
    data() {
        return {
            users: [] as any[],
            ChangePic: false as boolean,
            ChangeEmail: false as boolean,
            ChangeDOB: false as boolean,
            new_pic: '' as string,
            new_email: '' as string,
            new_dob: '' as unknown as Date
        };
    },
    methods: {
      async fetchUsers() {
            let response = await fetch("http://127.0.0.1:8000/api/usertest_api");       //GET request
            let data = await response.json();
            this.users = data;
        },
        // async SavePic(id:number,pic: string){
        //   const updated_pic = {
        //     user_id:id,
        //     user_pic:pic

        //   }
        //   await fetch("http://127.0.0.1:8000/api/usertest_api" , {
        //       method: "PUT",
        //       headers: {
        //           'Content-Type': 'application/json',
        //       },
        //       body: JSON.stringify(updated_pic),
        //   })
        //   .then((response) => response.json())
        //   this.fetchUsers()
        // },

        async SaveEmail(id:number,email: string){
          const updated_email = {
            user_id:id,
            user_email:email

          }
          await fetch("http://127.0.0.1:8000/api/useremail_api" , {
              method: "PUT",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(updated_email),
          })
          .then((response) => response.json())
          this.fetchUsers()
        },

        async SaveDOB(id:number,dob: string){
          const updated_dob = {
            user_id:id,
            user_dob:dob

          }
          await fetch("http://127.0.0.1:8000/api/userdob_api" , {
              method: "PUT",
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(updated_dob),
          })
          .then((response) => response.json())
          this.fetchUsers()
        }
  },
  mounted(){
    this.fetchUsers()
  },
}
</script>
