<template>
    <div class="window">
        <close-transparent-button 
        class="close-button" 
        @click="$emit('close')"
        >
        </close-transparent-button>
        <slot></slot>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'modal-window',
    emits: [
        'close'
    ]
})
</script>
<style scoped>
.window
{
    transition: 1s;
    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    background: rgba( 255, 255, 255, 0.15 );
    backdrop-filter: blur( 5.5px );
    -webkit-backdrop-filter: blur( 5.5px );
    border-radius: 10px;
    border: 1px solid rgba( 255, 255, 255, 0.18 );
    color: rgb(161, 161, 161);
    position: absolute;
}

.close-button
{
    position: absolute;
    left: 7px;
    top: 7px;
}
</style>