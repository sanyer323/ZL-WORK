const { cloud, ok, fail } = require('../common/db')

/** 正式环境需配置微信支付商户号，并在云开发控制台开通云支付 */
exports.main = async (event) => {
  const amount = Number(event.amount)
  if (!amount || amount <= 0) return fail('金额无效')

  return fail(
    '微信支付尚未配置。请先在云开发控制台绑定商户号，或暂时使用演示充值模式（settings.mockPay = true）',
    'PAY_NOT_CONFIGURED'
  )

  // 配置完成后可参考：
  // const res = await cloud.cloudPay.unifiedOrder({ ... })
  // return ok({ orderId: res.outTradeNo, payment: { timeStamp, nonceStr, package, signType, paySign } })
}
