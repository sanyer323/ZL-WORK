const { CLOUD_ENV_ID, PREVIEW_MODE } = require('./config')

function shouldUsePreview() {
  return PREVIEW_MODE || !CLOUD_ENV_ID || CLOUD_ENV_ID === 'your-cloud-env-id'
}

App({
  globalData: {
    userInfo: null,
    student: null,
    isAdmin: false,
    cloudReady: false,
    sessionReady: false,
    previewMode: shouldUsePreview(),
    loadError: ''
  },

  onLaunch() {
    this.bootstrapSession()
  },

  async bootstrapSession() {
    const usePreview = shouldUsePreview()
    this.globalData.previewMode = usePreview

    if (usePreview) {
      console.info('[文房] 本地预览模式：使用模拟数据')
      this.globalData.cloudReady = true
      try {
        const data = await require('./utils/preview').mockCall('login')
        this.globalData.student = data.student || null
        this.globalData.isAdmin = !!data.isAdmin
      } catch (err) {
        console.warn('预览数据加载失败', err)
        this.globalData.loadError = '预览数据加载失败'
      }
      this.globalData.sessionReady = true
      return
    }

    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上基础库以使用云能力')
      this.globalData.loadError = '不支持云开发'
      this.globalData.sessionReady = true
      return
    }

    try {
      wx.cloud.init({ env: CLOUD_ENV_ID, traceUser: true })
      this.globalData.cloudReady = true
      const res = await wx.cloud.callFunction({ name: 'login' })
      const data = res.result || {}
      this.globalData.student = data.student || null
      this.globalData.isAdmin = !!data.isAdmin
    } catch (err) {
      console.warn('云开发登录失败，回退预览模式', err)
      this.globalData.previewMode = true
      this.globalData.loadError = '云开发未就绪，已切换预览数据'
      try {
        const data = await require('./utils/preview').mockCall('login')
        this.globalData.student = data.student || null
        this.globalData.isAdmin = !!data.isAdmin
      } catch (_) {}
    }

    this.globalData.sessionReady = true
  },

  async refreshProfile() {
    if (this.globalData.previewMode) {
      const data = await require('./utils/preview').mockCall('getProfile')
      this.globalData.student = data.student || null
      this.globalData.isAdmin = !!data.isAdmin
      return data
    }
    const res = await wx.cloud.callFunction({ name: 'getProfile' })
    const data = res.result || {}
    this.globalData.student = data.student || null
    this.globalData.isAdmin = !!data.isAdmin
    return data
  }
})
