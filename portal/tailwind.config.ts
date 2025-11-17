import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#01579B',
        accent: '#c10fff',
        heading: '#1e293b',
        body: '#67768e',
        yellow: '#ffcd57'
      }
    }
  },
  plugins: []
} satisfies Config
