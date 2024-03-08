<script lang="ts">
import { useAuthStore } from '@/store/auth';
import { defineComponent } from 'vue'
import router from '@/router/router'
export default defineComponent({
    async setup() {
        const authStore = useAuthStore()
        await authStore.signOutUser()
        router.push('/')
        
        return { 
            authStore
        }
    }
})
</script>