<template>
    <div class="hero">
        <navigation-panel>
        </navigation-panel>
        <div class="content">
            Hello {{ authStore.userModel.email }}
        </div>
    </div>
</template>
<script lang="ts">
import { useAuthStore } from '@/store/auth';
import { defineComponent } from 'vue'

import NavigationPanel from '@/components/NavigationPanel.vue'

export default defineComponent({
    components: {
        NavigationPanel
    },
    async setup() {
        const authStore = useAuthStore()
        await authStore.updatingPromise
        return {
            authStore
        }
    }
})
</script>
<style scoped>
    .hero
    {
        width: 100%;
        min-height: 100vh;
        background-color: rgb(36, 33, 33);
        display: flex;
        justify-content: center;

        color: white;
    }
    .content
    {
        display: flex;

        margin-top: 50px;
        height: 100%;
    }
</style>