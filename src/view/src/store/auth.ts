import { defineStore } from 'pinia';

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false,
            isLoginFormVisible: false,
        }
    },
    actions: {
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
    }
})