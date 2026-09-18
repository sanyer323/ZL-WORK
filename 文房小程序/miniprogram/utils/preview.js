const { DEFAULT_CLASS_PRICE } = require('../config')

function todayStr() {
  const d = new Date()
  const p = n => (n < 10 ? '0' + n : '' + n)
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`
}

function enrich(student) {
  const classPrice = student.classPrice || DEFAULT_CLASS_PRICE
  const balance = Number(student.balance) || 0
  return {
    ...student,
    balance,
    classPrice,
    estimatedLessons: classPrice > 0 ? Math.floor(balance / classPrice) : 0
  }
}

const KEY = 'wenfang_preview_state'

function loadState() {
  try {
    const raw = wx.getStorageSync(KEY)
    if (raw && raw.student) return raw
  } catch (_) {}
  return {
    student: enrich({
      _id: 'preview-1',
      name: '张明远',
      phone: '13800001001',
      balance: 3000,
      classPrice: 150,
      totalClasses: 8,
      note: '预览模式 · 配置云开发后使用真实数据'
    }),
    checkedInToday: false,
    isAdmin: true,
    records: [],
    attendanceDates: []
  }
}

function saveState(state) {
  wx.setStorageSync(KEY, state)
}

function mockCall(name, data = {}) {
  const state = loadState()
  const now = new Date().toISOString()

  switch (name) {
    case 'login':
    case 'getProfile':
      return Promise.resolve({
        ok: true,
        student: enrich(state.student),
        isAdmin: state.isAdmin,
        checkedInToday: state.attendanceDates.includes(todayStr())
      })

    case 'getSettings':
      return Promise.resolve({ ok: true, mockPay: true })

    case 'bindStudent':
      state.student.name = data.name || state.student.name
      state.student.phone = data.phone || state.student.phone
      saveState(state)
      return Promise.resolve({ ok: true, student: enrich(state.student) })

    case 'recharge': {
      const amount = Number(data.amount) || 0
      state.student.balance += amount
      state.records.unshift({
        _id: 'r' + Date.now(),
        type: 'recharge',
        amount,
        title: '预览充值',
        createdAt: now
      })
      saveState(state)
      return Promise.resolve({ ok: true, student: enrich(state.student) })
    }

    case 'checkin': {
      const date = todayStr()
      if (state.attendanceDates.includes(date)) {
        return Promise.reject({ message: '今日已签到，请勿重复操作' })
      }
      const price = state.student.classPrice
      if (state.student.balance < price) {
        return Promise.reject({ message: '余额不足，请先充值' })
      }
      state.student.balance -= price
      state.student.totalClasses = (state.student.totalClasses || 0) + 1
      state.attendanceDates.push(date)
      state.records.unshift({
        _id: 'd' + Date.now(),
        type: 'deduct',
        amount: -price,
        title: `${date} 上课扣费`,
        createdAt: now
      })
      saveState(state)
      return Promise.resolve({ ok: true, student: enrich(state.student) })
    }

    case 'getRecords': {
      let recharge = 0
      let deduct = 0
      for (const r of state.records) {
        if (r.amount > 0) recharge += r.amount
        else deduct += Math.abs(r.amount)
      }
      return Promise.resolve({
        ok: true,
        records: state.records,
        summary: { recharge, deduct }
      })
    }

    case 'adminGetOverview':
      return Promise.resolve({
        ok: true,
        overview: {
          todayCheckins: state.attendanceDates.includes(todayStr()) ? 1 : 0,
          todayDeduct: state.attendanceDates.includes(todayStr()) ? state.student.classPrice : 0,
          todayRecharge: 0,
          totalStudents: 5,
          totalBalance: 10650,
          lowBalanceCount: 1
        }
      })

    case 'adminGetStudents':
      return Promise.resolve({
        ok: true,
        students: [
          enrich(state.student),
          enrich({ name: '李雨桐', phone: '13800001002', balance: 1200, classPrice: 150, totalClasses: 12 }),
          enrich({ name: '王梓涵', phone: '13800001003', balance: 450, classPrice: 150, totalClasses: 5 })
        ]
      })

    case 'adminGetStats':
      return Promise.resolve({
        ok: true,
        stats: {
          month: data.month || todayStr().slice(0, 7),
          checkinCount: state.student.totalClasses || 0,
          deductTotal: (state.student.totalClasses || 0) * state.student.classPrice,
          rechargeTotal: 3000,
          byStudent: [{ name: state.student.name, count: state.student.totalClasses || 0, amount: 0 }]
        }
      })

    case 'createPayment':
      return Promise.reject({ message: '预览模式请使用演示充值' })

    default:
      return Promise.resolve({ ok: true })
  }
}

module.exports = { mockCall, loadState }
