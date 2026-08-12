/**
 * 调节阀厂家 / 系列骨架
 * 系数由用户按样本/图纸录入；算法按厂家默认分流（可改）。
 */

import type { ValveAlgorithmId } from '@/calc/engines/valveSizingCore'
import { defaultAlgorithmForVendor } from '@/calc/engines/valveSizingCore'

export interface ValveModelSeed {
  id: string
  name: string
  valveTypeId?: string
  FL?: number
  xT?: number
  Fp?: number
  Fd?: number
  ratedCv?: number
  note?: string
}

export interface ValveVendorSeed {
  id: string
  name: string
  nameEn: string
  sheetBrand: string
  /** 该厂家默认选型算法 */
  algorithm: ValveAlgorithmId
  models: ValveModelSeed[]
}

export const VENDOR_GENERIC = 'generic_iec'

/** 出厂种子目录：系列架子 + 厂家默认算法 */
export const VALVE_VENDOR_SEEDS: ValveVendorSeed[] = [
  {
    id: VENDOR_GENERIC,
    name: '通用 IEC',
    nameEn: 'Generic IEC 60534',
    sheetBrand: 'IEC 60534 Generic',
    algorithm: 'iec_60534',
    models: [
      {
        id: 'generic_single_seat',
        name: '单座球阀（通用）',
        valveTypeId: 'single_seat_ftc',
        note: '无厂家样本时用阀型典型系数',
      },
      {
        id: 'generic_cage',
        name: '套筒导向（通用）',
        valveTypeId: 'cage_guided',
      },
    ],
  },
  {
    id: 'fisher',
    name: 'Emerson Fisher',
    nameEn: 'Emerson Fisher',
    sheetBrand: 'Emerson Fisher',
    algorithm: 'isa_fisher',
    models: [
      {
        id: 'fisher_easy_e',
        name: 'easy-e / ET·ED 类单座',
        valveTypeId: 'single_seat_ftc',
        note: '请按 Fisher 样本填入 FL / xT；算法为 ISA/Fisher（Cv+Cg）',
      },
      {
        id: 'fisher_ew',
        name: 'EW 套筒类',
        valveTypeId: 'cage_guided',
        note: '请按 Fisher 样本填入 FL / xT',
      },
      {
        id: 'fisher_v150',
        name: 'Vee-Ball V150/V200/V300',
        valveTypeId: 'ball_segmented',
        note: '请按 Fisher 样本填入 FL / xT',
      },
    ],
  },
  {
    id: 'samson',
    name: 'Samson',
    nameEn: 'Samson',
    sheetBrand: 'Samson',
    algorithm: 'iec_60534',
    models: [
      {
        id: 'samson_3241',
        name: '3241 单座',
        valveTypeId: 'single_seat_ftc',
        note: '请按 Samson 样本填入 FL / xT；算法为 IEC 公制 Kv',
      },
      {
        id: 'samson_3251',
        name: '3251 高压单座',
        valveTypeId: 'single_seat_ftc',
      },
      {
        id: 'samson_3244',
        name: '3244 三通',
        valveTypeId: 'single_seat_fto',
      },
    ],
  },
  {
    id: 'masoneilan',
    name: 'Masoneilan',
    nameEn: 'Masoneilan / Baker Hughes',
    sheetBrand: 'Masoneilan',
    algorithm: 'isa_masoneilan',
    models: [
      {
        id: 'maso_21000',
        name: '21000 单座',
        valveTypeId: 'single_seat_ftc',
        note: '请按 Masoneilan 样本填入 FL / xT；算法为 ISA（Cv）',
      },
      {
        id: 'maso_41005',
        name: '41005 套筒',
        valveTypeId: 'cage_guided',
      },
      {
        id: 'maso_camflex',
        name: 'Camflex 旋塞',
        valveTypeId: 'eccentric_plug',
      },
    ],
  },
  {
    id: 'metso',
    name: 'Metso / Neles',
    nameEn: 'Metso / Neles / Valmet',
    sheetBrand: 'Neles',
    algorithm: 'iec_60534',
    models: [
      {
        id: 'neles_finetrol',
        name: 'Finetrol 偏心',
        valveTypeId: 'eccentric_plug',
      },
      {
        id: 'neles_neldisc',
        name: 'Neldisc 蝶阀',
        valveTypeId: 'butterfly_offset',
      },
      {
        id: 'neles_segment',
        name: 'Segment 球阀',
        valveTypeId: 'ball_segmented',
      },
    ],
  },
  {
    id: 'spirax',
    name: 'Spirax Sarco',
    nameEn: 'Spirax Sarco',
    sheetBrand: 'Spirax Sarco',
    algorithm: 'iec_60534',
    models: [
      {
        id: 'spirax_spira_trol',
        name: 'Spira-trol 单座',
        valveTypeId: 'single_seat_ftc',
      },
    ],
  },
  {
    id: 'wuzhong',
    name: '吴忠仪表',
    nameEn: 'Wuzhong Instrument',
    sheetBrand: '吴忠仪表',
    algorithm: 'gb_iec',
    models: [
      {
        id: 'wz_single_seat',
        name: '单座调节阀',
        valveTypeId: 'single_seat_ftc',
        note: '请按厂家图纸填入 FL / xT；算法为国内 GB/IEC（Kv）',
      },
      {
        id: 'wz_cage',
        name: '套筒调节阀',
        valveTypeId: 'cage_guided',
      },
    ],
  },
]

export function getVendorSeed(id: string): ValveVendorSeed {
  return VALVE_VENDOR_SEEDS.find((v) => v.id === id) ?? VALVE_VENDOR_SEEDS[0]!
}

export function vendorAlgorithm(vendorId: string): ValveAlgorithmId {
  const seed = VALVE_VENDOR_SEEDS.find((v) => v.id === vendorId)
  return seed?.algorithm ?? defaultAlgorithmForVendor(vendorId)
}
