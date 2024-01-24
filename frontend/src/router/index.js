import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeComponent from '../components/HomeComponent.vue'
import LoginComponent from '../components/LoginComponent.vue'
import RegisterComponent from '../components/RegisterComponent.vue'
import AddPost from '../components/AddPost.vue'
import PostDetail from '../components/PostDetail.vue'
import UpdatePost from '../components/UpdatePost.vue'
import MyPage from '../components/MyPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeComponent
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginComponent
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterComponent
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage
  },
  {
    path: '/postdetail/:id',
    name: 'PostDetail',
    component: PostDetail
  },
  {
    path: '/addpost',
    name: 'AddPost',
    component: AddPost
  },
  {
    path: '/updatepost/:id',
    name: UpdatePost,
    component: UpdatePost
  }
]
const router = new VueRouter({
  mode: 'history',
  routes
})
export default router
