import {
  FLUID_COUNT,
  fluidsByCategory,
  getFluid,
  searchFluids,
} from '@/calc/fluids'
import { Field } from '@/components/FormBits'
import { useMemo, useState } from 'react'

export function FluidPicker(props: {
  value: string
  onChange: (id: string) => void
}) {
  const [query, setQuery] = useState('')
  const groups = useMemo(() => fluidsByCategory(), [])
  const filtered = useMemo(() => {
    const list = searchFluids(query)
    // 始终保留当前选中项，避免搜索时 value 不在列表导致点选异常
    if (!list.some((f) => f.id === props.value)) {
      try {
        return [getFluid(props.value), ...list]
      } catch {
        return list
      }
    }
    return list
  }, [query, props.value])

  const filteredIds = useMemo(() => new Set(filtered.map((f) => f.id)), [filtered])

  const selected = useMemo(() => {
    try {
      return getFluid(props.value)
    } catch {
      return null
    }
  }, [props.value])

  const pick = (id: string) => {
    if (!id) return
    props.onChange(id)
    // 选中后清空搜索，方便在分组列表里看到当前介质
    setQuery('')
  }

  return (
    <div className="fluid-picker">
      <Field label={`工质（库内 ${FLUID_COUNT} 种）`}>
        <input
          type="search"
          placeholder="搜索中文名 / 英文 / CAS / 标签…"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </Field>
      <Field label="选择介质">
        <select
          value={props.value}
          size={10}
          onChange={(e) => pick(e.target.value)}
          onClick={(e) => {
            // listbox 模式下部分浏览器单击已选项/过滤后需再读一次 value
            const el = e.currentTarget
            if (el.value && el.value !== props.value) pick(el.value)
          }}
        >
          {query.trim()
            ? filtered.map((f) => (
                <option key={f.id} value={f.id}>
                  [{f.phase}] {f.name}
                  {f.id === props.value ? ' ✓' : ''}
                </option>
              ))
            : groups.map((g) => (
                <optgroup key={g.category} label={`${g.label} (${g.items.length})`}>
                  {g.items
                    .filter((f) => filteredIds.has(f.id))
                    .map((f) => (
                      <option key={f.id} value={f.id}>
                        [{f.phase}] {f.name}
                      </option>
                    ))}
                </optgroup>
              ))}
        </select>
      </Field>
      {selected && (
        <div className="fluid-meta" key={selected.id}>
          <div>
            <strong>{selected.name}</strong>
            <span> · {selected.nameEn}</span>
          </div>
          <div className="fluid-meta-row">
            ρ={selected.density} kg/m³ · μ={selected.viscosity} Pa·s
            {selected.kappa != null ? ` · κ=${selected.kappa}` : ''}
            {selected.molarMass != null ? ` · M=${selected.molarMass}` : ''}
          </div>
          {selected.note && <div className="fluid-note">{selected.note}</div>}
          {(selected.tags?.length ?? 0) > 0 && (
            <div className="meta" style={{ marginTop: '0.4rem' }}>
              {selected.tags!.map((t) => (
                <span className="chip" key={t}>
                  {t}
                </span>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
