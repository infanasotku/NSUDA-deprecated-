<template>
    <div
    v-show="isInfoVisible"
    class="content"
    >
        <transition
        leave-active-class="fade-leave-active"
        leave-to-class="fade-leave-to"
        enter-active-class="fade-enter-active"
        enter-from-class="fade-enter"
        enter-to-class="fade-enter-to"
        >
            <div v-if="isBlackoutVisible" class="blackout"></div>
        </transition>
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
            data-ty-delay="1500"
            data-ty-startDelay="1000" 
            :data-ty-prompt="'infanasotku@air  ~ %'"
            >ssh infanasotku@server</span>
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
            data-ty-delay="1000"
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
            isBlackoutVisible: false,
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
            new Termynal('#info-termynal',  { 
                startDelay: 600, 
                callback: this.termynalCallback
            })
        },
        termynalCallback() {
            this.isBlackoutVisible = true
            setTimeout(() => {
                this.isTermynalVisible = false
                this.isBlackoutVisible = false
            }, 1000)
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
.content
{
    width: 100%;
    height: 100%;
    position: relative;
}
.code-segment
{
    width: 600px;
}

.termynal
{
    height: 330px;
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
    background-color: black;
    transition: all 1s;
    z-index: 10;
    width: 100%;
    height: 100%;
    position: absolute;
}

</style>