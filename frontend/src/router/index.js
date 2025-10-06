import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import WriteUp from '../views/WriteUp.vue';
import Project from '../views/Project.vue';
import PostDetail from '../views/PostDetail.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/writeup',
    name: 'WriteUp',
    component: WriteUp
  },
  {
    path: '/project',
    name: 'Project',
    component: Project
  },
  {
    path: '/post/:name',
    name: 'PostDetail',
    component: PostDetail
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  }
});

export default router;