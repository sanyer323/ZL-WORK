/** ISO 5167-4 文丘里管（粗加工收敛段经典式） */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export type VenturiProfile = 'as_cast' | 'machined' | 'rough_welded' | 'low_loss'

export interface VenturiInput {
  D: number
  d: number
  deltaP: number
  density: number
  viscosity: number
  profile: VenturiProfile
  isCompressible?: boolean
  p1?: number
  kappa?: number
}

export function venturiC(profile: VenturiProfile, beta: number): number {
  // ISO 5167-4 典型常数（简化；精确值随 Re、粗糙度分段）
  switch (profile) {
    case 'as_cast':
      return 0.984
    case 'machined':
      return 0.995
    case 'rough_welded':
      return 0.985
    case 'low_loss':
      // PRESO LPL / CV 类低损文丘里：高回收，Cd 接近 1，永久压损更低
      return 0.99 - 0.01 * beta ** 2
  }
}

export function calcVenturi(input: VenturiInput): DpCommonResult & {
  profile: VenturiProfile
  standard: string
  productHint: string
} {
  const result = iterateMassFlow(
    input,
    (_Re, beta) => venturiC(input.profile, beta),
    'venturi',
  )

  const productHint =
    input.profile === 'low_loss'
      ? '对应 PRESO LPL / CV 低损文丘里系列'
      : input.profile === 'machined'
        ? '对应 PRESO SSL 精加工经典文丘里'
        : 'ISO 经典文丘里几何'

  return {
    ...result,
    profile: input.profile,
    standard: 'ISO 5167-4:2022',
    productHint,
  }
}
