<script lang="ts">
import { defineComponent } from 'vue'
import { AuthType } from '@/types';
import { useAuthStore } from '@/store/auth';

export default defineComponent({
    props: {
        authCode: {
            type: String,
            required: true
        },
        authService: {
            type: String,
            required: true
        },
        sessionSecret: {
            type: String,
            required: true
        }
    },
    async mounted() {
        switch (this.authService) {
            case 'google':
                await this.authStore.loginUser(
                    AuthType.Google, 
                    this.authCode,
                    this.sessionSecret
                )
                break;
        
            default:
                break;
        }
    },
    setup() {
        const authStore = useAuthStore()

        return {
            authStore
        }
    }
})
</script>