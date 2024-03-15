<template>
    <div class="block-wrapper">
        <div class="code-block">
            <span class="lang-label">{{ language }}</span>
            <highlightjs class="code" :code="interiorCode"/>
        </div>
    </div>
</template>
<script lang="ts">
import { PropType, defineComponent, defineExpose } from 'vue';
import { useStreamText } from '@/hooks/useStreamText';
import { Action } from '@/types';
export default defineComponent({
    name: 'code-block',
    props: {
        language: {
            type: String,
            required: true
        },
        code: {
            type: String,
            required: true 
        },
        time: {
            type: Number
        },
        onCodePrinted: {
            type: Function as PropType<Action>
        }
    },
    setup(props)
    {
        const { interiorCode, startStream } = useStreamText(props.onCodePrinted)


        const start = (stream: boolean) => {
            if (stream)
            {
                startStream(props.code, props.time! / props.code.length )
            }
            else
            {
                interiorCode.value = props.code
            }
        }
        defineExpose({
            start,
        })

        return {
            interiorCode, start
        }
    }
})
</script>
<style scoped>
    .code-block
    {
        position: relative;
    }
    .code
    {
        --tw-shadow: 7px 7px 15px 0 #000;
        box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
        margin: 0;
        width: 100%;
    }
    .lang-label
    {
        font-family: 'ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace';
        text-transform: uppercase;
        position: absolute;
        right: 0;
        color: rgba(255, 255, 255, 0.8);
        padding-top: 5px;
        padding-bottom: 3px;
        padding-right: 10px;
        padding-left: 10px;
        font-weight: 600;
        font-size: 12px;
        background-color: rgba(0,0,0,.3);
        border-bottom-left-radius: 5px;
    }
</style>@/hooks/useStreamText