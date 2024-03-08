<template>
    <transition
    leave-active-class="fade-leave-active"
    leave-to-class="fade-leave-to"
    enter-active-class="fade-enter-active"
    enter-from-class="fade-enter"
    enter-to-class="fade-enter-to"
    >
        <div class="wrapper" v-if="visible">
            <div class="notice">
                <close-transparent-button
                class="close-button"
                @click="$emit('close')"
                >
                </close-transparent-button>
                <span>
                    <slot></slot>
                </span>
            </div>
        </div>
    </transition>
    
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'error-notice',
    props: {
        visible: {
            type: Boolean,
        }
    },
    emits: [
        'close'
    ]
})
</script>
<style scoped>
    .wrapper
    {
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 4;
    }
    .notice
    {
        width: auto;
        height: 200px;
        padding-left: 50px;
        padding-right: 50px;
        position: relative;
        display: flex;
        justify-content: center;
        background: rgba( 255, 255, 255, 0.15 );
        backdrop-filter: blur( 5.5px );
        -webkit-backdrop-filter: blur( 5.5px );
        align-items: center;
        border: 1px solid rgba( 255, 255, 255, 0.18 );
    }
    span
    {
        width: auto;
        display: flex;
        justify-content: center;
        color: rgba(230, 50, 50, 0.8);
        font-weight: 800;
        text-transform: uppercase;
    }
    .close-button 
    {
        position: absolute;
        top: 0;
        left: 0;
    }
</style>