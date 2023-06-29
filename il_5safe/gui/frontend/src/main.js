import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import axios from 'axios'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import VueAxios from 'vue-axios'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app
    .use(router)
    .use(vuetify)
    .use(VueAxios, axios)
    .provide('axios', app.config.globalProperties.axios)  // provide 'axios'
    .mount('#app')
