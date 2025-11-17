import { Link, NavLink } from 'react-router-dom'
import { useAuth } from '@/state/AuthContext'

export default function NavBar() {
  const { user, role, signOut } = useAuth()
  return (
    <header className="sticky top-0 z-10 bg-white border-b">
      <div className="mx-auto max-w-6xl px-4 py-3 flex items-center gap-4">
        <Link to="/" className="font-semibold text-primary">Flyers Portal</Link>
        <nav className="flex-1 flex items-center gap-3 text-sm">
          {user && (
            <>
              <NavLink to="/" className={({isActive}) => isActive ? 'text-primary font-medium' : ''}>Home</NavLink>
              {(role === 'admin') && <NavLink to="/admin">Admin</NavLink>}
              {(role === 'admin' || role === 'hr') && <NavLink to="/hr">HR</NavLink>}
              {(role === 'admin' || role === 'finance') && <NavLink to="/finance">Finance</NavLink>}
              {(role === 'admin' || role === 'projects') && <NavLink to="/projects">Projects</NavLink>}
              <NavLink to="/volunteers">Volunteers</NavLink>
            </>
          )}
        </nav>
        <div className="text-sm">
          {user ? (
            <button onClick={signOut} className="px-3 py-1 rounded bg-primary text-white">Logout</button>
          ) : (
            <NavLink to="/login" className="px-3 py-1 rounded bg-primary text-white">Login</NavLink>
          )}
        </div>
      </div>
    </header>
  )
}
