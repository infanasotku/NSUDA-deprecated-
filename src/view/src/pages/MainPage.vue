<template>
    <div class="hero" :class="{ 'dark-background': isBackgroundVisible }">
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
            <!-- nav panel; ts/py code -->
            <transition-group
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <navigation-panel
                v-show="isNavigationVisible"
                :navigationLinks="navigationInfo"
                :key="'nav-panel'"
                @click="navPanelClicked"
                ></navigation-panel>
                <code-block 
                v-show="isTypescriptCodeVisible"
                ref="typescriptCodeRef"
                class="code-segment"
                language="typescript" 
                :time="3000"
                :code="typescriptCode"
                :onCodePrinted="activateElements"
                :key="'typescript-block'"
                ></code-block>
                <code-block 
                v-show="isPythonCodeVisible"
                ref="pythonCodeRef"
                class="code-segment"
                language="python" 
                :time="3000"
                :code="pythonCode"
                :onCodePrinted="setupBackground"
                ></code-block>
            </transition-group>
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
            <!-- termynal -->
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
                data-ty-startDelay="200" 
                data-ty-cursor="▋"
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
        </div>
    </div>
</template>
<script lang="ts">

import { useAuthStore } from '@/store/auth';
import { defineComponent, ref } from 'vue'
// Components
import NavigationPanel from '@/components/NavigationPanel.vue';
import CodeBlock from '@/components/CodeBlock.vue';
import LoginForm from '@/components/LoginForm.vue';
import ModalWindow from '@/components/ModalWindow.vue'

import { Termynal } from '@/static/js/termynal'
import router from '@/router/router';
import { AuthType } from '@/types';

export default defineComponent({
    components: {
    NavigationPanel,
    CodeBlock,
    LoginForm,
    ModalWindow
},
    data() {
        return {
            isBackgroundVisible: false,
            isPythonCodeVisible: false,
            pythonCode: `from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return 'Background'`,

            isNavigationVisible: false,
            isTypescriptCodeVisible: false,
            typescriptCode: `import App from '@/App.vue'
import { createApp } from 'vue'

const app = createApp(App)

app.component('navigarion', Navigation)
app.mount('#app')`,

            navigationInfo: [
                {
                    id: 1,
                    link: '/author',
                    content: 'Author',
                },
                {
                    id: 2,
                    link: '',
                    content: 'Sign in',
                },
            ],
            
            isLoading: false,
            
            isAuthGreetings: false
        }
    },
    methods:
    {
        setupBackground() {
            this.isBackgroundVisible = true
            this.isPythonCodeVisible = false
            this.isTypescriptCodeVisible = true
            this.typescriptCodeRef?.start(true)
        },
        activateElements() {
            this.isNavigationVisible = true
            this.isLoading = false
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
            this.navigationInfo[1].content = 'Account'
            this.navigationInfo[1].link = '/account'
            this.navigationInfo.push({
                id: 3,
                link: '/signout',
                content: 'Sign out'
            })
            this.isNavigationVisible = true
            this.isBackgroundVisible = true
            this.isAuthGreetings = true
            let termynal = new Termynal('#termynal', { 
            startDelay: 600,  
            noInit: true,
            callback: () => {
                if (this.authStore.authType != AuthType.NoAuth) {
                    router.push('/account')
                }
            }
            })
            termynal.init()
        }
        else
        {
            if (this.authStore.isPagesLoaded) {
                this.isNavigationVisible = true
                this.isBackgroundVisible = true
                this.typescriptCodeRef?.start(false)
                this.isTypescriptCodeVisible = true
            }
            else
            {
                this.isLoading = true
                this.isPythonCodeVisible = true
                this.pythonCodeRef?.start(true)
            }
        }
        this.authStore.isPagesLoaded = true
    },
    setup() {
        const authStore = useAuthStore()
        const pythonCodeRef = ref<InstanceType<typeof CodeBlock>>()
        const typescriptCodeRef = ref<InstanceType<typeof CodeBlock>>()
        
        return { 
            pythonCodeRef, 
            typescriptCodeRef, 
            authStore
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
        min-height: 100vh;
        width: 100%;
        color: white;
        display: flex;
        background-color: rgb(255, 255, 255);
    }

    .dark-background
    {
        animation-name: coloring;
        animation-duration: 1s;
        animation-fill-mode: forwards;
    }

    @keyframes coloring
    {
        to
        {
            background-color: rgb(36, 33, 33);
        }
    }

    .content
    {
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }
    .code-segment
    {
        width: 600px;
    }

    .loader
    {
        position: absolute;
        bottom: 15vh;
    }

    @keyframes ariving
    {
        to
        {
            opacity: 1;
        }
    }

    @keyframes hiding
    {
        to
        {
            opacity: 0;
        }
    }


    .form
    {
        width: 250px;
        height: 150px;
        position: absolute;
    }

    .termynal
    {
        position: absolute;
        height: 250px;
        --tw-shadow: 7px 7px 15px 0 #000;
        box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
    }

</style>