import type { Role } from '@/types/roles'
import { useAuth } from '@/state/AuthContext'

export function RoleGate({ allow, children }: { allow: Role[]; children: JSX.Element }) {
  const { role } = useAuth()
  if (!role) return null
  if (!allow.includes(role)) {
    return <div className="p-6 text-red-600">Access denied for role: {role}</div>
  }
  return children
}
