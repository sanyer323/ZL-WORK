import { Link } from 'react-router-dom'
import { MODULES, CATEGORY_LABEL } from '@/calc/registry'
import { FLUID_COUNT } from '@/calc/fluids'

export function HomePage() {
  return (
    <div>
      <div className="topbar">
        <div>
          <h2>产品概览</h2>
          <p className="sub">
            调节阀 + 差压节流计量（含 PRESO 族与调整型孔板）· 先 Web，后桌面同引擎
          </p>
        </div>
        <span className="badge ready">MVP 0.1</span>
      </div>

      <div className="hero-home">
        <div className="hero-copy">
          <h2>流衡 FlowSize</h2>
          <p>
            面向过程工业的工程计算产品：制造商中立选型、标准可追溯、计算书可沉淀。
            本版本覆盖调节阀（IEC 60534）与完整差压一次元件族（ISO 5167 全系列 + 厂商标定扩展）。
          </p>
        </div>
        <div className="hero-side">
          <h3>本版模块地图</h3>
          <ul>
            <li>调节阀：Cv/Kv、阻塞流、气蚀风险</li>
            <li>标准孔板 + Toolkit 调整型孔板</li>
            <li>PRESO：文丘里 / 喷嘴 / 楔形 / V 锥 / Ellipse 均速管</li>
            <li>限流孔板：单级/多级压降分配（Beta）</li>
            <li>自建工质库约 {FLUID_COUNT} 种（水/蒸汽、工业气、烃、热油、浆料等）</li>
          </ul>
        </div>
      </div>

      <div className="grid-cards">
        {MODULES.map((m) => (
          <Link key={m.id} to={`/calc/${m.id}`} className="card">
            <span className={`badge ${m.status}`}>
              {m.status === 'ready' ? '可用' : m.status === 'beta' ? 'Beta' : '规划中'}
            </span>
            <h3>{m.name}</h3>
            <p>{m.description}</p>
            <div className="meta">
              <span className="chip">{CATEGORY_LABEL[m.category]}</span>
              <span className="chip">{m.productFamily}</span>
              {m.standards.slice(0, 2).map((s) => (
                <span className="chip" key={s}>
                  {s}
                </span>
              ))}
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
