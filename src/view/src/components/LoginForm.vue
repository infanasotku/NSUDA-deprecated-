<template>
    <div class="form-wrapper">
        <form @submit.prevent>
            <close-transparent-button 
            class="close-button" 
            @click="authStore.setFormVisibility(false)"
            >
            </close-transparent-button>
        </form>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/auth';
export default defineComponent({
    name: 'login-form',
    setup() {
        const authStore = useAuthStore()

        return { authStore }
    },
    methods: {
    }
    
})
</script>
<style scoped>
    form
    {
        flex-direction: column;
        transition: 1s;
        display: flex;
        align-items: center;
        width: 400px;
        height: 450px;
        background: rgba( 255, 255, 255, 0.15 );
        backdrop-filter: blur( 5.5px );
        -webkit-backdrop-filter: blur( 5.5px );
        border-radius: 10px;
        border: 1px solid rgba( 255, 255, 255, 0.18 );
        color: rgb(161, 161, 161);;
    }

    .close-button
    {
        position: absolute;
        left: 7px;
        top: 7px;
    }

</style>