import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import WriteUp from '../views/WriteUp.vue'

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', name: 'Home', component: Home },
  { path: '/writeup', name: 'WriteUp', component: WriteUp }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
