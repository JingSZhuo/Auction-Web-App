import { createApp } from 'vue'
import './style.css'
import App from './AllItems.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import router from "./router/router";



createApp(App).use(router).mount('#app')
