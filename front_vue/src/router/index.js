import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/clock'
  },
  {
    path: '/clock',
    name: 'Clock',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/Clock.vue')
  },
  {
    path: '/dashboard',
    name: 'DashBoard',
    component: () => import('@/views/DashBoard.vue')
  },
  {
    path: '/historyChart',
    name: 'HistoryChart',
    component: () => import('@/views/HistoryChart.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
