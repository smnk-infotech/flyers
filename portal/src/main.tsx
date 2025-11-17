import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import './index.css'
import { AuthProvider } from './state/AuthContext'
import { initGA } from './analytics/ga4'

const container = document.getElementById('root')!
const root = createRoot(container)
initGA(import.meta.env.VITE_GA_MEASUREMENT_ID)
root.render(
  <React.StrictMode>
    <BrowserRouter basename="/portal">
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
)
