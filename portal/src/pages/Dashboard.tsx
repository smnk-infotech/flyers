import { Link } from 'react-router-dom'
import { useAuth } from '@/state/AuthContext'

export default function Dashboard() {
  const { profile, role } = useAuth()
  return (
    <div className="grid gap-4">
      <h1 className="text-2xl font-semibold text-heading">Welcome{profile?.displayName ? `, ${profile.displayName}` : ''}</h1>
      <p className="text-sm text-gray-600">Your role: <span className="font-medium">{role}</span></p>
      <div className="grid gap-2">
        <Link className="underline text-primary" to="/volunteers">Go to Volunteers</Link>
        {role === 'admin' && <Link className="underline text-primary" to="/admin">Go to Admin</Link>}
        {(role==='admin'||role==='hr') && <Link className="underline text-primary" to="/hr">Go to HR</Link>}
        {(role==='admin'||role==='finance') && <Link className="underline text-primary" to="/finance">Go to Finance</Link>}
        {(role==='admin'||role==='projects') && <Link className="underline text-primary" to="/projects">Go to Projects</Link>}
      </div>
    </div>
  )
}
