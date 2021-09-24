import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Col, Row, Radio } from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
import ECharts from 'vue-echarts'
import { use } from 'echarts/core'
//全局scss
import "./styles/index.scss";

Vue.config.productionTip = false

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

VueTouch.config.swipe = {
  threshold:50  //设置左右滑动的距离
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
