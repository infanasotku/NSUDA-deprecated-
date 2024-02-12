<template>
    <div class="hero" :class="{ 'dark-background': isBackgroundVisible }">
        <navigation-panel
            class="non-visible" 
            :class="{ 'smoothly-visible': isNavigationVisible }"
            :navigationLinks="navigationInfo"
        ></navigation-panel>
        <div class="content">
            <code-block
            ref="pythonCodeRef"
            v-if="!isBackgroundVisible"
            class="code-segment"
            :stream="true"
            language="python" 
            :time="4000"
            :code="pythonCode"
            :onCodePrinted="setupBackground"
            :class="{ 'smoothly-non-visible': isBackgroundVisible }"
            ></code-block>
            <!-- <code-block v-if="isBackgroundVisible"
            class="code-segment non-visible"
            :stream="true"
            language="typescript" 
            :time="4000"
            :code="typescriptCode"
            :onCodePrinted="activateElements"
            :class="{ 'smoothly-visible': isBackgroundVisible }"
            ></code-block> -->
            <loading-icon class="loader"></loading-icon>
        </div>
    </div>
</template>
<script lang="ts">
import NavigationPanel from '@/components/NavigationPanel.vue';
import CodeBlock from '@/components/CodeBlock.vue';
import { defineComponent, ref } from 'vue'
import LoadingIcon from '@/components/UI/LoadingIcon.vue';
export default defineComponent({
    components: {
    NavigationPanel,
    CodeBlock,
    LoadingIcon
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
            typescriptCode: `import App from '@/App.vue'
import { createApp } from 'vue'

const app = createApp(App)

app.component('navigarion', Navigation)
app.mount('#app')
            `,

            navigationInfo: [
                {
                    id: 1,
                    link: '/author',
                    content: 'Author'
                },
                {
                    id: 2,
                    link: '/',
                    content: 'Sign in'
                }
            ]
        }
    },
    methods:
    {
        setupBackground() 
        {
            this.isBackgroundVisible = true
        },
        activateElements()
        {
            this.isNavigationVisible = true
        }
    },
    mounted() {
        this.pythonCodeRef?.start()
    },
    setup() {
        const pythonCodeRef = ref<InstanceType<typeof CodeBlock>>()

        return { pythonCodeRef }
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
        margin-bottom: 50px;
    }


    .loader
    {
        position: absolute;
        bottom: 15vh;
    }


    .smoothly-visible
    {
        animation-name: ariving;
        animation-duration: 1s;
        animation-fill-mode: forwards;
    }

    .non-visible
    {
        opacity: 0;
    }

    .smoothly-non-visible
    {
        animation-name: hiding;
        animation-duration: 1s;
        animation-fill-mode: forwards;
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
</style>