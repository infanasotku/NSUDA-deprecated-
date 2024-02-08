import { fileURLToPath, URL } from 'node:url'

import { defineConfig, UserConfig, UserConfigFnObject } from 'vite'
import vue from '@vitejs/plugin-vue'

const config = defineConfig(({ command, mode }) => {
  let proxyTarget: string
  if (command === 'serve')
  {
    // Debug config
    proxyTarget = 'http://localhost:5000'
  }
  else
  {
    proxyTarget = 'https://infanasotku.com'
  }

  return {
    plugins: [
          vue(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    server: {
      proxy: {
        '/api': proxyTarget
      }
    }
  }
})

export default config

// // https://vitejs.dev/config/
// export default defineConfig({
//   
//   server: {
//     port: 5001,
//     proxy: (() =>
//     {
//       return {

//       }
//     })()
//     // {
//     //   '/api': {
//     //     target: 'http://localhost:5000'
//     //   }
//     // }
//   }
// })
