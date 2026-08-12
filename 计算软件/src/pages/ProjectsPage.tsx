import { Link } from 'react-router-dom'
import { useAppStore } from '@/store/appStore'
import { getModule } from '@/calc/registry'

export function ProjectsPage() {
  const { projects, removeProject } = useAppStore()

  return (
    <div>
      <div className="topbar">
        <div>
          <h2>项目</h2>
          <p className="sub">本地浏览器保存计算记录（后续可接云端账号与桌面同步）</p>
        </div>
      </div>

      {projects.length === 0 ? (
        <div className="panel">
          <p style={{ margin: 0, color: 'var(--ink-soft)' }}>
            暂无项目。在任意计算页点击「保存到项目」即可归档。
          </p>
        </div>
      ) : (
        <div className="grid-cards">
          {projects.map((p) => {
            const mod = getModule(p.moduleId)
            return (
              <div key={p.id} className="card">
                <h3>{p.name}</h3>
                <p>
                  {mod?.name ?? p.moduleId}
                  {p.note ? ` · ${p.note}` : ''}
                </p>
                <div className="meta">
                  <span className="chip">{new Date(p.updatedAt).toLocaleString()}</span>
                </div>
                <div className="btn-row">
                  <Link className="btn secondary" to={`/calc/${p.moduleId}`}>
                    打开模块
                  </Link>
                  <button className="btn secondary" type="button" onClick={() => removeProject(p.id)}>
                    删除
                  </button>
                </div>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
