const { callCloud, showError } = require('../../../utils/api')
const { formatMoney } = require('../../../utils/format')

Page({
  data: {
    overview: null,
    loading: true
  },

  onShow() {
    this.loadOverview()
  },

  async loadOverview() {
    this.setData({ loading: true })
    try {
      const res = await callCloud('adminGetOverview')
      this.setData({ overview: res.overview, loading: false })
    } catch (err) {
      this.setData({ loading: false })
      showError(err, '无权限或加载失败')
      setTimeout(() => wx.navigateBack(), 1500)
    }
  },

  goStudents() {
    wx.navigateTo({ url: '/pages/admin/students/students' })
  },

  goStats() {
    wx.navigateTo({ url: '/pages/admin/stats/stats' })
  },

  formatMoney
})
