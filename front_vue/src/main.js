import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
//全局scss
import "./styles/index.scss";

Vue.config.productionTip = false

var VueTouch = require('vue-touch')
Vue.use(VueTouch, {name: 'v-touch'})

VueTouch.config.swipe = {
  threshold:50  //设置左右滑动的距离
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
