import React, { createContext, useContext, useEffect, useMemo, useState } from 'react'
import { auth, db } from '@/firebase'
import {
  User,
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut as fbSignOut,
  updateProfile,
  GoogleAuthProvider,
  signInWithPopup
} from 'firebase/auth'
import { collection, doc, getDoc, serverTimestamp, setDoc } from 'firebase/firestore'
import type { Role } from '@/types/roles'

type Profile = {
  uid: string
  email: string
  displayName?: string
  role: Role
  createdAt?: unknown
}

type AuthContextType = {
  user: User | null
  profile: Profile | null
  role: Role | null
  loading: boolean
  signIn: (email: string, password: string) => Promise<void>
  register: (email: string, password: string, displayName?: string) => Promise<void>
  signInWithGoogle: () => Promise<void>
  signOut: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

async function ensureUserProfile(user: User): Promise<Profile> {
  const ref = doc(collection(db, 'users'), user.uid)
  const snap = await getDoc(ref)
  if (snap.exists()) {
    return snap.data() as Profile
  }
  const profile: Profile = {
    uid: user.uid,
    email: user.email || '',
    displayName: user.displayName || '',
    role: 'volunteer',
    createdAt: serverTimestamp(),
  }
  await setDoc(ref, profile, { merge: true })
  return profile
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [profile, setProfile] = useState<Profile | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, async (u) => {
      setUser(u)
      if (u) {
        const p = await ensureUserProfile(u)
        setProfile(p)
      } else {
        setProfile(null)
      }
      setLoading(false)
    })
    return () => unsub()
  }, [])

  const value = useMemo<AuthContextType>(() => ({
    user,
    profile,
    role: profile?.role ?? null,
    loading,
    async signIn(email, password) {
      await signInWithEmailAndPassword(auth, email, password)
    },
    async signInWithGoogle() {
      const provider = new GoogleAuthProvider()
      const cred = await signInWithPopup(auth, provider)
      if (cred.user) {
        await ensureUserProfile(cred.user)
      }
    },
    async register(email, password, displayName) {
      const cred = await createUserWithEmailAndPassword(auth, email, password)
      if (displayName) {
        await updateProfile(cred.user, { displayName })
      }
      await ensureUserProfile(cred.user)
    },
    async signOut() {
      await fbSignOut(auth)
    }
  }), [user, profile, loading])

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
