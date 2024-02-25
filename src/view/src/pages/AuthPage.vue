<template></template>
<script lang="ts">
import { defineComponent } from 'vue'
// Components
import { AuthType } from '@/types';
import { useAuthStore } from '@/store/auth';

export default defineComponent({
    props: {
        authCode: {
            type: String,
            required: true
        },
        authService: {
            type: String,
            required: true
        }
    },
    mounted() {
        console.log(this.authService)
        console.log(this.authCode)
        switch (this.authService) {
            case 'google':
                this.authStore.authenticateUser(AuthType.Google, this.authCode)
                break;
        
            default:
                break;
        }
    },
    setup() {
        const authStore = useAuthStore()

        return {
            authStore
        }
    }
})
</script>
<style>
</style>