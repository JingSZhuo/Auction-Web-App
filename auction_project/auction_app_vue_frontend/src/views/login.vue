<template>

    <body>

    <h1>Login</h1>

    <br/>

    <input type="email" placeholder="email.." v-model="email_field"> <br><br>

    <input type="password" placeholder="password..." v-model="password_field"/> <br><br>

    <button @click="redirect">Check</button>
    <button @click="Login">Login</button>
    <button @click="logout">Logout</button>

    </body>

</template>

<script lang="ts">

   export default {

    data() {
        return {
            email_field: "",
            password_field: "",
        }
    },

    methods: {
        async Login () {
            const loginDetails = {
                email: this.email_field,
                password: this.password_field
            }

            await fetch('http://127.0.0.1:8000/login/' , { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(loginDetails),
                credentials: 'include',                  //Include credentials
                mode: 'cors',
            })
        },
        async redirect () {                          //To test login/logout status

            await fetch('http://127.0.0.1:8000/redirect/' , { 
                method: 'GET',
                mode: 'cors',
                })
                
        },
        async logout () {

            await fetch('http://127.0.0.1:8000/logout/' , { 
                method: 'GET',
                mode: 'cors',
                credentials: 'include',               //Include credentials
                })
            },
        }
    }

</script>