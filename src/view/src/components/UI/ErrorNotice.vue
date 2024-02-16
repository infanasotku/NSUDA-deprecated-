<template>
    <div class="wrapper">
        <div class="notice">
            <span>
                <slot></slot>
            </span>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'error-notice'
})
</script>
<style scoped>
    .wrapper
    {
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        transition: .3s;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 4;
    }
    .notice
    {
        width: 300px;
        height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid rgba( 255, 255, 255, 0.18 );
    }
    span
    {
        width: 100px;
        display: flex;
        justify-content: center;
        color: rgba(230, 50, 50, 0.5);
        font-weight: 800;
        text-transform: uppercase;
    }
</style>