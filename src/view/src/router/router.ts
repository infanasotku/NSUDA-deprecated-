import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/pages/MainPage.vue'
import Auth from '@/pages/AuthPage.vue'
import User from '@/pages/UserPage.vue'
import SignInStub from '@/components/auth/SignInStub.vue'
import SignOutStub from '@/components/auth/SignOutStub.vue'

import { useAuthStore } from '@/store/auth'

const routes = [
    {
        path: '/signout',
        component: SignOutStub,
    },
    {
        path: '/',
        component: Main,
    },
    {
        path: '/auth/',
        component: SignInStub,
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
    },
    {
        path: '/account',
        component: User
    }
]

const router = createRouter({
    routes, 
    history: createWebHistory(),
})
export default router