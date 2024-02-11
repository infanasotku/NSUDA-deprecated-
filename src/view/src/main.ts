import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router/router'
import components from '@/components/UI'
import 'highlight.js/styles/atom-one-dark.css'
import 'highlight.js/lib/common';
import hljsVuePlugin from "@highlightjs/vue-plugin";

const app = createApp(App)

components.forEach(component => app.component(component.name!, component));

app.
use(router).
use(hljsVuePlugin).
mount('#app')
