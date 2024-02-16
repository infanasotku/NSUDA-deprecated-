<template>
    <div>
        <transparent-button 
        class="close-button" 
        @click="authStore.setFormVisibility(false)"
        >
                <div class="line f">
                </div>
                <div class="line s">
                </div>
        </transparent-button>
    </div>
</template>
<script lang="ts">
import { useAuthStore } from '@/store/auth';
export default {
    name: 'close-transparent-button',
    props: {
        onCloseClicked: {
            type: Function,
            required: true
        }
    },
    setup() {
        const authStore = useAuthStore()

        return { authStore }
    }
}
</script>
<style lang="">
    
</style>