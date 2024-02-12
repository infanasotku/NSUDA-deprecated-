import { defineStore } from 'pinia';

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false
        }
    },
    getters: {
        checkAuth: (state) => state.isAuth,
    },
    actions: {
        refreshAuthState() {
            
        }
    }
})