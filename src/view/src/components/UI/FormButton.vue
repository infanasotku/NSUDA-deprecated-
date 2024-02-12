<template>
    <button>
        <div class="box">
            <slot></slot>

        </div>
    </button>
</template>
<script lang="ts">
export default {
    name: 'form-button'
}
</script>
<style scoped>
    .box {
        width: 140px;
        height: auto;
        float: left;
        transition: .5s linear;
        position: relative;
        display: flex;
        justify-content: center;
        overflow: hidden;
        padding: 15px;
        text-align: center;
        background: transparent;
        text-transform: uppercase;
        font-weight: 900;
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

    button {
        color: rgb(161, 161, 161);
        text-decoration: none;
        cursor: pointer;
        outline: none;
        border: none;
        background: transparent;
    }

    .box:active {
        color: #d6d6d6;
        -webkit-transition: 100ms;
        transition: 100ms;
    }

</style>