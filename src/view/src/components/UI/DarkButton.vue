<template>
    <button>
        <slot></slot>
    </button>
</template>
<script lang="ts">
export default {
    name: 'dark-button'
}
</script>
<style scoped>
    button {
        height: 30px;
        margin: 5px;
        width: 120px;
        background: rgb(41, 44, 51);
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        justify-content: center;
        cursor: pointer;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        font-family: Consolas, Courier New, monospace;
        border: solid #404c5d 1px;
        font-size: 16px;
        color: rgb(161, 161, 161);
        -webkit-transition: 500ms;
        transition: 500ms;
        border-radius: 5px;
        background: linear-gradient(145deg, #2e2d2d, #212121);
        --tw-shadow: 7px 7px 15px 0 #000;
        box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
    }

    button:hover {
        -webkit-transition: 500ms;
        transition: 500ms;
        color: #d6d6d6;
    }

    button:active {
        color: #d6d6d6;
        border: solid #d6d6d698 1px;
        -webkit-transition: 100ms;
        transition: 100ms;
    }
</style>