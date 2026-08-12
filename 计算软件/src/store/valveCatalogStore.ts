/**
 * 调节阀厂家目录（本地可编辑）
 * 种子来自 valveVendors；用户按图纸录入的系数持久化到 localStorage。
 */

import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { getValveType } from '@/calc/valveTypes'
import {
  VALVE_VENDOR_SEEDS,
  VENDOR_GENERIC,
  vendorAlgorithm,
  type ValveModelSeed,
  type ValveVendorSeed,
} from '@/calc/valveVendors'
import type { ValveAlgorithmId } from '@/calc/engines/valveSizingCore'
import { downloadTextFile } from '@/export/report'

export interface ValveCatalogModel {
  id: string
  name: string
  valveTypeId?: string
  FL?: number
  xT?: number
  Fp?: number
  Fd?: number
  ratedCv?: number
  note?: string
  fromDrawing?: boolean
}

export interface ValveCatalogVendor {
  id: string
  name: string
  nameEn: string
  sheetBrand: string
  /** 该厂家选用的选型算法（可覆盖默认） */
  algorithm: ValveAlgorithmId
  models: ValveCatalogModel[]
}

function seedToCatalog(): ValveCatalogVendor[] {
  return VALVE_VENDOR_SEEDS.map((v) => ({
    id: v.id,
    name: v.name,
    nameEn: v.nameEn,
    sheetBrand: v.sheetBrand,
    algorithm: v.algorithm,
    models: v.models.map((m) => ({ ...m })),
  }))
}

function resolveCoeffs(model: ValveCatalogModel): {
  FL: number
  xT: number
  Fp: number
  Fd: number
  ratedCv?: number
} {
  const vt = getValveType(model.valveTypeId ?? 'single_seat_ftc')
  return {
    FL: model.FL ?? vt.FL,
    xT: model.xT ?? vt.xT,
    Fp: model.Fp ?? 1,
    Fd: model.Fd ?? vt.Fd,
    ratedCv: model.ratedCv,
  }
}

interface ValveCatalogState {
  vendors: ValveCatalogVendor[]
  selectedVendorId: string
  selectedModelId: string
  setSelection: (vendorId: string, modelId?: string) => void
  setVendorAlgorithm: (vendorId: string, algorithm: ValveAlgorithmId) => void
  updateModel: (
    vendorId: string,
    modelId: string,
    patch: Partial<ValveCatalogModel>,
  ) => void
  addModel: (vendorId: string, model: Omit<ValveCatalogModel, 'id'> & { id?: string }) => void
  removeModel: (vendorId: string, modelId: string) => void
  addVendor: (vendor: Omit<ValveCatalogVendor, 'models'> & { models?: ValveCatalogModel[] }) => void
  resetToSeeds: () => void
  exportJson: () => void
  importJson: (raw: string) => { ok: boolean; error?: string }
  getVendor: (id?: string) => ValveCatalogVendor
  getModel: (vendorId?: string, modelId?: string) => ValveCatalogModel | undefined
  getResolvedCoeffs: (vendorId?: string, modelId?: string) => ReturnType<typeof resolveCoeffs>
}

function firstModelId(vendors: ValveCatalogVendor[], vendorId: string): string {
  const v = vendors.find((x) => x.id === vendorId) ?? vendors[0]!
  return v.models[0]?.id ?? ''
}

const initialVendors = seedToCatalog()

export const useValveCatalogStore = create<ValveCatalogState>()(
  persist(
    (set, get) => ({
      vendors: initialVendors,
      selectedVendorId: VENDOR_GENERIC,
      selectedModelId: firstModelId(initialVendors, VENDOR_GENERIC),

      setSelection: (vendorId, modelId) => {
        const { vendors } = get()
        const v = vendors.find((x) => x.id === vendorId) ?? vendors[0]!
        const mid = modelId && v.models.some((m) => m.id === modelId)
          ? modelId
          : v.models[0]?.id ?? ''
        set({ selectedVendorId: v.id, selectedModelId: mid })
      },

      setVendorAlgorithm: (vendorId, algorithm) => {
        set((state) => ({
          vendors: state.vendors.map((v) =>
            v.id === vendorId ? { ...v, algorithm } : v,
          ),
        }))
      },

      updateModel: (vendorId, modelId, patch) => {
        set((state) => ({
          vendors: state.vendors.map((v) =>
            v.id !== vendorId
              ? v
              : {
                  ...v,
                  models: v.models.map((m) =>
                    m.id !== modelId
                      ? m
                      : { ...m, ...patch, fromDrawing: patch.fromDrawing ?? true },
                  ),
                },
          ),
        }))
      },

      addModel: (vendorId, model) => {
        const id =
          model.id?.trim() ||
          `${vendorId}_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 6)}`
        set((state) => ({
          vendors: state.vendors.map((v) =>
            v.id !== vendorId
              ? v
              : {
                  ...v,
                  models: [...v.models, { ...model, id, fromDrawing: true }],
                },
          ),
          selectedVendorId: vendorId,
          selectedModelId: id,
        }))
      },

      removeModel: (vendorId, modelId) => {
        set((state) => {
          const vendors = state.vendors.map((v) =>
            v.id !== vendorId
              ? v
              : { ...v, models: v.models.filter((m) => m.id !== modelId) },
          )
          let selectedModelId = state.selectedModelId
          if (state.selectedVendorId === vendorId && state.selectedModelId === modelId) {
            selectedModelId = firstModelId(vendors, vendorId)
          }
          return { vendors, selectedModelId }
        })
      },

      addVendor: (vendor) => {
        const id =
          vendor.id?.trim() ||
          `vendor_${Date.now().toString(36)}`
        const entry: ValveCatalogVendor = {
          id,
          name: vendor.name,
          nameEn: vendor.nameEn,
          sheetBrand: vendor.sheetBrand || vendor.name,
          algorithm: vendor.algorithm ?? vendorAlgorithm(id),
          models: vendor.models?.length
            ? vendor.models
            : [
                {
                  id: `${id}_model1`,
                  name: '型号 1（请改名并填图纸系数）',
                  valveTypeId: 'single_seat_ftc',
                  fromDrawing: false,
                },
              ],
        }
        set((state) => ({
          vendors: [...state.vendors, entry],
          selectedVendorId: id,
          selectedModelId: entry.models[0]!.id,
        }))
      },

      resetToSeeds: () => {
        const vendors = seedToCatalog()
        set({
          vendors,
          selectedVendorId: VENDOR_GENERIC,
          selectedModelId: firstModelId(vendors, VENDOR_GENERIC),
        })
      },

      exportJson: () => {
        const { vendors } = get()
        const payload = {
          version: 1,
          exportedAt: new Date().toISOString(),
          source: 'flowsize-valve-catalog',
          note: '系数由用户按厂家样本/图纸录入，非厂商数据库拷贝',
          vendors,
        }
        downloadTextFile(
          `FlowSize_阀厂家目录_${new Date().toISOString().slice(0, 10)}.json`,
          JSON.stringify(payload, null, 2),
          'application/json;charset=utf-8',
        )
      },

      importJson: (raw) => {
        try {
          const data = JSON.parse(raw) as {
            vendors?: ValveCatalogVendor[]
          }
          if (!Array.isArray(data.vendors) || data.vendors.length === 0) {
            return { ok: false, error: 'JSON 中缺少 vendors 数组' }
          }
          for (const v of data.vendors) {
            if (!v.id || !v.name || !Array.isArray(v.models)) {
              return { ok: false, error: '厂家条目格式无效' }
            }
          }
          const vendors = data.vendors.map((v) => ({
            ...v,
            sheetBrand: v.sheetBrand || v.name,
            algorithm: (v as ValveCatalogVendor).algorithm ?? vendorAlgorithm(v.id),
            models: v.models.map((m) => ({ ...m })),
          }))
          set({
            vendors,
            selectedVendorId: vendors[0]!.id,
            selectedModelId: firstModelId(vendors, vendors[0]!.id),
          })
          return { ok: true }
        } catch (e) {
          return { ok: false, error: e instanceof Error ? e.message : '解析失败' }
        }
      },

      getVendor: (id) => {
        const { vendors, selectedVendorId } = get()
        const vid = id ?? selectedVendorId
        return vendors.find((v) => v.id === vid) ?? vendors[0]!
      },

      getModel: (vendorId, modelId) => {
        const v = get().getVendor(vendorId)
        const mid = modelId ?? get().selectedModelId
        return v.models.find((m) => m.id === mid) ?? v.models[0]
      },

      getResolvedCoeffs: (vendorId, modelId) => {
        const m = get().getModel(vendorId, modelId)
        return resolveCoeffs(
          m ?? { id: '_', name: '_', valveTypeId: 'single_seat_ftc' },
        )
      },
    }),
    {
      name: 'flowsize-valve-catalog-v1',
      partialize: (s) => ({
        vendors: s.vendors,
        selectedVendorId: s.selectedVendorId,
        selectedModelId: s.selectedModelId,
      }),
      merge: (persisted, current) => {
        const p = (persisted ?? {}) as Partial<
          Pick<ValveCatalogState, 'vendors' | 'selectedVendorId' | 'selectedModelId'>
        >
        const vendorsRaw =
          Array.isArray(p.vendors) && p.vendors.length > 0 ? p.vendors : current.vendors
        const vendors = vendorsRaw.map((v) => ({
          ...v,
          algorithm: v.algorithm ?? vendorAlgorithm(v.id),
        }))
        const selectedVendorId =
          p.selectedVendorId && vendors.some((x) => x.id === p.selectedVendorId)
            ? p.selectedVendorId
            : vendors[0]!.id
        const vv = vendors.find((x) => x.id === selectedVendorId) ?? vendors[0]!
        const selectedModelId =
          p.selectedModelId && vv.models.some((m) => m.id === p.selectedModelId)
            ? p.selectedModelId
            : vv.models[0]?.id ?? ''
        return {
          ...current,
          vendors,
          selectedVendorId,
          selectedModelId,
        }
      },
    },
  ),
)

/** 从种子型号补全显示用系数说明 */
export function modelCoeffSource(model: ValveCatalogModel): string {
  if (model.fromDrawing || model.FL != null || model.xT != null) {
    return '用户按图纸/样本录入'
  }
  return '阀型典型值（待按图纸填写）'
}

export type { ValveVendorSeed, ValveModelSeed }
