/** ISO 5167-3 喷嘴 / 文丘里喷嘴（PRESO SSM） */

import { iterateMassFlow, type DpCommonResult } from './dpCommon'

export type NozzleType = 'isa1932' | 'long_radius' | 'venturi_nozzle'

export interface NozzleInput {
  D: number
  d: number
  deltaP: number
  density: number
  viscosity: number
  nozzleType: NozzleType
  isCompressible?: boolean
  p1?: number
  kappa?: number
}

export function nozzleC(type: NozzleType, ReD: number, beta: number): number {
  if (type === 'long_radius') {
    return 0.9965 - 0.00653 * beta ** 0.5 * (1e6 / ReD) ** 0.5
  }
  if (type === 'venturi_nozzle') {
    // PRESO SSM 类
    return 0.9858 - 0.196 * beta ** 4.5
  }
  // ISA 1932
  return 0.99 - 0.2262 * beta ** 4.1 - (0.00175 * beta - 0.0033 * beta ** 4.15) * (1e6 / ReD) ** 1.15
}

export function calcNozzle(input: NozzleInput): DpCommonResult & {
  nozzleType: NozzleType
  standard: string
  productHint: string
} {
  const result = iterateMassFlow(
    input,
    (Re, beta) => nozzleC(input.nozzleType, Re, beta),
    'nozzle',
  )
  return {
    ...result,
    nozzleType: input.nozzleType,
    standard: 'ISO 5167-3:2022',
    productHint:
      input.nozzleType === 'venturi_nozzle'
        ? '对应 PRESO SSM 文丘里喷嘴'
        : '标准喷嘴几何',
  }
}
