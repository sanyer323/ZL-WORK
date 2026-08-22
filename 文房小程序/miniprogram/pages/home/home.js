const app = getApp()
const { callCloud, showError } = require('../../utils/api')
const { formatMoney, formatDateTime } = require('../../utils/format')

Page({
  data: {
    loading: true,
    student: null,
    isAdmin: false,
    classPrice: 150,
    checkedInToday: false,
    recentRecords: []
  },

  onShow() {
    this.loadData()
  },

  async loadData() {
    this.setData({ loading: true })
    try {
      const data = await callCloud('getProfile')
      app.globalData.student = data.student
      app.globalData.isAdmin = data.isAdmin

      const recordsRes = await callCloud('getRecords', { limit: 5 })
      this.setData({
        student: data.student,
        isAdmin: data.isAdmin,
        classPrice: data.student?.classPrice || 150,
        checkedInToday: !!data.checkedInToday,
        recentRecords: recordsRes.records || [],
        loading: false
      })
    } catch (err) {
      this.setData({ loading: false })
      showError(err, '加载失败')
    }
  },

  goRecharge() {
    wx.navigateTo({ url: '/pages/recharge/recharge' })
  },

  goCheckin() {
    wx.switchTab({ url: '/pages/checkin/checkin' })
  },

  goRecords() {
    wx.switchTab({ url: '/pages/records/records' })
  },

  goAdmin() {
    wx.navigateTo({ url: '/pages/admin/index/index' })
  },

  formatMoney,
  formatDateTime
})
