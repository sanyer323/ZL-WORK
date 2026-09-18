const app = getApp()
const { callCloud, showError, waitForAppReady } = require('../../utils/api')

Page({
  data: {
    loading: true,
    previewMode: false,
    loadError: '',
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
    this.setData({ loading: true, loadError: '' })

    try {
      await waitForAppReady(app)

      const previewMode = app.globalData.previewMode
      const data = await callCloud('getProfile')

      app.globalData.student = data.student
      app.globalData.isAdmin = data.isAdmin

      let recentRecords = []
      if (data.student) {
        const recordsRes = await callCloud('getRecords', { limit: 5 })
        recentRecords = recordsRes.records || []
      }

      this.setData({
        previewMode,
        loadError: app.globalData.loadError || '',
        student: data.student || null,
        isAdmin: !!data.isAdmin,
        classPrice: data.student?.classPrice || 150,
        checkedInToday: !!data.checkedInToday,
        recentRecords,
        loading: false
      })
    } catch (err) {
      this.setData({
        loading: false,
        loadError: (err && err.message) || '加载失败',
        previewMode: app.globalData.previewMode,
        student: app.globalData.student || null
      })
      showError(err, '加载失败')
    }
  },

  goBind() {
    wx.switchTab({ url: '/pages/profile/profile' })
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
  }
})
