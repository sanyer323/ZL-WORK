/** 流衡 FlowSize 计算书（CDS）— 参照市售 Rosemount / 节流装置计算书版式 */

export interface SheetCell {
  label: string
  value: string
}

export interface SheetBlock {
  /** 区块标题，如「工艺输入」「计算结果」 */
  title: string
  cells: SheetCell[]
}

export interface CalcSheet {
  /** 文档主标题 */
  docTitle: string
  /** 产品线副标题 */
  productLine: string
  /** 计算书抬头品牌（厂家名）；空则显示流衡 FlowSize */
  brandName?: string
  moduleName: string
  standards: string
  tag: string
  project: string
  date: string
  blocks: SheetBlock[]
  notes: string[]
  warnings: string[]
}

export type ReportRow = { section: string; item: string; value: string }

/** 兼容旧扁平行 → CDS 区块（双列配对） */
export function rowsToSheet(
  rows: ReportRow[],
  meta: {
    docTitle: string
    productLine?: string
    moduleName: string
    standards: string
    tag?: string
    project?: string
  },
): CalcSheet {
  const order: string[] = []
  const map = new Map<string, SheetCell[]>()
  for (const r of rows) {
    if (!map.has(r.section)) {
      map.set(r.section, [])
      order.push(r.section)
    }
    map.get(r.section)!.push({ label: r.item, value: r.value })
  }
  return {
    docTitle: meta.docTitle,
    productLine: meta.productLine ?? 'Calculation Data Sheet',
    moduleName: meta.moduleName,
    standards: meta.standards,
    tag: meta.tag ?? '—',
    project: meta.project ?? '—',
    date: new Date().toLocaleString('zh-CN'),
    blocks: order.map((title) => ({ title, cells: map.get(title)! })),
    notes: [],
    warnings: [],
  }
}

export function downloadTextFile(filename: string, content: string, mime: string) {
  const blob = new Blob([content], { type: mime })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  a.click()
  URL.revokeObjectURL(url)
}

function escapeHtml(s: string) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

/** 将 cells 排成 4 列：Label | Value | Label | Value */
function pairRowsHtml(cells: SheetCell[]): string {
  const rows: string[] = []
  for (let i = 0; i < cells.length; i += 2) {
    const a = cells[i]
    const b = cells[i + 1]
    rows.push(`<tr>
      <td class="k">${escapeHtml(a.label)}</td>
      <td class="v">${escapeHtml(a.value)}</td>
      <td class="k">${b ? escapeHtml(b.label) : ''}</td>
      <td class="v">${b ? escapeHtml(b.value) : ''}</td>
    </tr>`)
  }
  return rows.join('')
}

function sheetCss(): string {
  return `
@page { size: A4; margin: 10mm 12mm; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: "Segoe UI", "Microsoft YaHei", "Noto Sans SC", sans-serif;
  color: #1a2428;
  font-size: 9pt;
  line-height: 1.22;
  background: #fff;
}
.sheet { width: 100%; max-width: 190mm; margin: 0 auto; }
.hdr {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  align-items: end;
  border-bottom: 2.5px solid #0b3a4a;
  padding-bottom: 5px;
  margin-bottom: 6px;
}
.brand {
  font-size: 15pt;
  font-weight: 700;
  color: #0b3a4a;
  letter-spacing: 0.02em;
  margin: 0;
}
.brand small {
  display: block;
  font-size: 7.5pt;
  font-weight: 500;
  color: #4a6670;
  margin-top: 1px;
  letter-spacing: 0.03em;
}
.doc-meta {
  text-align: right;
  font-size: 8pt;
  color: #334;
}
.doc-meta strong { color: #0b3a4a; font-size: 10pt; }
.banner {
  background: #0b3a4a;
  color: #e8f1f0;
  font-size: 8pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 7px;
  margin: 0;
}
table.kv {
  width: 100%;
  border-collapse: collapse;
  margin: 0 0 5px;
  table-layout: fixed;
}
table.kv col.k { width: 18%; }
table.kv col.v { width: 32%; }
table.kv td {
  border: 1px solid #b8c9c6;
  padding: 2px 5px;
  vertical-align: middle;
}
table.kv td.k {
  background: #eef4f3;
  color: #3d5258;
  font-size: 7.5pt;
  font-weight: 600;
}
table.kv td.v {
  font-family: Consolas, "Courier New", monospace;
  font-size: 8pt;
  font-weight: 500;
  color: #0b3a4a;
  word-break: break-all;
}
.head-grid {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 6px;
  table-layout: fixed;
}
.head-grid td {
  border: 1px solid #b8c9c6;
  padding: 2px 5px;
  font-size: 8pt;
}
.head-grid td.k { background: #eef4f3; font-weight: 600; width: 14%; color: #3d5258; }
.head-grid td.v { width: 36%; font-family: Consolas, monospace; color: #0b3a4a; }
.warn { color: #a65d1a; }
.sign {
  width: 100%;
  border-collapse: collapse;
  margin-top: 8px;
  table-layout: fixed;
}
.sign td {
  border: 1px solid #b8c9c6;
  padding: 6px 8px;
  font-size: 8pt;
  vertical-align: top;
  height: 28px;
}
.sign td.lab {
  background: #eef4f3;
  font-weight: 600;
  width: 12%;
  color: #3d5258;
}
.sign td.val { width: 21.3%; }
.foot {
  margin-top: 4px;
  font-size: 7pt;
  color: #778;
  text-align: right;
}
@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .no-print { display: none !important; }
}
.toolbar {
  margin: 8px 0 12px;
  display: flex;
  gap: 8px;
}
.toolbar button {
  font: inherit;
  font-size: 9pt;
  padding: 6px 12px;
  border: 1px solid #0b3a4a;
  background: #0b3a4a;
  color: #fff;
  border-radius: 3px;
  cursor: pointer;
}
`
}

function renderSheetBody(sheet: CalcSheet): string {
  const head = `<table class="head-grid">
    <tr>
      <td class="k">模块</td><td class="v">${escapeHtml(sheet.moduleName)}</td>
      <td class="k">位号 Tag</td><td class="v">${escapeHtml(sheet.tag)}</td>
    </tr>
    <tr>
      <td class="k">项目</td><td class="v">${escapeHtml(sheet.project)}</td>
      <td class="k">日期</td><td class="v">${escapeHtml(sheet.date)}</td>
    </tr>
    <tr>
      <td class="k">计算依据</td><td class="v" colspan="3">${escapeHtml(sheet.standards)}</td>
    </tr>
  </table>`

  const blocks = sheet.blocks
    .map(
      (b) => `
      <div class="banner">${escapeHtml(b.title)}</div>
      <table class="kv">
        <colgroup><col class="k"/><col class="v"/><col class="k"/><col class="v"/></colgroup>
        ${pairRowsHtml(b.cells)}
      </table>`,
    )
    .join('')

  // 参照市售节流装置计算书：备注栏 + 签核；有工程警告时写入备注，不另附说明小字
  const remarkItems = [...sheet.warnings, ...sheet.notes]
  const remarkHtml = remarkItems.length
    ? `<ul class="warn" style="margin:0;padding-left:14px">${remarkItems.map((n) => `<li>${escapeHtml(n)}</li>`).join('')}</ul>`
    : '&nbsp;'

  const sign = `<table class="sign">
    <tr>
      <td class="lab">备注</td>
      <td class="val" colspan="5">${remarkHtml}</td>
    </tr>
    <tr>
      <td class="lab">计算者</td><td class="val"></td>
      <td class="lab">核验者</td><td class="val"></td>
      <td class="lab">日期</td><td class="val">${escapeHtml(sheet.date)}</td>
    </tr>
  </table>
  <div class="foot">Printed On: ${escapeHtml(sheet.date)}</div>`

  return `${head}${blocks}${sign}`
}

function sheetChrome(sheet: CalcSheet): string {
  const brand = sheet.brandName?.trim()
    ? escapeHtml(sheet.brandName)
    : '流衡 FlowSize'
  const sub = sheet.brandName?.trim()
    ? escapeHtml(sheet.productLine || '流衡 FlowSize · 按样本系数计算')
    : escapeHtml(sheet.productLine)
  return `<div class="sheet">
  <div class="hdr">
    <div>
      <p class="brand">${brand}<small>${sub}</small></p>
    </div>
    <div class="doc-meta"><strong>${escapeHtml(sheet.docTitle)}</strong><br/>Calculation Report</div>
  </div>
  ${renderSheetBody(sheet)}
</div>`
}

/** 导出 Excel（HTML .xls，紧凑四列表格） */
export function exportExcelSheet(filenameBase: string, sheet: CalcSheet) {
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8" />
<title>${escapeHtml(sheet.docTitle)}</title>
<style>${sheetCss()}</style></head><body>
${sheetChrome(sheet)}
</body></html>`
  downloadTextFile(`${filenameBase}.xls`, html, 'application/vnd.ms-excel;charset=utf-8')
}

/** 导出 CSV（扁平备份） */
export function exportExcelCsv(filenameBase: string, sheet: CalcSheet) {
  const lines = ['分组,项目,数值']
  for (const b of sheet.blocks) {
    for (const c of b.cells) {
      lines.push(
        [b.title, c.label, c.value]
          .map((x) => `"${String(x).replace(/"/g, '""')}"`)
          .join(','),
      )
    }
  }
  downloadTextFile(`${filenameBase}.csv`, `\uFEFF${lines.join('\r\n')}`, 'text/csv;charset=utf-8')
}

/** PDF：打开紧凑 CDS 打印页 */
export function exportPdfSheet(sheet: CalcSheet) {
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8" />
<title>${escapeHtml(sheet.docTitle)}</title>
<style>${sheetCss()}</style></head><body>
<div class="toolbar no-print">
  <button type="button" onclick="window.print()">打印 / 另存为 PDF</button>
  <button type="button" onclick="window.close()" style="background:#fff;color:#0b3a4a">关闭</button>
</div>
${sheetChrome(sheet)}
<script>window.onload=function(){setTimeout(function(){window.print()},200)}</script>
</body></html>`

  const w = window.open('', '_blank')
  if (!w) {
    alert('浏览器拦截了弹窗，请允许本站弹窗后再导出 PDF')
    return
  }
  w.document.open()
  w.document.write(html)
  w.document.close()
}

/** @deprecated 兼容旧调用 */
export function exportExcelHtml(filenameBase: string, title: string, rows: ReportRow[]) {
  exportExcelSheet(
    filenameBase,
    rowsToSheet(rows, { docTitle: title, moduleName: title, standards: '—' }),
  )
}

export function exportPdfPrint(title: string, _meta: string, rows: ReportRow[]) {
  exportPdfSheet(
    rowsToSheet(rows, { docTitle: title, moduleName: title, standards: '—' }),
  )
}
