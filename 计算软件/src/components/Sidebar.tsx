import { NavLink } from 'react-router-dom'
import {
  Gauge,
  LayoutDashboard,
  FolderKanban,
  Pipette,
} from 'lucide-react'
import { MODULES, CATEGORY_LABEL, type ModuleCategory } from '@/calc/registry'

const categoryOrder: ModuleCategory[] = [
  'control_valve',
  'dp_meter',
  'restriction',
]

export function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-mark" aria-hidden>
          <Pipette size={20} color="#7DD3C0" />
        </div>
        <div>
          <h1>流衡 FlowSize</h1>
          <p>工程计算 · Web 版</p>
        </div>
      </div>

      <nav className="nav-section">
        <div className="nav-label">工作区</div>
        <NavLink to="/" className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} end>
          <LayoutDashboard size={16} />
          概览
        </NavLink>
        <NavLink
          to="/projects"
          className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
        >
          <FolderKanban size={16} />
          项目
        </NavLink>
      </nav>

      {categoryOrder.map((cat) => (
        <nav className="nav-section" key={cat}>
          <div className="nav-label">{CATEGORY_LABEL[cat]}</div>
          {MODULES.filter((m) => m.category === cat).map((m) => (
            <NavLink
              key={m.id}
              to={`/calc/${m.id}`}
              className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
            >
              <Gauge size={16} />
              {m.name}
            </NavLink>
          ))}
        </nav>
      ))}
    </aside>
  )
}
