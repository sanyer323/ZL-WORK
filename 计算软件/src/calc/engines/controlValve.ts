/**
 * 调节阀选型 — 按厂家算法分流（IEC / Fisher·ISA / Masoneilan·ISA / 国内 GB）
 */

import {
  type ValveAlgorithmId,
  type ValveFlowStyle,
  getValveAlgorithm,
  sizeGasCv,
  sizeLiquidKv,
} from './valveSizingCore'

export type { ValveFlowStyle, ValveAlgorithmId }

export interface ControlValveInput {
  style: ValveFlowStyle
  /** 厂家算法；决定 N 路径、主报 Cv/Kv、是否算 Cg */
  algorithm?: ValveAlgorithmId
  massFlow: number
  density: number
  p1: number
  p2: number
  pv?: number
  pc?: number
  kappa?: number
  FL?: number
  xT?: number
  Fp?: number
  Fd?: number
  valveTypeName?: string
  vendorName?: string
  modelName?: string
  sheetBrand?: string
  coeffSource?: string
  ratedCv?: number
}

export interface ControlValveResult {
  deltaP: number
  Kv: number
  Cv: number
  /** Fisher/Masoneilan 气体附加系数 */
  Cg?: number
  regime: 'normal' | 'choked' | 'flashing' | 'cavitation_risk'
  sigma?: number
  Ff?: number
  x?: number
  Y?: number
  FL: number
  Fp: number
  xT: number
  Fd: number
  algorithm: ValveAlgorithmId
  algorithmName: string
  primaryCoeff: 'Cv' | 'Kv'
  valveTypeName?: string
  vendorName?: string
  modelName?: string
  sheetBrand?: string
  coeffSource?: string
  ratedCv?: number
  warnings: string[]
  standard: string
}

export function calcControlValve(input: ControlValveInput): ControlValveResult {
  const { massFlow, density, p1, p2 } = input
  if (p1 - p2 <= 0) throw new Error('上游压力必须大于下游压力')
  if (massFlow <= 0) throw new Error('流量必须为正')

  const algorithm: ValveAlgorithmId = input.algorithm ?? 'iec_60534'
  const algoMeta = getValveAlgorithm(algorithm)
  const FL = input.FL ?? 0.9
  const Fp = input.Fp ?? 1
  const xT = input.xT ?? 0.75
  const Fd = input.Fd ?? 0.46

  const baseMeta = {
    FL,
    Fp,
    xT,
    Fd,
    algorithm,
    algorithmName: algoMeta.name,
    primaryCoeff: algoMeta.primary,
    valveTypeName: input.valveTypeName,
    vendorName: input.vendorName,
    modelName: input.modelName,
    sheetBrand: input.sheetBrand,
    coeffSource: input.coeffSource,
    ratedCv: input.ratedCv,
  }

  if (input.style === 'liquid') {
    const r = sizeLiquidKv({
      massFlow_kg_s: massFlow,
      density,
      p1,
      p2,
      pv: input.pv ?? 2339,
      pc: input.pc ?? 22.06e6,
      FL,
      Fp,
    })
    const warnings = [...r.warnings]
    if (algorithm === 'isa_fisher') {
      warnings.push(`Fisher 压力恢复相关 Km = FL² = ${(FL * FL).toFixed(4)}`)
    }
    return {
      ...baseMeta,
      deltaP: r.deltaP,
      Kv: r.Kv,
      Cv: r.Cv,
      regime: r.regime,
      sigma: r.sigma,
      Ff: r.Ff,
      warnings,
      standard: `${algoMeta.standardLabel}（液体）`,
    }
  }

  const g = sizeGasCv({
    massFlow_kg_s: massFlow,
    density,
    p1,
    p2,
    kappa: input.kappa ?? 1.4,
    xT,
    Fp,
    algorithm,
  })

  const phase = input.style === 'steam' ? '蒸汽' : '气体'
  return {
    ...baseMeta,
    deltaP: g.deltaP,
    Kv: g.Kv,
    Cv: g.Cv,
    Cg: g.Cg,
    regime: g.regime,
    x: g.x,
    Y: g.Y,
    warnings: g.warnings,
    standard: `${algoMeta.standardLabel}（${phase}）`,
  }
}

// 兼容旧导入
export { kvToCv, cvToKv, getValveAlgorithm, VALVE_ALGORITHMS, defaultAlgorithmForVendor } from './valveSizingCore'
