const HALL_WIZARD = [
  { text: '停止反复插拔。确认工艺是否需切手动/旁路，阀门处于已知安全状态。', clip: 'hall' },
  { text: '断开回路电源，等待 30 秒，重新上电复位 CPU。', clip: 'hall' },
  { text: '目视检查霍尔接插件：无弯针、无破皮、锁扣到位。', clip: 'hall' },
  { text: '确认磁铁仍固定在阀杆上；测量磁铁面到传感器间隙 2–4 mm。', clip: 'hall' },
  { text: '（M1 自动）HART 读 Hall raw：手动推阀杆约 10%，读数应明显变化。', clip: 'hall' },
  { text: '确认气源 ≥ 约 20 psi，过滤网与排气孔正常。', clip: 'pilot' },
  { text: '执行 Auto Setup（约 4 分钟）。若仍 HALL → 查远程霍尔电缆屏蔽与接地。', clip: 'hall' },
  { text: '仍失败：记录报警码、压电电压、间隙照片 → 生成厂家服务单。', clip: 'chain' },
]

const state = {
  faults: [],
  clipsDoc: null,
  activeClipId: 'hall',
  wizIndex: 0,
  listening: false,
  recognition: null,
}

const $ = (s) => document.querySelector(s)

function fmtTime(sec) {
  const m = Math.floor(sec / 60)
  const s = Math.floor(sec % 60)
  return `${m}:${String(s).padStart(2, '0')}`
}

async function loadData() {
  const [f, c] = await Promise.all([fetch('knowledge/faults.json'), fetch('knowledge/clips.json')])
  state.faults = await f.json()
  state.clipsDoc = await c.json()
}

function clipById(id) {
  return state.clipsDoc?.clips.find((x) => x.id === id)
}

function videoSrc() {
  return state.clipsDoc?.videos?.engineer?.file
}

function simHref(simId) {
  return state.clipsDoc?.sims?.[simId]?.href
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

function showClip(clipId, { play = true, switchTabToClip = false } = {}) {
  const clip = clipById(clipId) || clipById('hall')
  if (!clip) return
  state.activeClipId = clip.id

  const card = $('#clip-card')
  const sim = simHref(clip.sim)
  card.innerHTML = `
    <h3>${esc(clip.title)}</h3>
    <p class="clip-time">工程师培训版 ${fmtTime(clip.start)} – ${fmtTime(clip.end)}</p>
    <p>${esc(clip.line)}</p>
    <p class="clip-actions">
      ${sim ? `<a href="${sim}" target="_blank" rel="noopener">打开仿真对照</a>` : ''}
      <button type="button" id="btn-replay">重播这一段</button>
    </p>
  `
  card.querySelector('#btn-replay')?.addEventListener('click', () => seekClip(clip, true))

  document.querySelectorAll('.clip-chip').forEach((b) => {
    b.classList.toggle('active', b.dataset.clip === clip.id)
  })

  seekClip(clip, play)
  if (switchTabToClip) switchTab('clip')
}

function seekClip(clip, play) {
  const video = $('#clip-video')
  const fallback = $('#clip-fallback')
  const src = videoSrc()
  if (!src) {
    fallback.hidden = false
    return
  }
  if (video.getAttribute('data-src') !== src) {
    video.src = src
    video.setAttribute('data-src', src)
  }
  const onMeta = () => {
    video.currentTime = clip.start
    if (play) video.play().catch(() => {})
    video.removeEventListener('loadedmetadata', onMeta)
  }
  if (video.readyState >= 1) {
    video.currentTime = clip.start
    if (play) video.play().catch(() => {})
  } else {
    video.addEventListener('loadedmetadata', onMeta)
  }
  video.ontimeupdate = () => {
    if (video.currentTime >= clip.end) {
      video.pause()
      video.ontimeupdate = null
    }
  }
  video.onerror = () => {
    fallback.hidden = false
  }
}

function renderClipList() {
  const box = $('#clip-list')
  box.innerHTML = '<p class="muted">五段切片（对应工程师培训版，不再整片播放）：</p>'
  for (const clip of state.clipsDoc.clips) {
    const b = document.createElement('button')
    b.type = 'button'
    b.className = 'clip-chip'
    b.dataset.clip = clip.id
    b.textContent = `${fmtTime(clip.start)} ${clip.title}`
    b.onclick = () => showClip(clip.id, { play: true })
    box.appendChild(b)
  }
}

function diagnose(text) {
  if (!text.trim()) return
  appendMsg('user', text)
  const hit = matchFault(text)
  if (hit) {
    const clip = clipById(hit.clip)
    const extra = clip
      ? `\n\n对应培训切片：${clip.title}（${fmtTime(clip.start)}–${fmtTime(clip.end)}）。点「对应切片」只看这一段，不要再从头放整部视频。`
      : ''
    appendMsg('bot', hit.answer + extra, `${hit.title} · ${hit.source}`, hit.severity)
    speak(hit.title + '。请按步骤操作，需要时看对应切片。')
    if (hit.clip) showClip(hit.clip, { play: false })
    if (hit.id === 'hall-hotplug' || text.includes('霍尔')) {
      setTimeout(() => switchTab('wizard'), 600)
    }
  } else {
    appendMsg(
      'bot',
      '暂未精确匹配。建议：\n1. 点「排查链」按顺序查\n2. 或描述 LCD 报警码（HALL / MGNT / FAIL MOVE）\n3. 说明是否动过霍尔线、气源是否正常\n\n不要只看完整培训视频——用「对应切片」按故障跳转。',
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
  HALL_WIZARD.forEach((step, i) => {
    const li = document.createElement('li')
    li.innerHTML = `${esc(step.text)} <button type="button" class="mini-clip" data-clip="${step.clip}">看切片</button>`
    if (i < state.wizIndex) li.classList.add('done')
    if (i === state.wizIndex) li.classList.add('current')
    ol.appendChild(li)
  })
  ol.querySelectorAll('.mini-clip').forEach((b) => {
    b.onclick = (e) => {
      e.stopPropagation()
      showClip(b.dataset.clip, { play: true, switchTabToClip: true })
    }
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
      showClip(HALL_WIZARD[state.wizIndex].clip, { play: false })
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
    appendMsg('bot', '霍尔恢复向导已完成。若问题仍在，请记录 HART 变量并联系厂家。不要只回头重看整部培训视频。', '向导完成')
  }
}

async function init() {
  await loadData()
  setupSpeech()
  bind()
  renderClipList()
  renderWizard()
  showClip('hall', { play: false })
  switchTab('chat')
  appendMsg(
    'bot',
    '昨天现场还停在「看培训视频」：看完霍尔原理，仍不知道先断电再量间隙。\n\n今天 TechMate 改成：问答 + 逐步向导为主，视频只作为对应切片（霍尔段约 2:35–3:19）。\n\n点「带电拔霍尔」走昨天场景。',
    '从视频态 → 现场手操器'
  )
}

init()
