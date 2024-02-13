import { FormType } from '@/types';
import { defineStore } from 'pinia';

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false,
            isLoginFormVisible: false,
            loginFormType: FormType.SignIn
        }
    },
    actions: {
        refreshAuthState() {
            
        },
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
        setFormType(value: FormType) {
            this.loginFormType = value
        }
    }
})