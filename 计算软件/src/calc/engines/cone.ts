/** ISO 5167-5 V 锥流量计（PRESO Cone） */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export interface ConeInput {
  D: number
  /** 等效喉部直径 d = D * sqrt(1 - β²) 关系由 β 定义；此处直接给锥直径 dc */
  d: number
  deltaP: number
  density: number
  viscosity: number
  Cd?: number
  isCompressible?: boolean
  p1?: number
  kappa?: number
}

/**
 * V 锥 β 定义：β = sqrt(1 - (dc/D)²)
 * 输入 d 视为喉部等效流通直径，便于与通用式统一
 */
export function coneCd(ReD: number, beta: number): number {
  return 0.82 + 0.05 * beta - 1500 / Math.max(ReD, 5000)
}

export function calcCone(input: ConeInput): DpCommonResult & {
  standard: string
  productHint: string
} {
  const result = iterateMassFlow(
    { ...input, C: input.Cd },
    (Re, beta) => coneCd(Re, beta),
    'cone',
  )
  return {
    ...result,
    standard: 'ISO 5167-5:2022',
    productHint: '对应 PRESO Cone；典型 β 0.40–0.80，短直管段',
  }
}
