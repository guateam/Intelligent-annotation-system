import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import store from './store/store'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import './common/style/index.styl'
import './common/style/my-iview-theme.less'
import global_ from './components/Global/Global.vue'//引用文件
Vue.prototype.GLOBAL = global_//挂载到Vue实例上面
Vue.use(iView);
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)
new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})
