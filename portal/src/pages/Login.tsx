import { FormEvent, useState } from 'react'
import { useAuth } from '@/state/AuthContext'
import { Navigate, useLocation } from 'react-router-dom'

export default function Login() {
  const { user, signIn, register, signInWithGoogle } = useAuth()
  const location = useLocation() as any
  // prefer explicit ?redirect= param, then state.from, then '/'
  const params = new URLSearchParams(location.search)
  const from = params.get('redirect') || location.state?.from?.pathname || '/'
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [displayName, setDisplayName] = useState('')
  const [mode, setMode] = useState<'login'|'register'>('login')
  const [error, setError] = useState<string|undefined>()
  const [busy, setBusy] = useState(false)

  if (user) return <Navigate to={from} replace />

  async function onSubmit(e: FormEvent) {
    e.preventDefault()
    setBusy(true)
    setError(undefined)
    try {
      if (mode === 'login') {
        await signIn(email, password)
      } else {
        await register(email, password, displayName)
      }
    } catch (e: any) {
      setError(e?.message || 'Failed')
    } finally {
      setBusy(false)
    }
  }

  async function onGoogleSignIn() {
    setBusy(true)
    setError(undefined)
    try {
      await signInWithGoogle()
    } catch (e: any) {
      setError(e?.message || 'Google sign-in failed')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow">
      <h1 className="text-xl font-semibold mb-4">{mode === 'login' ? 'Login' : 'Register'}</h1>
      <form onSubmit={onSubmit} className="grid gap-3">
        <div>
          <button type="button" onClick={onGoogleSignIn} disabled={busy} className="w-full px-4 py-2 rounded border bg-white flex items-center justify-center gap-2">
            <i className="fab fa-google" aria-hidden="true"></i>
            <span>Sign in with Google</span>
          </button>
        </div>
        {mode === 'register' && (
          <div>
            <label htmlFor="name" className="block text-sm mb-1">Name</label>
            <input id="name" placeholder="Your name" className="w-full border rounded px-3 py-2" value={displayName} onChange={e=>setDisplayName(e.target.value)} />
          </div>
        )}
        <div>
          <label htmlFor="email" className="block text-sm mb-1">Email</label>
          <input id="email" placeholder="you@example.com" type="email" className="w-full border rounded px-3 py-2" value={email} onChange={e=>setEmail(e.target.value)} required />
        </div>
        <div>
          <label htmlFor="password" className="block text-sm mb-1">Password</label>
          <input id="password" placeholder="••••••••" type="password" className="w-full border rounded px-3 py-2" value={password} onChange={e=>setPassword(e.target.value)} required />
        </div>
        {error && <div className="text-sm text-red-600">{error}</div>}
        <button disabled={busy} className="px-4 py-2 rounded bg-primary text-white">{busy ? 'Please wait…' : (mode==='login'?'Login':'Create Account')}</button>
      </form>
      <div className="mt-3 text-sm">
        {mode==='login' ? (
          <button className="underline" onClick={()=>setMode('register')}>New user? Create an account</button>
        ) : (
          <button className="underline" onClick={()=>setMode('login')}>Have an account? Login</button>
        )}
      </div>
    </div>
  )
}
