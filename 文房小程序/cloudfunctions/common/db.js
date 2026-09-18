const cloud = require('wx-server-sdk')

cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

const db = cloud.database()
const _ = db.command

const COL = {
  students: 'students',
  transactions: 'transactions',
  attendance: 'attendance',
  settings: 'settings'
}

async function getSettings() {
  const res = await db.collection(COL.settings).limit(1).get()
  if (res.data.length) return res.data[0]
  return {
    adminOpenids: [],
    mockPay: true,
    defaultClassPrice: 150,
    studioName: '文房书法'
  }
}

async function isAdmin(openid) {
  const settings = await getSettings()
  return (settings.adminOpenids || []).includes(openid)
}

function enrichStudent(student) {
  if (!student) return null
  const classPrice = student.classPrice || 150
  const balance = Number(student.balance) || 0
  return {
    ...student,
    balance,
    classPrice,
    estimatedLessons: classPrice > 0 ? Math.floor(balance / classPrice) : 0
  }
}

function todayStr(date = new Date()) {
  const y = date.getFullYear()
  const m = String(date.getMonth() + 1).padStart(2, '0')
  const d = String(date.getDate()).padStart(2, '0')
  return `${y}-${m}-${d}`
}

function ok(data = {}) {
  return { ok: true, ...data }
}

function fail(message, code = 'ERROR') {
  return { ok: false, message, code }
}

module.exports = {
  cloud,
  db,
  _,
  COL,
  getSettings,
  isAdmin,
  enrichStudent,
  todayStr,
  ok,
  fail
}
