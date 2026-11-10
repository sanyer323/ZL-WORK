# 流衡 FlowSize

过程工业工程计算软件（CONVAL 类能力方向）：**调节阀 + 差压节流装置**。

## 本版范围

| 模块 | 标准 / 依据 | 产品族参考 |
|------|-------------|------------|
| 调节阀 | IEC 60534-2-1 | 制造商中立 |
| 标准孔板 | ISO 5167-2 | 标准节流件 |
| 调整型孔板 | ISO 5167-1 + 标定 Cd | Toolkit / 平衡孔板 |
| 文丘里管 | ISO 5167-4 | PRESO SSL / LPL / CV |
| 文丘里喷嘴 | ISO 5167-3 | PRESO SSM |
| 楔形流量计 | ISO 5167-6 | PRESO COIN® |
| V 锥 | ISO 5167-5 | PRESO Cone |
| 均速管 | ASME MFC-12M + K | PRESO Ellipse® |
| 限流孔板 | 工程经验 / 阻塞流判据 | 单级/多级 RO |

## 技术路线

- **现在**：Web（React + TypeScript），计算引擎与 UI 分离
- **以后**：同一 `src/calc` 引擎嵌入桌面壳（Electron / Tauri）

## 开发

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # 输出 dist/
npm run preview    # 本地预览构建结果
npm run lint       # oxlint
```

## 部署与演示

### 本地演示

1. 进入本目录，执行 `npm install && npm run dev`
2. 浏览器打开终端提示的地址（默认 `http://localhost:5173`）
3. 首页为产品概览；侧边栏可进入各计算模块与「项目」归档页

### 静态站点部署

构建产物为纯静态文件，可部署到任意静态托管：

```bash
npm run build
# dist/ 目录即为可发布内容
```

| 平台 | 说明 |
|------|------|
| **Nginx / 对象存储** | 将 `dist/` 上传到站点根目录；SPA 需配置 `try_files $uri /index.html` |
| **GitHub Pages** | 构建后推送 `dist` 到 gh-pages 分支，或使用 Actions 自动部署 |
| **Vercel / Netlify** | 根目录设为 `计算软件`，构建命令 `npm run build`，输出目录 `dist` |

### 环境要求

- Node.js 18+（推荐 20 LTS）
- 无后端依赖；项目数据保存在浏览器 localStorage

### 产品入口

| 路由 | 说明 |
|------|------|
| `/` | 产品概览与模块卡片 |
| `/calc/:moduleId` | 各计算模块（如 `/calc/orifice`、`/calc/control-valve`） |
| `/projects` | 已保存的计算记录 |

## 工质库

自建公开参考物性，按过程工业常用场景分类（水/蒸汽、工业气、天然气与烃气、液态烃、燃料油、溶剂、酸碱、制冷剂、导热油、浆料、低温等），约百种量级；支持搜索与分组选择。气体计算可按 P/T 修正密度。正式交付请用实测或状态方程复核。

