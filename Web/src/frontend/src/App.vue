<template>
  <router-view :key="$route.path" v-slot="{ Component }">
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
        transition: all 1s;
        background-color: rgb(36, 33, 33);
        overflow: hidden;
    }
</style>
