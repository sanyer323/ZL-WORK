const { CLOUD_ENV_ID } = require('./config')

App({
  globalData: {
    userInfo: null,
    student: null,
    isAdmin: false,
    cloudReady: false
  },

  onLaunch() {
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上基础库以使用云能力')
      return
    }

    wx.cloud.init({
      env: CLOUD_ENV_ID,
      traceUser: true
    })

    this.globalData.cloudReady = true
    this.bootstrapSession()
  },

  async bootstrapSession() {
    try {
      const res = await wx.cloud.callFunction({ name: 'login' })
      const data = res.result || {}
      this.globalData.userInfo = data.userInfo || null
      this.globalData.student = data.student || null
      this.globalData.isAdmin = !!data.isAdmin
    } catch (err) {
      console.warn('登录初始化失败', err)
    }
  },

  async refreshProfile() {
    const res = await wx.cloud.callFunction({ name: 'getProfile' })
    const data = res.result || {}
    this.globalData.student = data.student || null
    this.globalData.isAdmin = !!data.isAdmin
    return data
  }
})
