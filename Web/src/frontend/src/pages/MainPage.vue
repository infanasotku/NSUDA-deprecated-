<template>
    <div class="hero">
        <div class="content">
            <!-- loading icon -->
            <transition
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            >
                <loading-icon
                v-show="isLoading"
                class="loader"
                :key="'loading-block'"
                ></loading-icon>
            </transition>
            <!-- nav panel -->
            <navigation-panel
            :navigationLinks="navigationInfo"
            :key="'nav-panel'"
            @click="navPanelClicked"
            ></navigation-panel>
            <!-- login form -->
            <transition
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <modal-window
                v-show="authStore.isLoginFormVisible"
                :key="'login-form'"
                class="form"
                @close="authStore.setFormVisibility(false)"
                >
                    <login-form
                    @load="isLoading = true"
                    >
                    </login-form >
                </modal-window>
            
            </transition>
            <!-- User termynal -->
            <transition
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <div 
                id="termynal" 
                data-termynal 
                class="termynal"
                v-show="isAuthGreetings"
                >
                    <span 
                    data-ty-typeDelay="100"
                    data-ty="input" 
                    data-ty-delay="1000"
                    :data-ty-prompt="'' + authStore.userModel.email + ' ~ %'"
                    >Welcome to NSUDA webpage!</span>
                    <span
                    data-ty="output"
                    >Are you sure you want to redirect to account page?</span>
                    <span 
                    data-ty-delay="1000"
                    data-ty-typeDelay="1500"
                    data-ty="input" 
                    data-ty-prompt="(y/n)"
                    >y</span>
                    <span
                    data-ty="progress"
                    data-ty-typeDelay="40"
                    data-ty-delay="500"
                    progressChar="|"
                    ></span>
                </div>
            </transition>
            <!-- NSUDA termynal -->
            <transition
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <nsuda-info
                ref="nsudaInfoRef"
                :isInfoVisible="isNsudaInfoVisible"
                ></nsuda-info>
            </transition>
        </div>
    </div>
</template>
<script lang="ts">

import { useAuthStore } from '@/store/auth';
import { defineComponent, ref } from 'vue'
// Components
import NavigationPanel from '@/components/NavigationPanel.vue';
import LoginForm from '@/components/LoginForm.vue';
import ModalWindow from '@/components/ModalWindow.vue'
import NsudaInfo from '@/components/UI/NsudaInfo.vue'

import { Termynal } from '@/static/js/termynal'
import router from '@/router/router';
import { AuthType } from '@/types';

export default defineComponent({
    components: {
    NavigationPanel,
    LoginForm,
    ModalWindow,
    NsudaInfo
},
    data() {
        return {
            navigationInfo: [
                {
                    id: 1,
                    link: '/author',
                    content: 'Author',
                },
                {
                    id: 2,
                    link: '/downloads',
                    content: 'Downloads'
                },
                {
                    id: 3,
                    link: '',
                    content: 'Sign in',
                }
            ],
            
            isLoading: false,
            
            isAuthGreetings: false,

            isNsudaInfoVisible: false
        }
    },
    methods:
    {
        startNsudaInfo() {
            this.isNsudaInfoVisible = true
            this.nsudaInfoRef?.start()
        },
        navPanelClicked(content: string) {
            switch (content) {
                // author
                case 'Author':
                    
                    break;
                // sign
                case 'Sign in':
                    // sign in
                    this.authStore.setFormVisibility(true)
                    break;
                case 'Sign out':
                    router.push('/signout')
                    break;
                case 'Account':
                    router.push('/account')
                    break;
                default:
                    break;
            }
        }
    },
    mounted() {
        if (this.authStore.authType != AuthType.NoAuth) {
            this.navigationInfo[2].content = 'Account'
            this.navigationInfo[2].link = '/account'
            this.navigationInfo.push({
                id: 3,
                link: '/signout',
                content: 'Sign out'
            })
            this.isAuthGreetings = true
            new Termynal('#termynal', { 
                startDelay: 600,  
                callback: () => {
                    if (this.authStore.authType != AuthType.NoAuth) {
                        router.push('/account')
                    }
                }
            })
        }
        else
        {
            this.startNsudaInfo()
        }
        this.authStore.isPagesLoaded = true
    },
    setup() {
        const authStore = useAuthStore()
        const nsudaInfoRef = ref<InstanceType<typeof NsudaInfo>>()
        
        return { 
            authStore,
            nsudaInfoRef
        }
    }
})
</script>
<style>
@import url('../static/css/termynal.css');
</style>
<style scoped>

    .hero
    {
        font-family: Consolas, Courier New, monospace;
        min-height: 100vh;
        width: 100%;
        display: flex;
        color: rgb(161, 161, 161);
    }

    .content
    {
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .loader
    {
        position: absolute;
        bottom: 15vh;
    }

    .form
    {
        width: 250px;
        height: 150px;
        position: absolute;
        z-index: 10;
    }

    .termynal
    {
        position: absolute;
        height: 250px;
        --tw-shadow: 7px 7px 15px 0 #000;
        box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
    }
</style>