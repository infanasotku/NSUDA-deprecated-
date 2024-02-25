import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/pages/MainPage.vue'
import Auth from '@/pages/AuthPage.vue'

const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/auth/',
        component: Auth,
        props: (route: any) => ({ authCode: route.query.code, authService: route.query.state })
    }
]

const router = createRouter({
    routes, 
    history: createWebHistory()
})

export default router