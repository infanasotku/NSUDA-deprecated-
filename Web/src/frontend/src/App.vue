<template>
  <router-view v-slot="{ Component }">
    <template v-if="Component">
      <component :is="Component"></component>
    </template>
  </router-view>
</template>
<script>
import { defineComponent } from 'vue';
import axios from 'axios';
export default defineComponent({
  setup() {
    axios.defaults.withCredentials = true
  }
})
</script>
<style>
    body
    {
        overflow: hidden;
    }
</style>
