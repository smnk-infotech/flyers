import NavBar from '@/components/NavBar'

export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-full grid grid-rows-[auto,1fr]">
      <NavBar />
      <main className="mx-auto max-w-6xl w-full px-4 py-6">{children}</main>
    </div>
  )
}
