import { createWebHashHistory, createRouter, RouteRecordRaw } from "vue-router";  //importing API
// import AllItems from '../AllItems.vue'

//below: dynamically routed! 
const Home = import('../views/Home.vue')
const AllItems = import('../AllItems.vue')
const ItemPage = import('../views/AddItem.vue')


// const history = createWebHashHistory(); //switches view from hash to history mode

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',                  //URL where route can be found
        name: 'Home',               //(optional) name used to link to this route
        component: Home             //component loaded when route is called
    },
    {
        path: '/allItems/',
        name: 'AllItems',
        component: AllItems
    },
    {
        path: '/allItems/:id',
        name: 'ItemPage',
        component: ItemPage
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})


// const router = createRouter({
//     history,
//     routes: [               //array of routes
//         {
//             path: '/',
//             component: AllItems
//         },
//         {
//             path:'/ItemPage/:item.id',
//             component: ItemPage,
//         }
//     ]
// })

export default router ;