/**
 * 限流孔板（Restriction Orifice）— 单级/多级
 * 目标：给定流量与允许压降，估算孔径；气体阻塞流判据 P2/P1 ≈ 0.55
 */

export interface RestrictionStage {
  p1: number
  p2: number
  d: number
  beta: number
  choked: boolean
}

export interface RestrictionOrificeInput {
  D: number
  massFlow: number
  density: number
  p1: number
  p2: number
  phase: 'liquid' | 'gas'
  stages?: number
  Cd?: number
  kappa?: number
}

export interface RestrictionOrificeResult {
  stages: RestrictionStage[]
  totalDeltaP: number
  recommendedStages: number
  warnings: string[]
  standard: string
}

function singleHoleDiameter(
  qm: number,
  density: number,
  deltaP: number,
  Cd: number,
): number {
  // qm = Cd * A * sqrt(2 ρ Δp)
  const A = qm / (Cd * Math.sqrt(2 * density * deltaP))
  return Math.sqrt((4 * A) / Math.PI)
}

export function calcRestrictionOrifice(input: RestrictionOrificeInput): RestrictionOrificeResult {
  const Cd = input.Cd ?? 0.63
  const warnings: string[] = []
  const totalDeltaP = input.p1 - input.p2
  if (totalDeltaP <= 0) throw new Error('压降必须为正')

  let recommendedStages = input.stages ?? 1
  if (input.phase === 'gas') {
    const ratio = input.p2 / input.p1
    if (ratio < 0.55) {
      // 每级保持 p_out/p_in >= 0.55
      let p = input.p1
      let n = 0
      while (p * 0.55 > input.p2 && n < 10) {
        p *= 0.55
        n++
      }
      recommendedStages = Math.max(n + 1, input.stages ?? n + 1)
      warnings.push(
        `气体压比 P2/P1=${ratio.toFixed(3)} < 0.55，建议多级限流以避免单级阻塞（推荐 ${recommendedStages} 级）。`,
      )
    }
  } else if (totalDeltaP > 2.5e6) {
    recommendedStages = Math.max(2, Math.ceil(totalDeltaP / 2.5e6))
    warnings.push(`液体压降较大（>${2.5} MPa），建议多级以降低冲蚀与噪声。`)
  }

  const n = input.stages ?? recommendedStages
  const stages: RestrictionStage[] = []
  let pUp = input.p1

  for (let i = 0; i < n; i++) {
    const pDown =
      i === n - 1
        ? input.p2
        : input.p1 * Math.pow(input.p2 / input.p1, (i + 1) / n)
    const dp = pUp - pDown
    const d = singleHoleDiameter(input.massFlow, input.density, Math.max(dp, 1), Cd)
    const beta = d / input.D
    const choked = input.phase === 'gas' && pDown / pUp < 0.55
    if (choked) warnings.push(`第 ${i + 1} 级可能阻塞流。`)
    stages.push({ p1: pUp, p2: pDown, d, beta, choked })
    pUp = pDown
  }

  return {
    stages,
    totalDeltaP,
    recommendedStages,
    warnings,
    standard: '工程经验式 / ISA 限流孔板实践（阻塞流判据）',
  }
}
