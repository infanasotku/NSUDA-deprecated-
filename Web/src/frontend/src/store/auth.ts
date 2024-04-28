import { AuthType, UserOIDCModel } from '@/types'
import { defineStore } from 'pinia'
import axios from 'axios'
import { googleEnv, globalEnv, vkEnv } from '../../env'
import router from '@/router/router'

export const useAuthStore = defineStore('auth', {
    state() {
        return {
            isLoginFormVisible: false,
            authType: AuthType.NoAuth,
            userModel: new UserOIDCModel(),
        }
    },
    actions: {
        async updateAuthState() {
            let resp = await axios.get(globalEnv.apiUri +
                `/auth/default`).catch(() => {
                    this.authType = AuthType.NoAuth
                })
            if (!resp) {
                return;
            }

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
            const params = new URLSearchParams()
            // Default params
            params.append('redirect_uri', globalEnv.redirectUri)
            params.append('response_type', 'code')
            params.append('state', "None")
            switch (authType) {
                case AuthType.Google:
                    const info = axios.get(googleEnv.openIDConfigUri, {
                        withCredentials: false
                    })
                    info.then((value) => {
                        const googleAuthUri = value.data['authorization_endpoint']
                        params.append('client_id', googleEnv.clientID)
                        params.append('scope', googleEnv.scope)
                        params.append('access_type', googleEnv.accessType)
                        window.location.href = googleAuthUri + '?' + params.toString()
                    })
                    break
                case AuthType.VK:
                    params.append('client_id', vkEnv.clientID)
                    params.append('scope', vkEnv.scope)
                    window.location.href = vkEnv.authUri + '?' + params.toString()
                    break

                default:
                    break;
            }
            // Redirect url
        },
        async signOutUser() {
            await axios.post(globalEnv.apiUri +
                `/auth/signout`)
            this.authType = AuthType.NoAuth
        },
        async authenticateUser(authType: AuthType, authCode: string, _: string) {
            switch (authType) {
                case AuthType.Google:
                    this.authenticateUserByGoogle(authCode)
                    break
                case AuthType.VK:
                    //this.authenticateUserByVK(authCode)
                    break
                default:
                    throw new Error('401')
            }
        },
        async authenticateUserByGoogle(authCode: string) {
            let resp = await axios.get(globalEnv.apiUri +
                `/auth/?auth_code=${authCode}`)
                .catch(() => {
                    this.authType = AuthType.NoAuth
                })
            if (!resp) {
                return;
            }

            this.userModel = new UserOIDCModel(
                resp.data['name'],
                resp.data['surname'],
                resp.data['email'],
                resp.data['picture_uri']
            )
            router.push('/')
        },
        async authenticateUserByVK(authCode: string) {
            let resp = await axios.get(globalEnv.apiUri +
                `/auth/?auth_code=${authCode}`)
                .catch(() => {
                    this.authType = AuthType.NoAuth
                })
            if (!resp) {
                return;
            }

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
            switch (type) {
                case 'google':
                    this.authType = AuthType.Google
                    break
                case 'vk':
                    this.authType = AuthType.VK
                    break
            }
        },
    },

})