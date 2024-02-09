<template>
    <nav class="panel col">
        <div v-for="navigationLink in navigationLinks" :key="navigationLink.id">
            <router-link :to="navigationLink.href">
                <transparent-button>
                    <p>{{ navigationLink.content }}</p>
                </transparent-button>
            </router-link>
        </div>
    </nav>
</template>

<script lang="ts">
export default {
    name: 'navigation-panel',
    data: () =>
    {
        return {
            navigationLinks: [
                {
                    id: 1,
                    content: 'About',
                    href: "/about"
                },
                {
                    id: 2,
                    content: 'Home',
                    href: "/"
                }
            ]
        }
    }
}
</script>

<style scoped>
    .panel
    {
        position: fixed;
        top: 0px;
        left: 0px;
        right: 0px;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 20px;
        padding-right: 20px;
        width: 100%;
        display: flex;
        justify-content: right;
        gap: 20px;
    }
</style>