<template>
  <div>
    <h1>Email</h1>
    <div>{{profile['username' as unknown as any]}}</div>
    <button @click="ChangeEmail=!ChangeEmail">Change Email</button><br>
        <div v-if="ChangeEmail==true">
          <input type="text" v-model="new_email">
          <button @click="SaveEmail(profile['id' as unknown as number],new_email)">Change Email</button>
        </div>
    <h1>Date of Birth</h1>
    <div>{{profile['date_of_birth' as unknown as any]}}</div>
    <button @click="ChangeDOB=!ChangeDOB">Change Date of Birth</button><br>
        <div v-if="ChangeDOB==true">
          <input type="date" v-model="new_dob">
          <button @click="SaveDOB(profile['id' as unknown as number],new_dob)">Change D.O.B</button>
        </div>
  </div>
</template>

<script lang="ts">
  export default{
    data() {
        return {
            profile: [] as any[],
            users: [] as any[],
            ChangePic: false as boolean,
            ChangeEmail: false as boolean,
            ChangeDOB: false as boolean,
            new_pic: '' as string,
            new_email: '' as string,
            new_dob: '' as unknown as Date,
        };
    },
    methods: {
        async fetchUsers() {
            let response = await fetch("http://127.0.0.1:8000/api/usertest_api");       //GET request
            let data = await response.json();
            this.users = data;
        },
        async fetchProfile () {
            let fetchingUser = await fetch("http://127.0.0.1:8000/fetchuser/" , {
              credentials: 'include'
            });
            let data = await fetchingUser.json();
            this.profile = data
            console.log("Data", data)
        },
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
          this.fetchProfile()
          alert("Email Changed")
        },

        async SaveDOB(id:number,dob: Date){
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
          this.fetchProfile()
          alert("D.O.B Changed")
        },
        async changeProfilePicture () {
          const formData = new FormData()
          const fileField = document.querySelector('input[type="file"]')

          formData.append('profile', (fileField as any).files[0] );      //JSON object key-value pairs

          fetch('http://127.0.0.1:8000/api/profilepicture' , {
            method: 'POST',
            body: formData
          })
        }
  },
  mounted(){
    //this.fetchUsers(),
    this.fetchProfile()
  },
}
</script>
