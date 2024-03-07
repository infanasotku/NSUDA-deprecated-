import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/pages/MainPage.vue'
import User from '@/pages/UserPage.vue'
import SignInStub from '@/components/auth/SignInStub.vue'
import SignOutStub from '@/components/auth/SignOutStub.vue'

import { useAuthStore } from '@/store/auth'

const routes = [
    // SignOut
    {
        path: '/signout',
        component: SignOutStub,
    },
    // Main
    {
        path: '/',
        component: Main,
        beforeEnter: async () => {
            const authStore = useAuthStore()
            await authStore.updateAuthState()
        }
    },
    // Auth
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
    // Account
    {
        path: '/account',
        component: User,
        beforeEnter: async () => {
            const authStore = useAuthStore()
            await authStore.updateAuthState()
        }
    }
]

const router = createRouter({
    routes, 
    history: createWebHistory(),
})
export default router