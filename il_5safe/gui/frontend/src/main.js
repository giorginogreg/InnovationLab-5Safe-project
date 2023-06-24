import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';


const app = createApp(App)
    app.use(router)
    .use(VueAxios, axios)
    .provide('axios', app.config.globalProperties.axios)  // provide 'axios'
    .mount('#app')
