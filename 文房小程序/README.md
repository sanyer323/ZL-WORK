# 文房书法 · 微信小程序

书法培训机构自助缴费与上课签到系统。学生用微信打开小程序即可 **充值**、**到课签到自动扣费**；老板在后台查看学员余额与统计，**无需手工记账**。

## 功能

| 角色 | 功能 |
|------|------|
| 学生 | 绑定档案、微信充值（或演示充值）、到课一键签到扣费、消费明细 |
| 老板 | 今日签到/充值概况、学员列表与余额预警、月度上课统计 |

## 技术方案

- **前端**：原生微信小程序
- **后端**：微信云开发（云函数 + 云数据库）
- **支付**：微信支付（可先用 `mockPay` 演示模式，不配商户号也能体验流程）

## 快速开始

### 1. 注册小程序

1. 登录 [微信公众平台](https://mp.weixin.qq.com/) 注册小程序
2. 获取 **AppID**，写入 `project.config.json` 的 `appid` 字段

### 2. 开通云开发

1. 用 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html) 打开本目录 `文房小程序/`
2. 点击「云开发」→ 创建环境 → 复制 **环境 ID**
3. 写入 `miniprogram/config.js` → `CLOUD_ENV_ID`

### 3. 创建数据库集合

在云开发控制台 → 数据库，新建集合：

- `students` — 学员档案（姓名、手机、余额、课费、openid）
- `transactions` — 充值/扣费流水
- `attendance` — 签到记录（按日）
- `settings` — 全局配置（见下方初始化文档）

建议为 `attendance` 添加组合索引：`openid + date`。

### 4. 部署云函数

在微信开发者工具中，右键 `cloudfunctions` 下每个文件夹 → **上传并部署：云端安装依赖**。

必需云函数：`login`、`getProfile`、`getSettings`、`bindStudent`、`recharge`、`checkin`、`getRecords`、`adminGetOverview`、`adminGetStudents`、`adminGetStats`、`seedStudents`。

### 5. 初始化 settings（老板权限）

在 `settings` 集合手动添加一条记录：

```json
{
  "studioName": "文房书法",
  "defaultClassPrice": 150,
  "mockPay": true,
  "adminOpenids": ["你的微信openid"]
}
```

**获取 openid**：部署 `login` 后，在小程序「我的」页面临时加日志，或在云函数日志中查看 `login` 返回的 openid。老板微信 openid 填入 `adminOpenids` 后即可进入「老板后台」。

### 6. 导入学员（来自「文房」文件夹）

您本地的 `C:\Users\sanye\Downloads\文房` 无法直接被云端读取，请：

**方式 A — Excel 解析（推荐）**

```bash
cd 文房小程序/scripts
npm install
node import-from-excel.js "C:/Users/sanye/Downloads/文房/你的表格.xlsx"
```

脚本会输出 JSON。然后在云开发控制台 → 云函数 → `seedStudents` → 测试，传入：

```json
{ "students": [ /* 粘贴解析结果 */ ] }
```

**方式 B — 使用示例数据试跑**

`data/sample-students.json` 含 5 名示例学员，可先导入验证流程，再用真实表格覆盖。

**支持的表格列名（自动识别）**

| 字段 | 可识别列名 |
|------|-----------|
| 姓名 | 姓名、名字、学员、学生 |
| 手机 | 手机、电话、手机号 |
| 余额 | 余额、剩余、预存、账户余额 |
| 课费 | 课费、单价、单次、课时费 |
| 已上课 | 已上课、次数、累计课时 |
| 备注 | 备注、说明、班级 |

### 7. 学生使用流程

1. 打开小程序 → 「我的」→ 输入报名时姓名（+ 手机）→ **绑定**
2. 「充值」→ 选择金额（演示模式下直接到账）
3. 每次到课 → 「签到」→ 确认扣费

### 8. 启用真实微信支付（可选）

1. 开通微信支付商户号，并与小程序 AppID 绑定
2. 云开发控制台 → 设置 → 微信支付 → 绑定商户号
3. 将 `settings.mockPay` 设为 `false`
4. 完善 `cloudfunctions/createPayment/index.js` 中的 `cloud.cloudPay.unifiedOrder` 调用

## 目录结构

```
文房小程序/
├── miniprogram/          # 小程序页面
├── cloudfunctions/       # 云函数
├── data/                 # 示例学员 JSON
├── scripts/              # Excel 导入工具
├── project.config.json
└── README.md
```

## 常见问题

**Q: 学生绑定提示找不到档案？**  
A: 先用 `seedStudents` 导入学员；姓名需与表格一致。

**Q: 同一天能签两次吗？**  
A: 不能，同一 openid 每天仅允许签到一次。

**Q: 余额不足能签到吗？**  
A: 不能，需先充值。

---

如需把「文房」文件夹里的真实表格导入，请将 Excel/CSV **上传到本仓库 `文房小程序/data/`** 或发给我列名截图，我可帮您调整导入脚本字段映射。
