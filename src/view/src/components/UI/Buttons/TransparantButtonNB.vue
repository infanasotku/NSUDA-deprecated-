<template>
    <button @click="$emit('click')">
        <slot></slot>
    </button>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'transparent-button-nb',
    emits: [
        'click'
    ]
})
</script>
<style scoped>
    button:before {
        position: absolute;
        content: '';
        left: 0;
        bottom: 0;
        height: 4px;
        width: 100%;
        border-bottom: 2px solid transparent;
        border-left: 2px solid transparent;
        box-sizing: border-box;
        transform: translateX(100%);
    }

    button:after {
        position: absolute;
        content: '';
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        border-top: 2px solid transparent;
        border-right: 2px solid transparent;
        box-sizing: border-box;
        transform: translateX(-100%);
    }

    button:hover {
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    }

    button {
        font-weight: 900;
        padding: 0;
        color: rgb(161, 161, 161);
        text-decoration: none;
        cursor: pointer;
        outline: none;
        border: none;
        background: transparent;
        text-transform: uppercase;
        width: 100%;
        height: 100%;
        float: left;
        transition: .5s linear;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        text-align: center;
    }

    button:active {
        color: #d6d6d6;
        -webkit-transition: 100ms;
        transition: 100ms;
    }

</style>