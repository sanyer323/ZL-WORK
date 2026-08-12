import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { Sidebar } from '@/components/Sidebar'
import { HomePage } from '@/pages/HomePage'
import { ProjectsPage } from '@/pages/ProjectsPage'
import { CalcPage } from '@/pages/CalcPage'

export default function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <Sidebar />
        <main className="main">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/projects" element={<ProjectsPage />} />
            <Route path="/calc/:moduleId" element={<CalcPage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}
