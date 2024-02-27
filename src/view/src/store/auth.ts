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
            sessionSecret: ''
        }
    },
    actions: {
        getSessionSecret() {
            // TODO getting session secret with JWT token
        },
        updateAuthState() {

        },
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
        requestCode(authType: AuthType) {
            switch (authType) {
                case AuthType.Google:
                    const info = axios.get(googleEnv.openIDConfigUri)
                    info.then((value) => {
                        const googleAuthUri = value.data['authorization_endpoint']

                        const params = new URLSearchParams()
                        params.append('client_id', googleEnv.googleClientID)
                        params.append('redirect_uri', googleEnv.redirectUri)
                        params.append('response_type', 'code')
                        params.append('scope', googleEnv.scope)
                        params.append('state', this.sessionSecret)
                        window.location.href = googleAuthUri + '?' + params.toString()
                    })
                    break;
            
                default:
                    break;
            }
            
        },
        async authenticateUser(authType: AuthType, authCode: string, sessionSecret: string) {
            this.authType = authType
            // TODO send code to backend

            
        }
    }
})