<template>
    <div
    v-show="isInfoVisible"
    class="content"
    >
        <div
        v-show="isFirstStepTextVisible"
        >
            <h2>There is your steps to using proxy each times:</h2>
        </div>
        <div
        id="info-termynal" 
        data-termynal 
        data-ty-startDelay="0" 
        class="termynal"
        v-show="isTermynalVisible"
        >
            <span 
            data-ty-typeDelay="100"
            data-ty="input" 
            data-ty-delay="3000"
            data-ty-startDelay="1000" 
            :data-ty-prompt="'infanasotku@air  ~ %'"
            >ssh infanasotku@server-ip</span>
            <span
            data-ty="output"
            data-ty-delay="0"
            >Welcome to Ubuntu 18.04.6 LTS</span>
            <span 
            data-ty-typeDelay="100"
            data-ty="input" 
            data-ty-delay="1000"
            data-ty-startDelay="1000" 
            class="linux-view"
            :data-ty-prompt="'infanasotku@server:~$'"
            >sudo systemctl start xray</span>
            <span 
            data-ty-typeDelay="100"
            data-ty="input" 
            data-ty-delay="1000"
            class="linux-view"
            :data-ty-prompt="'infanasotku@server:~$'"
            >exit</span>
            <span 
            data-ty-typeDelay="100"
            data-ty="input" 
            data-ty-delay="1000"
            :data-ty-prompt="'infanasotku@air  ~ %'"
            >./xray -c config.json</span>
            <span
            data-ty="output"
            data-ty-delay="0"
            >Xray (Xray, Penetrates Everything.)
A unified platform for anti-censorship.</span>
            
        </div>
    </div>
</template>
<script lang="ts">
import { Termynal } from '@/static/js/termynal'
import { useAuthStore } from '@/store/auth'

export default {
    name: 'nsuda-info',
    data() {
        return {
            isTermynalVisible: false,
            isFirstStepTextVisible: false,
        }
    },
    props: {
        isInfoVisible: {
            type: Boolean,
            required: true
        }
    },
    methods: {
        start() {
            this.isTermynalVisible = true
            new Termynal('#info-termynal',  { startDelay: 600 })
        }
    },
    watch: {
        isInfoVisible: {
            handler(val) {
                if(val) {
                    this.start()
                }
            }
        }
    },
    mounted() {
        
    },
    setup() {
        const authStore = useAuthStore()
        return {
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

.termynal
{
    height: 350px;
    --tw-shadow: 7px 7px 15px 0 #000;
    box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
}

.linux-view::before
{
    color: green;
}

h2
{
    margin-bottom: 60px;
    font-weight: 600;
}

.blackout
{
    background: black;
}

</style>