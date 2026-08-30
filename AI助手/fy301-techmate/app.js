const HALL_WIZARD = [
  '停止反复插拔。确认工艺是否需切手动/旁路，阀门处于已知安全状态。',
  '断开回路电源，等待 30 秒，重新上电复位 CPU。',
  '目视检查霍尔接插件：无弯针、无破皮、锁扣到位。',
  '确认磁铁仍固定在阀杆上；测量磁铁面到传感器间隙 2–4 mm。',
  '（M1 自动）HART 读 Hall raw：手动推阀杆约 10%，读数应明显变化。',
  '确认气源 ≥ 约 20 psi，过滤网与排气孔正常。',
  '执行 Auto Setup（约 4 分钟）。若仍 HALL → 查远程霍尔电缆屏蔽与接地。',
  '仍失败：记录报警码、压电电压、间隙照片 → 生成厂家服务单。',
]

const state = { faults: [], wizIndex: 0, listening: false, recognition: null }

const $ = (s) => document.querySelector(s)

async function loadFaults() {
  const res = await fetch('knowledge/faults.json')
  state.faults = await res.json()
}

function norm(s) {
  return s.toLowerCase().replace(/\s+/g, '')
}

function matchFault(text) {
  const n = norm(text)
  let best = null
  let bestScore = 0
  for (const f of state.faults) {
    let score = 0
    for (const kw of f.keywords) {
      if (n.includes(norm(kw))) score += 2
    }
    if (score > bestScore) {
      bestScore = score
      best = f
    }
  }
  return bestScore >= 2 ? best : null
}

function appendMsg(role, text, meta = '', severity = '') {
  const el = document.createElement('div')
  el.className = `msg msg-${role} ${severity ? 'severity-' + severity : ''}`
  el.innerHTML = `<div class="bubble">${esc(text)}</div>${meta ? `<div class="meta">${esc(meta)}</div>` : ''}`
  $('#chat').appendChild(el)
  $('#chat').scrollTop = $('#chat').scrollHeight
}

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function diagnose(text) {
  if (!text.trim()) return
  appendMsg('user', text)
  const hit = matchFault(text)
  if (hit) {
    appendMsg('bot', hit.answer, `${hit.title} · ${hit.source}`, hit.severity)
    speak(hit.title + '。请按步骤操作。')
    if (hit.id === 'hall-hotplug' || text.includes('霍尔')) {
      setTimeout(() => switchTab('wizard'), 800)
    }
  } else {
    appendMsg(
      'bot',
      '暂未精确匹配。建议：\n1. 点「排查链」按顺序查\n2. 或描述 LCD 报警码（HALL / MGNT / FAIL MOVE）\n3. 说明是否动过霍尔线、气源是否正常',
      '提示'
    )
  }
}

function speak(t) {
  if (!window.speechSynthesis) return
  window.speechSynthesis.cancel()
  const u = new SpeechSynthesisUtterance(t)
  u.lang = 'zh-CN'
  window.speechSynthesis.speak(u)
}

function switchTab(name) {
  document.querySelectorAll('.tab').forEach((t) => {
    t.classList.toggle('active', t.dataset.tab === name)
  })
  document.querySelectorAll('.panel').forEach((p) => {
    p.classList.toggle('active', p.id === `panel-${name}`)
  })
}

function renderWizard() {
  const ol = $('#wizard-steps')
  ol.innerHTML = ''
  HALL_WIZARD.forEach((text, i) => {
    const li = document.createElement('li')
    li.textContent = text
    if (i < state.wizIndex) li.classList.add('done')
    if (i === state.wizIndex) li.classList.add('current')
    ol.appendChild(li)
  })
  $('#wiz-prev').disabled = state.wizIndex === 0
  $('#wiz-next').hidden = state.wizIndex >= HALL_WIZARD.length - 1
  $('#wiz-done').hidden = state.wizIndex < HALL_WIZARD.length - 1
}

function setupSpeech() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition
  if (!SR) {
    $('#btn-voice').disabled = true
    return
  }
  state.recognition = new SR()
  state.recognition.lang = 'zh-CN'
  state.recognition.onresult = (ev) => {
    let t = ''
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      if (ev.results[i].isFinal) t += ev.results[i][0].transcript
    }
    if (t) $('#input').value = t
  }
  state.recognition.onend = () => {
    state.listening = false
    $('#btn-voice').classList.remove('active')
    $('#btn-voice').textContent = '按住说话'
  }
}

function bind() {
  $('#btn-send').onclick = () => {
    diagnose($('#input').value)
    $('#input').value = ''
  }
  $('#input').onkeydown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      diagnose($('#input').value)
      $('#input').value = ''
    }
  }

  const v = $('#btn-voice')
  v.onmousedown = () => {
    if (!state.recognition) return
    state.listening = true
    v.classList.add('active')
    v.textContent = '松开结束'
    state.recognition.start()
  }
  const stop = () => {
    if (!state.listening) return
    state.recognition.stop()
    diagnose($('#input').value)
    $('#input').value = ''
  }
  v.onmouseup = stop
  v.onmouseleave = () => state.listening && stop()

  document.querySelectorAll('.tab').forEach((t) => {
    t.onclick = () => switchTab(t.dataset.tab)
  })

  document.querySelectorAll('[data-q]').forEach((b) => {
    b.onclick = () => diagnose(b.dataset.q)
  })

  $('#wiz-next').onclick = () => {
    if (state.wizIndex < HALL_WIZARD.length - 1) {
      state.wizIndex++
      renderWizard()
    }
  }
  $('#wiz-prev').onclick = () => {
    if (state.wizIndex > 0) {
      state.wizIndex--
      renderWizard()
    }
  }
  $('#wiz-done').onclick = () => {
    switchTab('chat')
    appendMsg('bot', '霍尔恢复向导已完成。若问题仍在，请记录 HART 变量并联系厂家。', '向导完成')
  }
}

async function init() {
  await loadFaults()
  setupSpeech()
  bind()
  renderWizard()
  switchTab('chat')
  appendMsg(
    'bot',
    'FY301 TechMate M0 就绪。\n\n您可描述现场故障，或点「带电拔霍尔」模拟昨天场景。\n\nM1 将接入 HART 自动读压电电压与 Hall 值。',
    'AI 智能调试手操器'
  )
}

init()
