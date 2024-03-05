import { AuthType, UserOIDCModel } from '@/types'
import { defineStore } from 'pinia'
import axios from 'axios'
import { googleEnv, globalEnv } from '../../env'
import router from '@/router/router'

export const useAuthStore =  defineStore('auth', {
    state() {
        return {
            isAuth: false,
            isLoginFormVisible: false,
            authType: AuthType.NoAuth,
            userModel: new UserOIDCModel()
        }
    },
    actions: {
        async updateAuthState() {
            switch(this.authType) {
                case AuthType.Google:
                    let res = await axios.get(globalEnv.apiUri + 
                        `/auth/google`)
        
                    if (res.status == 200) {
                        this.isAuth = true
                        this.userModel = new UserOIDCModel(
                            res.data['name'],
                            res.data['surname'],
                            res.data['email'],
                            res.data['picture_uri']
                        )
                    }
                    else {
                        this.isAuth = false
                    }
                    break
                case AuthType.NoAuth:
                    return
            }
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
        async signOutUser() {
            switch(this.authType) {
                case AuthType.Google:
                    await axios.get(globalEnv.apiUri + 
                        `/auth/google/signout`)
                    this.authType = AuthType.NoAuth
                    break
                case AuthType.NoAuth:
                    return
            }
            
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
            let res = await axios.get(globalEnv.apiUri + 
                `/auth/google/?auth_code=${authCode}`)

            if (res.status == 200) {
                this.isAuth = true
                this.authType = authType
                this.userModel = new UserOIDCModel(
                    res.data['name'],
                    res.data['surname'],
                    res.data['email'],
                    res.data['picture_uri']
                )
            }
            router.push('/')
        }
    }
})