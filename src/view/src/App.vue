<template>
  <router-view v-slot="{ Component }">
    <template v-if="Component">
      <suspense>
        <component :is="Component"></component>
      </suspense>
    </template>
  </router-view>
</template>
<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import { useAuthStore } from '@/store/auth';
export default defineComponent({
  setup() {
    axios.defaults.withCredentials = true
    const authStore = useAuthStore()
    authStore.updateAuthState()
  }
})

</script>
<style>
    body
    {
        overflow: hidden;
    }
</style>
