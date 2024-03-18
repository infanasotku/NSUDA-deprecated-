<template>
    <transition
    enter-active-class="fade-enter-active"
    enter-from-class="fade-enter"
    enter-to-class="fade-enter-to"
    leave-active-class="fade-leave-active"
    leave-to-class="fade-leave-to"
    >
        <Page @load="() => { loadEnd = true }" :loaded="loaded"/>
    </transition>
</template>
<script setup lang="ts">
import { useAuthStore } from '@/store/auth';
import { defineAsyncComponent, ref } from 'vue'
import LoadingPage from '@/pages/LoadingPage.vue';

const props = defineProps({
    page: {
        type: String,
        required: true
    }
})

const pagePath = './' + props.page

const authStore = useAuthStore()
const loadEnd = ref(false)
const loaded = ref(false)
const Page = defineAsyncComponent({

    loader: async () => {
        await authStore.updateAuthState()
        const component = await import(/* @vite-ignore */ pagePath)
        loaded.value = true
        while (!loadEnd.value) {
            await new Promise(resolve => setTimeout(resolve, 10))
        }
        return component
    },                                                                                  
    loadingComponent: LoadingPage,
    delay: 0,
})
</script>
