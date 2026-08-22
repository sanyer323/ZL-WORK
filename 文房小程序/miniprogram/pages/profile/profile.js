const app = getApp()
const { callCloud, showError } = require('../../utils/api')
const { formatMoney } = require('../../utils/format')

Page({
  data: {
    student: null,
    isAdmin: false,
    bindForm: { name: '', phone: '' },
    binding: false
  },

  onShow() {
    this.setData({
      student: app.globalData.student,
      isAdmin: app.globalData.isAdmin
    })
    this.refresh()
  },

  async refresh() {
    try {
      const data = await callCloud('getProfile')
      app.globalData.student = data.student
      app.globalData.isAdmin = data.isAdmin
      this.setData({ student: data.student, isAdmin: data.isAdmin })
    } catch (err) {
      showError(err)
    }
  },

  onNameInput(e) {
    this.setData({ 'bindForm.name': e.detail.value })
  },

  onPhoneInput(e) {
    this.setData({ 'bindForm.phone': e.detail.value })
  },

  async onBind() {
    const { name, phone } = this.data.bindForm
    if (!name.trim()) {
      showError({ message: '请输入姓名' })
      return
    }
    this.setData({ binding: true })
    try {
      const res = await callCloud('bindStudent', { name: name.trim(), phone: phone.trim() })
      app.globalData.student = res.student
      wx.showToast({ title: '绑定成功', icon: 'success' })
      this.setData({ student: res.student, binding: false })
    } catch (err) {
      this.setData({ binding: false })
      showError(err, '绑定失败')
    }
  },

  goAdmin() {
    wx.navigateTo({ url: '/pages/admin/index/index' })
  },

  formatMoney
})
