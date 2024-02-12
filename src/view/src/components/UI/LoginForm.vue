<template>
    <div class="form-wrapper">
        <form>
            <div class="input">
                
            </div>
            <form-button class="button">
                Sumbit
            </form-button>
        </form>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import SignInForm from '@/components/SignInForm.vue'
import SignUpForm from '@/components/SignUpForm.vue'
export default defineComponent({
    name: 'login-form',
    components: {
        SignInForm, SignUpForm
    },
})
</script>
<style scoped>
    form
    {
        flex-direction: column;
        transition: 1s;
        gap: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 400px;
        height: 400px;
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
        width: 150px;
        height: 50px;
        bottom: 50px;
    }
</style>