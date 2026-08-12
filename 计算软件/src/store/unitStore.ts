import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type {
  DensityUnit,
  DiffPressureUnit,
  FlowMassUnit,
  FlowVolUnit,
  LengthUnit,
  PressureRef,
  PressureUnit,
  TempUnit,
  ViscosityUnit,
} from '@/calc/units'

export interface UnitPrefs {
  /** 过程压力单位，默认 MPa */
  pressure: PressureUnit
  /** 表压 / 绝压，默认表压 */
  pressureRef: PressureRef
  diffPressure: DiffPressureUnit
  length: LengthUnit
  temperature: TempUnit
  flowVol: FlowVolUnit
  flowMass: FlowMassUnit
  density: DensityUnit
  viscosity: ViscosityUnit
}

interface UnitState extends UnitPrefs {
  setUnit: <K extends keyof UnitPrefs>(key: K, value: UnitPrefs[K]) => void
  reset: () => void
}

const defaults: UnitPrefs = {
  pressure: 'MPa',
  pressureRef: 'gauge',
  diffPressure: 'kPa',
  length: 'mm',
  temperature: 'C',
  flowVol: 'm3/h',
  flowMass: 'kg/h',
  density: 'kg/m3',
  viscosity: 'cP',
}

export const useUnitStore = create<UnitState>()(
  persist(
    (set) => ({
      ...defaults,
      setUnit: (key, value) => set({ [key]: value }),
      reset: () => set({ ...defaults }),
    }),
    {
      name: 'flowsize-units-v2',
      merge: (persisted, current) => {
        const p = (persisted ?? {}) as Partial<UnitPrefs>
        return {
          ...current,
          ...p,
          // 旧版本无 pressureRef 时默认表压
          pressureRef: p.pressureRef ?? 'gauge',
          pressure: p.pressure ?? 'MPa',
        }
      },
    },
  ),
)
