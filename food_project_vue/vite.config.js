import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
const backendPath = '../food_project'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/vite/',
  server: {
    watch: {
      ignored: []
    }
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: backendPath + '/core/static/vite/',
    rollupOptions: {
      input: {
        vue_food_edit: './src/apps/food_edit/food_edit.js',
        vue_order_edit: './src/apps/order_edit/order_edit.js'

      }
    }
  }
})
