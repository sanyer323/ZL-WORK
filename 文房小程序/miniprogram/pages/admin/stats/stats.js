const { callCloud, showError } = require('../../../utils/api')
const { formatMoney } = require('../../../utils/format')

Page({
  data: {
    month: '',
    stats: null,
    loading: true
  },

  onLoad() {
    const d = new Date()
    const month = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`
    this.setData({ month })
  },

  onShow() {
    this.loadStats()
  },

  onMonthChange(e) {
    this.setData({ month: e.detail.value })
    this.loadStats()
  },

  async loadStats() {
    this.setData({ loading: true })
    try {
      const res = await callCloud('adminGetStats', { month: this.data.month })
      this.setData({ stats: res.stats, loading: false })
    } catch (err) {
      this.setData({ loading: false })
      showError(err)
    }
  },

  formatMoney
})
