const { callCloud, showError } = require('../../utils/api')
const { formatMoney, formatDateTime, txnTypeLabel } = require('../../utils/format')

Page({
  data: {
    loading: true,
    records: [],
    summary: { recharge: 0, deduct: 0 }
  },

  onShow() {
    this.loadRecords()
  },

  async loadRecords() {
    this.setData({ loading: true })
    try {
      const res = await callCloud('getRecords', { limit: 100 })
      this.setData({
        records: res.records || [],
        summary: res.summary || { recharge: 0, deduct: 0 },
        loading: false
      })
    } catch (err) {
      this.setData({ loading: false })
      showError(err)
    }
  },

  formatMoney,
  formatDateTime,
  txnTypeLabel
})
