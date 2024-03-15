<template>
    <div
    class="content"
    >
        <div
        id="termynal" 
        data-termynal 
        class="termynal"
        data-ty-startDelay="200" 
        data-ty-cursor="▋"
        v-show="false"
        >
            <span 
            data-ty-typeDelay="100"
            data-ty="input" 
            data-ty-delay="1000"
            :data-ty-prompt="'' + authStore.userModel.email + ' ~ %'"
            >Welcome to NSUDA webpage!</span>
            <span
            data-ty="output"
            >Are you sure you want to redirect to account page?</span>
            <span 
            data-ty-delay="1000"
            data-ty-typeDelay="1500"
            data-ty="input" 
            data-ty-prompt="(y/n)"
            >y</span>
            <span
            data-ty="progress"
            data-ty-typeDelay="40"
            data-ty-delay="500"
            progressChar="|"
            ></span>
        </div>
        <div>
            <h2>There is your steps to using proxy each times</h2>
        </div>
    </div>
</template>
<script lang="ts">
import { useAuthStore } from '@/store/auth'

export default {
    name: 'nsuda-info',
    data() {
        return {
            
        }
    },
    methods: {
        startInfo() {
            
        }
    },
    setup() {
        const authStore = useAuthStore()
        const start = () => {
            
        }


        return {
            start,
            authStore
        }
    }
}
</script>
<style scoped>
.code-segment
{
    width: 600px;
}

.move-down
{
    transform: translateY(-150px);
    transition: all .5s;
    transition-delay: .5s;
}
</style>