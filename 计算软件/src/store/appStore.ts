import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export interface ProjectItem {
  id: string
  name: string
  moduleId: string
  updatedAt: string
  note?: string
}

interface AppState {
  projects: ProjectItem[]
  addProject: (p: Omit<ProjectItem, 'id' | 'updatedAt'>) => void
  removeProject: (id: string) => void
}

export const useAppStore = create<AppState>()(
  persist(
    (set) => ({
      projects: [],
      addProject: (p) =>
        set((s) => ({
          projects: [
            {
              ...p,
              id: crypto.randomUUID(),
              updatedAt: new Date().toISOString(),
            },
            ...s.projects,
          ],
        })),
      removeProject: (id) =>
        set((s) => ({ projects: s.projects.filter((x) => x.id !== id) })),
    }),
    { name: 'flowsize-projects' },
  ),
)
