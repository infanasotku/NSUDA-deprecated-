import { createRouter, createWebHistory } from 'vue-router'
import SignInStub from '@/components/auth/SignInStub.vue'
import SignOutStub from '@/components/auth/SignOutStub.vue'
import LazyPageWrapper from '@/pages/LazyPageWrapper.vue'

const routes = [
    // SignOut
    {
        path: '/signout',
        component: SignOutStub,
    },
    // Main
    {
        path: '/',
        component: LazyPageWrapper,
        props: {
            page: 'MainPage.vue'
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
        component: LazyPageWrapper,
        props: {
            page: 'UserPage.vue'
        }
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})
export default router