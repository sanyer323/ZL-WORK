/**
 * 调整型 / 平衡孔板（Toolkit / A+K 类）
 * 多孔整流结构：短直管段、厂商标定 Cd 为主，ISO 5167-1 通用质量流量式
 */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export interface ConditioningOrificeInput {
  D: number
  /** 等效节流直径（或按开孔总面积换算）m */
  d: number
  deltaP: number
  density: number
  viscosity: number
  /** 厂商标定流出系数，缺省用经验关联 */
  Cd?: number
  holeCount?: number
  isCompressible?: boolean
  p1?: number
  kappa?: number
}

/** 调整型孔板经验 Cd（无标定数据时） */
export function conditioningCd(ReD: number, beta: number): number {
  // 多孔整流后 Cd 通常高于单孔锐边，且对 Re 更平坦
  const base = 0.72 + 0.04 * (1 - beta)
  const reCorr = 1 - 1200 / Math.max(ReD, 2000)
  return Math.min(0.85, Math.max(0.65, base * reCorr))
}

export function calcConditioningOrifice(
  input: ConditioningOrificeInput,
): DpCommonResult & {
  holeCount: number
  standard: string
  straightRunHint: string
} {
  const holeCount = input.holeCount ?? 4
  const result = iterateMassFlow(
    { ...input, C: input.Cd },
    (Re, beta) => conditioningCd(Re, beta),
    'conditioning',
  )

  const warnings = [...result.warnings]
  if (holeCount < 2) warnings.push('调整型孔板通常为多孔结构，请确认开孔数。')
  if (!input.Cd) warnings.push('未提供厂商标定 Cd，当前为经验关联，产品交付应以标定值为准。')

  return {
    ...result,
    warnings,
    holeCount,
    standard: 'ISO 5167-1 通用式 + 厂商标定 Cd（调整型/平衡孔板）',
    straightRunHint: '典型直管段要求约前 3D / 后 1D（视上游扰动，以厂家样本为准）',
  }
}
