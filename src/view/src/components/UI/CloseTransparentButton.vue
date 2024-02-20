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
<style>
    
    .f
    {
        transform: rotate(45deg);
    }

    .s
    {
        transform: rotate(135deg);
    }

    .line
    {
        border-top: 3px solid rgb(161, 161, 161);
        width: 19px;
        position: absolute;
    }

    .close-button 
    {
        width: 35px;
        height: 35px;
    }
</style>