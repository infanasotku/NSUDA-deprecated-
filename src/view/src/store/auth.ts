import { AuthType } from '@/types'
import { defineStore } from 'pinia'
import axios from 'axios'
import { googleEnv } from '../../env'

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false,
            isLoginFormVisible: false,
            authType: AuthType.NoAuth,
        }
    },
    actions: {
        updateAuthState() {

        },
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
        requestCode(authType: AuthType) {
            switch (authType) {
                case AuthType.Google:
                    const params = new URLSearchParams()
                    params.append('client_id', googleEnv.googleClientID)
                    params.append('redirect_uri', googleEnv.redirectUri)
                    params.append('response_type', 'code')
                    params.append('scope', googleEnv.scope)
                    params.append('state', 'google')
                    window.location.href = googleEnv.googleAuthUri + '?' + params.toString()
                    break;
            
                default:
                    break;
            }
            
        },
        authenticateUser(authType: AuthType, authCode: string) {
            this.authType = authType
            
            
        }
    }
})