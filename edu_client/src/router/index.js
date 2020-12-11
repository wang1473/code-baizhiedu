import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from "@/views/Login";
import Register from "@/views/Register";
import Course from "@/views/Course";
import CourseDetail from "@/views/CourseDetail";
import Cart from "@/views/Cart";

Vue.use(VueRouter)

const routes = [
    {path: '/', redirect: '/home'},
    {path: '/home', name: 'Home', component: Home},
    {path: '/login', name: 'Login', component: Login},
    {path: '/register', name: 'Register', component: Register},
    {path: '/course', name: 'Course', component: Course},
    {path: '/courseDetail/:id', name: 'CourseDetail', component: CourseDetail},
    {path: '/cart', name: 'Cart', component: Cart},
]

const router = new VueRouter({
    routes
})

export default router
