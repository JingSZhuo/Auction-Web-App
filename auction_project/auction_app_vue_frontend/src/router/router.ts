import { createWebHashHistory, createRouter } from "vue-router";  //importing API
import ItemPage from '../views/ItemPage.vue'
import Home from '../views/Home.vue'
import AddItem from '../views/AddItem.vue'
import SignUp from '../views/signup.vue'
import Login from '../views/login.vue'
import AllItems from '../AllItems.vue'

//below: dynamically routed! 
//const Home = import('../views/Home.vue')
//const AllItems = import('../AllItems.vue')
//const ItemPage = import('../views/AddItem.vue')


// const history = createWebHashHistory(); //switches view from hash to history mode

const routes = [
    {
        path: '/home',                  //URL where route can be found
        name: 'Home',               //(optional) name used to link to this route
        component: Home             //component loaded when route is called
    },
    {
        path: '/addItem',
        name: 'AddItem',
        component: AddItem
    },
    {
        path: '/signUp',
        name: 'signup',
        component: SignUp
    },    
    {
        path: '/allItems/:id',
        name: 'ItemPage',
        component: ItemPage
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },

    // {
    //     path: '/allItems/:id',
    //     name: 'ItemPage',
    //     component: ItemPage
    // }
    {
        path: '/allItems',
        name: 'AllItems',
        component: AllItems
    }
    

]

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes
})


export default router;