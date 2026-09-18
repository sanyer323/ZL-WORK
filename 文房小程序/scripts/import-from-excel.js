#!/usr/bin/env node
/**
 * 从 Excel / CSV 导入学员到云数据库（通过 seedStudents 云函数）
 *
 * 用法：
 *   cd 文房小程序/scripts
 *   npm install
 *   node import-from-excel.js ../data/你的表格.xlsx
 *   node import-from-excel.js "C:/Users/sanye/Downloads/文房/学员.xlsx"
 *
 * 需先在微信开发者工具中登录，并配置 CLOUD_ENV 与 ADMIN_OPENID（见 README）
 */

const fs = require('fs')
const path = require('path')
const XLSX = require('xlsx')

const COLUMN_MAP = {
  name: ['姓名', '名字', '学员', '学生', 'name'],
  phone: ['手机', '电话', '手机号', 'phone', '联系电话'],
  balance: ['余额', '剩余', '剩余金额', '账户余额', 'balance', '预存'],
  classPrice: ['课费', '单价', '每次', '单次', 'classPrice', '课时费'],
  totalClasses: ['已上课', '上课次数', '次数', 'totalClasses', '累计课时'],
  note: ['备注', '说明', '班级', 'note', '班型']
}

function pickColumn(row, keys) {
  for (const k of Object.keys(row)) {
    const norm = String(k).trim()
    if (keys.some(alias => norm === alias || norm.includes(alias))) {
      return row[k]
    }
  }
  return undefined
}

function num(v) {
  const n = Number(v)
  return Number.isFinite(n) ? n : undefined
}

function parseRow(row) {
  const name = pickColumn(row, COLUMN_MAP.name)
  if (!name) return null
  return {
    name: String(name).trim(),
    phone: String(pickColumn(row, COLUMN_MAP.phone) || '').trim(),
    balance: num(pickColumn(row, COLUMN_MAP.balance)),
    classPrice: num(pickColumn(row, COLUMN_MAP.classPrice)),
    totalClasses: num(pickColumn(row, COLUMN_MAP.totalClasses)),
    note: String(pickColumn(row, COLUMN_MAP.note) || '').trim()
  }
}

function loadRows(filePath) {
  const ext = path.extname(filePath).toLowerCase()
  if (ext === '.json') {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'))
  }
  const wb = XLSX.readFile(filePath)
  const sheet = wb.Sheets[wb.SheetNames[0]]
  return XLSX.utils.sheet_to_json(sheet, { defval: '' })
}

function main() {
  const file = process.argv[2]
  if (!file) {
    console.error('请指定 Excel/CSV/JSON 文件路径')
    process.exit(1)
  }

  const abs = path.resolve(file)
  if (!fs.existsSync(abs)) {
    console.error('文件不存在:', abs)
    process.exit(1)
  }

  const raw = loadRows(abs)
  const students = raw.map(parseRow).filter(Boolean)

  console.log(`解析到 ${students.length} 条学员记录：`)
  console.log(JSON.stringify(students, null, 2))
  console.log('\n--- 下一步 ---')
  console.log('1. 在微信开发者工具 → 云开发 → 数据库，确认 collections: students, transactions, attendance, settings')
  console.log('2. 部署 cloudfunctions/seedStudents')
  console.log('3. 在控制台调用 seedStudents，传入 { students: 上述JSON }')
  console.log('   或将 students 写入 data/import-payload.json 后使用云开发 CLI 调用')
}

main()
