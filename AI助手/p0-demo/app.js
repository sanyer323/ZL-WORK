/**
 * 流衡助手 P0 — FAQ 匹配 + 可选 LLM + 备忘（Pocket）
 */
const state = {
  mode: 'station',
  faq: [],
  config: null,
  memos: [],
  listening: false,
  recognition: null,
}

const $ = (sel) => document.querySelector(sel)

async function loadFaq() {
  const res = await fetch('knowledge/faq.json')
  state.faq = await res.json()
}

async function loadConfig() {
  try {
    const res = await fetch('config.json')
    if (res.ok) state.config = await res.json()
  } catch {
    state.config = null
  }
}

function loadMemos() {
  try {
    state.memos = JSON.parse(localStorage.getItem('liheng-memos') || '[]')
  } catch {
    state.memos = []
  }
  renderMemos()
}

function saveMemos() {
  localStorage.setItem('liheng-memos', JSON.stringify(state.memos))
  renderMemos()
}

function normalize(s) {
  return s.toLowerCase().replace(/\s+/g, '')
}

function matchFaq(text) {
  const n = normalize(text)
  let best = null
  let bestScore = 0
  for (const item of state.faq) {
    let score = 0
    for (const kw of item.keywords) {
      if (n.includes(normalize(kw))) score += 2
    }
    if (normalize(item.question).includes(n) || n.includes(normalize(item.question.slice(0, 8)))) {
      score += 3
    }
    if (score > bestScore) {
      bestScore = score
      best = item
    }
  }
  return bestScore >= 2 ? best : null
}

function isMemoIntent(text) {
  return /^记(一下|住|录)?[:：]?/.test(text.trim()) || /^帮我记/.test(text.trim())
}

function extractMemo(text) {
  return text
    .replace(/^记(一下|住|录)?[:：]?/, '')
    .replace(/^帮我记(一下|录)?[:：]?/, '')
    .trim()
}

function appendMessage(role, text, meta = '') {
  const el = document.createElement('div')
  el.className = `msg msg-${role}`
  el.innerHTML = `<div class="bubble">${escapeHtml(text)}</div>${meta ? `<div class="meta">${escapeHtml(meta)}</div>` : ''}`
  $('#chat').appendChild(el)
  $('#chat').scrollTop = $('#chat').scrollHeight
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function refuseMessage() {
  return (
    '这个问题我在当前知识库里没有可靠依据。' +
    '我主要负责：站场限流孔板、变送器选型、FlowSize、FY301 培训等。' +
    '你可以换个问法，或联系文档维护人补充知识库。'
  )
}

async function callLlm(userText, faqContext) {
  const cfg = state.config?.llm
  if (!cfg?.enabled || !cfg.apiKey || cfg.apiKey.includes('YOUR_')) return null

  const system = state.config.systemPrompt || ''
  const context = faqContext
    ? `参考条目：${faqContext.question}\n${faqContext.answer}\n来源：${faqContext.source}`
    : '无匹配 FAQ。'

  const res = await fetch(`${cfg.apiBase}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${cfg.apiKey}`,
    },
    body: JSON.stringify({
      model: cfg.model,
      messages: [
        { role: 'system', content: `${system}\n\n${context}` },
        { role: 'user', content: userText },
      ],
      temperature: 0.3,
    }),
  })

  if (!res.ok) throw new Error(`LLM ${res.status}`)
  const data = await res.json()
  return data.choices?.[0]?.message?.content?.trim() || null
}

async function handleUserText(text) {
  if (!text.trim()) return
  appendMessage('user', text)

  if (state.mode === 'pocket' && isMemoIntent(text)) {
    const body = extractMemo(text) || text
    state.memos.unshift({ text: body, at: new Date().toISOString() })
    saveMemos()
    appendMessage('assistant', `已记下：${body}`, 'Pocket · 备忘')
    speak(`好的，已记下：${body}`)
    return
  }

  const hit = matchFaq(text)
  let reply = hit?.answer
  let meta = hit ? `来源：${hit.source}` : ''

  if (state.config?.llm?.enabled) {
    try {
      const llmReply = await callLlm(text, hit)
      if (llmReply) {
        reply = llmReply
        meta = hit ? `${meta} · LLM 润色` : 'LLM'
      }
    } catch (e) {
      console.warn(e)
    }
  }

  if (!reply) reply = refuseMessage()

  appendMessage('assistant', reply, meta || (state.mode === 'station' ? 'Station' : 'Pocket'))
  speak(reply.slice(0, 120))
}

function speak(text) {
  if (!window.speechSynthesis) return
  window.speechSynthesis.cancel()
  const u = new SpeechSynthesisUtterance(text)
  u.lang = 'zh-CN'
  u.rate = 1.05
  window.speechSynthesis.speak(u)
}

function setupSpeech() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition
  if (!SR) {
    $('#voice-hint').textContent = '当前浏览器不支持语音识别，请用 Chrome/Edge 或改用文字输入。'
    $('#btn-voice').disabled = true
    return
  }
  state.recognition = new SR()
  state.recognition.lang = 'zh-CN'
  state.recognition.continuous = false
  state.recognition.interimResults = true

  state.recognition.onresult = (ev) => {
    let final = ''
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      if (ev.results[i].isFinal) final += ev.results[i][0].transcript
    }
    if (final) $('#input').value = final
  }
  state.recognition.onend = () => {
    state.listening = false
    $('#btn-voice').classList.remove('active')
    $('#btn-voice').textContent = '按住 说话'
  }
}

function startListen() {
  if (!state.recognition || state.listening) return
  state.listening = true
  $('#btn-voice').classList.add('active')
  $('#btn-voice').textContent = '松开 结束'
  state.recognition.start()
}

function stopListen() {
  if (!state.recognition || !state.listening) return
  state.recognition.stop()
  const t = $('#input').value.trim()
  if (t) handleUserText(t)
  $('#input').value = ''
}

function renderMemos() {
  const box = $('#memo-list')
  if (!box) return
  box.innerHTML = ''
  if (!state.memos.length) {
    box.innerHTML = '<li class="empty">暂无备忘 · 说「记一下：……」</li>'
    return
  }
  for (const m of state.memos.slice(0, 8)) {
    const li = document.createElement('li')
    li.textContent = m.text
    box.appendChild(li)
  }
}

function setMode(mode) {
  state.mode = mode
  document.body.dataset.mode = mode
  $('#mode-station').classList.toggle('active', mode === 'station')
  $('#mode-pocket').classList.toggle('active', mode === 'pocket')
  $('#pocket-panel').hidden = mode !== 'pocket'
}

function bindUi() {
  $('#btn-send').addEventListener('click', () => {
    handleUserText($('#input').value)
    $('#input').value = ''
  })
  $('#input').addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleUserText($('#input').value)
      $('#input').value = ''
    }
  })

  const btn = $('#btn-voice')
  btn.addEventListener('mousedown', startListen)
  btn.addEventListener('mouseup', stopListen)
  btn.addEventListener('mouseleave', () => {
    if (state.listening) stopListen()
  })
  btn.addEventListener('touchstart', (e) => {
    e.preventDefault()
    startListen()
  })
  btn.addEventListener('touchend', (e) => {
    e.preventDefault()
    stopListen()
  })

  $('#mode-station').addEventListener('click', () => setMode('station'))
  $('#mode-pocket').addEventListener('click', () => setMode('pocket'))

  document.querySelectorAll('[data-quick]').forEach((el) => {
    el.addEventListener('click', () => handleUserText(el.dataset.quick))
  })
}

async function init() {
  await loadFaq()
  await loadConfig()
  loadMemos()
  setupSpeech()
  bindUi()
  setMode('station')
  appendMessage(
    'assistant',
    '你好，我是流衡助手 P0 原型。Station 模式适合工位问答；Pocket 模式可说「记一下：……」添加备忘。按住下方按钮说话，或直接输入文字。',
    'P0 Demo'
  )
}

init()
