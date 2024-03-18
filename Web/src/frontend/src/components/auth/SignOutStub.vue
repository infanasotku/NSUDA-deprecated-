<script lang="ts">
import { useAuthStore } from '@/store/auth';
import { defineComponent } from 'vue'
import router from '@/router/router'
export default defineComponent({
    setup() {
        const authStore = useAuthStore()
        authStore.signOutUser().then(() => router.push('/'))
        
        
        return { 
            authStore
        }
    }
})
</script>