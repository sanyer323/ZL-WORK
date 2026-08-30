# 流衡助手 P0 Demo

浏览器原型：**Station（工厂问答）** 与 **Pocket（备忘）** 共用同一页面，验证双产品线交互。

## 运行

```bash
cd AI助手/p0-demo
python3 -m http.server 8765
```

打开 **http://localhost:8765**（需 Chrome / Edge，支持 Web Speech API）。

## 能力

| 功能 | P0 状态 |
|------|---------|
| 文字对话 | ✓ |
| 按住说话（浏览器 STT） | ✓ |
| TTS 朗读回复 | ✓ |
| FAQ 匹配（10 条，来自 ZL-WORK） | ✓ |
| Pocket 备忘「记一下：…」 | ✓ localStorage |
| LLM 增强 | 可选，见下 |

## 可选：接入 LLM

```bash
cp config.example.json config.json
# 编辑 config.json：enabled=true，填入 apiKey
```

`config.json` 已加入 `.gitignore`，勿提交密钥。

## 演示问题

- PH02 两级孔板推荐孔径是多少？
- 3051CD 推荐型号是什么？
- FY301 压电正常工作电压范围？
- Pocket 模式：记一下：下周更新 FlowSize 限流孔板模块

## 下一步（P1）

- FastAPI 后端 + 向量 RAG
- Station 平板全屏 kiosk 模式
- Pocket ESP32 + BLE 桥（见 [../技术选型.md](../技术选型.md)）
