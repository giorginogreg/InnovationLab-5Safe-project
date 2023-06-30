
import UploadForm from '../components/UploadForm.vue'
import ResultView from '../components/ResultView.vue'
import {createRouter, createWebHashHistory} from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'UploadForm',
    component: UploadForm
  },
  {
    path: '/result',
    name: 'Result',
    component: ResultView,
    props: route => ({ resultUrl: route.query.resultUrl })
  }
]
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history:  createWebHashHistory(),
  routes, // short for `routes: routes`
})
export default router
