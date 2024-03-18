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
                ></loading-icon>
            </transition>
            <!-- ts code -->
            <transition
            enter-active-class="fade-enter-active"
            enter-from-class="fade-enter"
            enter-to-class="fade-enter-to"
            leave-active-class="fade-leave-active"
            leave-to-class="fade-leave-to"
            >
                <code-block 
                v-show="isTypescriptCodeVisible"
                ref="typescriptCodeRef"
                class="code-segment"
                language="typescript" 
                :time="3000"
                :code="typescriptCode"
                :onCodePrinted="codePrinted"
                ></code-block>
            </transition>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, ref } from 'vue'
// Components
import CodeBlock from '@/components/CodeBlock.vue';

export default defineComponent({
    components: {
        CodeBlock,
    },
    emits: [
        'load'
    ],
    data() {
        return {
            isBackgroundVisible: false,
            isTypescriptCodeVisible: false,
            typescriptCode: `import App from '@/App.vue'
import { createApp } from 'vue'

const app = createApp(App)

app.component('data', Data)
app.mount('#app')`,

            isLoading: false,
        }
    },
    props: {
        loaded: {
            type: Boolean,
            required: true
        }
    },
    methods: {
        async codePrinted() {
            this.isBackgroundVisible = true;
            while (!this.loaded) {
                await new Promise(resolve => setTimeout(resolve, 10))
            }
            setTimeout(() => {
                this.$emit('load')
            }, 200)
        }
    },
    mounted() {
        this.isTypescriptCodeVisible = true
        this.isLoading = true
        this.typescriptCodeRef?.start(true)
    },
    setup() {
        const typescriptCodeRef = ref<InstanceType<typeof CodeBlock>>()
        
        return { 
            typescriptCodeRef, 
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
    .code-segment
    {
        width: 600px;
    }

    .loader
    {
        position: absolute;
        bottom: 15vh;
    }
</style>