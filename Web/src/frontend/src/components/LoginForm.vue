<template>
    <form @submit.prevent>
        <span>Sign in with</span>
        <div class="auth-wrapper">
            <transparent-button-nb 
            class="button"
            @click="authStore.requestCode(AuthType.Google); submit()"
            >
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
                    <path d="M15.545 6.558a9.4 9.4 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.7 7.7 0 0 1 5.352 2.082l-2.284 2.284A4.35 4.35 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.8 4.8 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.7 3.7 0 0 0 1.599-2.431H8v-3.08z"/>
                </svg>
            </transparent-button-nb>
            <transparent-button-nb 
            class="button"
            @click="authStore.requestCode(AuthType.VK); submit()"
            >
            <svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="101.000000pt" height="100.000000pt" viewBox="0 0 101.000000 100.000000" preserveAspectRatio="xMidYMid meet">
                <g transform="translate(0.000000,100.000000) scale(0.100000,-0.100000)" fill="currentColor" stroke="none">
                    <path d="M180 655 c0 -131 75 -272 174 -329 41 -24 124 -46 171 -46 24 0 25 2 25 76 0 84 -1 83 76 48 31 -15 94 -88 94 -111 0 -9 17 -13 60 -13 33 0 60 2 60 5 0 40 -128 195 -161 195 -6 0 11 21 39 48 46 42 91 117 92 150 0 8 -16 12 -49 12 -48 0 -49 -1 -74 -47 -24 -48 -96 -113 -123 -113 -11 0 -14 17 -14 80 l0 80 -50 0 -50 0 0 -140 c0 -130 -1 -140 -19 -140 -10 0 -36 18 -58 40 -43 43 -83 141 -83 205 l0 35 -55 0 -55 0 0 -35z"/>
                </g>
            </svg>
            </transparent-button-nb>
        </div>
    </form>
    <div 
    class="block_all"
    v-if="isLoading" 
    >
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/auth';
import { AuthType } from '@/types'
export default defineComponent({
    name: 'login-form',
    emits: [
        'load'
    ],
    data() {
        return {
            isLoading: false
        }
    },
    setup() {
        const authStore = useAuthStore()

        return { authStore, AuthType }
    },
    methods: {
        submit() {
            this.isLoading = true
            this.$emit('load')
        }
    }
})
</script>
<style scoped>
    form
    {
        flex-direction: column;
        display: flex;
        align-items: center;
        width: 100%;
        height: 100%;
    }

    

    span
    {
        margin-top: 10px;
        font-weight: 800;
        font-size: 20px;
        font-family: Consolas, Courier New, monospace;
    }

    .auth-wrapper
    {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: auto;
        margin-bottom: 30px;
        gap: 5px;
    }

    .button
    {
        height: 50px;
        border-radius: 50px;
        width: 50px;
    }

    .block_all
    {
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 10;
    }
</style>