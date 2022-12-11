<template>

    <body>

        <h1>Signup</h1>

        <br/>

        <input type="email" placeholder="email.." v-model="email_field"> <br><br>

        <input type="date" placeholder="date-of-birth" v-model="date_field"/> <br><br>

        <input type="password" placeholder="password..." v-model="password_field"/> <br><br>

        <input type="text" placeholder="Image..." v-model="image_field"/> <br><br>

        <button @click="submitUserDetails">Signup</button>

    </body>

</template>

<script lang="ts">

export default{

    data(){
        return{
            email_field: "",
            date_field: "",
            password_field: "",
            image_field: ""
        }
    },
    methods: {
        async submitUserDetails() {
            const createNewUserDetails = {
                email: this.email_field as string,
                dob: this.date_field as any,
                password: this.password_field as any,
                image: this.image_field as any,
            }

            try {
                await fetch("http://localhost:8000/signup/" , {
                    method: 'POST',
                    headers: {
                    'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(createNewUserDetails)
                })
                alert("User created")
                console.log("Sent!")
            }
            catch { alert("Error creating a user") }

        }
    }

}

</script>