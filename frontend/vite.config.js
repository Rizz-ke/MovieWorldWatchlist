import { defineConfig } from 'vite';

export default defineConfig({
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
      rewrite: path => path.replace(/^\/api/, ''),
    },
  },
});
