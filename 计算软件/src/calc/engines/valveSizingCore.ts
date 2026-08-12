/**
 * 调节阀选型算法族 — 各厂家公开的 IEC / ISA 路径不同处在此分流。
 * 系数（FL/xT）仍来自样本/图纸；公式常数与主报 Cv/Kv/Cg 按厂家算法切换。
 */

export type ValveFlowStyle = 'liquid' | 'gas' | 'steam'

/** 厂家算法 ID（决定 N 系数路径、主报量、附加量） */
export type ValveAlgorithmId =
  | 'iec_60534'
  | 'isa_fisher'
  | 'isa_masoneilan'
  | 'gb_iec'

export const VALVE_ALGORITHMS: {
  id: ValveAlgorithmId
  name: string
  nameEn: string
  standardLabel: string
  primary: 'Cv' | 'Kv'
}[] = [
  {
    id: 'iec_60534',
    name: 'IEC 60534（公制 Kv）',
    nameEn: 'IEC 60534-2-1 metric',
    standardLabel: 'IEC 60534-2-1',
    primary: 'Kv',
  },
  {
    id: 'isa_fisher',
    name: 'Fisher / ANSI·ISA（Cv + Cg）',
    nameEn: 'ANSI/ISA-75.01 (Fisher)',
    standardLabel: 'ANSI/ISA-75.01.01 · IEC 60534-2-1（Fisher 路径）',
    primary: 'Cv',
  },
  {
    id: 'isa_masoneilan',
    name: 'Masoneilan / ISA（Cv）',
    nameEn: 'ISA-75.01 (Masoneilan)',
    standardLabel: 'ANSI/ISA-75.01.01 · IEC 60534-2-1（Masoneilan 路径）',
    primary: 'Cv',
  },
  {
    id: 'gb_iec',
    name: '国内 GB/IEC（公制 Kv）',
    nameEn: 'GB / IEC 60534',
    standardLabel: 'GB/T（参照 IEC 60534-2-1）',
    primary: 'Kv',
  },
]

export function getValveAlgorithm(id: ValveAlgorithmId) {
  return VALVE_ALGORITHMS.find((a) => a.id === id) ?? VALVE_ALGORITHMS[0]!
}

/** 厂家默认算法 */
export const VENDOR_DEFAULT_ALGORITHM: Record<string, ValveAlgorithmId> = {
  generic_iec: 'iec_60534',
  fisher: 'isa_fisher',
  samson: 'iec_60534',
  masoneilan: 'isa_masoneilan',
  metso: 'iec_60534',
  spirax: 'iec_60534',
  wuzhong: 'gb_iec',
}

export function defaultAlgorithmForVendor(vendorId: string): ValveAlgorithmId {
  return VENDOR_DEFAULT_ALGORITHM[vendorId] ?? 'iec_60534'
}

/** IEC/ISA 液体体积流量常数：q m³/h，Δp bar → 得到 Kv；再换 Cv */
const N1_KV_M3H_BAR = 1 // Kv = q/(Fp*sqrt(dp_bar/SG)) 即 N1=1 对 Kv

/**
 * 气体质量流量（IEC/ISA 表）：
 * W[kg/h] = N6 * Fp * Y * Cv * sqrt(x * P1[bar] * ρ[kg/m³])
 * Fisher/ISA 常用 N6 = 27.3（kg/h, bar）
 */
const N6_KG_H_BAR_CV = 27.3

/** Kv ↔ Cv（IEC）：Kv = 0.865·Cv；Cv = 1.156·Kv */
export function kvToCv(Kv: number): number {
  return Kv / 0.865
}
export function cvToKv(Cv: number): number {
  return 0.865 * Cv
}

export function criticalPressureRatioFactor(pv: number, pc: number): number {
  return 0.96 - 0.28 * Math.sqrt(Math.max(pv, 0) / Math.max(pc, 1))
}

export function expansibilityY(x: number, Fgamma: number, xT: number): {
  Y: number
  xEff: number
  xChoked: number
} {
  const xChoked = Fgamma * xT
  const xEff = Math.min(x, xChoked)
  // IEC：Y = 1 - x/(3·Fγ·xT)，且 Y ≥ 2/3
  const Y = Math.max(2 / 3, 1 - xEff / (3 * Fgamma * xT))
  return { Y, xEff, xChoked }
}

/** 液体：求所需 Kv（阻塞用 FL） */
export function sizeLiquidKv(opts: {
  massFlow_kg_s: number
  density: number
  p1: number
  p2: number
  pv: number
  pc: number
  FL: number
  Fp: number
}): {
  Kv: number
  Cv: number
  deltaP: number
  deltaPeff: number
  deltaPmax: number
  Ff: number
  regime: 'normal' | 'choked' | 'flashing' | 'cavitation_risk'
  sigma?: number
  warnings: string[]
} {
  const { massFlow_kg_s, density, p1, p2, pv, pc, FL, Fp } = opts
  const deltaP = p1 - p2
  const warnings: string[] = []
  const Ff = criticalPressureRatioFactor(pv, pc)
  const deltaPmax = FL ** 2 * (p1 - Ff * pv)
  const deltaPeff = Math.min(deltaP, deltaPmax)
  const q_m3h = (massFlow_kg_s / density) * 3600
  const dp_bar = deltaPeff / 1e5
  const SG = density / 1000
  const Kv = q_m3h / (N1_KV_M3H_BAR * Fp * Math.sqrt(dp_bar / SG))
  const Cv = kvToCv(Kv)

  let regime: 'normal' | 'choked' | 'flashing' | 'cavitation_risk' = 'normal'
  let sigma: number | undefined
  if (deltaP >= deltaPmax) {
    regime = p2 < pv ? 'flashing' : 'choked'
    warnings.push('达到阻塞流（Δp ≥ FL²(p1−Ff·pv)），继续增大压降不会增加流量。')
  } else {
    sigma = (p1 - pv) / deltaP
    if (sigma < 1.5) {
      regime = 'cavitation_risk'
      warnings.push(`气蚀风险指标 σ=${sigma.toFixed(2)} 偏低，建议校核抗气蚀阀内件。`)
    }
  }

  return { Kv, Cv, deltaP, deltaPeff, deltaPmax, Ff, regime, sigma, warnings }
}

/**
 * 气体/蒸汽：密度已知时用质量式（N6）。
 * Fisher 另报 Cg = 40·Cv·√xT
 */
export function sizeGasCv(opts: {
  massFlow_kg_s: number
  density: number
  p1: number
  p2: number
  kappa: number
  xT: number
  Fp: number
  algorithm: ValveAlgorithmId
}): {
  Kv: number
  Cv: number
  Cg?: number
  deltaP: number
  x: number
  Y: number
  xChoked: number
  regime: 'normal' | 'choked'
  warnings: string[]
} {
  const { massFlow_kg_s, density, p1, p2, kappa, xT, Fp, algorithm } = opts
  const deltaP = p1 - p2
  const warnings: string[] = []
  const x = deltaP / p1
  const Fgamma = kappa / 1.4
  const { Y, xEff, xChoked } = expansibilityY(x, Fgamma, xT)
  const W_kg_h = massFlow_kg_s * 3600
  const P1_bar = p1 / 1e5

  // 统一用 ISA/IEC 的 Cv 质量式；厂家差异在主报量与 Cg
  const Cv =
    W_kg_h / (N6_KG_H_BAR_CV * Fp * Y * Math.sqrt(xEff * P1_bar * density))
  const Kv = cvToKv(Cv)

  let regime: 'normal' | 'choked' = 'normal'
  if (x >= xChoked) {
    regime = 'choked'
    warnings.push('气体达到阻塞流（x ≥ Fγ·xT）。')
  }

  // Fisher 气动噪声用 Cg；Masoneilan 偶有 C1=Cg/Cv 习惯，一并给出 Cg
  let Cg: number | undefined
  if (algorithm === 'isa_fisher' || algorithm === 'isa_masoneilan') {
    Cg = 40 * Cv * Math.sqrt(xT)
  }

  return { Kv, Cv, Cg, deltaP, x, Y, xChoked, regime, warnings }
}
