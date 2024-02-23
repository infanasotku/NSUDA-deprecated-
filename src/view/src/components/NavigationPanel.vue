<template>
    <nav class="panel col">
        <span class="label">NSUDA</span>
        <div v-for="navigationLink in navigationLinks" :key="navigationLink.id">
            <router-link :to="navigationLink.link">
                <dark-button @click="$emit('click', { id: navigationLink.id })">
                    <p>{{ navigationLink.content }}</p>
                </dark-button>
            </router-link>
        </div>
    </nav>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue';
import type { NavigationContent } from '@/types'
export default defineComponent({
    name: 'navigation-panel',
    props: {
        navigationLinks: {
            type: Array as PropType<NavigationContent[]>,
        }
    },
    emits: [
        'click'
    ]
})
</script>

<style scoped>
    .label:hover {
        -webkit-transition: 500ms;
        transition: 500ms;
        color: #d6d6d6;
    }
    .label
    {
        -webkit-transition: 500ms;
        transition: 500ms;
        font-family: Consolas, Courier New, monospace;
        font-size: 23px;
        font-weight: 600;
        color: rgb(161, 161, 161);
        margin-right: auto;
        height: auto;
        display: flex;
        align-content: center;
        text-align: center;
        padding-top: 4px;
    }
    .panel
    {
        position: fixed;
        top: 0px;
        padding-top: 0px;
        padding-bottom: 5px;
        padding-left: 20px;
        padding-right: 20px;
        width: 100%;
        display: flex;
        gap: 10px;
    }
</style>