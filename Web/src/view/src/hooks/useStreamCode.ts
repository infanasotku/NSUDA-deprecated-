import { Action } from "@/types";
import { ref } from "vue";

export function useStreamCode(onStreamPrinted: Action | undefined) {
    const interiorCode = ref('')
    const startStream = (text: string, sleepTime: number) =>
    {
        if (text.length === 0) {
            if (onStreamPrinted)
            {
                onStreamPrinted()
            }
            return
        }
        interiorCode.value += text[0]
        setTimeout(() => { startStream(text.substring(1, text.length),
            sleepTime) }, sleepTime)
    }

    return {
        interiorCode, startStream
    }
}