/** ISO 5167-2 同心锐边孔板 — Reader-Harris/Gallagher 流出系数 */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export type TapType = 'corner' | 'flange' | 'D_D2'
export type OrificePlateType = 'concentric' | 'eccentric' | 'segmental' | 'quadrant'

export interface OrificeInput {
  D: number
  d: number
  deltaP: number
  density: number
  viscosity: number
  tap: TapType
  isCompressible?: boolean
  p1?: number
  kappa?: number
  /** 强制使用的流出系数 */
  C?: number
  /** 强制可膨胀系数 */
  epsilon?: number
  plateType?: OrificePlateType
  /** 孔板厚度 E (m) */
  plateThickness?: number
  /** 上游锐边厚度 e (m) */
  edgeThickness?: number
  /** 排污/排气孔直径 (m) */
  drainHole?: number
  /** 管壁绝对粗糙度 Ra (m)，仅提示 */
  roughness?: number
}

export function orificeDischargeC(ReD: number, beta: number, tap: TapType, D: number): number {
  const L1 = tap === 'corner' ? 0 : tap === 'flange' ? 0.0254 / D : 1
  const L2 = tap === 'corner' ? 0 : tap === 'flange' ? 0.0254 / D : 0.47
  const M2 = (2 * L2) / (1 - beta)

  const A = ((19000 * beta) / ReD) ** 0.8
  const C =
    0.5961 +
    0.0261 * beta ** 2 -
    0.216 * beta ** 8 +
    0.000521 * ((1e6 * beta) / ReD) ** 0.7 +
    (0.0188 + 0.0063 * A) * beta ** 3.5 * (1e6 / ReD) ** 0.3 +
    (0.043 + 0.08 * Math.exp(-10 * L1) - 0.123 * Math.exp(-7 * L1)) *
      (1 - 0.11 * A) *
      (beta ** 4 / (1 - beta ** 4)) -
    0.031 * (M2 - 0.8 * M2 ** 1.1) * beta ** 1.3

  if (D < 0.07112) {
    return C + 0.011 * (0.75 - beta) * (2.8 - D / 0.0254)
  }
  return C
}

export function calcOrifice(
  input: OrificeInput,
): DpCommonResult & {
  tap: TapType
  standard: string
  plateType: OrificePlateType
  geometryNotes: string[]
} {
  const plateType = input.plateType ?? 'concentric'
  const geometryNotes: string[] = []

  if (plateType !== 'concentric') {
    geometryNotes.push(
      `${plateType} 孔板的 Cd 本版仍按同心锐边近似；正式计算请用专用关联或标定。`,
    )
  }
  if (input.plateThickness != null && input.D > 0) {
    const ED = input.plateThickness / input.D
    if (ED < 0.005 || ED > 0.1) {
      geometryNotes.push(`板厚比 E/D=${ED.toFixed(4)} 超出 ISO 5167-2 常用 0.005–0.1 范围。`)
    }
  }
  if (input.edgeThickness != null && input.d > 0) {
    const ed = input.edgeThickness / input.d
    if (ed > 0.02) {
      geometryNotes.push(`上游边缘厚度比 e/d=${ed.toFixed(4)} 偏大，锐边假设可能不成立。`)
    }
  }
  if (input.drainHole && input.drainHole > 0) {
    geometryNotes.push(
      `已计入排污孔直径 ${((input.drainHole * 1000).toFixed(2))} mm（面积修正未自动并入 d，请按厂家方法处理）。`,
    )
  }
  if (input.roughness != null) {
    geometryNotes.push(`管壁粗糙度 Ra=${(input.roughness * 1e6).toFixed(1)} μm（本版作记录，未改 Cd）。`)
  }

  const result = iterateMassFlow(
    input,
    (Re, beta) => orificeDischargeC(Re, beta, input.tap, input.D),
    'orifice',
  )

  return {
    ...result,
    warnings: [...result.warnings, ...geometryNotes.filter((n) => n.includes('超出') || n.includes('偏大'))],
    tap: input.tap,
    standard: 'ISO 5167-2:2022',
    plateType,
    geometryNotes,
  }
}

export function sizeOrificeBore(
  targetQm: number,
  base: Omit<OrificeInput, 'd'>,
  betaMin = 0.2,
  betaMax = 0.75,
): { d: number; beta: number; result: ReturnType<typeof calcOrifice> } {
  let lo = betaMin
  let hi = betaMax
  let mid = 0.5
  let last = calcOrifice({ ...base, d: mid * base.D })

  for (let i = 0; i < 50; i++) {
    mid = (lo + hi) / 2
    last = calcOrifice({ ...base, d: mid * base.D })
    if (last.massFlow < targetQm) lo = mid
    else hi = mid
  }

  return { d: mid * base.D, beta: mid, result: last }
}

/** 已知流量与几何 → 反算差压 */
export function sizeOrificeDp(
  targetQm: number,
  base: Omit<OrificeInput, 'deltaP'>,
): { deltaP: number; result: ReturnType<typeof calcOrifice> } {
  let lo = 10
  let hi = 2e6
  let mid = 25e3
  let last = calcOrifice({ ...base, deltaP: mid })

  for (let i = 0; i < 60; i++) {
    mid = Math.sqrt(lo * hi)
    last = calcOrifice({ ...base, deltaP: mid })
    if (last.massFlow < targetQm) lo = mid
    else hi = mid
  }

  return { deltaP: mid, result: last }
}
