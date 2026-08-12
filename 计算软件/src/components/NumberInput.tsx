import { useEffect, useState } from 'react'

/**
 * 可控数字输入：允许输入负号「-」、小数点等中间态
 * （原生 type=number + Number(value) 会在输入「-」时被清掉）
 */
export function NumberInput(props: {
  value: number
  onChange: (n: number) => void
  min?: number
  max?: number
  placeholder?: string
  className?: string
}) {
  const [text, setText] = useState(() => String(props.value))
  const [focused, setFocused] = useState(false)

  useEffect(() => {
    if (!focused) setText(String(props.value))
  }, [props.value, focused])

  return (
    <input
      type="text"
      inputMode="decimal"
      className={props.className}
      placeholder={props.placeholder}
      value={text}
      onFocus={() => setFocused(true)}
      onChange={(e) => {
        const v = e.target.value
        if (v === '' || v === '-' || v === '.' || v === '-.') {
          setText(v)
          return
        }
        if (!/^-?\d*\.?\d*(e[+-]?\d*)?$/i.test(v)) return
        setText(v)
        const n = Number(v)
        if (!Number.isFinite(n)) return
        if (props.min != null && n < props.min) return
        if (props.max != null && n > props.max) return
        props.onChange(n)
      }}
      onBlur={() => {
        setFocused(false)
        const n = Number(text)
        if (!Number.isFinite(n)) {
          setText(String(props.value))
          return
        }
        let next = n
        if (props.min != null && next < props.min) next = props.min
        if (props.max != null && next > props.max) next = props.max
        setText(String(next))
        props.onChange(next)
      }}
    />
  )
}
