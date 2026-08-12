/** 计算模块注册表 — 产品化可插拔架构，桌面端可复用同一引擎 */

export type ModuleCategory =
  | 'control_valve'
  | 'dp_meter'
  | 'restriction'
  | 'utility'

export interface CalcModuleMeta {
  id: string
  name: string
  nameEn: string
  category: ModuleCategory
  /** 主要依据标准 */
  standards: string[]
  /** 对应参考产品族（如 PRESO / 标准孔板 / 调整型） */
  productFamily: string
  description: string
  status: 'ready' | 'beta' | 'planned'
}

export const MODULES: CalcModuleMeta[] = [
  {
    id: 'control-valve',
    name: '调节阀选型',
    nameEn: 'Control Valve Sizing',
    category: 'control_valve',
    standards: ['IEC 60534-2-1', 'IEC 60534-8-3', 'ISA-75.01'],
    productFamily: '通用（制造商中立）',
    description: '液体/气体/蒸汽 Cv·Kv、气蚀闪蒸判据、噪声估算',
    status: 'ready',
  },
  {
    id: 'orifice',
    name: '标准孔板',
    nameEn: 'Orifice Plate',
    category: 'dp_meter',
    standards: ['ISO 5167-2:2022', 'GB/T 2624.2', 'ASME MFC-3M'],
    productFamily: '标准节流件',
    description: '同心锐边孔板；角接/法兰/D-D/2 取压',
    status: 'ready',
  },
  {
    id: 'conditioning-orifice',
    name: '调整型孔板',
    nameEn: 'Conditioning Orifice',
    category: 'dp_meter',
    standards: ['ISO 5167-1 通用式', '厂商标定 Cd（Toolkit/A+K 类）'],
    productFamily: 'Toolkit 调整型 / 平衡孔板',
    description: '多孔整流孔板，短直管段；支持标定 Cd 与 β 选型',
    status: 'ready',
  },
  {
    id: 'venturi',
    name: '文丘里管',
    nameEn: 'Venturi Tube',
    category: 'dp_meter',
    standards: ['ISO 5167-4:2022'],
    productFamily: 'PRESO Venturi (SSL / LPL / CV)',
    description: '经典/低损文丘里；低压损计量',
    status: 'ready',
  },
  {
    id: 'venturi-nozzle',
    name: '文丘里喷嘴',
    nameEn: 'Venturi Nozzle',
    category: 'dp_meter',
    standards: ['ISO 5167-3:2022'],
    productFamily: 'PRESO SSM',
    description: 'ISA 1932 / 长径喷嘴与文丘里喷嘴',
    status: 'ready',
  },
  {
    id: 'wedge',
    name: '楔形流量计',
    nameEn: 'Wedge Meter',
    category: 'dp_meter',
    standards: ['ISO 5167-6:2022'],
    productFamily: 'PRESO COIN® Wedge',
    description: '脏污、高粘度、浆料工况差压计量',
    status: 'ready',
  },
  {
    id: 'cone',
    name: 'V 锥流量计',
    nameEn: 'Cone Meter',
    category: 'dp_meter',
    standards: ['ISO 5167-5:2022'],
    productFamily: 'PRESO Cone',
    description: '短直管段、宽量程比锥形节流件',
    status: 'ready',
  },
  {
    id: 'averaging-pitot',
    name: '均速管 / 椭圆巴',
    nameEn: 'Averaging Pitot',
    category: 'dp_meter',
    standards: ['ASME MFC-12M', '厂商标定'],
    productFamily: 'PRESO Ellipse®',
    description: '多点均速取压，极低压损插入式元件',
    status: 'ready',
  },
  {
    id: 'restriction-orifice',
    name: '限流孔板',
    nameEn: 'Restriction Orifice',
    category: 'restriction',
    standards: ['ISA RP 75', 'IEC 60534-8-3（噪声）', '工程经验式'],
    productFamily: '单级/多级/多孔 RO',
    description: '降压限流；阻塞流判据；多级压降分配',
    status: 'beta',
  },
]

export function getModule(id: string): CalcModuleMeta | undefined {
  return MODULES.find((m) => m.id === id)
}

export const CATEGORY_LABEL: Record<ModuleCategory, string> = {
  control_valve: '调节阀',
  dp_meter: '差压节流计量',
  restriction: '限流 / 降压',
  utility: '公用工具',
}
