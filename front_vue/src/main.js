import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Col, Row, Radio } from 'ant-design-vue';
import { VueAxios } from '@/utils/requests'
import 'ant-design-vue/dist/antd.css';
import ECharts from 'vue-echarts'
import { use } from 'echarts/core'
import VueSocketIO from 'vue-socket.io'
import SocketIO from "socket.io-client"
//全局scss
import "./styles/index.scss";
import api from './api'

Vue.config.productionTip = false

Vue.use(VueAxios)

var VueTouch = require('vue-touch')
Vue.use(VueTouch, {name: 'v-touch'})
Vue.use(Col)
Vue.use(Row)
Vue.use(Radio)

// import ECharts modules manually to reduce bundle size
import {
  CanvasRenderer
} from 'echarts/renderers'
import {
  GaugeChart,LineChart
} from 'echarts/charts'
import {
  GridComponent,
  LegendComponent,
  DataZoomComponent,
  TooltipComponent
} from 'echarts/components'

use([
  CanvasRenderer,
  GaugeChart,LineChart,
  GridComponent,
  LegendComponent,
  DataZoomComponent,
  TooltipComponent
]);

// register globally (or you can do it locally)
Vue.component('v-chart', ECharts)
Vue.prototype.$api = api;

VueTouch.config.swipe = {
  threshold:50  //设置左右滑动的距离
}

const socketOptions = {
  autoConnect: false,       // 自动连接     这里为我项目需求  需要在指定情况下才连接socket
}

// 注册
Vue.use(
  new VueSocketIO({
    debug: true ,   // debug调试，生产建议关闭
    connection: SocketIO("127.0.0.1:13140/test_conn", socketOptions),
  })
)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
