import { AuthType, UserOIDCModel } from '@/types'
import { defineStore } from 'pinia'
import axios from 'axios'
import { googleEnv, globalEnv } from '../../env'
import router from '@/router/router'

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isPagesLoaded: false,
            isAuth: false,
            isLoginFormVisible: false,
            authType: AuthType.NoAuth,
            userModel: new UserOIDCModel(),
            updatingPromise: (async () => {})()
        }
    },
    actions: {
        updateAuthState() {
            this.updatingPromise = this._updateUserModel()
        },
        async _updateUserModel() {
            let resp = await axios.get(globalEnv.apiUri + 
                `/auth/default`).catch(() => {
                    this.isAuth = false
                })
            if (!resp) {
                return;
            }

            this.isAuth = true
            this.userModel = new UserOIDCModel(
                resp.data['name'],
                resp.data['surname'],
                resp.data['email'],
                resp.data['picture_uri'],
            )
            this.validateServiceType(resp.data['service'])
        },
        setFormVisibility(value: boolean) {
            this.isLoginFormVisible = value
        },
        requestCode(authType: AuthType) {
            switch (authType) {
                case AuthType.Google:
                    const info = axios.get(googleEnv.openIDConfigUri, {
                        withCredentials: false
                    })
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
        async signOutUser() {
            await axios.post(globalEnv.apiUri + 
                `/auth/default/signout`)
            this.authType = AuthType.NoAuth
            this.isAuth = false
        },
        async authenticateUser(authType: AuthType, authCode: string, _: string) {
            switch(authType) {
                case AuthType.Google:
                    this.authenticateUserByGoogle(authType, authCode)
                    break;
                default:
                    throw new Error('401')
            }
        },
        async authenticateUserByGoogle(authType: AuthType, authCode: string) {
            let resp = await axios.get(globalEnv.apiUri + 
                `/auth/google/?auth_code=${authCode}`)
                .catch(() => {
                    this.isAuth = false
                })
            if (!resp) {
                return;
            }

            this.isAuth = true
            this.authType = authType
            this.userModel = new UserOIDCModel(
                resp.data['name'],
                resp.data['surname'],
                resp.data['email'],
                resp.data['picture_uri']
            )
            router.push('/')
        },
        //-
        validateServiceType(type: string) {
            switch(type) {
                case 'google':
                    this.authType = AuthType.Google
                    break
            }
        },
    },
    
})