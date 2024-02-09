<template>
    <video class="bg-video" autoplay loop muted plays-inline>
        <source type="video/mp4" src="./@/../../../../public/matrix-blueprint.mp4">
    </video>
</template>

<script lang="ts">

export default {
    name: 'background-video'
}
</script>

<style scoped>
    .bg-video {
        position: fixed;
        width: 100%;
        z-index: -1;
    }
</style>