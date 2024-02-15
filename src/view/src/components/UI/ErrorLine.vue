<template>
    <span class="line">
        <slot></slot>
    </span>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'error-line'
})
</script>
<style>
    
</style>