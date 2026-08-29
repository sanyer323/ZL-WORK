const { getSettings, ok } = require('../common/db')

exports.main = async () => {
  const settings = await getSettings()
  return ok({
    mockPay: settings.mockPay !== false,
    defaultClassPrice: settings.defaultClassPrice || 150,
    studioName: settings.studioName || '文房书法'
  })
}
