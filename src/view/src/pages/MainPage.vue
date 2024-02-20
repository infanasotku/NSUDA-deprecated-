<template>
    <div class="hero" :class="{ 'dark-background': isBackgroundVisible }">
        <div class="content">
            <transition-group
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            >
                <loading-icon
                v-show="!isNavigationVisible"
                class="loader"
                :key="'loading-block'"
                ></loading-icon>
            </transition-group>
            <transition-group
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <navigation-panel
                v-show="isNavigationVisible"
                :navigationLinks="navigationInfo"
                :key="'nav-panel'"
                @click="onNavPanelClicked"
                ></navigation-panel>
                <code-block 
                v-show="isTypescriptCodeVisible"
                ref="typescriptCodeRef"
                class="code-segment"
                :stream="true"
                language="typescript" 
                :time="3000"
                :code="typescriptCode"
                :onCodePrinted="activateElements"
                :key="'typescript-block'"
                ></code-block>

            </transition-group>
            <transition
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            >
                <login-form
                v-show="authStore.isLoginFormVisible"
                :key="'login-form'"
                class="form"
                >
                </login-form >
            </transition>
            
            <code-block 
            v-show="!isBackgroundVisible"
            ref="pythonCodeRef"
            class="code-segment"
            :stream="true"
            language="python" 
            :time="3000"
            :code="pythonCode"
            :onCodePrinted="setupBackground"
            ></code-block>
        </div>
    </div>
</template>
<script lang="ts">

import { useAuthStore } from '@/store/auth';
import { defineComponent, ref } from 'vue'
import { FormType } from '@/types';
// Components
import NavigationPanel from '@/components/NavigationPanel.vue';
import CodeBlock from '@/components/CodeBlock.vue';
import LoginForm from '@/components/LoginForm.vue';

export default defineComponent({
    components: {
    NavigationPanel,
    CodeBlock,
    LoginForm
},
    data() {
        return {
            isBackgroundVisible: false,
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
                {
                    id: 3,
                    link: '',
                    content: 'Sign up'
                }
            ],
        }
    },
    methods:
    {
        setupBackground() {
            this.isBackgroundVisible = true
            this.isTypescriptCodeVisible = true
            this.typescriptCodeRef?.start()
        },
        activateElements() {
            this.isNavigationVisible = true
        },
        onNavPanelClicked(data: { id: number}) {
            switch (data.id) {
                // author
                case 1:
                    
                    break;
                // sign in
                case 2:
                    this.authStore.setFormVisibility(true)
                    this.authStore.setFormType(FormType.SignIn)
                    break;
                // sign up
                case 3:
                    this.authStore.setFormVisibility(true)
                    this.authStore.setFormType(FormType.SignUp)
                    break;
                default:
                    break;
            }
        }
    },
    mounted() {
        this.pythonCodeRef?.start()
    },
    setup() {
        const authStore = useAuthStore()
        const pythonCodeRef = ref<InstanceType<typeof CodeBlock>>()
        const typescriptCodeRef = ref<InstanceType<typeof CodeBlock>>()
        return { 
            pythonCodeRef, 
            typescriptCodeRef, 
            authStore, 
            FormType,
        }
    }
})
</script>
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
        position: absolute;
    }

</style>