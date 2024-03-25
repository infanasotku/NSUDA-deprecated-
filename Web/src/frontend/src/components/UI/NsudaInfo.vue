<template>
    <div
    v-show="isInfoVisible"
    class="content"
    >
        <div
        class="glass-plate"
        ></div>
        <dark-card 
        title="Common proxy"
        class="card">
            
        </dark-card>
        <dark-card 
        title="Common proxy"
        class="card">
            
        </dark-card>
        <dark-card 
        title="Common proxy"
        class="card">
            
        </dark-card>
        <!-- termynal -->
        <transition
        leave-active-class="fade-leave-active"
        leave-to-class="fade-leave-to"
        enter-active-class="fade-enter-active"
        enter-from-class="fade-enter"
        enter-to-class="fade-enter-to"
        >
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
        </transition>
        
        <!-- nsuda view -->
        <transition
        enter-active-class="fade-enter-active"
        enter-from-class="fade-enter"
        enter-to-class="fade-enter-to"
        >
            <div
            class="nsuda-view"
            v-if="isViewVisible"
            >
                <video
                autoplay 
                muted
                >
                    <source src="../../static/videos/nsuda_window.webm" type="video/mp4">
                </video>
            </div>
        </transition>
    </div>
</template>
<script lang="ts">
import { Termynal } from '@/static/js/termynal'
import { Action } from '@/types'

export default {
    name: 'nsuda-info',
    data() {
        return {
            isTermynalVisible: false,
            isViewVisible: false,
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
            // this.isTermynalVisible = true
            // new Termynal('#info-termynal',  { 
            //     startDelay: 600, 
            //     callback: this.termynalCallback
            // })
        },
        async wait(time: number, callback?: Action, ignoreSkip?: boolean) {
            if (!ignoreSkip) {
                return
            }
            await new Promise(resolve => setTimeout(resolve, time));
            callback?.call(this)
        },
        async termynalCallback() {
            //this.isTermynalVisible = false
            
        },
        
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
}
</script>
<style scoped>
.content
{
    width: 100%;
    height: 100%;
    position: relative;
}


.glass-plate
{
    width: 900px;
    height: 450px;
    background: rgba(255,255,255,.05);
    border-radius: 5px;

    position: relative;
    left: 100px;

    backdrop-filter: blur( 10px );
    -webkit-backdrop-filter: blur( 10px );
}











.code-segment
{
    width: 600px;
}

.termynal
{
    height: inherit;
    width: inherit;
    --tw-shadow: 7px 7px 15px 0 #000;
    box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
}

.linux-view::before
{
    color: green;
}

h2
{
    font-weight: 600;
}

.nsuda-view
{
    display: flex;
    justify-content: center;
    width: 390px;
    height: 336px;
    overflow: hidden;
    position: relative;
    --tw-shadow: 7px 7px 15px 0 #000;
    box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
    border: solid #404c5d 1px;
    border-radius: 10px;
}

.nsuda-view video
{
    top: -57px;
    position: absolute;
    width: 600px;
}

.card
{
    position: absolute;
}

.card:nth-child(2)
{
    top: 100px;
    left: 200px;
}
.card:nth-child(3)
{
    top: 290px;
    left: 280px;
}
.card:nth-child(4)
{
    top: 480px;
    left: 160px;
}




</style>