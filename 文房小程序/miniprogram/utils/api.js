const { PREVIEW_MODE } = require('../config')
const { mockCall } = require('./preview')

/** 等待 App 启动完成，避免首页 onShow 时 session 尚未就绪 */
function waitForAppReady(app, timeoutMs = 5000) {
  if (app.globalData.sessionReady) {
    return Promise.resolve()
  }
  return new Promise(resolve => {
    const start = Date.now()
    const tick = () => {
      if (app.globalData.sessionReady || Date.now() - start > timeoutMs) {
        resolve()
        return
      }
      setTimeout(tick, 50)
    }
    tick()
  })
}

async function callCloud(name, data = {}) {
  const app = getApp()

  if (PREVIEW_MODE || app.globalData.previewMode) {
    return mockCall(name, data).then(result => {
      if (result.ok === false) {
        const err = new Error(result.message || '操作失败')
        err.code = result.code
        throw err
      }
      return result
    })
  }

  await waitForAppReady(app)

  if (!wx.cloud) {
    throw new Error('当前环境不支持云开发，请开启预览模式或升级基础库')
  }

  return wx.cloud.callFunction({ name, data }).then(res => {
    const result = res.result || {}
    if (result.ok === false) {
      const err = new Error(result.message || '操作失败')
      err.code = result.code
      throw err
    }
    return result
  })
}

function showError(err, fallback = '操作失败') {
  wx.showToast({
    title: (err && err.message) || fallback,
    icon: 'none',
    duration: 2500
  })
}

function confirm(content) {
  return new Promise(resolve => {
    wx.showModal({
      title: '确认',
      content,
      success: res => resolve(!!res.confirm)
    })
  })
}

function showBalanceHint(balance, classPrice) {
  const { formatMoney } = require('./format')
  const lessons = classPrice > 0 ? Math.floor(balance / classPrice) : 0
  return `余额 ¥${formatMoney(balance)}，约可上 ${lessons} 次课（¥${formatMoney(classPrice)}/次）`
}

module.exports = {
  callCloud,
  showError,
  confirm,
  showBalanceHint,
  waitForAppReady
}
