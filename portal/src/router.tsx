import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import NotFound from './pages/NotFound'
import { ProtectedRoute } from './components/ProtectedRoute'
import { RoleGate } from './components/RoleGate'
import AdminDashboard from './pages/admin/AdminDashboard'
import HrDashboard from './pages/hr/HrDashboard'
import FinanceDashboard from './pages/finance/FinanceDashboard'
import ProjectsDashboard from './pages/projects/ProjectsDashboard'
import VolunteersDashboard from './pages/volunteers/VolunteersDashboard'

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
      <Route
        path="/admin"
        element={
          <ProtectedRoute>
            <RoleGate allow={["admin"]}>
              <AdminDashboard />
            </RoleGate>
          </ProtectedRoute>
        }
      />
      <Route
        path="/hr"
        element={
          <ProtectedRoute>
            <RoleGate allow={["admin", "hr"]}>
              <HrDashboard />
            </RoleGate>
          </ProtectedRoute>
        }
      />
      <Route
        path="/finance"
        element={
          <ProtectedRoute>
            <RoleGate allow={["admin", "finance"]}>
              <FinanceDashboard />
            </RoleGate>
          </ProtectedRoute>
        }
      />
      <Route
        path="/projects"
        element={
          <ProtectedRoute>
            <RoleGate allow={["admin", "projects"]}>
              <ProjectsDashboard />
            </RoleGate>
          </ProtectedRoute>
        }
      />
      <Route
        path="/volunteers"
        element={
          <ProtectedRoute>
            <RoleGate allow={["admin", "volunteer"]}>
              <VolunteersDashboard />
            </RoleGate>
          </ProtectedRoute>
        }
      />
      <Route path="/404" element={<NotFound />} />
      <Route path="*" element={<Navigate to="/404" replace />} />
    </Routes>
  )
}
