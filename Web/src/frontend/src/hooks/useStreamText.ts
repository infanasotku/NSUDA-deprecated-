import { Action } from "@/types";
import { ref } from "vue";

export function useStreamText(onStreamPrinted: Action | undefined) {
    const interiorText = ref('')
    const startStream = (text: string, sleepTime: number) => {
        if (text.length === 0) {
            if (onStreamPrinted) {
                onStreamPrinted()
            }
            return
        }
        interiorText.value += text[0]
        setTimeout(() => {
            startStream(text.substring(1, text.length),
                sleepTime)
        }, sleepTime)
    }

    return {
        interiorCode: interiorText, startStream
    }
}