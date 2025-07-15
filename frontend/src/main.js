import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import Vue3Toastify from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

const app = createApp(App)
app.use(Vue3Toastify, {
  autoClose: 2500,
  position: 'top-center',
})
app.mount('#app')
