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
        props: (route: any) => {
            const scope: string = route.query.scope
            if (scope.indexOf('google')) {
                return {
                    authService: 'google',
                    authCode: route.query.code, 
                    sessionSecret: route.query.state
                }
            }
            throw new Error('400')
        },
        
    }
]

const router = createRouter({
    routes, 
    history: createWebHistory()
})

export default router