/**
 * 调节阀阀型典型系数（IEC 60534-2-1 表级量级）
 * 实际选型应以厂家样本为准；此处供初选与可比计算。
 */

export interface ValveTypePreset {
  id: string
  name: string
  nameEn: string
  /** 液体压力恢复系数 FL */
  FL: number
  /** 气体压差比系数 xT */
  xT: number
  /** 阀型修正因子 Fd（噪声等，IEC 60534-8-3） */
  Fd: number
  note?: string
}

/** 自定义：不覆盖用户已填系数 */
export const VALVE_TYPE_CUSTOM = 'custom'

export const VALVE_TYPES: ValveTypePreset[] = [
  {
    id: 'single_seat_ftc',
    name: '单座球阀 · 流关 (FTC)',
    nameEn: 'Single-seat globe, flow-to-close',
    FL: 0.9,
    xT: 0.7,
    Fd: 0.46,
    note: '等百分比轮廓阀芯，流关；最常见单座默认',
  },
  {
    id: 'single_seat_fto',
    name: '单座球阀 · 流开 (FTO)',
    nameEn: 'Single-seat globe, flow-to-open',
    FL: 0.9,
    xT: 0.72,
    Fd: 0.46,
    note: '等百分比轮廓阀芯，流开',
  },
  {
    id: 'double_seat',
    name: '双座球阀',
    nameEn: 'Double-seated globe',
    FL: 0.85,
    xT: 0.7,
    Fd: 0.46,
    note: '不平衡力小，泄漏等级通常低于单座',
  },
  {
    id: 'cage_guided',
    name: '套筒导向球阀',
    nameEn: 'Cage-guided globe',
    FL: 0.9,
    xT: 0.75,
    Fd: 0.28,
    note: '多孔套筒；噪声与气蚀性能优于光杆单座',
  },
  {
    id: 'cage_multistage',
    name: '多级降压 / 抗气蚀套筒',
    nameEn: 'Multi-stage / anti-cavitation cage',
    FL: 0.95,
    xT: 0.85,
    Fd: 0.15,
    note: '高压差、抗气蚀；xT 偏高，初选偏保守',
  },
  {
    id: 'eccentric_plug',
    name: '偏心旋塞阀',
    nameEn: 'Eccentric rotary plug',
    FL: 0.85,
    xT: 0.6,
    Fd: 0.42,
  },
  {
    id: 'butterfly_offset',
    name: '偏心蝶阀',
    nameEn: 'Offset-seat butterfly',
    FL: 0.68,
    xT: 0.38,
    Fd: 0.57,
    note: '高恢复阀，气蚀/阻塞更敏感',
  },
  {
    id: 'butterfly_swing',
    name: '中线蝶阀',
    nameEn: 'Swing-through butterfly',
    FL: 0.55,
    xT: 0.25,
    Fd: 0.7,
    note: '高恢复；FL/xT 偏低',
  },
  {
    id: 'ball_segmented',
    name: 'V 型球阀 / 分段球阀',
    nameEn: 'Segmented / V-notch ball',
    FL: 0.6,
    xT: 0.3,
    Fd: 0.98,
  },
  {
    id: 'ball_fullbore',
    name: '全通径球阀',
    nameEn: 'Full-bore ball',
    FL: 0.55,
    xT: 0.15,
    Fd: 1.0,
    note: '极高压力恢复；阻塞流与气蚀风险大',
  },
  {
    id: VALVE_TYPE_CUSTOM,
    name: '自定义（手动填系数）',
    nameEn: 'Custom coefficients',
    FL: 0.9,
    xT: 0.75,
    Fd: 0.46,
    note: '不自动改写 FL / xT / Fd',
  },
]

export function getValveType(id: string): ValveTypePreset {
  return VALVE_TYPES.find((t) => t.id === id) ?? VALVE_TYPES[0]!
}
