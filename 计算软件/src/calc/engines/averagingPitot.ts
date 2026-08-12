/**
 * 均速管 / 椭圆巴（PRESO Ellipse®）
 * 以厂商标定 K / Cd 为主，ASME MFC-12M 参考
 */

import type { DpCommonResult } from './dpCommon'

export interface AveragingPitotInput {
  D: number
  deltaP: number
  density: number
  viscosity: number
  /** 流量系数 K（厂家），典型 0.6–0.8 */
  K?: number
  probeBlockage?: number
}

export function calcAveragingPitot(input: AveragingPitotInput): DpCommonResult & {
  K: number
  standard: string
  productHint: string
} {
  const K = input.K ?? 0.7
  const { D, deltaP, density, viscosity } = input
  if (deltaP <= 0 || D <= 0) throw new Error('管径与差压必须为正')

  const area = Math.PI * (D / 2) ** 2
  // qm = K * A * sqrt(2 ρ ΔP)
  const massFlow = K * area * Math.sqrt(2 * density * deltaP)
  const volFlow = massFlow / density
  const velocity = volFlow / area
  const reynolds = (density * velocity * D) / viscosity
  const warnings: string[] = []
  if (!input.K) warnings.push('未输入厂家 K 系数，采用默认 0.70，交付前请替换为标定值。')
  if (input.probeBlockage && input.probeBlockage > 0.05) {
    warnings.push('插入件堵塞比较大，建议做堵塞修正。')
  }

  return {
    beta: 0,
    C: K,
    epsilon: 1,
    massFlow,
    volFlow,
    reynolds,
    velocity,
    permanentPressureLossPa: deltaP * 0.05,
    warnings,
    K,
    standard: 'ASME MFC-12M + 厂商标定 K',
    productHint: '对应 PRESO Ellipse® 环形/椭圆均速管，量程比可达约 17:1',
  }
}
