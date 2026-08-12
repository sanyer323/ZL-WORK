/**
 * ISO 5167 尺寸温度修正
 * D_t = D_20 * [1 + α_pipe * (t - t_ref)]
 * d_t = d_20 * [1 + α_plate * (t - t_ref)]
 */

export function expandDiameter(
  Dref_m: number,
  alpha: number,
  tOp_C: number,
  tRef_C = 20,
): number {
  return Dref_m * (1 + alpha * (tOp_C - tRef_C))
}

export interface ExpandedGeometry {
  Dref: number
  dref: number
  Dop: number
  dop: number
  betaRef: number
  betaOp: number
  alphaPipe: number
  alphaPlate: number
  tOp: number
  tRef: number
}

export function expandGeometry(input: {
  Dref_mm: number
  dref_mm: number
  alphaPipe: number
  alphaPlate: number
  tOp_C: number
  tRef_C?: number
}): ExpandedGeometry {
  const tRef = input.tRef_C ?? 20
  const Dref = input.Dref_mm / 1000
  const dref = input.dref_mm / 1000
  const Dop = expandDiameter(Dref, input.alphaPipe, input.tOp_C, tRef)
  const dop = expandDiameter(dref, input.alphaPlate, input.tOp_C, tRef)
  return {
    Dref,
    dref,
    Dop,
    dop,
    betaRef: dref / Dref,
    betaOp: dop / Dop,
    alphaPipe: input.alphaPipe,
    alphaPlate: input.alphaPlate,
    tOp: input.tOp_C,
    tRef,
  }
}

/** 可选数字：空字符串视为未覆盖 */
export function parseOptionalNumber(raw: string): number | undefined {
  const t = raw.trim()
  if (t === '') return undefined
  const n = Number(t)
  return Number.isFinite(n) ? n : undefined
}
