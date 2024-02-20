<template>
    <div 
    class="input-wrapper"
    >
        <div class="description">
            <h1>Sign in</h1>
        </div>
        <transparent-input 
        placeholder="username"
        @input="authStore.setUsername($event)"
        :content="authStore.username"
        class="input"
        ></transparent-input>
        <transparent-input 
        placeholder="password" 
        @input="authStore.setPassword($event)"
        :content="authStore.password"
        class="input"
        type="password"
        ></transparent-input>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/auth';
export default defineComponent({
    name: 'sign-in-form',
    setup() {
        const authStore = useAuthStore()
        return {
            authStore
        }
    }
})
</script>
<style scoped>
    .input-wrapper
    {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    .input
    {
        width: 100%;
        height: 60px !important;
        margin-bottom: 20px;
    }
    .description
    {
        margin-top: 30px;
        text-transform: uppercase;
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
    }

    .description h1
    {
        font-weight: 700;
    }

</style>