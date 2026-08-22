const { formatMoney } = require('./format')

function callCloud(name, data = {}) {
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
  const lessons = classPrice > 0 ? Math.floor(balance / classPrice) : 0
  return `余额 ¥${formatMoney(balance)}，约可上 ${lessons} 次课（¥${formatMoney(classPrice)}/次）`
}

module.exports = {
  callCloud,
  showError,
  confirm,
  showBalanceHint
}
