/** 部署时改为你的云环境 ID，在微信开发者工具 → 云开发控制台查看 */
const CLOUD_ENV_ID = 'your-cloud-env-id'

/** 未配置云环境时自动开启本地预览（模拟数据，仅开发者工具内有效） */
const PREVIEW_MODE = CLOUD_ENV_ID === 'your-cloud-env-id'

module.exports = {
  CLOUD_ENV_ID,
  PREVIEW_MODE,

  /** 单次课默认扣费（元），新学生未单独设置时使用 */
  DEFAULT_CLASS_PRICE: 150,

  /** 充值快捷金额（元） */
  RECHARGE_PRESETS: [500, 1000, 2000, 3000, 5000],

  /** 老板微信 openid 列表 — 也可在云数据库 settings 集合里配置 adminOpenids */
  ADMIN_OPENIDS: []
}
