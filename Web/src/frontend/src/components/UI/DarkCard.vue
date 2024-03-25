<template>
    <div class="card">
        <div class="header">
            <bright-checkbox class="figure">
            </bright-checkbox>
            <h2>
                {{ props.title }}
            </h2>
        </div>

        <slot></slot>
    </div>
</template>
<script lang="ts">
export default {
    name: 'dark-card'
}
</script>
<script setup lang="ts">
import { ref } from 'vue';

const wrapperVisible = ref(true)
const props = defineProps({
    title: {
        type: String,
        required: true
    }
})
</script>
<style scoped>
.card {
    width: 275px;
    color: rgb(161, 161, 161);
    height: 150px;
    background-color: #252a33;
    box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.5);
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.figure {
    width: 20px;
    height: 20px;
    position: relative;
    top: 2px;
}

.header {
    width: 100%;
    padding: 5px 10px 10px;
    height: 30px;
    overflow: hidden;
    display: flex;
    flex-direction: row;
}

h2 {
    margin-left: 15px;
    font-size: 22px;
    font-weight: 600;
}

.wrapper {
    background-color: rgb(125, 125, 158);
    left: calc(100% / 2 - width/2);
    position: absolute;
    width: 700px;
    height: 200px;
}
</style>