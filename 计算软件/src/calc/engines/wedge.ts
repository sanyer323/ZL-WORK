/** ISO 5167-6 楔形流量计（PRESO COIN®） */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export interface WedgeInput {
  D: number
  /** 楔形喉部等效开度高度相关：用等效 d 或 H/D */
  d: number
  deltaP: number
  density: number
  viscosity: number
  /** 楔角 °，常见 60° */
  wedgeAngleDeg?: number
  Cd?: number
  isCompressible?: boolean
  p1?: number
  kappa?: number
}

export function wedgeCd(ReD: number, beta: number): number {
  // 楔形 Cd 对低 Re 更稳健（浆料/高粘）
  const base = 0.8 - 0.05 * beta
  return base * (1 - 80 / Math.max(ReD, 300))
}

export function calcWedge(input: WedgeInput): DpCommonResult & {
  wedgeAngleDeg: number
  standard: string
  productHint: string
} {
  const wedgeAngleDeg = input.wedgeAngleDeg ?? 60
  const result = iterateMassFlow(
    { ...input, C: input.Cd },
    (Re, beta) => wedgeCd(Re, beta),
    'wedge',
  )
  const warnings = [...result.warnings]
  if (result.reynolds < 500) {
    warnings.push('低雷诺数工况是楔形计优势区，建议用实流/厂家曲线复核。')
  }
  return {
    ...result,
    warnings,
    wedgeAngleDeg,
    standard: 'ISO 5167-6:2022',
    productHint: '对应 PRESO COIN® 楔形流量计（FF / NW / NN / NB）',
  }
}
