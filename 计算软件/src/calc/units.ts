/** SI 单位换算与工程单位工具 */

export type PressureRef = 'gauge' | 'absolute'

export type PressureUnit =
  | 'Pa'
  | 'kPa'
  | 'MPa'
  | 'bar'
  | 'mbar'
  | 'psi'
  | 'kgf/cm2'
  | 'ata'
  | 'mmH2O'
  | 'mH2O'
  | 'inH2O'
  | 'mmHg'
  | 'torr'

export type DiffPressureUnit =
  | 'Pa'
  | 'kPa'
  | 'MPa'
  | 'bar'
  | 'mbar'
  | 'psi'
  | 'kgf/cm2'
  | 'mmH2O'
  | 'mH2O'
  | 'inH2O'
  | 'mmHg'
  | 'inHg'

export type FlowVolUnit =
  | 'm3/s'
  | 'm3/min'
  | 'm3/h'
  | 'L/s'
  | 'L/min'
  | 'L/h'
  | 'gpm'
  | 'cfm'
  | 'Nm3/h'
  | 'Nm3/s'
  | 'SCFH'

export type FlowMassUnit = 'kg/s' | 'kg/min' | 'kg/h' | 't/h' | 'lb/s' | 'lb/min' | 'lb/h'
export type LengthUnit = 'm' | 'cm' | 'mm' | 'in' | 'ft'
export type TempUnit = 'C' | 'K' | 'F'
export type DensityUnit = 'kg/m3' | 'g/cm3' | 'kg/L' | 'lb/ft3' | 'lb/gal'
export type ViscosityUnit = 'Pa·s' | 'mPa·s' | 'cP' | 'µPa·s'

/** 过程压力 — 常用 MPa / bar / kPa 靠前 */
export const PRESSURE_UNITS: PressureUnit[] = [
  'MPa',
  'bar',
  'kPa',
  'Pa',
  'mbar',
  'psi',
  'kgf/cm2',
  'ata',
  'mmH2O',
  'mH2O',
  'inH2O',
  'mmHg',
  'torr',
]

export const DP_UNITS: DiffPressureUnit[] = [
  'kPa',
  'MPa',
  'Pa',
  'bar',
  'mbar',
  'psi',
  'kgf/cm2',
  'mmH2O',
  'mH2O',
  'inH2O',
  'mmHg',
  'inHg',
]

export const LENGTH_UNITS: LengthUnit[] = ['mm', 'cm', 'm', 'in', 'ft']
export const TEMP_UNITS: TempUnit[] = ['C', 'K', 'F']
export const FLOW_VOL_UNITS: FlowVolUnit[] = [
  'm3/h',
  'm3/min',
  'm3/s',
  'L/h',
  'L/min',
  'L/s',
  'gpm',
  'cfm',
  'Nm3/h',
  'Nm3/s',
  'SCFH',
]
export const FLOW_MASS_UNITS: FlowMassUnit[] = [
  'kg/h',
  'kg/min',
  'kg/s',
  't/h',
  'lb/h',
  'lb/min',
  'lb/s',
]
export const DENSITY_UNITS: DensityUnit[] = ['kg/m3', 'g/cm3', 'kg/L', 'lb/ft3', 'lb/gal']
export const VISCOSITY_UNITS: ViscosityUnit[] = ['Pa·s', 'mPa·s', 'cP', 'µPa·s']

const toPa: Record<PressureUnit | DiffPressureUnit, number> = {
  Pa: 1,
  kPa: 1e3,
  MPa: 1e6,
  mbar: 100,
  bar: 1e5,
  psi: 6894.757,
  'kgf/cm2': 98066.5,
  ata: 98066.5,
  mmH2O: 9.80665,
  mH2O: 9806.65,
  inH2O: 249.089,
  mmHg: 133.322,
  torr: 133.322,
  inHg: 3386.39,
}

const toM3s: Record<FlowVolUnit, number> = {
  'm3/s': 1,
  'm3/min': 1 / 60,
  'm3/h': 1 / 3600,
  'L/s': 1e-3,
  'L/min': 1e-3 / 60,
  'L/h': 1e-3 / 3600,
  gpm: 6.30902e-5,
  cfm: 4.71947e-4,
  'Nm3/h': 1 / 3600,
  'Nm3/s': 1,
  SCFH: 7.86579e-6,
}

const toKgs: Record<FlowMassUnit, number> = {
  'kg/s': 1,
  'kg/min': 1 / 60,
  'kg/h': 1 / 3600,
  't/h': 1000 / 3600,
  'lb/s': 0.45359237,
  'lb/min': 0.45359237 / 60,
  'lb/h': 0.45359237 / 3600,
}

const toM: Record<LengthUnit, number> = {
  m: 1,
  cm: 0.01,
  mm: 1e-3,
  in: 0.0254,
  ft: 0.3048,
}

const toKgM3: Record<DensityUnit, number> = {
  'kg/m3': 1,
  'g/cm3': 1000,
  'kg/L': 1000,
  'lb/ft3': 16.01846,
  'lb/gal': 119.8264,
}

const toPas: Record<ViscosityUnit, number> = {
  'Pa·s': 1,
  'mPa·s': 1e-3,
  cP: 1e-3,
  'µPa·s': 1e-6,
}

export function pressureToPa(value: number, unit: PressureUnit | DiffPressureUnit): number {
  return value * toPa[unit]
}

export function paToPressure(pa: number, unit: PressureUnit | DiffPressureUnit): number {
  return pa / toPa[unit]
}

/**
 * 显示用过程压力：内部存绝压 Pa
 * gauge → 显示表压 = 绝压 − 大气压
 */
export function absPaToDisplay(
  absPa: number,
  atmPa: number,
  unit: PressureUnit,
  ref: PressureRef,
): number {
  const p = ref === 'gauge' ? absPa - atmPa : absPa
  return paToPressure(p, unit)
}

/** 输入显示值 → 绝压 Pa */
export function displayToAbsPa(
  display: number,
  atmPa: number,
  unit: PressureUnit,
  ref: PressureRef,
): number {
  const p = pressureToPa(display, unit)
  return ref === 'gauge' ? p + atmPa : p
}

export function flowVolToM3s(value: number, unit: FlowVolUnit): number {
  return value * toM3s[unit]
}

export function m3sToFlowVol(m3s: number, unit: FlowVolUnit): number {
  return m3s / toM3s[unit]
}

export function flowMassToKgs(value: number, unit: FlowMassUnit): number {
  return value * toKgs[unit]
}

export function kgsToFlowMass(kgs: number, unit: FlowMassUnit): number {
  return kgs / toKgs[unit]
}

export function lengthToM(value: number, unit: LengthUnit): number {
  return value * toM[unit]
}

export function mToLength(m: number, unit: LengthUnit): number {
  return m / toM[unit]
}

export function densityToKgM3(value: number, unit: DensityUnit): number {
  return value * toKgM3[unit]
}

export function kgM3ToDensity(kgm3: number, unit: DensityUnit): number {
  return kgm3 / toKgM3[unit]
}

export function viscosityToPas(value: number, unit: ViscosityUnit): number {
  return value * toPas[unit]
}

export function pasToViscosity(pas: number, unit: ViscosityUnit): number {
  return pas / toPas[unit]
}

export function tempToK(value: number, unit: TempUnit): number {
  if (unit === 'K') return value
  if (unit === 'C') return value + 273.15
  return ((value - 32) * 5) / 9 + 273.15
}

export function tempToC(value: number, unit: TempUnit): number {
  if (unit === 'C') return value
  if (unit === 'K') return value - 273.15
  return ((value - 32) * 5) / 9
}

export function cToTemp(c: number, unit: TempUnit): number {
  if (unit === 'C') return c
  if (unit === 'K') return c + 273.15
  return (c * 9) / 5 + 32
}

export function formatEng(value: number, digits = 4): string {
  if (!Number.isFinite(value)) return '—'
  if (value === 0) return '0'
  const abs = Math.abs(value)
  if (abs >= 1e5 || abs < 1e-3) return value.toExponential(digits - 1)
  return value.toPrecision(digits)
}

export function pressureUnitLabel(
  u: PressureUnit | DiffPressureUnit,
  ref: PressureRef | boolean = 'absolute',
): string {
  const mode: PressureRef = typeof ref === 'boolean' ? (ref ? 'absolute' : 'gauge') : ref
  const abs = mode === 'absolute'
  switch (u) {
    case 'bar':
      return abs ? 'bar(a)' : 'bar(g)'
    case 'kPa':
      return abs ? 'kPa(a)' : 'kPa(g)'
    case 'MPa':
      return abs ? 'MPa(a)' : 'MPa(g)'
    case 'psi':
      return abs ? 'psia' : 'psig'
    case 'mbar':
      return abs ? 'mbar(a)' : 'mbar(g)'
    case 'kgf/cm2':
      return abs ? 'kgf/cm²(a)' : 'kgf/cm²(g)'
    case 'ata':
      return abs ? 'ata' : 'at(g)'
    default:
      return abs ? `${u}(a)` : `${u}(g)`
  }
}
