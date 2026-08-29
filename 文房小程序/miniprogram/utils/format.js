function pad(n) {
  return n < 10 ? '0' + n : '' + n
}

function formatDate(d) {
  if (!d) return ''
  const date = d instanceof Date ? d : new Date(d)
  if (Number.isNaN(date.getTime())) return ''
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`
}

function formatDateTime(d) {
  if (!d) return ''
  const date = d instanceof Date ? d : new Date(d)
  if (Number.isNaN(date.getTime())) return ''
  return `${formatDate(date)} ${pad(date.getHours())}:${pad(date.getMinutes())}`
}

function formatMoney(yuan) {
  const n = Number(yuan)
  if (Number.isNaN(n)) return '0.00'
  return n.toFixed(2)
}

function txnTypeLabel(type) {
  const map = {
    recharge: '充值',
    deduct: '扣费',
    adjust: '调整',
    refund: '退款'
  }
  return map[type] || type
}

module.exports = {
  formatDate,
  formatDateTime,
  formatMoney,
  txnTypeLabel
}
