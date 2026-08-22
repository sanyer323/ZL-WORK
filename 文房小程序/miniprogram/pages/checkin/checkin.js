const app = getApp()
const { callCloud, showError, confirm, showBalanceHint } = require('../../utils/api')
const { formatMoney, formatDate } = require('../../utils/format')

Page({
  data: {
    loading: true,
    student: null,
    classPrice: 150,
    checkedInToday: false,
    checking: false,
    today: formatDate(new Date())
  },

  onShow() {
    this.loadData()
  },

  async loadData() {
    this.setData({ loading: true })
    try {
      const data = await callCloud('getProfile')
      this.setData({
        student: data.student,
        classPrice: data.student?.classPrice || 150,
        checkedInToday: !!data.checkedInToday,
        loading: false
      })
    } catch (err) {
      this.setData({ loading: false })
      showError(err)
    }
  },

  async onCheckin() {
    if (!this.data.student) {
      showError({ message: '尚未绑定学员，请联系老师' })
      return
    }
    if (this.data.checkedInToday) {
      wx.showToast({ title: '今日已签到', icon: 'none' })
      return
    }
    if (this.data.student.balance < this.data.classPrice) {
      wx.showModal({
        title: '余额不足',
        content: showBalanceHint(this.data.student.balance, this.data.classPrice) + '，是否去充值？',
        confirmText: '去充值',
        success: res => {
          if (res.confirm) wx.navigateTo({ url: '/pages/recharge/recharge' })
        }
      })
      return
    }

    const ok = await confirm(
      `确认今日到课？将扣费 ¥${formatMoney(this.data.classPrice)}，扣后余额约 ¥${formatMoney(this.data.student.balance - this.data.classPrice)}`
    )
    if (!ok) return

    this.setData({ checking: true })
    try {
      const res = await callCloud('checkin')
      app.globalData.student = res.student
      wx.showToast({ title: '签到成功', icon: 'success' })
      this.setData({
        student: res.student,
        checkedInToday: true,
        checking: false
      })
    } catch (err) {
      this.setData({ checking: false })
      showError(err, '签到失败')
    }
  },

  formatMoney
})
