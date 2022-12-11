import { createApp } from 'vue'
import './style.css'
import App from './AllItems.vue'       //Root Component
import 'bootstrap'                           //Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'

import router from "./router/router";        //Using router.ts file



createApp(App).use(router).mount('#app')        //Create Root App with routing
