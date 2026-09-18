const { callCloud, showError } = require('../../../utils/api')
const { formatMoney } = require('../../../utils/format')

Page({
  data: {
    students: [],
    loading: true,
    keyword: ''
  },

  onShow() {
    this.loadStudents()
  },

  onSearch(e) {
    this.setData({ keyword: e.detail.value })
    this.loadStudents()
  },

  async loadStudents() {
    this.setData({ loading: true })
    try {
      const res = await callCloud('adminGetStudents', { keyword: this.data.keyword })
      this.setData({ students: res.students || [], loading: false })
    } catch (err) {
      this.setData({ loading: false })
      showError(err)
    }
  },

  formatMoney
})
