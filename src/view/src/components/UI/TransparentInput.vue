<template>
    <div class="box">
        <slot name="input">
            <input
            :placeholder="placeholder" 
            :type="type"
            maxlength="15"
            >
        </slot>
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
    name: 'transparent-input',
    emits: [
        'click'
    ],
    props: {
        placeholder: {
            type: String
        },
        type: {
            type: String
        }
    }
})
</script>
<style scoped>
    .box {
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
        background: transparent;
        z-index: 1;
    }

    .box:before {
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

    .box:after {
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

    .box:hover {
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    }

    .box:hover:before {
        border-color: rgb(161, 161, 161);
        height: 100%;
        transform: translateX(0);
        transition: .3s transform linear, .3s height linear .3s;
    }

    .box:hover:after {
        border-color: rgb(161, 161, 161);
        height: 100%;
        transform: translateX(0);
        transition: .3s transform linear, .3s height linear .5s;
    }

    input {
        font-weight: 900;
        color: rgb(161, 161, 161);
        text-decoration: none;
        cursor: pointer;
        outline: none;
        border: none;
        background: transparent;
        height: 100%;
        width: 90%;
        z-index: 4;
        caret-color: transparent;
    }

    input::placeholder {
        font-size: 14px;
        text-transform: uppercase;
    }

    .box:active {
        color: #d6d6d6;
        -webkit-transition: 100ms;
        transition: 100ms;
    }

</style>