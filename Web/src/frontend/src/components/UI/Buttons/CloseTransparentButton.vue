<template>
    <div>
        <transparent-button 
        class="close-button" 
        >
            <div class="line f">
            </div>
            <div class="line s">
            </div>
        </transparent-button>
    </div>
</template>
<script lang="ts">
export default {
    name: 'close-transparent-button',
}
</script>
<style>
    
    .f
    {
        transform: rotate(45deg);
    }

    .s
    {
        transform: rotate(135deg);
    }

    .line
    {
        border-top: 3px solid rgb(161, 161, 161);
        width: 19px;
        position: absolute;
    }

    .close-button 
    {
        width: 35px;
        height: 35px;
    }
</style>