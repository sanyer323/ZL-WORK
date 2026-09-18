const { RECHARGE_PRESETS } = require('../../config')
const { callCloud, showError, confirm } = require('../../utils/api')
const { formatMoney } = require('../../utils/format')

Page({
  data: {
    presets: RECHARGE_PRESETS,
    selected: 1000,
    customAmount: '',
    paying: false,
    mockMode: true
  },

  onLoad() {
    this.checkPayMode()
  },

  async checkPayMode() {
    try {
      const res = await callCloud('getSettings')
      this.setData({ mockMode: !!res.mockPay })
    } catch (_) {
      this.setData({ mockMode: true })
    }
  },

  selectPreset(e) {
    this.setData({ selected: Number(e.currentTarget.dataset.amount), customAmount: '' })
  },

  onCustomInput(e) {
    const v = e.detail.value
    this.setData({ customAmount: v, selected: 0 })
  },

  getAmount() {
    if (this.data.customAmount) {
      return Number(this.data.customAmount)
    }
    return this.data.selected
  },

  async onPay() {
    const amount = this.getAmount()
    if (!amount || amount <= 0) {
      showError({ message: '请输入有效金额' })
      return
    }
    if (amount > 50000) {
      showError({ message: '单次充值不超过 50000 元' })
      return
    }

    const ok = await confirm(`确认充值 ¥${formatMoney(amount)} ？`)
    if (!ok) return

    this.setData({ paying: true })
    try {
      if (this.data.mockMode) {
        await callCloud('recharge', { amount, channel: 'mock' })
        wx.showToast({ title: '充值成功', icon: 'success' })
        setTimeout(() => wx.navigateBack(), 1200)
        return
      }

      const order = await callCloud('createPayment', { amount })
      await wx.requestPayment({
        ...order.payment
      })
      await callCloud('recharge', { amount, channel: 'wxpay', orderId: order.orderId })
      wx.showToast({ title: '充值成功', icon: 'success' })
      setTimeout(() => wx.navigateBack(), 1200)
    } catch (err) {
      if (err.errMsg && err.errMsg.includes('cancel')) return
      showError(err, '充值失败')
    } finally {
      this.setData({ paying: false })
    }
  },

  formatMoney
})
