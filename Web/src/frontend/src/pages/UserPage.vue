<template>
    <div class="hero">
        <navigation-panel
        :navigation-links="navigationInfo"
        @click="navPanelClicked"
        >
        </navigation-panel>
        <div class="content">
            Hello {{ authStore.userModel.email }}
        </div>
    </div>
</template>
<script lang="ts">
import { useAuthStore } from '@/store/auth';
import { defineComponent } from 'vue'
import router from '@/router/router'

import NavigationPanel from '@/components/NavigationPanel.vue'
import { AuthType } from '@/types';

export default defineComponent({
    components: {
        NavigationPanel
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
                    link: '/signout',
                    content: 'Sign out',
                },
            ],
        }
        
    },
    methods: {
        async navPanelClicked(id: number) {
            switch (id) {
                // author
                case 1:
                    
                    break;
                // sign out
                case 2:
                    router.push(this.navigationInfo[id - 1].link)
                    break;
                default:
                    break;
            }
        }
    },
    setup() {
        const authStore = useAuthStore()
        if (authStore.authType == AuthType.NoAuth) {
            router.push('/')
        }
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