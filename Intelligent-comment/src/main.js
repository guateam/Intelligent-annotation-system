import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/store'
import './common/style/index.styl'

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})
