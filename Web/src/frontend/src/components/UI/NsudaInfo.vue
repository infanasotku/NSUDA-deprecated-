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
            <dark-button
            v-if="isSkipButtonVisible"
            class="skip-button"
            @click="() => { isSkip = true; isSkipButtonVisible = false }"
            >Skip</dark-button>
        </transition>
        <!-- text -->
        <transition
        leave-active-class="fade-leave-active"
        leave-to-class="fade-leave-to"
        enter-active-class="fade-enter-active"
        enter-from-class="fade-enter"
        enter-to-class="fade-enter-to"
        >
        <div
        v-if="isTextVisible"
        >
            <h2>{{ textContent }}</h2>
        </div>
        </transition>
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
        <!-- nsuda banner -->
        <transition
        leave-active-class="fade-leave-active"
        leave-to-class="fade-leave-to"
        enter-active-class="fade-enter-active"
        enter-from-class="fade-enter"
        enter-to-class="fade-enter-to"
        >
            <nsuda-banner
            v-if="isBannerVisible"
            ></nsuda-banner>
        </transition>
    </div>
</template>
<script lang="ts">
import { Termynal } from '@/static/js/termynal'
import { useAuthStore } from '@/store/auth'
import { Action } from '@/types'
import NsudaBanner from '@/components/UI/NsudaBanner.vue'

export default {
    name: 'nsuda-info',
    data() {
        return {
            isBlackoutVisible: false,
            isTermynalVisible: false,
            isTextVisible: false,
            textContent: 'There',
            isViewVisible: false,
            isSkip: false,
            isBannerVisible: false,
            isSkipButtonVisible: false
        }
    },
    components: {
        NsudaBanner
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
        async wait(time: number, callback?: Action, ignoreSkip?: boolean) {
            if (this.isSkip && !ignoreSkip) {
                return
            }
            await new Promise(resolve => setTimeout(resolve, time));
            callback?.call(this)
        },
        async termynalCallback() {
            this.isTermynalVisible = false
            await this.wait(1000, () => {
                this.isSkipButtonVisible = true
                this.isTextVisible = true
            })
            
            await this.wait(2000, () => this.isTextVisible = false)

            await this.wait(1000, () => {
                this.isTextVisible = true
                this.textContent = 'is your daily routine'
            })

            await this.wait(2000, () => this.isTextVisible = false)
            
            await this.wait(1000, () => {
                this.isTextVisible = true
                this.textContent = 'with common proxy'
            })

            await this.wait(2000, () => {
                this.isTextVisible = false
                this.textContent = 'with common proxy'
            })
            
            await this.wait(2000, () => {
                this.isTextVisible = true
                this.textContent = 'This'
            })

            await this.wait(2000, () => this.isTextVisible = false)
            
            await this.wait(1000, () => this.isViewVisible = true)
            
            await this.wait(1875, () => {
                this.isViewVisible = false
                this.textContent = 'with NSUDA'
            })
            
            await this.wait(1000, () => this.isTextVisible = true)
            
            await this.wait(2000, () => this.isTextVisible = false)

            await this.startFinalStage()
        },
        async startFinalStage() {
            this.isTextVisible = false
            this.isViewVisible = false
            this.isSkipButtonVisible = false
            await this.wait(1000, () => this.isBannerVisible = true, true)
            

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
    height: 360px;
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

.skip-button
{
    position: absolute;
    right: 100px;
    top: 200px;
}

</style>