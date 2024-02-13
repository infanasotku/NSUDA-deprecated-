<template>
    <div class="form-wrapper">
        <form @submit.prevent>
            <div class="input">
                <transition-group
                enter-from-class="fade-enter"
                enter-active-class="fade-enter-active"
                enter-to-class="fade-enter-to"
                leave-from-class="fade-enter"
                >
                    <sign-in-form
                    v-if="authStore.loginFormType === FormType.SignIn"
                    :key="1"
                    >

                    </sign-in-form>
                    <sign-up-form
                    v-if="authStore.loginFormType === FormType.SignUp"
                    :key="2"
                    >

                    </sign-up-form>
                </transition-group>
            </div>
            <transparent-button class="button" @click="$emit('submit')">
                Sumbit
            </transparent-button>
            <transparent-button class="close-button" @click="$emit('close')">
                x
            </transparent-button>
        </form>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import SignInForm from '@/components/SignInForm.vue'
import SignUpForm from '@/components/SignUpForm.vue'
import { useAuthStore } from '@/store/auth';
import { FormType } from '@/types';
export default defineComponent({
    name: 'login-form',
    components: {
        SignInForm, SignUpForm
    },
    setup() {
        const authStore = useAuthStore()

        return { authStore, FormType }
    },
    emits: [
        'submit',
        'close'
    ]
})
</script>
<style scoped>
    form
    {
        flex-direction: column;
        transition: 1s;
        gap: 40px;
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

    .button
    {
        position: absolute;
        width: 190px;
        height: 60px;
        bottom: 30px;
    }

    .close-button
    {
        position: absolute;
        width: 40px;
        height: 35px;
        left: 0px;
        top: 3px;
        font-weight: 500;
    }

    .input 
    {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 350px;
        height: 350px;
    }
</style>