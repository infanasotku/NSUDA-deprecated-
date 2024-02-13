<template>
    <div 
    class="input-wrapper"
    >
        <div class="description">
            <h1>Sign up</h1>
        </div>
        <transparent-input 
        placeholder="login" 
        class="input"
        ></transparent-input>
        <transparent-input 
        placeholder="password" 
        class="input"
        type="password"
        ></transparent-input>
        <transparent-input 
        placeholder="confirm password" 
        class="input"
        type="password"
        ></transparent-input>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'sign-up-form'
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