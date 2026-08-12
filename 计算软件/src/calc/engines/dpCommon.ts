/** 差压节流件通用公式（ISO 5167-1） */

export interface DpCommonInput {
  /** 管内径 m */
  D: number
  /** 节流直径或等效直径 m */
  d: number
  /** 差压 Pa */
  deltaP: number
  /** 上游密度 kg/m³ */
  density: number
  /** 动力粘度 Pa·s */
  viscosity: number
  /** 流出系数（若已知则跳过迭代初始） */
  C?: number
  /** 可膨胀系数，液体=1 */
  epsilon?: number
  isCompressible?: boolean
  /** 上游绝对压力 Pa（气体 ε 估算） */
  p1?: number
  kappa?: number
}

export interface DpCommonResult {
  beta: number
  C: number
  epsilon: number
  /** kg/s */
  massFlow: number
  /** m³/s（工况体积） */
  volFlow: number
  reynolds: number
  velocity: number
  permanentPressureLossPa: number
  warnings: string[]
}

export function betaOf(d: number, D: number): number {
  return d / D
}

export function velocityOfThroat(qm: number, density: number, d: number): number {
  const area = Math.PI * (d / 2) ** 2
  return qm / (density * area)
}

/** ISO 5167 气体可膨胀系数近似（孔板法兰/角接类） */
export function orificeEpsilon(
  beta: number,
  deltaP: number,
  p1: number,
  kappa = 1.4,
): number {
  const x = deltaP / p1
  if (x <= 0 || x >= 1) return 1
  return 1 - (0.351 + 0.256 * beta ** 4 + 0.93 * beta ** 8) * (1 - (1 - x) ** (1 / kappa))
}

/** 永久压损近似（相对差压的比例系数）
 * 孔板：ISO/工程常用 Δϖ ≈ Δp·(1−β^1.9)，系数取 1
 * 其它一次元件按回收能力减小
 */
export function permanentLossFactor(kind: 'orifice' | 'venturi' | 'nozzle' | 'cone' | 'wedge' | 'pitot' | 'conditioning'): number {
  switch (kind) {
    case 'orifice':
      return 1.0
    case 'conditioning':
      return 0.65
    case 'nozzle':
      return 0.55
    case 'wedge':
      return 0.6
    case 'cone':
      return 0.45
    case 'venturi':
      return 0.15
    case 'pitot':
      return 0.05
  }
}

export function iterateMassFlow(
  input: DpCommonInput,
  resolveC: (Re: number, beta: number) => number,
  lossKind: Parameters<typeof permanentLossFactor>[0],
  maxIter = 40,
): DpCommonResult {
  const { D, d, deltaP, density, viscosity } = input
  const beta = betaOf(d, D)
  const warnings: string[] = []

  if (beta < 0.1 || beta > 0.9) warnings.push(`β=${beta.toFixed(3)} 超出常用范围，请核对几何。`)
  if (D <= 0 || d <= 0) throw new Error('管径/孔径必须为正')
  if (deltaP <= 0) throw new Error('差压必须为正')

  let epsilon = input.epsilon ?? 1
  if (input.epsilon == null && input.isCompressible && input.p1) {
    epsilon = orificeEpsilon(beta, deltaP, input.p1, input.kappa ?? 1.4)
  }

  const area = Math.PI * (d / 2) ** 2
  let C = input.C ?? 0.6
  let qm = 0
  let Re = 1e5

  for (let i = 0; i < maxIter; i++) {
    C = input.C ?? resolveC(Re, beta)
    const E = 1 / Math.sqrt(1 - beta ** 4)
    qm = C * epsilon * E * area * Math.sqrt(2 * density * deltaP)
    const vPipe = qm / (density * Math.PI * (D / 2) ** 2)
    Re = (density * vPipe * D) / viscosity
    if (!Number.isFinite(Re) || Re <= 0) {
      warnings.push('雷诺数计算异常，请检查粘度与密度。')
      break
    }
  }

  const volFlow = qm / density
  const velocity = velocityOfThroat(qm, density, d)
  const permanentPressureLossPa = deltaP * permanentLossFactor(lossKind) * (1 - beta ** 1.9)

  if (Re < 5000) warnings.push('雷诺数偏低，标准不确定度可能增大。')

  return {
    beta,
    C,
    epsilon,
    massFlow: qm,
    volFlow,
    reynolds: Re,
    velocity,
    permanentPressureLossPa,
    warnings,
  }
}
