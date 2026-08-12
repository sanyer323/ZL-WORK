import { materialsByGroup, type MaterialProps } from '@/calc/materials'
import { Field } from '@/components/FormBits'

export function MaterialSelect(props: {
  label: string
  value: string
  onChange: (id: string) => void
  material: MaterialProps
  customAlpha: string
  onCustomAlphaChange: (v: string) => void
}) {
  const groups = materialsByGroup()
  return (
    <>
      <Field label={props.label}>
        <select value={props.value} onChange={(e) => props.onChange(e.target.value)}>
          {groups.map((g) => (
            <optgroup key={g.group} label={g.label}>
              {g.items.map((m) => (
                <option key={m.id} value={m.id}>
                  {m.name} (α={m.alpha.toExponential(2)})
                </option>
              ))}
            </optgroup>
          ))}
        </select>
      </Field>
      {props.value === 'custom' && (
        <Field label="自定义 α" unit="1/K">
          <input
            type="number"
            step="1e-7"
            value={props.customAlpha}
            onChange={(e) => props.onCustomAlphaChange(e.target.value)}
          />
        </Field>
      )}
      <div className="hint-line">
        {props.material.nameEn} · α = {props.material.alpha.toExponential(3)} 1/K
        {props.material.note ? ` · ${props.material.note}` : ''}
      </div>
    </>
  )
}
