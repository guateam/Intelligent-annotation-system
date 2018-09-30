import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/store'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import './common/style/index.styl'

Vue.use(iView);

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})
