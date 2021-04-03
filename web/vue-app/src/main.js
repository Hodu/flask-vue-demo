import { createApp } from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';

import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';


const Todo = () => import('@/components/todo/Todo')
const routes = [
  { path: '/todo', component:  Todo},
]

const router = new VueRouter({
  routes
})


const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.mount('#app')
