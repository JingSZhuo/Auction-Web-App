import { createWebHashHistory, createRouter, RouteRecordRaw } from "vue-router";  //importing API
// import AllItems from '../AllItems.vue'
import Home from '../views/Home.vue'
import AddItem from '../views/AddItem.vue'

//below: dynamically routed! 
//const Home = import('../views/Home.vue')
//const AllItems = import('../AllItems.vue')
//const ItemPage = import('../views/AddItem.vue')


// const history = createWebHashHistory(); //switches view from hash to history mode

const routes: Array<RouteRecordRaw> = [
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
    // {
    //     path: '/allItems/:id',
    //     name: 'ItemPage',
    //     component: ItemPage
    // }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})


export default router;