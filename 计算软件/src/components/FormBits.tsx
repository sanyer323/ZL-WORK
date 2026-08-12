import type { ReactNode } from 'react'

export function Field(props: {
  label: string
  children: ReactNode
  unit?: string
}) {
  return (
    <div className="field">
      <label>{props.label}</label>
      {props.unit ? (
        <div className="field-row">
          {props.children}
          <div className="unit">{props.unit}</div>
        </div>
      ) : (
        props.children
      )}
    </div>
  )
}

export function Metric(props: { label: string; value: string }) {
  return (
    <div className="metric">
      <div className="k">{props.label}</div>
      <div className="v">{props.value}</div>
    </div>
  )
}
