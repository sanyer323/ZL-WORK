import {
  DENSITY_UNITS,
  DP_UNITS,
  FLOW_MASS_UNITS,
  FLOW_VOL_UNITS,
  LENGTH_UNITS,
  PRESSURE_UNITS,
  TEMP_UNITS,
  VISCOSITY_UNITS,
  pressureUnitLabel,
  type PressureRef,
} from '@/calc/units'
import { useUnitStore } from '@/store/unitStore'
import { Field } from '@/components/FormBits'

export function UnitPrefsPanel() {
  const u = useUnitStore()
  return (
    <details open className="param-block">
      <summary>工程单位</summary>
      <div className="unit-grid">
        <Field label="过程压力基准（默认表压）">
          <select
            value={u.pressureRef}
            onChange={(e) => u.setUnit('pressureRef', e.target.value as PressureRef)}
          >
            <option value="gauge">表压 (g)</option>
            <option value="absolute">绝压 (a)</option>
          </select>
        </Field>
        <Field label="过程压力单位">
          <select
            value={u.pressure}
            onChange={(e) => u.setUnit('pressure', e.target.value as typeof u.pressure)}
          >
            {PRESSURE_UNITS.map((x) => (
              <option key={x} value={x}>
                {pressureUnitLabel(x, u.pressureRef)}
              </option>
            ))}
          </select>
        </Field>
        <Field label="差压 Δp">
          <select
            value={u.diffPressure}
            onChange={(e) => u.setUnit('diffPressure', e.target.value as typeof u.diffPressure)}
          >
            {DP_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="长度 / 口径">
          <select
            value={u.length}
            onChange={(e) => u.setUnit('length', e.target.value as typeof u.length)}
          >
            {LENGTH_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="温度">
          <select
            value={u.temperature}
            onChange={(e) => u.setUnit('temperature', e.target.value as typeof u.temperature)}
          >
            {TEMP_UNITS.map((x) => (
              <option key={x} value={x}>
                °{x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="体积流量">
          <select
            value={u.flowVol}
            onChange={(e) => u.setUnit('flowVol', e.target.value as typeof u.flowVol)}
          >
            {FLOW_VOL_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="质量流量">
          <select
            value={u.flowMass}
            onChange={(e) => u.setUnit('flowMass', e.target.value as typeof u.flowMass)}
          >
            {FLOW_MASS_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="密度">
          <select
            value={u.density}
            onChange={(e) => u.setUnit('density', e.target.value as typeof u.density)}
          >
            {DENSITY_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
        <Field label="粘度">
          <select
            value={u.viscosity}
            onChange={(e) => u.setUnit('viscosity', e.target.value as typeof u.viscosity)}
          >
            {VISCOSITY_UNITS.map((x) => (
              <option key={x} value={x}>
                {x}
              </option>
            ))}
          </select>
        </Field>
      </div>
      <button className="btn secondary" type="button" onClick={() => u.reset()}>
        恢复默认单位
      </button>
      <div className="hint-line">
        默认：表压 + MPa。切换表压/绝压时，输入框按当前基准显示；内部计算始终用绝压。
      </div>
    </details>
  )
}
