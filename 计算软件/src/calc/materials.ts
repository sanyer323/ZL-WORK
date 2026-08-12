/**
 * 管道 / 节流件常用材料 — 线膨胀系数（自建工程参考值）
 * α：平均线膨胀系数 1/K（相对 20°C 常用值）
 */

export interface MaterialProps {
  id: string
  name: string
  nameEn: string
  /** 平均线膨胀系数 1/K */
  alpha: number
  group: 'carbon_steel' | 'stainless' | 'alloy' | 'nonferrous' | 'plastic' | 'other'
  note?: string
}

export const MATERIALS: MaterialProps[] = [
  {
    id: 'cs_a106',
    name: '碳钢 (A106 / 20# 类)',
    nameEn: 'Carbon steel',
    alpha: 11.7e-6,
    group: 'carbon_steel',
  },
  {
    id: 'cs_a105',
    name: '碳钢锻件 (A105)',
    nameEn: 'CS A105',
    alpha: 11.5e-6,
    group: 'carbon_steel',
  },
  {
    id: 'ltcs',
    name: '低温碳钢 (A333 Gr.6)',
    nameEn: 'LTCS',
    alpha: 11.2e-6,
    group: 'carbon_steel',
  },
  {
    id: 'ss304',
    name: '不锈钢 304 / 304L',
    nameEn: 'SS304/304L',
    alpha: 17.3e-6,
    group: 'stainless',
  },
  {
    id: 'ss316',
    name: '不锈钢 316 / 316L',
    nameEn: 'SS316/316L',
    alpha: 16.0e-6,
    group: 'stainless',
  },
  {
    id: 'ss321',
    name: '不锈钢 321',
    nameEn: 'SS321',
    alpha: 16.6e-6,
    group: 'stainless',
  },
  {
    id: 'ss310',
    name: '不锈钢 310',
    nameEn: 'SS310',
    alpha: 15.9e-6,
    group: 'stainless',
  },
  {
    id: 'duplex_2205',
    name: '双相钢 2205',
    nameEn: 'Duplex 2205',
    alpha: 13.0e-6,
    group: 'stainless',
  },
  {
    id: 'super_duplex',
    name: '超级双相钢 2507',
    nameEn: 'Super duplex 2507',
    alpha: 13.5e-6,
    group: 'stainless',
  },
  {
    id: 'alloy_400',
    name: '蒙乃尔 400',
    nameEn: 'Monel 400',
    alpha: 13.9e-6,
    group: 'alloy',
  },
  {
    id: 'inconel_625',
    name: 'Inconel 625',
    nameEn: 'Inconel 625',
    alpha: 12.8e-6,
    group: 'alloy',
  },
  {
    id: 'hastelloy_c276',
    name: 'Hastelloy C-276',
    nameEn: 'Hastelloy C-276',
    alpha: 11.2e-6,
    group: 'alloy',
  },
  {
    id: 'titanium_gr2',
    name: '钛 Gr.2',
    nameEn: 'Titanium Gr.2',
    alpha: 8.6e-6,
    group: 'nonferrous',
  },
  {
    id: 'copper',
    name: '铜',
    nameEn: 'Copper',
    alpha: 16.5e-6,
    group: 'nonferrous',
  },
  {
    id: 'brass',
    name: '黄铜',
    nameEn: 'Brass',
    alpha: 18.7e-6,
    group: 'nonferrous',
  },
  {
    id: 'aluminum',
    name: '铝合金',
    nameEn: 'Aluminum',
    alpha: 23.0e-6,
    group: 'nonferrous',
  },
  {
    id: 'pvc',
    name: 'PVC',
    nameEn: 'PVC',
    alpha: 50e-6,
    group: 'plastic',
    note: '塑料管热膨胀大，温差大时务必复核',
  },
  {
    id: 'ptfe',
    name: 'PTFE / 内衬参考',
    nameEn: 'PTFE',
    alpha: 100e-6,
    group: 'plastic',
  },
  {
    id: 'custom',
    name: '自定义 α',
    nameEn: 'Custom alpha',
    alpha: 12e-6,
    group: 'other',
    note: '在下方输入自定义线膨胀系数',
  },
]

export const MATERIAL_GROUP_LABEL: Record<MaterialProps['group'], string> = {
  carbon_steel: '碳钢',
  stainless: '不锈钢',
  alloy: '镍基 / 特种合金',
  nonferrous: '有色金属',
  plastic: '塑料',
  other: '其他',
}

export function getMaterial(id: string): MaterialProps {
  const m = MATERIALS.find((x) => x.id === id)
  if (!m) throw new Error(`未知材料: ${id}`)
  return m
}

export function materialsByGroup() {
  const order: MaterialProps['group'][] = [
    'carbon_steel',
    'stainless',
    'alloy',
    'nonferrous',
    'plastic',
    'other',
  ]
  return order.map((group) => ({
    group,
    label: MATERIAL_GROUP_LABEL[group],
    items: MATERIALS.filter((m) => m.group === group),
  }))
}
