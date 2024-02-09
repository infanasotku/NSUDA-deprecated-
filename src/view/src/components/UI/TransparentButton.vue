<template>
    <button class="button-wrapper">
        <slot></slot>
    </button>
</template>
<script lang="ts">
export default {
    name: 'transparent-button'
}
</script>
<style scoped>
    @keyframes smoothing
    {
        to
        {
            background: rgba(129, 3, 255, 0.4);
        }
    }

    .button-wrapper
    {
        color: white;
        box-shadow: 0px 0px 30px 3px rgb(129, 3, 255);
        background: transparent;
        border: 1px solid rgb(255, 255, 255);
        border-radius: 15px;
        padding: 15px 20px 0px 20px;
    }

    .button-wrapper:hover
    {
        animation-name: smoothing;
        animation-duration: 0.4s;
        animation-fill-mode: forwards;
        text-decoration: none;
    }

</style>