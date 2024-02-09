<template>
    <background-video></background-video>
    <div class="content row">
        <navigation-panel></navigation-panel>
    </div>
</template>
<script lang="ts">
import NavigationPanel from '@/components/NavigationPanel.vue'
export default {
    components: {
        NavigationPanel
    }
}
</script>
<style scoped>
    .content {
        position: absolute;
        display: flex;
        align-items: center;
        color: white;
        width: 100%;
        height: 100%;
    }
</style>