<template>
    <div 
    class="input-wrapper"
    >
        <div class="description">
            <h1>Sign up</h1>
        </div>
        <transparent-input 
        placeholder="username" 
        class="input"
        @input="authStore.setUsername($event)"
        :content="authStore.username"
        ></transparent-input>
        <transparent-input 
        placeholder="password" 
        class="input"
        type="password"
        @input="authStore.setPassword($event); validatePasswordConfirmation()"
        :content="authStore.password"   
        ></transparent-input>
        <transparent-input 
        placeholder="confirm password" 
        class="input"
        type="password"
        @input="passwordConfirmation = $event; validatePasswordConfirmation()"
        ></transparent-input>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/auth';
export default defineComponent({
    name: 'sign-up-form',
    data() {
        return {
            passwordConfirmation: ''
        }
    },
    setup() {
        const authStore = useAuthStore()
        return {
            authStore
        }
    },
    emits: [
        'confirm-input'
    ],
    methods: {
        validatePasswordConfirmation() {
            if (this.passwordConfirmation !== this.authStore.password) {
                this.$emit('confirm-input', false )
            }
            else
            {
                this.$emit('confirm-input', true)
            }
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
        margin-top: 20px;
    }
    .description
    {
        margin-top: 30px;
        text-transform: uppercase;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .description h1
    {
        font-weight: 700;
    }

</style>