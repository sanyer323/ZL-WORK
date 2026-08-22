const { CLOUD_ENV_ID, PREVIEW_MODE } = require('./config')

App({
  globalData: {
    userInfo: null,
    student: null,
    isAdmin: false,
    cloudReady: false,
    previewMode: PREVIEW_MODE
  },

  onLaunch() {
    if (PREVIEW_MODE) {
      console.info('[文房] 本地预览模式：未配置云环境，使用模拟数据')
      this.globalData.cloudReady = true
      this.bootstrapSession()
      return
    }

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
      const res = PREVIEW_MODE
        ? await require('./utils/preview').mockCall('login')
        : (await wx.cloud.callFunction({ name: 'login' })).result
      const data = res || {}
      this.globalData.userInfo = data.userInfo || null
      this.globalData.student = data.student || null
      this.globalData.isAdmin = !!data.isAdmin
    } catch (err) {
      console.warn('登录初始化失败', err)
    }
  },

  async refreshProfile() {
    const res = PREVIEW_MODE
      ? await require('./utils/preview').mockCall('getProfile')
      : (await wx.cloud.callFunction({ name: 'getProfile' })).result
    const data = res || {}
    this.globalData.student = data.student || null
    this.globalData.isAdmin = !!data.isAdmin
    return data
  }
})
