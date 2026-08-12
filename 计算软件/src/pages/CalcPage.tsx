import { useMemo, useState, useRef, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { getModule } from '@/calc/registry'
import { getFluid, gasDensity } from '@/calc/fluids'
import { getMaterial } from '@/calc/materials'
import { expandGeometry, parseOptionalNumber } from '@/calc/thermalExpansion'
import {
  formatEng,
  kgsToFlowMass,
  m3sToFlowVol,
  paToPressure,
  pressureToPa,
  pressureUnitLabel,
  absPaToDisplay,
  displayToAbsPa,
  lengthToM,
  mToLength,
  tempToC,
  cToTemp,
  flowMassToKgs,
  flowVolToM3s,
  densityToKgM3,
  kgM3ToDensity,
  viscosityToPas,
  pasToViscosity,
} from '@/calc/units'
import { Field, Metric } from '@/components/FormBits'
import { FluidPicker } from '@/components/FluidPicker'
import { MaterialSelect } from '@/components/MaterialSelect'
import { NumberInput } from '@/components/NumberInput'
import { UnitPrefsPanel } from '@/components/UnitPrefsPanel'
import { useAppStore } from '@/store/appStore'
import { useUnitStore } from '@/store/unitStore'
import {
  exportExcelCsv,
  exportExcelSheet,
  exportPdfSheet,
  type CalcSheet,
  type SheetCell,
  type SheetBlock,
} from '@/export/report'
import {
  calcOrifice,
  calcConditioningOrifice,
  calcVenturi,
  calcNozzle,
  calcWedge,
  calcCone,
  calcAveragingPitot,
  calcControlValve,
  calcRestrictionOrifice,
  sizeOrificeBore,
  sizeOrificeDp,
  VALVE_ALGORITHMS,
  type TapType,
  type VenturiProfile,
  type NozzleType,
  type OrificePlateType,
  type ValveAlgorithmId,
} from '@/calc/engines'
import {
  VALVE_TYPES,
  VALVE_TYPE_CUSTOM,
  getValveType,
} from '@/calc/valveTypes'
import {
  useValveCatalogStore,
  modelCoeffSource,
} from '@/store/valveCatalogStore'

type DpMode = 'flow_from_dp' | 'size_bore' | 'size_dp'

export function CalcPage() {
  const { moduleId = '' } = useParams()
  const meta = getModule(moduleId)
  const addProject = useAppStore((s) => s.addProject)
  const units = useUnitStore()

  // —— 工质 ——
  const [fluidId, setFluidId] = useState('water_20c')
  const [rhoOverride, setRhoOverride] = useState('')
  const [muOverride, setMuOverride] = useState('')
  const [kappaOverride, setKappaOverride] = useState('')
  const [pvOverride, setPvOverride] = useState('')
  const [pcOverride, setPcOverride] = useState('')

  // —— 工况（内部基准：°C / bar(a) / kPa / mm / kg/h / m³/h）——
  const [tOpC, setTOpC] = useState(20)
  const [tRefC, setTRefC] = useState(20)
  const [p1BarA, setP1BarA] = useState(6)
  const [p2BarA, setP2BarA] = useState(4)
  const [patmBar, setPatmBar] = useState(1.01325)
  const [dpKPa, setDpKPa] = useState(25)

  // —— 几何 / 材料 ——
  const [Dmm, setDmm] = useState(100)
  const [dmm, setDmmHole] = useState(50)
  const [pipeMatId, setPipeMatId] = useState('cs_a106')
  const [plateMatId, setPlateMatId] = useState('ss316')
  const [pipeAlphaCustom, setPipeAlphaCustom] = useState('1.17e-5')
  const [plateAlphaCustom, setPlateAlphaCustom] = useState('1.6e-5')
  const [applyThermal, setApplyThermal] = useState(true)

  // —— 孔板专用 ——
  const [tap, setTap] = useState<TapType>('flange')
  const [plateType, setPlateType] = useState<OrificePlateType>('concentric')
  const [plateThickMm, setPlateThickMm] = useState('3')
  const [edgeThickMm, setEdgeThickMm] = useState('0.5')
  const [drainHoleMm, setDrainHoleMm] = useState('')
  const [roughnessUm, setRoughnessUm] = useState('40')
  const [mode, setMode] = useState<DpMode>('flow_from_dp')
  const [betaMin, setBetaMin] = useState(0.2)
  const [betaMax, setBetaMax] = useState(0.75)

  // —— 其它节流 ——
  const [venturiProfile, setVenturiProfile] = useState<VenturiProfile>('low_loss')
  const [nozzleType, setNozzleType] = useState<NozzleType>('venturi_nozzle')
  const [holeCount, setHoleCount] = useState(4)
  const [wedgeAngle, setWedgeAngle] = useState(60)
  const [probeBlockage, setProbeBlockage] = useState('0.02')
  const [Cd, setCd] = useState('')
  const [epsOverride, setEpsOverride] = useState('')
  const [K, setK] = useState('0.70')

  // —— 流量 / 阀 / RO ——
  const [targetQmh, setTargetQmh] = useState(50)
  const [massKgH, setMassKgH] = useState(36000)
  const [flowInputMode, setFlowInputMode] = useState<'mass' | 'vol'>('vol')
  const [valveStyle, setValveStyle] = useState<'liquid' | 'gas' | 'steam'>('liquid')
  const [valveTypeId, setValveTypeId] = useState('single_seat_ftc')
  const [FL, setFL] = useState('0.90')
  const [Fp, setFp] = useState('1.0')
  const [xT, setXT] = useState('0.70')
  const [Fd, setFd] = useState('0.46')
  const [ratedCv, setRatedCv] = useState('')
  const [roStages, setRoStages] = useState(1)
  const [sheetTag, setSheetTag] = useState('FE-001')
  const [sheetProject, setSheetProject] = useState('')
  const catalogFileRef = useRef<HTMLInputElement>(null)

  const catalogVendors = useValveCatalogStore((s) => s.vendors)
  const selectedVendorId = useValveCatalogStore((s) => s.selectedVendorId)
  const selectedModelId = useValveCatalogStore((s) => s.selectedModelId)
  const setCatalogSelection = useValveCatalogStore((s) => s.setSelection)
  const setVendorAlgorithm = useValveCatalogStore((s) => s.setVendorAlgorithm)
  const updateCatalogModel = useValveCatalogStore((s) => s.updateModel)
  const addCatalogModel = useValveCatalogStore((s) => s.addModel)
  const exportCatalogJson = useValveCatalogStore((s) => s.exportJson)
  const importCatalogJson = useValveCatalogStore((s) => s.importJson)
  const resetCatalogSeeds = useValveCatalogStore((s) => s.resetToSeeds)
  const getCatalogVendor = useValveCatalogStore((s) => s.getVendor)
  const getCatalogModel = useValveCatalogStore((s) => s.getModel)

  const fluid = useMemo(() => getFluid(fluidId), [fluidId])
  const pipeMat = useMemo(() => getMaterial(pipeMatId), [pipeMatId])
  const plateMat = useMemo(() => getMaterial(plateMatId), [plateMatId])
  const valveType = useMemo(() => getValveType(valveTypeId), [valveTypeId])
  const catalogVendor = useMemo(
    () => getCatalogVendor(selectedVendorId),
    [getCatalogVendor, selectedVendorId, catalogVendors],
  )
  const catalogModel = useMemo(
    () => getCatalogModel(selectedVendorId, selectedModelId),
    [getCatalogModel, selectedVendorId, selectedModelId, catalogVendors],
  )

  const applyCatalogModel = (vendorId: string, modelId?: string) => {
    setCatalogSelection(vendorId, modelId)
    const model = useValveCatalogStore.getState().getModel(vendorId, modelId)
    if (!model) return
    const coeffs = useValveCatalogStore.getState().getResolvedCoeffs(vendorId, model.id)
    if (model.valveTypeId) setValveTypeId(model.valveTypeId)
    setFL(coeffs.FL.toFixed(2))
    setXT(coeffs.xT.toFixed(2))
    setFp(coeffs.Fp.toFixed(2))
    setFd(coeffs.Fd.toFixed(2))
    setRatedCv(coeffs.ratedCv != null ? String(coeffs.ratedCv) : '')
  }

  const persistDrawingCoeffs = (patch: {
    FL?: number
    xT?: number
    Fp?: number
    Fd?: number
    ratedCv?: number
  }) => {
    if (!selectedVendorId || !selectedModelId) return
    updateCatalogModel(selectedVendorId, selectedModelId, {
      ...patch,
      fromDrawing: true,
    })
  }

  const applyValveType = (id: string) => {
    setValveTypeId(id)
    if (id === VALVE_TYPE_CUSTOM) return
    const t = getValveType(id)
    setFL(t.FL.toFixed(2))
    setXT(t.xT.toFixed(2))
    setFd(t.Fd.toFixed(2))
    if (selectedVendorId && selectedModelId) {
      updateCatalogModel(selectedVendorId, selectedModelId, {
        valveTypeId: id,
        FL: t.FL,
        xT: t.xT,
        Fd: t.Fd,
        fromDrawing: false,
      })
    }
  }

  // 进入调节阀页或目录选择变化时，用目录系数同步输入框
  useEffect(() => {
    if (moduleId !== 'control-valve') return
    applyCatalogModel(selectedVendorId, selectedModelId)
  }, [moduleId, selectedVendorId, selectedModelId])
  const isGas = fluid.phase !== 'liquid'
  const isDpFamily = ![
    'control-valve',
  ].includes(moduleId)

  const alphaPipe =
    pipeMatId === 'custom'
      ? Number(pipeAlphaCustom) || pipeMat.alpha
      : pipeMat.alpha
  const alphaPlate =
    plateMatId === 'custom'
      ? Number(plateAlphaCustom) || plateMat.alpha
      : plateMat.alpha

  const computed = useMemo(() => {
    try {
      const p1 = p1BarA * 1e5
      const p2 = p2BarA * 1e5
      const tK = tOpC + 273.15
      const deltaP = dpKPa * 1000

      const rhoOv = parseOptionalNumber(rhoOverride)
      let density =
        rhoOv != null ? densityToKgM3(rhoOv, units.density) : fluid.density
      if (rhoOv == null && isGas) {
        density = gasDensity(fluid.density, p1, tK)
      }
      const muOv = parseOptionalNumber(muOverride)
      const viscosity =
        muOv != null ? viscosityToPas(muOv, units.viscosity) : fluid.viscosity
      const kappa = parseOptionalNumber(kappaOverride) ?? fluid.kappa ?? 1.4
      const pv = parseOptionalNumber(pvOverride) ?? fluid.vaporPressure ?? 2339
      const pc = parseOptionalNumber(pcOverride) ?? fluid.pc ?? 22.06e6
      const cdNum = parseOptionalNumber(Cd)
      const epsNum = parseOptionalNumber(epsOverride)

      const geo = expandGeometry({
        Dref_mm: Dmm,
        dref_mm: dmm,
        alphaPipe,
        alphaPlate,
        tOp_C: tOpC,
        tRef_C: tRefC,
      })
      const D = applyThermal && isDpFamily ? geo.Dop : Dmm / 1000
      const d = applyThermal && isDpFamily ? geo.dop : dmm / 1000

      const targetMass =
        flowInputMode === 'mass'
          ? massKgH / 3600
          : (targetQmh / 3600) * density

      if (moduleId === 'control-valve') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'valve' as const,
            data: calcControlValve({
              style: valveStyle,
              algorithm: catalogVendor.algorithm,
              massFlow: massKgH / 3600,
              density,
              p1,
              p2,
              pv,
              pc,
              kappa,
              FL: parseOptionalNumber(FL) ?? valveType.FL,
              Fp: parseOptionalNumber(Fp) ?? 1,
              xT: parseOptionalNumber(xT) ?? valveType.xT,
              Fd: parseOptionalNumber(Fd) ?? valveType.Fd,
              valveTypeName: valveType.name,
              vendorName: catalogVendor.name,
              modelName: catalogModel?.name,
              sheetBrand: catalogVendor.sheetBrand,
              coeffSource: catalogModel
                ? modelCoeffSource(catalogModel)
                : '阀型典型值',
              ratedCv: parseOptionalNumber(ratedCv),
            }),
          },
        }
      }

      if (moduleId === 'restriction-orifice') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'ro' as const,
            data: calcRestrictionOrifice({
              D,
              massFlow: targetMass,
              density,
              p1,
              p2,
              phase: isGas ? 'gas' : 'liquid',
              stages: roStages,
              Cd: cdNum,
              kappa,
            }),
          },
        }
      }

      const commonBase = {
        D,
        density,
        viscosity,
        isCompressible: isGas || fluid.phase === 'steam',
        p1,
        kappa,
        C: cdNum,
        epsilon: epsNum,
      }

      if (moduleId === 'averaging-pitot') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'dp' as const,
            data: calcAveragingPitot({
              D,
              deltaP,
              density,
              viscosity,
              K: parseOptionalNumber(K) ?? 0.7,
              probeBlockage: parseOptionalNumber(probeBlockage),
            }),
          },
        }
      }

      if (moduleId === 'orifice') {
        const orificeBase = {
          ...commonBase,
          tap,
          plateType,
          plateThickness: parseOptionalNumber(plateThickMm)
            ? parseOptionalNumber(plateThickMm)! / 1000
            : undefined,
          edgeThickness: parseOptionalNumber(edgeThickMm)
            ? parseOptionalNumber(edgeThickMm)! / 1000
            : undefined,
          drainHole: parseOptionalNumber(drainHoleMm)
            ? parseOptionalNumber(drainHoleMm)! / 1000
            : undefined,
          roughness: parseOptionalNumber(roughnessUm)
            ? parseOptionalNumber(roughnessUm)! * 1e-6
            : undefined,
        }

        if (mode === 'size_bore') {
          const sized = sizeOrificeBore(targetMass, { ...orificeBase, deltaP }, betaMin, betaMax)
          return {
            error: null as string | null,
            geo,
            props: { density, viscosity, kappa, pv, pc },
            result: { type: 'sized_bore' as const, data: sized },
          }
        }
        if (mode === 'size_dp') {
          const sized = sizeOrificeDp(targetMass, { ...orificeBase, d })
          return {
            error: null as string | null,
            geo,
            props: { density, viscosity, kappa, pv, pc },
            result: { type: 'sized_dp' as const, data: sized },
          }
        }
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'orifice' as const,
            data: calcOrifice({ ...orificeBase, d, deltaP }),
          },
        }
      }

      const common = { ...commonBase, d, deltaP }

      if (moduleId === 'conditioning-orifice') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'conditioning' as const,
            data: calcConditioningOrifice({ ...common, holeCount, Cd: cdNum }),
          },
        }
      }
      if (moduleId === 'venturi') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'venturi' as const,
            data: calcVenturi({ ...common, profile: venturiProfile }),
          },
        }
      }
      if (moduleId === 'venturi-nozzle') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'nozzle' as const,
            data: calcNozzle({ ...common, nozzleType }),
          },
        }
      }
      if (moduleId === 'wedge') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'wedge' as const,
            data: calcWedge({ ...common, wedgeAngleDeg: wedgeAngle, Cd: cdNum }),
          },
        }
      }
      if (moduleId === 'cone') {
        return {
          error: null as string | null,
          geo,
          props: { density, viscosity, kappa, pv, pc },
          result: {
            type: 'cone' as const,
            data: calcCone({ ...common, Cd: cdNum }),
          },
        }
      }

      return {
        error: null as string | null,
        geo,
        props: { density, viscosity, kappa, pv, pc },
        result: null,
      }
    } catch (e) {
      return {
        error: e instanceof Error ? e.message : String(e),
        geo: null,
        props: null,
        result: null,
      }
    }
  }, [
    moduleId,
    fluid,
    isGas,
    Dmm,
    dmm,
    dpKPa,
    p1BarA,
    p2BarA,
    tOpC,
    tRefC,
    applyThermal,
    alphaPipe,
    alphaPlate,
    isDpFamily,
    tap,
    plateType,
    plateThickMm,
    edgeThickMm,
    drainHoleMm,
    roughnessUm,
    venturiProfile,
    nozzleType,
    holeCount,
    wedgeAngle,
    probeBlockage,
    Cd,
    epsOverride,
    K,
    mode,
    betaMin,
    betaMax,
    targetQmh,
    massKgH,
    flowInputMode,
    valveStyle,
    valveType,
    catalogVendor,
    catalogModel,
    FL,
    Fp,
    xT,
    Fd,
    ratedCv,
    roStages,
    rhoOverride,
    muOverride,
    kappaOverride,
    pvOverride,
    pcOverride,
    units.density,
    units.viscosity,
  ])

  const { error, result, geo, props: usedProps } = computed

  const showGeometry = moduleId !== 'control-valve'
  const showDp =
    !['control-valve', 'restriction-orifice'].includes(moduleId) ||
    moduleId === 'restriction-orifice'
  const showMaterials = showGeometry

  const calcSheet = useMemo((): CalcSheet | null => {
    if (!meta || error || !result) return null

    const block = (title: string, cells: SheetCell[]): SheetBlock => ({
      title,
      cells: cells.filter((c) => c.value !== '' && c.value != null),
    })

    const productCells: SheetCell[] = [
      { label: '计算模块', value: meta.name },
      { label: '产品族', value: meta.productFamily },
      { label: '工质', value: `${fluid.name} / ${fluid.nameEn}` },
      { label: '相态', value: fluid.phase },
    ]
    if (moduleId === 'orifice') {
      productCells.push(
        { label: '孔板型式', value: plateType },
        { label: '取压方式', value: tap },
      )
    }
    if (moduleId === 'venturi') {
      productCells.push({ label: '文丘里型式', value: venturiProfile })
    }
    if (moduleId === 'venturi-nozzle') {
      productCells.push({ label: '喷嘴型式', value: nozzleType })
    }
    if (moduleId === 'control-valve') {
      productCells.push(
        { label: '厂家', value: catalogVendor.name },
        { label: '系列/型号', value: catalogModel?.name ?? '—' },
        { label: '选型算法', value: catalogVendor.algorithm },
        { label: '阀型', value: valveType.name },
        { label: '介质类型', value: valveStyle },
        {
          label: '系数来源',
          value: catalogModel ? modelCoeffSource(catalogModel) : '阀型典型值',
        },
        { label: 'FL', value: FL || String(valveType.FL) },
        { label: 'xT', value: xT || String(valveType.xT) },
        { label: 'Fp', value: Fp || '1' },
        { label: 'Fd', value: Fd || String(valveType.Fd) },
      )
      if (ratedCv) {
        productCells.push({ label: '样本额定 Cv', value: ratedCv })
      }
    }

    const processCells: SheetCell[] = [
      {
        label: '操作温度',
        value: `${formatEng(cToTemp(tOpC, units.temperature))} °${units.temperature}`,
      },
      {
        label: '参考温度',
        value: `${formatEng(cToTemp(tRefC, units.temperature))} °${units.temperature}`,
      },
      {
        label: units.pressureRef === 'gauge' ? '上游压力 p1（表压）' : '上游压力 p1（绝压）',
        value: `${formatEng(absPaToDisplay(p1BarA * 1e5, patmBar * 1e5, units.pressure, units.pressureRef))} ${pressureUnitLabel(units.pressure, units.pressureRef)}`,
      },
      {
        label: '差压 Δp',
        value: `${formatEng(paToPressure(dpKPa * 1000, units.diffPressure))} ${units.diffPressure}`,
      },
    ]
    if (moduleId === 'control-valve' || moduleId === 'restriction-orifice') {
      processCells.push({
        label: units.pressureRef === 'gauge' ? '下游压力 p2（表压）' : '下游压力 p2（绝压）',
        value: `${formatEng(absPaToDisplay(p2BarA * 1e5, patmBar * 1e5, units.pressure, units.pressureRef))} ${pressureUnitLabel(units.pressure, units.pressureRef)}`,
      })
    }
    if (usedProps) {
      processCells.push(
        {
          label: '密度 ρ',
          value: `${formatEng(kgM3ToDensity(usedProps.density, units.density))} ${units.density}`,
        },
        {
          label: '粘度 μ',
          value: `${formatEng(pasToViscosity(usedProps.viscosity, units.viscosity))} ${units.viscosity}`,
        },
        { label: '等熵指数 κ', value: formatEng(usedProps.kappa) },
      )
    }

    const geoCells: SheetCell[] = [
      {
        label: '管内径 D (ref)',
        value: `${formatEng(mToLength(Dmm / 1000, units.length))} ${units.length}`,
      },
      {
        label: '节流径 d (ref)',
        value: `${formatEng(mToLength(dmm / 1000, units.length))} ${units.length}`,
      },
    ]
    if (showMaterials) {
      geoCells.push(
        { label: '管道材质', value: pipeMat.name },
        { label: '节流件材质', value: plateMat.name },
        { label: '温补', value: applyThermal ? '启用' : '关闭' },
      )
    }
    if (geo && applyThermal && showMaterials) {
      geoCells.push(
        {
          label: 'D @ 操作温',
          value: `${formatEng(mToLength(geo.Dop, units.length))} ${units.length}`,
        },
        {
          label: 'd @ 操作温',
          value: `${formatEng(mToLength(geo.dop, units.length))} ${units.length}`,
        },
        { label: 'β @ 操作温', value: formatEng(geo.betaOp) },
        { label: 'β @ 参考温', value: formatEng(geo.betaRef) },
      )
    }

    const resultCells: SheetCell[] = []
    const warnings: string[] = []

    const pushDp = (data: {
      massFlow: number
      volFlow: number
      beta?: number
      C: number
      epsilon: number
      reynolds: number
      velocity: number
      permanentPressureLossPa: number
      standard?: string
      warnings?: string[]
    }) => {
      resultCells.push(
        {
          label: '质量流量',
          value: `${formatEng(kgsToFlowMass(data.massFlow, units.flowMass))} ${units.flowMass}`,
        },
        {
          label: '体积流量',
          value: `${formatEng(m3sToFlowVol(data.volFlow, units.flowVol))} ${units.flowVol}`,
        },
        { label: '流出系数 C/K', value: formatEng(data.C) },
        { label: '可膨胀系数 ε', value: formatEng(data.epsilon) },
      )
      if (data.beta != null && data.beta > 0) {
        resultCells.push({ label: '直径比 β', value: formatEng(data.beta) })
      }
      resultCells.push(
        { label: '管雷诺数 ReD', value: formatEng(data.reynolds, 5) },
        { label: '喉部流速', value: `${formatEng(data.velocity)} m/s` },
        {
          label: '永久压损',
          value: `${formatEng(paToPressure(data.permanentPressureLossPa, units.diffPressure))} ${units.diffPressure}`,
        },
      )
      if (data.warnings) warnings.push(...data.warnings)
    }

    if (result.type === 'valve') {
      resultCells.push(
        { label: '厂家', value: result.data.vendorName ?? catalogVendor.name },
        { label: '系列/型号', value: result.data.modelName ?? catalogModel?.name ?? '—' },
        { label: '选型算法', value: result.data.algorithmName },
        { label: '计算依据', value: result.data.standard },
        { label: '阀型', value: result.data.valveTypeName ?? valveType.name },
        { label: '主报系数', value: result.data.primaryCoeff },
        { label: 'Kv', value: formatEng(result.data.Kv) },
        { label: 'Cv', value: formatEng(result.data.Cv) },
      )
      if (result.data.Cg != null) {
        resultCells.push({ label: 'Cg（Fisher/ISA）', value: formatEng(result.data.Cg) })
      }
      resultCells.push(
        {
          label: 'Δp',
          value: `${formatEng(paToPressure(result.data.deltaP, units.diffPressure))} ${units.diffPressure}`,
        },
        { label: '工况判定', value: result.data.regime },
        { label: '采用 FL', value: formatEng(result.data.FL) },
        { label: '采用 xT', value: formatEng(result.data.xT) },
        { label: '采用 Fp', value: formatEng(result.data.Fp) },
        { label: '采用 Fd', value: formatEng(result.data.Fd) },
      )
      if (result.data.ratedCv != null) {
        resultCells.push({ label: '样本额定 Cv', value: formatEng(result.data.ratedCv) })
      }
      warnings.push(...result.data.warnings.filter((w) => !w.startsWith('算法：')))
    } else if (result.type === 'ro') {
      resultCells.push(
        {
          label: '总压降',
          value: `${formatEng(paToPressure(result.data.totalDeltaP, units.pressure))} ${units.pressure}`,
        },
        { label: '级数', value: String(result.data.stages.length) },
        { label: '推荐级数', value: String(result.data.recommendedStages) },
      )
      result.data.stages.forEach((s, i) => {
        resultCells.push({
          label: `第${i + 1}级 d / β`,
          value: `${formatEng(mToLength(s.d, units.length))} ${units.length} / ${formatEng(s.beta)}${s.choked ? ' (阻塞)' : ''}`,
        })
      })
      warnings.push(...result.data.warnings)
    } else if (result.type === 'sized_bore') {
      resultCells.push(
        {
          label: '设计孔径 d',
          value: `${formatEng(mToLength(result.data.d, units.length))} ${units.length}`,
        },
        { label: '设计 β', value: formatEng(result.data.beta) },
      )
      pushDp(result.data.result)
    } else if (result.type === 'sized_dp') {
      resultCells.push({
        label: '所需差压',
        value: `${formatEng(paToPressure(result.data.deltaP, units.diffPressure))} ${units.diffPressure}`,
      })
      pushDp(result.data.result)
    } else if (
      result.type === 'dp' ||
      result.type === 'orifice' ||
      result.type === 'conditioning' ||
      result.type === 'venturi' ||
      result.type === 'nozzle' ||
      result.type === 'wedge' ||
      result.type === 'cone'
    ) {
      pushDp({
        ...result.data,
        standard: 'standard' in result.data ? String(result.data.standard) : undefined,
      })
      if ('geometryNotes' in result.data && Array.isArray(result.data.geometryNotes)) {
        warnings.push(...result.data.geometryNotes)
      }
    }

    return {
      docTitle: `${meta.name} 计算书`,
      brandName:
        moduleId === 'control-valve' ? catalogVendor.sheetBrand : undefined,
      productLine:
        moduleId === 'control-valve'
          ? `流衡 FlowSize · ${catalogVendor.name} · ${VALVE_ALGORITHMS.find((a) => a.id === catalogVendor.algorithm)?.name ?? catalogVendor.algorithm}`
          : 'FlowSize Calculation Data Sheet',
      moduleName: meta.name,
      standards: meta.standards.join('；'),
      tag: sheetTag.trim() || '—',
      project: sheetProject.trim() || '—',
      date: new Date().toLocaleString('zh-CN'),
      blocks: [
        block('1. 产品 / 装置描述  PRODUCT', productCells),
        block('2. 工艺输入  INPUT DATA', processCells),
        block('3. 几何与材质  METER GEOMETRY', geoCells),
        block('4. 计算结果  CALCULATED DATA', resultCells),
      ].filter((b) => b.cells.length > 0),
      notes: [],
      warnings,
    }
  }, [
    meta,
    error,
    result,
    fluid,
    tOpC,
    tRefC,
    p1BarA,
    p2BarA,
    patmBar,
    dpKPa,
    usedProps,
    geo,
    applyThermal,
    showMaterials,
    pipeMat,
    plateMat,
    Dmm,
    dmm,
    units,
    moduleId,
    plateType,
    tap,
    venturiProfile,
    nozzleType,
    sheetTag,
    sheetProject,
    valveType,
    valveStyle,
    catalogVendor,
    catalogModel,
    FL,
    Fp,
    xT,
    Fd,
    ratedCv,
  ])

  if (!meta) {
    return (
      <div className="panel">
        <h3>未找到模块</h3>
        <p>模块 ID：{moduleId}</p>
      </div>
    )
  }

  const filenameBase =
    moduleId === 'control-valve'
      ? `${meta.name}_${catalogVendor.sheetBrand}_${catalogModel?.name ?? 'model'}_${new Date().toISOString().slice(0, 10)}`
      : `${meta.name}_${fluid.name}_${new Date().toISOString().slice(0, 10)}`

  const save = () => {
    addProject({
      name: `${meta.name} · ${fluid.name} · ${Dmm}mm`,
      moduleId: meta.id,
      note: result ? '已计算' : undefined,
    })
  }

  const doExportExcel = () => {
    if (!calcSheet) {
      alert('暂无计算结果可导出')
      return
    }
    exportExcelCsv(filenameBase, calcSheet)
    exportExcelSheet(filenameBase, calcSheet)
  }

  const doExportPdf = () => {
    if (!calcSheet) {
      alert('暂无计算结果可导出')
      return
    }
    exportPdfSheet(calcSheet)
  }

  return (
    <div>
      <div className="topbar">
        <div>
          <h2>{meta.name}</h2>
          <p className="sub">
            {meta.description} · {meta.productFamily}
          </p>
        </div>
        <span className={`badge ${meta.status}`}>
          {meta.status === 'ready' ? '可用' : 'Beta'}
        </span>
      </div>

      <div className="workbench">
        <div className="panel input-scroll">
          <h3>输入参数</h3>

          <UnitPrefsPanel />

          <details open className="param-block">
            <summary>工质</summary>
            <FluidPicker value={fluidId} onChange={setFluidId} />
            <Field label="密度覆盖（空=库值/气体按P·T）" unit={units.density}>
              <input value={rhoOverride} onChange={(e) => setRhoOverride(e.target.value)} placeholder="可选" />
            </Field>
            <Field label="动力粘度覆盖" unit={units.viscosity}>
              <input value={muOverride} onChange={(e) => setMuOverride(e.target.value)} placeholder="可选" />
            </Field>
            <Field label="等熵指数 κ 覆盖">
              <input value={kappaOverride} onChange={(e) => setKappaOverride(e.target.value)} placeholder="可选" />
            </Field>
            {(moduleId === 'control-valve' || isGas === false) && (
              <>
                <Field label="蒸汽压 pv 覆盖" unit="Pa">
                  <input value={pvOverride} onChange={(e) => setPvOverride(e.target.value)} placeholder="可选" />
                </Field>
                <Field label="临界压力 pc 覆盖" unit="Pa">
                  <input value={pcOverride} onChange={(e) => setPcOverride(e.target.value)} placeholder="可选" />
                </Field>
              </>
            )}
          </details>

          <details open className="param-block">
            <summary>工况</summary>
            <Field label="操作温度 t" unit={`°${units.temperature}`}>
              <NumberInput
                value={cToTemp(tOpC, units.temperature)}
                onChange={(v) => setTOpC(tempToC(v, units.temperature))}
              />
            </Field>
            {showMaterials && (
              <Field label="尺寸测量参考温度 t_ref" unit={`°${units.temperature}`}>
                <NumberInput
                  value={cToTemp(tRefC, units.temperature)}
                  onChange={(v) => setTRefC(tempToC(v, units.temperature))}
                />
              </Field>
            )}
            <Field
              label={units.pressureRef === 'gauge' ? '上游压力 p1（表压）' : '上游压力 p1（绝压）'}
              unit={pressureUnitLabel(units.pressure, units.pressureRef)}
            >
              <NumberInput
                value={absPaToDisplay(p1BarA * 1e5, patmBar * 1e5, units.pressure, units.pressureRef)}
                onChange={(v) =>
                  setP1BarA(displayToAbsPa(v, patmBar * 1e5, units.pressure, units.pressureRef) / 1e5)
                }
              />
            </Field>
            {(moduleId === 'control-valve' || moduleId === 'restriction-orifice') && (
              <Field
                label={units.pressureRef === 'gauge' ? '下游压力 p2（表压）' : '下游压力 p2（绝压）'}
                unit={pressureUnitLabel(units.pressure, units.pressureRef)}
              >
                <NumberInput
                  value={absPaToDisplay(p2BarA * 1e5, patmBar * 1e5, units.pressure, units.pressureRef)}
                  onChange={(v) =>
                    setP2BarA(displayToAbsPa(v, patmBar * 1e5, units.pressure, units.pressureRef) / 1e5)
                  }
                />
              </Field>
            )}
            <Field label="当地大气压" unit={pressureUnitLabel(units.pressure, 'absolute')}>
              <NumberInput
                value={paToPressure(patmBar * 1e5, units.pressure)}
                onChange={(v) => setPatmBar(pressureToPa(v, units.pressure) / 1e5)}
              />
            </Field>
            <div className="hint-line">
              当前 p1 绝压 ≈ {formatEng(paToPressure(p1BarA * 1e5, units.pressure))}{' '}
              {pressureUnitLabel(units.pressure, 'absolute')}
              {' · '}
              表压 ≈ {formatEng(paToPressure((p1BarA - patmBar) * 1e5, units.pressure))}{' '}
              {pressureUnitLabel(units.pressure, 'gauge')}
              （计算内核使用绝压）
            </div>
          </details>

          {showMaterials && (
            <details open className="param-block">
              <summary>材质与热膨胀</summary>
              <label className="check-line">
                <input
                  type="checkbox"
                  checked={applyThermal}
                  onChange={(e) => setApplyThermal(e.target.checked)}
                />
                按操作温度修正 D、d（ISO 5167）
              </label>
              <MaterialSelect
                label="管道材质"
                value={pipeMatId}
                onChange={setPipeMatId}
                material={pipeMat}
                customAlpha={pipeAlphaCustom}
                onCustomAlphaChange={setPipeAlphaCustom}
              />
              <MaterialSelect
                label="节流件 / 孔板材质"
                value={plateMatId}
                onChange={setPlateMatId}
                material={plateMat}
                customAlpha={plateAlphaCustom}
                onCustomAlphaChange={setPlateAlphaCustom}
              />
            </details>
          )}

          {showGeometry && (
            <details open className="param-block">
              <summary>几何</summary>
              <Field label="管内径 D（参考温度）" unit={units.length}>
                <NumberInput
                  value={mToLength(Dmm / 1000, units.length)}
                  onChange={(v) => setDmm(lengthToM(v, units.length) * 1000)}
                  min={0}
                />
              </Field>
              {moduleId !== 'averaging-pitot' && !(moduleId === 'orifice' && mode === 'size_bore') && (
                <Field
                  label={
                    moduleId === 'cone'
                      ? '等效喉径 d（参考温度）'
                      : '节流孔径 / 喉径 d（参考温度）'
                  }
                  unit={units.length}
                >
                  <NumberInput
                    value={mToLength(dmm / 1000, units.length)}
                    onChange={(v) => setDmmHole(lengthToM(v, units.length) * 1000)}
                    min={0}
                  />
                </Field>
              )}
            </details>
          )}

          {moduleId === 'orifice' && (
            <details open className="param-block">
              <summary>孔板参数</summary>
              <Field label="计算模式">
                <select value={mode} onChange={(e) => setMode(e.target.value as DpMode)}>
                  <option value="flow_from_dp">已知几何+差压 → 流量</option>
                  <option value="size_bore">已知流量+差压 → 孔径</option>
                  <option value="size_dp">已知流量+几何 → 差压</option>
                </select>
              </Field>
              <Field label="孔板型式">
                <select
                  value={plateType}
                  onChange={(e) => setPlateType(e.target.value as OrificePlateType)}
                >
                  <option value="concentric">同心锐边</option>
                  <option value="eccentric">偏心</option>
                  <option value="segmental">扇形</option>
                  <option value="quadrant">1/4 圆</option>
                </select>
              </Field>
              <Field label="取压方式">
                <select value={tap} onChange={(e) => setTap(e.target.value as TapType)}>
                  <option value="flange">法兰取压</option>
                  <option value="corner">角接取压</option>
                  <option value="D_D2">D − D/2 取压</option>
                </select>
              </Field>
              <Field label="孔板厚度 E" unit="mm">
                <input value={plateThickMm} onChange={(e) => setPlateThickMm(e.target.value)} />
              </Field>
              <Field label="上游锐边厚度 e" unit="mm">
                <input value={edgeThickMm} onChange={(e) => setEdgeThickMm(e.target.value)} />
              </Field>
              <Field label="排污/排气孔直径" unit="mm">
                <input value={drainHoleMm} onChange={(e) => setDrainHoleMm(e.target.value)} placeholder="无则留空" />
              </Field>
              <Field label="管壁粗糙度 Ra" unit="μm">
                <input value={roughnessUm} onChange={(e) => setRoughnessUm(e.target.value)} />
              </Field>
              {mode === 'size_bore' && (
                <>
                  <Field label="β 下限">
                    <NumberInput value={betaMin} onChange={setBetaMin} min={0.1} max={0.9} />
                  </Field>
                  <Field label="β 上限">
                    <NumberInput value={betaMax} onChange={setBetaMax} min={0.1} max={0.9} />
                  </Field>
                </>
              )}
            </details>
          )}

          {moduleId === 'conditioning-orifice' && (
            <details open className="param-block">
              <summary>调整型孔板</summary>
              <Field label="开孔数">
                <NumberInput value={holeCount} onChange={setHoleCount} min={2} />
              </Field>
            </details>
          )}

          {moduleId === 'venturi' && (
            <details open className="param-block">
              <summary>文丘里型式</summary>
              <Field label="型式（PRESO）">
                <select
                  value={venturiProfile}
                  onChange={(e) => setVenturiProfile(e.target.value as VenturiProfile)}
                >
                  <option value="low_loss">低损 LPL / CV</option>
                  <option value="machined">精加工 SSL</option>
                  <option value="as_cast">铸造收敛</option>
                  <option value="rough_welded">粗焊收敛</option>
                </select>
              </Field>
            </details>
          )}

          {moduleId === 'venturi-nozzle' && (
            <details open className="param-block">
              <summary>喷嘴型式</summary>
              <Field label="型式">
                <select
                  value={nozzleType}
                  onChange={(e) => setNozzleType(e.target.value as NozzleType)}
                >
                  <option value="venturi_nozzle">文丘里喷嘴（SSM）</option>
                  <option value="isa1932">ISA 1932</option>
                  <option value="long_radius">长径喷嘴</option>
                </select>
              </Field>
            </details>
          )}

          {moduleId === 'wedge' && (
            <details open className="param-block">
              <summary>楔形参数</summary>
              <Field label="楔角" unit="°">
                <NumberInput value={wedgeAngle} onChange={setWedgeAngle} min={0} />
              </Field>
            </details>
          )}

          {moduleId === 'averaging-pitot' && (
            <details open className="param-block">
              <summary>均速管</summary>
              <Field label="厂家流量系数 K">
                <input value={K} onChange={(e) => setK(e.target.value)} />
              </Field>
              <Field label="探针堵塞比">
                <input value={probeBlockage} onChange={(e) => setProbeBlockage(e.target.value)} />
              </Field>
            </details>
          )}

          {moduleId === 'control-valve' && (
            <details open className="param-block">
              <summary>调节阀 · 厂家与系数</summary>
              <Field label="厂家">
                <select
                  value={selectedVendorId}
                  onChange={(e) => applyCatalogModel(e.target.value)}
                >
                  {catalogVendors.map((v) => (
                    <option key={v.id} value={v.id}>
                      {v.name}
                    </option>
                  ))}
                </select>
              </Field>
              <Field label="系列 / 型号">
                <select
                  value={selectedModelId}
                  onChange={(e) => applyCatalogModel(selectedVendorId, e.target.value)}
                >
                  {catalogVendor.models.map((m) => (
                    <option key={m.id} value={m.id}>
                      {m.name}
                      {m.fromDrawing || m.FL != null ? ' · 已录图纸' : ''}
                    </option>
                  ))}
                </select>
              </Field>
              <Field label="选型算法">
                <select
                  value={catalogVendor.algorithm}
                  onChange={(e) =>
                    setVendorAlgorithm(
                      selectedVendorId,
                      e.target.value as ValveAlgorithmId,
                    )
                  }
                >
                  {VALVE_ALGORITHMS.map((a) => (
                    <option key={a.id} value={a.id}>
                      {a.name}
                    </option>
                  ))}
                </select>
              </Field>
              <div className="hint-line" style={{ gridColumn: '1 / -1' }}>
                厂家默认绑定算法；换厂家会换算法路径（Fisher→ISA·Cv+Cg，Samson/Neles→IEC·Kv，吴忠→GB/IEC）。
                图纸系数仍须按该厂样本填写。当前：
                {VALVE_ALGORITHMS.find((a) => a.id === catalogVendor.algorithm)?.standardLabel}
                {catalogModel ? ` · ${modelCoeffSource(catalogModel)}` : ''}
              </div>
              <div
                style={{
                  gridColumn: '1 / -1',
                  display: 'flex',
                  flexWrap: 'wrap',
                  gap: '0.5rem',
                  alignItems: 'center',
                }}
              >
                <button
                  type="button"
                  className="btn secondary"
                  onClick={() => {
                    const name = window.prompt('新型号名称（按图纸）', '新型号')
                    if (!name?.trim()) return
                    addCatalogModel(selectedVendorId, {
                      name: name.trim(),
                      valveTypeId:
                        valveTypeId === VALVE_TYPE_CUSTOM ? 'single_seat_ftc' : valveTypeId,
                      FL: parseOptionalNumber(FL),
                      xT: parseOptionalNumber(xT),
                      Fp: parseOptionalNumber(Fp),
                      Fd: parseOptionalNumber(Fd),
                      ratedCv: parseOptionalNumber(ratedCv),
                      fromDrawing: true,
                      note: '用户按图纸新增',
                    })
                  }}
                >
                  新增型号
                </button>
                <button type="button" className="btn secondary" onClick={() => exportCatalogJson()}>
                  导出目录 JSON
                </button>
                <button
                  type="button"
                  className="btn secondary"
                  onClick={() => catalogFileRef.current?.click()}
                >
                  导入目录 JSON
                </button>
                <button
                  type="button"
                  className="btn secondary"
                  onClick={() => {
                    if (window.confirm('恢复出厂厂家骨架？本地已录图纸系数将丢失。')) {
                      resetCatalogSeeds()
                      applyCatalogModel('generic_iec')
                    }
                  }}
                >
                  重置骨架
                </button>
                <input
                  ref={catalogFileRef}
                  type="file"
                  accept="application/json,.json"
                  style={{ display: 'none' }}
                  onChange={(e) => {
                    const file = e.target.files?.[0]
                    e.target.value = ''
                    if (!file) return
                    const reader = new FileReader()
                    reader.onload = () => {
                      const r = importCatalogJson(String(reader.result ?? ''))
                      if (!r.ok) {
                        alert(r.error ?? '导入失败')
                        return
                      }
                      const st = useValveCatalogStore.getState()
                      applyCatalogModel(st.selectedVendorId, st.selectedModelId)
                    }
                    reader.readAsText(file)
                  }}
                />
              </div>
              <Field label="阀型（快捷）">
                <select
                  value={valveTypeId}
                  onChange={(e) => applyValveType(e.target.value)}
                >
                  {VALVE_TYPES.map((t) => (
                    <option key={t.id} value={t.id}>
                      {t.name}
                    </option>
                  ))}
                </select>
              </Field>
              {valveType.note && (
                <div className="hint-line" style={{ gridColumn: '1 / -1' }}>
                  {valveType.note}
                </div>
              )}
              <Field label="介质类型">
                <select
                  value={valveStyle}
                  onChange={(e) => setValveStyle(e.target.value as typeof valveStyle)}
                >
                  <option value="liquid">液体</option>
                  <option value="gas">气体</option>
                  <option value="steam">蒸汽</option>
                </select>
              </Field>
              <Field label="质量流量" unit={units.flowMass}>
                <NumberInput
                  value={kgsToFlowMass(massKgH / 3600, units.flowMass)}
                  onChange={(v) => setMassKgH(flowMassToKgs(v, units.flowMass) * 3600)}
                  min={0}
                />
              </Field>
              <Field label="FL（压力恢复系数）">
                <input
                  value={FL}
                  onChange={(e) => {
                    setFL(e.target.value)
                    setValveTypeId(VALVE_TYPE_CUSTOM)
                    const n = parseOptionalNumber(e.target.value)
                    if (n != null) persistDrawingCoeffs({ FL: n })
                  }}
                />
              </Field>
              <Field label="Fp（管路几何系数）">
                <input
                  value={Fp}
                  onChange={(e) => {
                    setFp(e.target.value)
                    const n = parseOptionalNumber(e.target.value)
                    if (n != null) persistDrawingCoeffs({ Fp: n })
                  }}
                />
              </Field>
              <Field label="xT（气体压差比系数）">
                <input
                  value={xT}
                  onChange={(e) => {
                    setXT(e.target.value)
                    setValveTypeId(VALVE_TYPE_CUSTOM)
                    const n = parseOptionalNumber(e.target.value)
                    if (n != null) persistDrawingCoeffs({ xT: n })
                  }}
                />
              </Field>
              <Field label="Fd（阀型修正因子）">
                <input
                  value={Fd}
                  onChange={(e) => {
                    setFd(e.target.value)
                    setValveTypeId(VALVE_TYPE_CUSTOM)
                    const n = parseOptionalNumber(e.target.value)
                    if (n != null) persistDrawingCoeffs({ Fd: n })
                  }}
                />
              </Field>
              <Field label="样本额定 Cv（可选）">
                <input
                  value={ratedCv}
                  placeholder="图纸额定值，仅记录"
                  onChange={(e) => {
                    setRatedCv(e.target.value)
                    const n = parseOptionalNumber(e.target.value)
                    persistDrawingCoeffs({ ratedCv: n })
                  }}
                />
              </Field>
            </details>
          )}

          {moduleId === 'restriction-orifice' && (
            <details open className="param-block">
              <summary>限流孔板</summary>
              <Field label="流量输入">
                <select
                  value={flowInputMode}
                  onChange={(e) => setFlowInputMode(e.target.value as 'mass' | 'vol')}
                >
                  <option value="vol">体积流量 ({units.flowVol})</option>
                  <option value="mass">质量流量 ({units.flowMass})</option>
                </select>
              </Field>
              {flowInputMode === 'vol' ? (
                <Field label="体积流量" unit={units.flowVol}>
                  <NumberInput
                    value={m3sToFlowVol(targetQmh / 3600, units.flowVol)}
                    onChange={(v) => setTargetQmh(flowVolToM3s(v, units.flowVol) * 3600)}
                    min={0}
                  />
                </Field>
              ) : (
                <Field label="质量流量" unit={units.flowMass}>
                  <NumberInput
                    value={kgsToFlowMass(massKgH / 3600, units.flowMass)}
                    onChange={(v) => setMassKgH(flowMassToKgs(v, units.flowMass) * 3600)}
                    min={0}
                  />
                </Field>
              )}
              <Field label="级数">
                <NumberInput value={roStages} onChange={setRoStages} min={1} max={10} />
              </Field>
            </details>
          )}

          {/* 差压与流量目标、系数覆盖 */}
          {showDp && moduleId !== 'restriction-orifice' && (
            <details open className="param-block">
              <summary>差压 / 流量 / 系数</summary>
              {!(moduleId === 'orifice' && mode === 'size_dp') && moduleId !== 'control-valve' && (
                <Field label="差压 Δp" unit={units.diffPressure}>
                  <NumberInput
                    value={paToPressure(dpKPa * 1000, units.diffPressure)}
                    onChange={(v) => setDpKPa(pressureToPa(v, units.diffPressure) / 1000)}
                  />
                </Field>
              )}
              {(moduleId === 'orifice' && mode !== 'flow_from_dp') && (
                <>
                  <Field label="目标流量输入方式">
                    <select
                      value={flowInputMode}
                      onChange={(e) => setFlowInputMode(e.target.value as 'mass' | 'vol')}
                    >
                      <option value="vol">体积流量 ({units.flowVol})</option>
                      <option value="mass">质量流量 ({units.flowMass})</option>
                    </select>
                  </Field>
                  {flowInputMode === 'vol' ? (
                    <Field label="目标体积流量" unit={units.flowVol}>
                      <NumberInput
                        value={m3sToFlowVol(targetQmh / 3600, units.flowVol)}
                        onChange={(v) => setTargetQmh(flowVolToM3s(v, units.flowVol) * 3600)}
                        min={0}
                      />
                    </Field>
                  ) : (
                    <Field label="目标质量流量" unit={units.flowMass}>
                      <NumberInput
                        value={kgsToFlowMass(massKgH / 3600, units.flowMass)}
                        onChange={(v) => setMassKgH(flowMassToKgs(v, units.flowMass) * 3600)}
                        min={0}
                      />
                    </Field>
                  )}
                </>
              )}
              {moduleId !== 'averaging-pitot' && moduleId !== 'control-valve' && (
                <>
                  <Field label="流出系数 C / Cd 覆盖">
                    <input value={Cd} onChange={(e) => setCd(e.target.value)} placeholder="空则按标准公式" />
                  </Field>
                  <Field label="可膨胀系数 ε 覆盖">
                    <input value={epsOverride} onChange={(e) => setEpsOverride(e.target.value)} placeholder="空则自动计算" />
                  </Field>
                </>
              )}
            </details>
          )}

          <details className="param-block">
            <summary>计算书抬头</summary>
            <Field label="位号 Tag">
              <input value={sheetTag} onChange={(e) => setSheetTag(e.target.value)} placeholder="如 FE-001" />
            </Field>
            <Field label="项目名称">
              <input
                value={sheetProject}
                onChange={(e) => setSheetProject(e.target.value)}
                placeholder="可选"
              />
            </Field>
          </details>

          <div className="btn-row">
            <button className="btn" type="button" onClick={save}>
              保存到项目
            </button>
            <button className="btn secondary" type="button" onClick={doExportExcel}>
              导出 Excel
            </button>
            <button className="btn secondary" type="button" onClick={doExportPdf}>
              导出 PDF
            </button>
          </div>
        </div>

        <div className="panel">
          <h3>计算结果</h3>
          <div className="btn-row" style={{ marginBottom: '0.85rem' }}>
            <button className="btn secondary" type="button" onClick={doExportExcel} disabled={!calcSheet}>
              导出 Excel
            </button>
            <button className="btn secondary" type="button" onClick={doExportPdf} disabled={!calcSheet}>
              导出 PDF
            </button>
          </div>
          {error && <div className="warn-list">{error}</div>}

          {!error && geo && applyThermal && showMaterials && (
            <div className="result-grid" style={{ marginBottom: '0.85rem' }}>
              <Metric
                label="D@操作温"
                value={`${formatEng(mToLength(geo.Dop, units.length))} ${units.length}`}
              />
              <Metric
                label="d@操作温"
                value={`${formatEng(mToLength(geo.dop, units.length))} ${units.length}`}
              />
              <Metric label="β@操作温" value={formatEng(geo.betaOp)} />
              <Metric label="β@参考温" value={formatEng(geo.betaRef)} />
            </div>
          )}

          {!error && usedProps && (
            <div className="hint-line" style={{ marginBottom: '0.75rem' }}>
              计算用物性：ρ={formatEng(kgM3ToDensity(usedProps.density, units.density))} {units.density}
              {' · '}μ={formatEng(pasToViscosity(usedProps.viscosity, units.viscosity))} {units.viscosity}
              {' · '}κ={formatEng(usedProps.kappa)}
            </div>
          )}

          {!error && result?.type === 'valve' && (
            <>
              <div className="result-grid">
                <Metric label="厂家" value={result.data.vendorName ?? catalogVendor.name} />
                <Metric label="型号" value={result.data.modelName ?? catalogModel?.name ?? '—'} />
                <Metric label="算法" value={result.data.algorithmName} />
                <Metric label="主报" value={result.data.primaryCoeff} />
                <Metric label="Kv" value={formatEng(result.data.Kv)} />
                <Metric label="Cv" value={formatEng(result.data.Cv)} />
                {result.data.Cg != null && (
                  <Metric label="Cg" value={formatEng(result.data.Cg)} />
                )}
                <Metric
                  label="Δp"
                  value={`${formatEng(paToPressure(result.data.deltaP, units.diffPressure))} ${units.diffPressure}`}
                />
                <Metric label="工况" value={result.data.regime} />
                <Metric
                  label="FL / xT / Fd"
                  value={`${formatEng(result.data.FL)} / ${formatEng(result.data.xT)} / ${formatEng(result.data.Fd)}`}
                />
                {result.data.Y != null && <Metric label="Y" value={formatEng(result.data.Y)} />}
                {result.data.x != null && <Metric label="x" value={formatEng(result.data.x)} />}
              </div>
              <p className="std-line">依据：{result.data.standard}</p>
              {result.data.warnings.filter((w) => !w.startsWith('算法：')).length > 0 && (
                <ul className="warn-list">
                  {result.data.warnings
                    .filter((w) => !w.startsWith('算法：'))
                    .map((w) => (
                      <li key={w}>{w}</li>
                    ))}
                </ul>
              )}
            </>
          )}

          {!error && result?.type === 'ro' && (
            <>
              <div className="result-grid">
                <Metric label="总压降" value={`${formatEng(result.data.totalDeltaP / 1e5)} bar`} />
                <Metric label="推荐级数" value={String(result.data.recommendedStages)} />
                <Metric label="当前级数" value={String(result.data.stages.length)} />
              </div>
              <div style={{ marginTop: '0.85rem', overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.88rem' }}>
                  <thead>
                    <tr>
                      <th align="left">级</th>
                      <th align="right">P1 bar(a)</th>
                      <th align="right">P2 bar(a)</th>
                      <th align="right">d mm</th>
                      <th align="right">β</th>
                      <th align="left">阻塞</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.data.stages.map((s, i) => (
                      <tr key={i}>
                        <td>{i + 1}</td>
                        <td align="right">{formatEng(s.p1 / 1e5)}</td>
                        <td align="right">{formatEng(s.p2 / 1e5)}</td>
                        <td align="right">{formatEng(s.d * 1000)}</td>
                        <td align="right">{formatEng(s.beta)}</td>
                        <td>{s.choked ? '是' : '否'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <p className="std-line">依据：{result.data.standard}</p>
              {result.data.warnings.length > 0 && (
                <ul className="warn-list">
                  {result.data.warnings.map((w) => (
                    <li key={w}>{w}</li>
                  ))}
                </ul>
              )}
            </>
          )}

          {!error && result?.type === 'sized_bore' && (
            <>
              <div className="result-grid">
                <Metric label="孔径 d@操作温" value={`${formatEng(mToLength(result.data.d, units.length))} ${units.length}`} />
                <Metric label="β" value={formatEng(result.data.beta)} />
                <Metric
                  label="质量流量"
                  value={`${formatEng(kgsToFlowMass(result.data.result.massFlow, units.flowMass))} ${units.flowMass}`}
                />
                <Metric label="C" value={formatEng(result.data.result.C)} />
                <Metric label="ε" value={formatEng(result.data.result.epsilon)} />
                <Metric label="ReD" value={formatEng(result.data.result.reynolds, 5)} />
              </div>
              <p className="std-line">依据：{result.data.result.standard}</p>
              {result.data.result.geometryNotes?.length > 0 && (
                <ul className="warn-list">
                  {result.data.result.geometryNotes.map((w) => (
                    <li key={w}>{w}</li>
                  ))}
                </ul>
              )}
            </>
          )}

          {!error && result?.type === 'sized_dp' && (
            <>
              <div className="result-grid">
                <Metric
                  label="所需差压"
                  value={`${formatEng(paToPressure(result.data.deltaP, units.diffPressure))} ${units.diffPressure}`}
                />
                <Metric
                  label="质量流量"
                  value={`${formatEng(kgsToFlowMass(result.data.result.massFlow, units.flowMass))} ${units.flowMass}`}
                />
                <Metric label="C" value={formatEng(result.data.result.C)} />
                <Metric label="ε" value={formatEng(result.data.result.epsilon)} />
                <Metric label="β" value={formatEng(result.data.result.beta)} />
                <Metric label="ReD" value={formatEng(result.data.result.reynolds, 5)} />
              </div>
              <p className="std-line">依据：{result.data.result.standard}</p>
            </>
          )}

          {!error &&
            result &&
            (result.type === 'dp' ||
              result.type === 'orifice' ||
              result.type === 'conditioning' ||
              result.type === 'venturi' ||
              result.type === 'nozzle' ||
              result.type === 'wedge' ||
              result.type === 'cone') && (
              <>
                <div className="result-grid">
                  <Metric
                    label="质量流量"
                    value={`${formatEng(kgsToFlowMass(result.data.massFlow, units.flowMass))} ${units.flowMass}`}
                  />
                  <Metric
                    label="体积流量"
                    value={`${formatEng(m3sToFlowVol(result.data.volFlow, units.flowVol))} ${units.flowVol}`}
                  />
                  {'beta' in result.data && result.data.beta > 0 && (
                    <Metric label="β" value={formatEng(result.data.beta)} />
                  )}
                  <Metric label="C / K" value={formatEng(result.data.C)} />
                  <Metric label="ε" value={formatEng(result.data.epsilon)} />
                  <Metric label="ReD" value={formatEng(result.data.reynolds, 5)} />
                  <Metric label="喉部流速" value={`${formatEng(result.data.velocity)} m/s`} />
                  <Metric
                    label="永久压损"
                    value={`${formatEng(paToPressure(result.data.permanentPressureLossPa, units.diffPressure))} ${units.diffPressure}`}
                  />
                </div>
                <p className="std-line">
                  依据：{'standard' in result.data ? result.data.standard : meta.standards.join(' / ')}
                  {'productHint' in result.data && result.data.productHint
                    ? ` · ${result.data.productHint}`
                    : ''}
                  {'straightRunHint' in result.data && result.data.straightRunHint
                    ? ` · ${result.data.straightRunHint}`
                    : ''}
                </p>
                {'geometryNotes' in result.data &&
                  Array.isArray(result.data.geometryNotes) &&
                  result.data.geometryNotes.length > 0 && (
                    <ul className="warn-list">
                      {result.data.geometryNotes.map((w: string) => (
                        <li key={w}>{w}</li>
                      ))}
                    </ul>
                  )}
                {result.data.warnings.length > 0 && (
                  <ul className="warn-list">
                    {result.data.warnings.map((w) => (
                      <li key={w}>{w}</li>
                    ))}
                  </ul>
                )}
              </>
            )}

          <div className="meta" style={{ marginTop: '1rem' }}>
            {meta.standards.map((s) => (
              <span className="chip" key={s}>
                {s}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
