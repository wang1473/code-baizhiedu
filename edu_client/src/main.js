import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.prototype.$axios = axios;

import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element);

import "./static/css/global.css"

Vue.config.productionTip = false

import settings from "./settings"

Vue.prototype.$settings = settings;
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
