import { AuthType } from '@/types'
import { defineStore } from 'pinia'
import axios from 'axios'
import { googleEnv, globalEnv } from '../../env'

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
                    const info = axios.get(googleEnv.openIDConfigUri)
                    info.then((value) => {
                        const googleAuthUri = value.data['authorization_endpoint']

                        const params = new URLSearchParams()
                        params.append('client_id', googleEnv.googleClientID)
                        params.append('redirect_uri', googleEnv.redirectUri)
                        params.append('response_type', 'code')
                        params.append('scope', googleEnv.scope)
                        params.append('state', "None")
                        params.append('access_type', googleEnv.accessType)
                        window.location.href = googleAuthUri + '?' + params.toString()
                    })
                    break;
            
                default:
                    break;
            }
            
        },
        async authenticateUser(authType: AuthType, authCode: string, _: string) {
            this.authType = authType
            switch(this.authType) {
                case AuthType.Google:
                    this.authenticateUserByGoogle(authCode)
                    break;
                default:
                    throw new Error('401')
            }
        },
        async authenticateUserByGoogle(authCode: string) {
            let res = axios.get(globalEnv.apiUri + 
                `/auth/google/?auth_code=${authCode}`)
            // TODO send code to backend
            console.log(res)
            
        }
    }
})