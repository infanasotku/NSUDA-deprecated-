import { FormType, UserAuthData } from '@/types';
import { defineStore } from 'pinia';
import axios from 'axios'

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false,
            isLoginFormVisible: false,
            loginFormType: FormType.SignIn,
            username: '',
            password: ''
        }
    },
    actions: {
        async authUser(userData: UserAuthData) {
            await axios.post('/api', userData).
            then(resp => {
                const token = resp.data.token
                localStorage.setItem('user-token', token)
            }).
            catch(() => {
                localStorage.removeItem('user-token')
            })
            this.isAuth = true
        },
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
        setFormType(value: FormType) {
            this.loginFormType = value
        },
        setUsername(value: string) {
            this.username = value
        },
        setPassword(value: string) {
            this.password = value
        }
    }
})