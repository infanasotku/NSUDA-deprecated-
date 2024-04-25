<template>
    <div class="card">
        <div class="header">
            <bright-checkbox color="white" :inputId="cardId" class="figure" v-model="status">
            </bright-checkbox>
            <h2>
                {{ props.title }}
            </h2>
        </div>
        <div class="content">
            <slot>
            </slot>
        </div>
    </div>
</template>
<script lang="ts">
export default {
    name: 'dark-card'
}
</script>
<script setup lang="ts">
import { watch } from 'vue';

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    cardId: {
        type: String,
        required: true
    }
})
const emit = defineEmits(['change'])
const status = defineModel()
watch(status, () => {
    emit('change', props.cardId)
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
    padding: 5px 10px 5px 10px;
    height: 35px;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    background-color: var(--pink-base);
    color: white;
}

h2 {
    margin-left: 15px;
    font-size: 22px;
    font-weight: 600;
    user-select: none;
}

.wrapper {
    background-color: rgb(125, 125, 158);
    left: calc(100% / 2 - width/2);
    position: absolute;
    width: 700px;
    height: 200px;
}

.content {
    padding-left: 5px;
    padding-top: 5px;
}
</style>
