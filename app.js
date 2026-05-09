/**
 * 共通テスト英語問題DB - Landing Page Application
 * レジストリからデータを読み込みカード一覧を描画
 */

// ===== レジストリ: 問題集・回の一覧 =====
const EXAM_REGISTRY = [
  {
    id: "kyotsu_2025_honshiken",
    publisher: "共通テスト",
    series: "本試験",
    year: 2025,
    round: "本試験",
    label: "★ 共通テスト 2025年度 本試験",
    dataPath: "data/kyotsu/2025/honshiken/data.json",
    pdfPaths: {
      mondai: "original_PDFs/Kyotuu-Test-2026/_2025年度本試験_問題.pdf",
      kaitou: "original_PDFs/Kyotuu-Test-2026/_2025年度本試験_解説.pdf"
    },
    icon: "🎯"
  },
  {
    id: "kyotsu_2025_tsuishiken",
    publisher: "共通テスト",
    series: "追試験",
    year: 2025,
    round: "追試験",
    label: "★ 共通テスト 2025年度 追試験",
    dataPath: "data/kyotsu/2025/tsuishiken/data.json",
    pdfPaths: {
      mondai: "original_PDFs/Kyotuu-Test-2026/_2025年度追試験_問題.pdf",
      kaitou: "original_PDFs/Kyotuu-Test-2026/_2025年度追試験_解説.pdf"
    },
    icon: "🎯"
  },
  {
    id: "kyotsu_2024_honshiken",
    publisher: "共通テスト",
    series: "本試験",
    year: 2024,
    round: "本試験",
    label: "★ 共通テスト 2024年度 本試験",
    dataPath: "data/kyotsu/2024/honshiken/data.json",
    pdfPaths: {
      mondai: "original_PDFs/Kyotuu-Test-2024/2024年_本試験_問題.pdf",
      kaitou: "original_PDFs/Kyotuu-Test-2024/2024年_本試験_解説.pdf"
    },
    icon: "🎯"
  },
  {
    id: "kyotsu_2023_honshiken",
    publisher: "共通テスト",
    series: "本試験",
    year: 2023,
    round: "本試験",
    label: "★ 共通テスト 2023年度 本試験",
    dataPath: "data/kyotsu/2023/honshiken/data.json",
    pdfPaths: {
      mondai: "original_PDFs/Kyotuu-Test-2023/2023_本試験_英語リーディング.pdf",
      kaitou: "original_PDFs/Kyotuu-Test-2023/2023_本試験_英語リーディング_解答.pdf"
    },
    icon: "🎯"
  },
  {
    id: "zkai_2026_01",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 1,
    label: "Z会 実戦模試 2026 ─ 第1回",
    dataPath: "data/zkai/2026/round01/data.json",
    icon: "📘"
  },
  {
    id: "zkai_2026_02",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 2,
    label: "Z会 実戦模試 2026 ─ 第2回",
    dataPath: "data/zkai/2026/round02/data.json",
    icon: "📗"
  },
  {
    id: "zkai_2026_03",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 3,
    label: "Z会 実戦模試 2026 ─ 第3回",
    dataPath: "data/zkai/2026/round03/data.json",
    icon: "📙"
  },
  {
    id: "zkai_2026_04",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 4,
    label: "Z会 実戦模試 2026 ─ 第4回",
    dataPath: "data/zkai/2026/round04/data.json",
    icon: "📕"
  },
  {
    id: "zkai_2026_05",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 5,
    label: "Z会 実戦模試 2026 ─ 第5回",
    dataPath: "data/zkai/2026/round05/data.json",
    icon: "📄"
  },
  {
    id: "zkai_2026_06",
    publisher: "Z会",
    series: "実戦模試",
    year: 2026,
    round: 6,
    label: "Z会 実戦模試 2026 ─ 第6回",
    dataPath: "data/zkai/2026/round06/data.json",
    icon: "📑"
  },
  {
    id: "sundai_2026_01",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2026,
    round: 1,
    label: "駿台実戦問題集 2026 ─ 第1回",
    dataPath: "data/sundai/2026/round01/data.json",
    icon: "📒"
  },
  {
    id: "sundai_2026_02",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2026,
    round: 2,
    label: "駿台実戦問題集 2026 ─ 第2回",
    dataPath: "data/sundai/2026/round02/data.json",
    icon: "📓"
  },
  {
    id: "sundai_2026_03",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2026,
    round: 3,
    label: "駿台実戦問題集 2026 ─ 第3回",
    dataPath: "data/sundai/2026/round03/data.json",
    icon: "📔"
  },
  {
    id: "sundai_2026_04",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2026,
    round: 4,
    label: "駿台実戦問題集 2026 ─ 第4回",
    dataPath: "data/sundai/2026/round04/data.json",
    icon: "📕"
  },
  {
    id: "sundai_2026_05",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2026,
    round: 5,
    label: "駿台実戦問題集 2026 ─ 第5回",
    dataPath: "data/sundai/2026/round05/data.json",
    icon: "📖",
    pdfPaths: {
      mondai: "original_PDFs/sundai2026/第5回_問題.pdf",
      kaitou: "original_PDFs/sundai2026/第5回_解説.pdf"
    }
  },
  {
    id: "sundai_2025_01",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2025,
    round: 1,
    label: "駿台実戦問題集 2025 ─ 第1回",
    dataPath: "data/sundai/2025/round01/data.json",
    icon: "📘"
  },
  {
    id: "sundai_2025_02",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2025,
    round: 2,
    label: "駿台実戦問題集 2025 ─ 第2回",
    dataPath: "data/sundai/2025/round02/data.json",
    icon: "📗"
  },
  {
    id: "sundai_2025_03",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2025,
    round: 3,
    label: "駿台実戦問題集 2025 ─ 第3回",
    dataPath: "data/sundai/2025/round03/data.json",
    icon: "📙"
  },
  {
    id: "sundai_2025_04",
    publisher: "駿台",
    series: "実戦問題集",
    year: 2025,
    round: 4,
    label: "駿台実戦問題集 2025 ─ 第4回",
    dataPath: "data/sundai/2025/round04/data.json",
    icon: "📕"
  },
];

// ===== 大問の説明テンプレート（data.jsonが未完成の大問向け） =====
const SECTION_DEFAULTS = {
  1: { desc: "短文読解", points: 6 },
  2: { desc: "事実把握", points: 10 },
  3: { desc: "概要把握", points: 9 },
  4: { desc: "論説文読解", points: 12 },
  5: { desc: "複数テキスト", points: 16 },
  6: { desc: "複数意見統合", points: 18 },
  7: { desc: "長文読解", points: 15 },
  8: { desc: "長文読解", points: 14 },
  '1A': { desc: "短文読解", points: 3 },
  '1B': { desc: "短文読解", points: 3 },
  '2A': { desc: "事実把握", points: 10 },
  '2B': { desc: "事実把握", points: 10 },
  '3A': { desc: "概要把握", points: 6 },
  '3B': { desc: "概要把握", points: 9 },
  '6A': { desc: "長文読解", points: 12 },
  '6B': { desc: "長文読解", points: 12 }
};

// ===== メイン =====
document.addEventListener('DOMContentLoaded', async () => {
  const app = document.getElementById('app');
  const loading = document.getElementById('loading');

  // 最後に開いていた exam ID / group key を取得（ビューアからの復帰用）
  const lastExamId = localStorage.getItem('readlens_last_exam') || '';
  const lastGroupKey = localStorage.getItem('readlens_last_group') || '';

  try {
    const groups = groupExams(EXAM_REGISTRY);
    let html = '';
    for (let gi = 0; gi < groups.length; gi++) {
      html += await renderYearGroup(groups[gi], gi, lastExamId, lastGroupKey);
    }
    loading.style.display = 'none';
    app.insertAdjacentHTML('beforeend', html);

    // 内側アコーディオン（各回）の開閉
    app.querySelectorAll('.exam-details').forEach(details => {
      details.addEventListener('toggle', () => {
        if (details.open) {
          localStorage.setItem('readlens_last_exam', details.dataset.examId);
        }
      });
    });
    // 外側アコーディオン（年グループ）の開閉
    app.querySelectorAll('.exam-year-group').forEach(details => {
      details.addEventListener('toggle', () => {
        if (details.open) {
          localStorage.setItem('readlens_last_group', details.dataset.groupKey);
        }
      });
    });

    // 最後に開いていた回までスクロール
    if (lastExamId) {
      const target = app.querySelector(`.exam-details[data-exam-id="${lastExamId}"]`);
      if (target) {
        setTimeout(() => target.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
      }
    }
    setupVocabLauncher();
  } catch (err) {
    loading.textContent = 'データの読み込みに失敗しました。';
    console.error(err);
  }
});

// ===== EXAM_REGISTRY を「出版社 × 年」でグループ化 =====
function groupExams(list) {
  const map = new Map();
  const groups = [];
  for (const ex of list) {
    let key = `${ex.publisher}__${ex.series}__${ex.year}`;
    if (ex.publisher === '共通テスト') {
      key = `${ex.publisher}__${ex.year}`;
    }
    if (!map.has(key)) {
      const g = { key, publisher: ex.publisher, series: ex.series, year: ex.year, exams: [] };
      map.set(key, g);
      groups.push(g);
    }
    map.get(key).exams.push(ex);
  }
  return groups;
}

function groupLabel(g) {
  if (g.publisher === '駿台') return `駿台 ${g.series} ${g.year}`;
  if (g.publisher === '共通テスト') return `🎯 共通テスト ${g.year}年度`;
  return `${g.publisher} ${g.year}年度`;
}

function groupIcon(g) {
  return g.publisher === '駿台' ? '📚' : '🏛';
}

async function renderYearGroup(group, gi, lastExamId, lastGroupKey) {
  const containsLast = group.exams.some(e => e.id === lastExamId);
  let body = '';
  for (let i = 0; i < group.exams.length; i++) {
    body += await renderExamBlock(group.exams[i], i, lastExamId, containsLast);
  }
  // 開閉判定: 直近開いていた exam を含む年 > 直近開いていた group の復元のみ
  // 初回訪問（履歴なし）はすべて閉じた状態をデフォルトにする
  let isOpen = '';
  if (lastExamId && containsLast) isOpen = 'open';
  else if (!lastExamId && lastGroupKey === group.key) isOpen = 'open';

  const countLabel = group.exams.length > 1 ? `<span class="exam-year-count">${group.exams.length}回</span>` : '';
  return `
    <section class="exam-year-block">
      <details class="exam-year-group" data-group-key="${group.key}" ${isOpen}>
        <summary class="exam-year-summary">
          <h2 class="exam-year-title"><span class="icon">${groupIcon(group)}</span>${groupLabel(group)}</h2>
          ${countLabel}
        </summary>
        <div class="exam-year-body">${body}</div>
      </details>
    </section>
  `;
}

// ===== 問題集ブロックの描画 =====
async function renderExamBlock(exam, indexInGroup, lastExamId, isFirstGroup) {
  let data = null;
  try {
    const resp = await fetch(exam.dataPath);
    if (resp.ok) {
      data = await resp.json();
    }
  } catch (e) {
    console.warn(`Failed to load ${exam.dataPath}:`, e);
  }

  const sections = data?.sections || [];
  let cardsHtml = '';

  // section_list があれば使う（6AB型対応）、なければ1-8
  const sectionList = data?.exam_info?.section_list || [1,2,3,4,5,6,7,8];
  for (const num of sectionList) {
    const sec = sections.find(s => String(s.section_number) === String(num));
    const defaults = SECTION_DEFAULTS[num] || {};
    const points = sec?.points || defaults.points || '?';
    const questionCount = sec ? countQuestions(sec) : '?';
    const desc = sec?.description || defaults.desc || '';
    const title = sec?.title || `第${num}問`;
    const isReady = !!sec;

    const printLinks = isReady ? `
        <div class="card-print-links">
          <a href="print.html?exam=${exam.id}&mode=passage&section=${num}" class="card-print-link" onclick="event.stopPropagation()" title="問題を印刷">📄問題</a>
          <a href="print.html?exam=${exam.id}&mode=questions&section=${num}" class="card-print-link" onclick="event.stopPropagation()" title="設問を印刷">📝設問</a>
        </div>` : '';

    const clickHandler = isReady ? `onclick="localStorage.setItem('readlens_last_exam','${exam.id}');location.href='viewer.html?exam=${exam.id}&section=${num}'"` : '';

    cardsHtml += `
      <div class="section-card${isReady ? '' : ' section-card--disabled'}"
         ${clickHandler}
         title="${title}${isReady ? 'の詳細を見る' : '（準備中）'}">
        <div class="section-number">${title}</div>
        <div class="section-desc">${desc}</div>
        <div class="tags">
          <span class="tag tag-points">配点 ${points}</span>
          <span class="tag tag-questions">問${questionCount}</span>
        </div>
        ${printLinks}
      </div>
    `;
  }

  // 最後に見ていた exam ID と一致したときだけ open。
  // 初回訪問（履歴なし）はすべて閉じた状態をデフォルトにする。
  // Build PDF links from exam_info
  let pdfDir = "";
  if (exam.publisher === '駿台') pdfDir = `sundai${exam.year}`;
  else if (exam.publisher === 'Z会') pdfDir = `Z-kai${exam.year}`;
  else pdfDir = `${exam.publisher}${exam.year}`;
  
  const pdfBase = `original_PDFs/${pdfDir}/`;
  
  const pdfMondai = exam.pdfPaths?.mondai || (data?.exam_info?.source_pdf_mondai ? `${pdfBase}${data.exam_info.source_pdf_mondai}` : null);
  const pdfKaitou = exam.pdfPaths?.kaitou || (data?.exam_info?.source_pdf_kaitou ? `${pdfBase}${data.exam_info.source_pdf_kaitou}` : null);
  const vocabPath = exam.dataPath.replace(/data\.json$/, 'vocabulary_explanations_only_all_sections.json');
  
  let pdfLinksHtml = '';
  const vocabButtonHtml = `<button class="btn-vocab-link" data-exam-id="${exam.id}" data-data-path="${exam.dataPath}" data-vocab-path="${vocabPath}" onclick="event.stopPropagation()" title="やっておきたい語句・表現（フラッシュカード）">🃏 やっておきたい語句・表現</button>`;
  if (pdfMondai) {
    pdfLinksHtml += `<a href="${pdfMondai}" target="_blank" class="btn-pdf-link" onclick="event.stopPropagation()" title="原本PDF（問題）">📄 問題PDF</a>`;
  }
  if (pdfKaitou) {
    pdfLinksHtml += `<a href="${pdfKaitou}" target="_blank" class="btn-pdf-link" onclick="event.stopPropagation()" title="原本PDF（解説）">📖 解説PDF</a>`;
  }

  const isOpen = (lastExamId && exam.id === lastExamId) ? 'open' : '';
  return `
    <section class="exam-block">
      <details class="exam-details" data-exam-id="${exam.id}" ${isOpen}>
        <summary class="exam-block-header">
          <h2 class="exam-block-title"><span class="icon">${exam.icon}</span>${exam.label}</h2>
          <div class="exam-header-actions">
            ${vocabButtonHtml}
            ${pdfLinksHtml}
          </div>
        </summary>
        <div class="section-grid">
          ${cardsHtml}
        </div>
      </details>
    </section>
  `;
}

// ===== 設問数カウント =====
function countQuestions(section) {
  let count = 0;
  if (section.questions) count += section.questions.length;
  if (section.subsections) {
    for (const sub of section.subsections) {
      if (sub.questions) count += sub.questions.length;
    }
  }
  return count;
}

// ===== 語彙フラッシュカード =====
const vocabState = {
  modal: null,
  examId: '',
  examTitle: '',
  allCards: [],
  selectedSections: new Set(),
  sectionCounts: new Map(),
  deck: [],
  index: 0,
  side: 'front',
  mode: 'all', // all | retry
  orderMode: 'inorder', // inorder | random
  autoPlay: true,
  unknownTerms: new Set(),
  sentenceMap: new Map(),
};

function setupVocabLauncher() {
  document.querySelectorAll('.btn-vocab-link').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.preventDefault();
      e.stopPropagation();
      const examId = btn.dataset.examId || '';
      const dataPath = btn.dataset.dataPath || '';
      const vocabPath = btn.dataset.vocabPath || '';
      await openVocabModal(examId, dataPath, vocabPath);
    });
  });
}

function getUnknownStorageKey(examId) {
  return `readlens_vocab_unknown_v2_${examId}`;
}

function ensureVocabModal() {
  if (vocabState.modal) return;
  const wrap = document.createElement('div');
  wrap.className = 'vocab-modal hidden';
  wrap.innerHTML = `
    <div class="vocab-modal-backdrop"></div>
    <div class="vocab-modal-dialog" role="dialog" aria-modal="true" aria-label="語彙フラッシュカード">
      <div class="vocab-modal-head">
        <div class="vocab-modal-title-wrap">
          <div class="vocab-modal-title">やっておきたい語句・表現</div>
          <div class="vocab-modal-subtitle"></div>
        </div>
        <button class="vocab-close-btn" type="button" title="閉じる">✕</button>
      </div>
      <div class="vocab-modal-body">
        <div class="vocab-screen vocab-screen-setup">
          <div class="vocab-stats">
            <div class="vocab-stat-card"><div class="vocab-stat-num stat-total">0</div><div class="vocab-stat-label">全単語</div></div>
            <div class="vocab-stat-card"><div class="vocab-stat-num stat-remaining">0</div><div class="vocab-stat-label">残り</div></div>
            <div class="vocab-stat-card"><div class="vocab-stat-num stat-learned">0</div><div class="vocab-stat-label">覚えた</div></div>
          </div>
          <div class="vocab-section-picker">
            <div class="vocab-section-title">出題範囲（大問）</div>
            <label class="vocab-section-item vocab-section-item-all">
              <input type="checkbox" class="vocab-section-all" checked />
              <span>全部</span>
              <span class="vocab-section-count section-count-all">0語</span>
            </label>
            <div class="vocab-section-list"></div>
          </div>
          <div class="vocab-order-toggle">
            <button type="button" class="vocab-order-btn active" data-mode="inorder">出現順</button>
            <button type="button" class="vocab-order-btn" data-mode="random">ランダム</button>
          </div>
          <label class="vocab-autoplay-line">
            <input type="checkbox" class="vocab-autoplay-check" checked />
            <span>自動音声再生</span>
          </label>
          <button type="button" class="vocab-start-btn">START</button>
          <button type="button" class="vocab-reset-btn">学習記録をリセット</button>
        </div>

        <div class="vocab-screen vocab-screen-study hidden">
          <div class="vocab-study-top">
            <div class="vocab-progress-text"></div>
            <button type="button" class="vocab-end-btn">終了</button>
          </div>
          <div class="vocab-progress-line"><span class="vocab-progress-fill"></span></div>
          <div class="vocab-card">
            <div class="vocab-card-no"></div>
            <button type="button" class="vocab-audio-btn vocab-play-term">🔊</button>
            <div class="vocab-front">
              <div class="vocab-term-en"></div>
            </div>
            <div class="vocab-back hidden">
              <div class="vocab-term-ja"></div>
              <div class="vocab-term-en-sub"></div>
              <div class="vocab-example-en"></div>
              <div class="vocab-example-ja"></div>
            </div>
          </div>
          <div class="vocab-front-controls">
            <button type="button" class="vocab-btn vocab-hint-btn">ヒント</button>
            <button type="button" class="vocab-btn vocab-answer-btn">答え</button>
            <button type="button" class="vocab-btn vocab-prev-btn">戻る</button>
          </div>
          <div class="vocab-back-controls hidden">
            <button type="button" class="vocab-btn vocab-hint-btn">ヒント</button>
            <button type="button" class="vocab-btn vocab-next-btn">次へ</button>
            <button type="button" class="vocab-btn vocab-prev-btn">戻る</button>
          </div>
          <div class="vocab-memo-controls hidden">
            <button type="button" class="vocab-btn vocab-still-btn">まだ</button>
            <button type="button" class="vocab-btn vocab-learned-btn">覚えた</button>
          </div>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(wrap);
  vocabState.modal = wrap;

  wrap.querySelector('.vocab-close-btn').addEventListener('click', closeVocabModal);
  wrap.querySelector('.vocab-start-btn').addEventListener('click', startVocabStudy);
  wrap.querySelector('.vocab-reset-btn').addEventListener('click', resetUnknownRecord);
  wrap.querySelector('.vocab-autoplay-check').addEventListener('change', (e) => {
    vocabState.autoPlay = !!e.target.checked;
  });
  wrap.querySelectorAll('.vocab-order-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.dataset.mode || 'inorder';
      vocabState.orderMode = mode;
      wrap.querySelectorAll('.vocab-order-btn').forEach(x => x.classList.toggle('active', x === btn));
    });
  });
  wrap.querySelectorAll('.vocab-hint-btn').forEach(btn => btn.addEventListener('click', playHintAudio));
  wrap.querySelector('.vocab-play-term').addEventListener('click', playTermAudio);
  wrap.querySelector('.vocab-answer-btn').addEventListener('click', () => setCardSide('back'));
  wrap.querySelector('.vocab-next-btn').addEventListener('click', () => moveCard(1));
  wrap.querySelectorAll('.vocab-prev-btn').forEach(btn => btn.addEventListener('click', () => moveCard(-1)));
  wrap.querySelector('.vocab-still-btn').addEventListener('click', () => markCard(false));
  wrap.querySelector('.vocab-learned-btn').addEventListener('click', () => markCard(true));
  wrap.querySelector('.vocab-end-btn').addEventListener('click', finishAndBackToSetup);
  wrap.querySelector('.vocab-section-all').addEventListener('change', handleToggleAllSections);
  wrap.querySelector('.vocab-section-list').addEventListener('change', handleToggleSectionItem);

  document.addEventListener('keydown', (ev) => {
    if (!vocabState.modal || vocabState.modal.classList.contains('hidden')) return;
    if (ev.key === 'Escape') {
      ev.preventDefault();
    }
  });
}

async function openVocabModal(examId, dataPath, vocabPath) {
  ensureVocabModal();
  try {
    const [vocabResp, dataResp] = await Promise.all([
      fetch(vocabPath + '?v=' + Date.now()),
      fetch(dataPath + '?v=' + Date.now()),
    ]);
    if (!vocabResp.ok) {
      alert('語彙データが見つかりません。先に語彙JSONを生成してください。');
      return;
    }
    const vocabData = await vocabResp.json();
    const examData = dataResp.ok ? await dataResp.json() : null;

    vocabState.examId = examId;
    vocabState.examTitle = examData?.exam_info?.title || examId;
    vocabState.sentenceMap = buildSentenceMap(examData);
    vocabState.allCards = normalizeVocabCards(vocabData);
    if (!vocabState.allCards.length) {
      alert('語彙データが空です。');
      return;
    }
    vocabState.sectionCounts = buildSectionCounts(vocabState.allCards);
    vocabState.selectedSections = new Set([...vocabState.sectionCounts.keys()]);
    const unknownRaw = localStorage.getItem(getUnknownStorageKey(examId));
    let unknownList = [];
    if (unknownRaw) {
      try { unknownList = JSON.parse(unknownRaw) || []; } catch (_) {}
    }
    vocabState.unknownTerms = new Set(unknownList);
    vocabState.mode = 'all';
    vocabState.deck = [...vocabState.allCards];
    vocabState.index = 0;
    vocabState.side = 'front';
    vocabState.orderMode = 'inorder';
    vocabState.autoPlay = true;
    vocabState.modal.classList.remove('hidden');
    showVocabSetup();
  } catch (err) {
    console.error(err);
    alert('語彙データの読み込みに失敗しました。');
  }
}

function closeVocabModal() {
  if (!vocabState.modal) return;
  vocabState.modal.classList.add('hidden');
  if ('speechSynthesis' in window) speechSynthesis.cancel();
}

function showVocabSetup() {
  const m = vocabState.modal;
  if (!m) return;
  m.querySelector('.vocab-modal-subtitle').textContent = vocabState.examTitle;
  m.querySelector('.vocab-screen-setup').classList.remove('hidden');
  m.querySelector('.vocab-screen-study').classList.add('hidden');
  m.querySelector('.vocab-autoplay-check').checked = vocabState.autoPlay;
  m.querySelectorAll('.vocab-order-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mode === vocabState.orderMode);
  });

  renderSectionPicker();

  const selectedCards = getCardsBySelectedSections(vocabState.allCards);
  const total = selectedCards.length;
  const selectedTermSet = new Set(selectedCards.map(c => c.termEn.toLowerCase()));
  const stillCnt = [...vocabState.unknownTerms].filter(t => selectedTermSet.has(t)).length;
  const learned = Math.max(0, total - stillCnt);
  const remaining = Math.max(0, total - learned);
  m.querySelector('.stat-total').textContent = String(total);
  m.querySelector('.stat-remaining').textContent = String(remaining);
  m.querySelector('.stat-learned').textContent = String(learned);
}

function startVocabStudy() {
  if (!vocabState.modal) return;
  const selected = getCardsBySelectedSections(vocabState.allCards);
  if (!selected.length) {
    alert('学習する大問を1つ以上選択してください。');
    return;
  }
  vocabState.mode = 'all';
  vocabState.deck = [...selected];
  if (vocabState.orderMode === 'random') {
    shuffleArray(vocabState.deck);
  }
  vocabState.index = 0;
  vocabState.side = 'front';
  vocabState.modal.querySelector('.vocab-screen-setup').classList.add('hidden');
  vocabState.modal.querySelector('.vocab-screen-study').classList.remove('hidden');
  renderVocabCard();
}

function finishAndBackToSetup() {
  showVocabSetup();
}

function resetUnknownRecord() {
  if (!confirm('「まだ」の記録をリセットしますか？')) return;
  vocabState.unknownTerms = new Set();
  localStorage.setItem(getUnknownStorageKey(vocabState.examId), JSON.stringify([]));
  showVocabSetup();
}

function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

function buildSentenceMap(examData) {
  const map = new Map();
  if (!examData || !examData.sections) return map;

  const addSent = (obj) => {
    if (!obj || typeof obj !== 'object') return;
    if (obj.id && (obj.en || obj.ja)) {
      map.set(obj.id, { en: obj.en || '', ja: obj.ja || '' });
    }
  };
  const walkParagraphNode = (node) => {
    if (Array.isArray(node)) return node.forEach(walkParagraphNode);
    if (node && typeof node === 'object') {
      addSent(node);
      if (Array.isArray(node.items)) node.items.forEach(walkParagraphNode);
    }
  };

  for (const sec of examData.sections) {
    const passages = [];
    if (sec.subsections) {
      for (const sub of sec.subsections) if (sub.passages) passages.push(...sub.passages);
    } else if (sec.passages) {
      passages.push(...sec.passages);
    }
    for (const p of passages) {
      if (Array.isArray(p.sentences)) p.sentences.forEach(addSent);
      if (Array.isArray(p.paragraphs)) p.paragraphs.forEach(walkParagraphNode);
      if (p.floating_aside && Array.isArray(p.floating_aside.sentences)) p.floating_aside.sentences.forEach(addSent);
    }
  }
  return map;
}

function normalizeVocabCards(vocabData) {
  const entries = Array.isArray(vocabData?.entries) ? vocabData.entries : [];
  const cards = [];
  for (const e of entries) {
    const term = cleanCardText(e.term_en);
    if (!term) continue;
    const occs = Array.isArray(e.occurrences) ? e.occurrences : [];
    occs.sort((a, b) => {
      const secCmp = compareSectionOrder(a.section_number, b.section_number);
      if (secCmp !== 0) return secCmp;
      return String(a.answer_number || '').localeCompare(String(b.answer_number || ''), 'ja');
    });
    const first = occs[0] || {};
    let exEn = cleanCardText(e.example_en);
    let exJa = cleanCardText(e.example_ja);
    const ids = Array.isArray(first.evidence_sentences) ? first.evidence_sentences : [];
    if ((!exEn || !exJa) && ids.length && vocabState.sentenceMap.has(ids[0])) {
      const x = vocabState.sentenceMap.get(ids[0]);
      exEn = exEn || cleanCardText(x.en);
      exJa = exJa || cleanCardText(x.ja);
    }
    const flashOrder = e.flashcard_order;
    cards.push({
      termEn: term,
      termJa: cleanCardText(e.term_ja) || '（訳未登録）',
      section: first.section_number,
      questionId: first.question_id,
      answerNumber: first.answer_number,
      exampleEn: exEn,
      exampleJa: exJa,
      flashcardOrder: typeof flashOrder === 'number' && Number.isFinite(flashOrder) ? flashOrder : null,
    });
  }
  cards.sort((a, b) => {
    const secCmp = compareSectionOrder(a.section, b.section);
    if (secCmp !== 0) return secCmp;
    const oa = a.flashcardOrder;
    const ob = b.flashcardOrder;
    if (oa != null && ob != null && oa !== ob) return oa - ob;
    if (oa != null && ob == null) return -1;
    if (oa == null && ob != null) return 1;
    return a.termEn.localeCompare(b.termEn, 'en');
  });
  return cards;
}

function currentCard() {
  if (!vocabState.deck.length) return null;
  return vocabState.deck[vocabState.index] || null;
}

function renderVocabCard() {
  const m = vocabState.modal;
  if (!m) return;
  const card = currentCard();
  const progressText = m.querySelector('.vocab-progress-text');
  const progressFill = m.querySelector('.vocab-progress-fill');
  const noEl = m.querySelector('.vocab-card-no');
  const termEnEl = m.querySelector('.vocab-term-en');
  const termJaEl = m.querySelector('.vocab-term-ja');
  const termEnSubEl = m.querySelector('.vocab-term-en-sub');
  const exEnEl = m.querySelector('.vocab-example-en');
  const exJaEl = m.querySelector('.vocab-example-ja');
  const front = m.querySelector('.vocab-front');
  const back = m.querySelector('.vocab-back');
  const frontControls = m.querySelector('.vocab-front-controls');
  const backControls = m.querySelector('.vocab-back-controls');
  const memoControls = m.querySelector('.vocab-memo-controls');

  if (!card) {
    progressText.textContent = '完了';
    progressFill.style.width = '100%';
    termEnEl.textContent = 'お疲れさまでした！';
    termJaEl.textContent = '';
    termEnSubEl.textContent = '';
    exEnEl.textContent = '';
    exJaEl.textContent = '';
    noEl.textContent = '';
    front.classList.remove('hidden');
    back.classList.add('hidden');
    frontControls.classList.add('hidden');
    backControls.classList.add('hidden');
    memoControls.classList.add('hidden');
    return;
  }

  const idx = vocabState.index + 1;
  const total = vocabState.deck.length;
  progressText.textContent = `${idx} / ${total}${vocabState.mode === 'retry' ? '（未習得のみ）' : ''}`;
  progressFill.style.width = `${Math.max(0, Math.min(100, (idx / total) * 100))}%`;
  noEl.textContent = `No.${idx}`;
  termEnEl.textContent = card.termEn;
  termJaEl.textContent = card.termJa;
  termEnSubEl.textContent = card.termEn;
  exEnEl.textContent = card.exampleEn ? `例: ${card.exampleEn}` : '例: （未登録）';
  exJaEl.textContent = card.exampleJa ? `訳: ${card.exampleJa}` : '訳: （未登録）';

  const isBack = vocabState.side === 'back';
  front.classList.toggle('hidden', isBack);
  back.classList.toggle('hidden', !isBack);
  frontControls.classList.toggle('hidden', isBack);
  backControls.classList.toggle('hidden', !isBack);
  memoControls.classList.toggle('hidden', !isBack);

  if (!isBack && vocabState.autoPlay) {
    playTermAudio();
  }
}

function setCardSide(side) {
  vocabState.side = side;
  renderVocabCard();
}

function moveCard(delta) {
  if (!vocabState.deck.length) return;
  let next = vocabState.index + delta;
  if (next < 0) next = 0;
  if (next >= vocabState.deck.length) {
    if (vocabState.mode === 'all') {
      const unknownCards = getCardsBySelectedSections(vocabState.allCards)
        .filter(c => vocabState.unknownTerms.has(c.termEn.toLowerCase()));
      if (unknownCards.length > 0) {
        vocabState.mode = 'retry';
        vocabState.deck = [...unknownCards];
        if (vocabState.orderMode === 'random') shuffleArray(vocabState.deck);
        vocabState.index = 0;
        vocabState.side = 'front';
        renderVocabCard();
        return;
      }
      next = vocabState.deck.length - 1;
    } else {
      next = vocabState.deck.length - 1;
    }
  }
  vocabState.index = next;
  setCardSide('front');
}

function markCard(learned) {
  const card = currentCard();
  if (!card) return;
  const key = card.termEn.toLowerCase();
  if (learned) vocabState.unknownTerms.delete(key);
  else vocabState.unknownTerms.add(key);
  localStorage.setItem(getUnknownStorageKey(vocabState.examId), JSON.stringify([...vocabState.unknownTerms]));
  moveCard(1);
}

function speakText(text, options = {}) {
  if (!text) return;
  if (!('speechSynthesis' in window)) return;
  const u = new SpeechSynthesisUtterance(text);
  u.lang = options.lang || 'en-US';
  u.rate = options.rate || 1.0;
  speechSynthesis.cancel();
  speechSynthesis.speak(u);
}

function playTermAudio() {
  const card = currentCard();
  if (!card) return;
  speakText(card.termEn, { lang: 'en-US', rate: 1.0 });
}

function playHintAudio() {
  const card = currentCard();
  if (!card) return;
  speakText(card.exampleEn || card.termEn, { lang: 'en-US', rate: 0.9 });
}

function cleanCardText(value) {
  return String(value || '')
    .replace(/<[^>]*>/g, ' ')
    .replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function normalizeSectionValue(value) {
  return String(value ?? '').trim();
}

/** 語彙モーダル用：大問3–8・6A・6B（… / 7P1–9 / 8M1–6・8N1–3・8U1–8（追試8-1）・8V1–4（追試8-2） / 6Aa–6Af / 6Ba–6Bh）を分かりやすく表示 */
function formatVocabSectionLabel(sec) {
  const s = normalizeSectionValue(sec);
  const m4 = s.match(/^4([A-D])$/i);
  if (m4) {
    const part = { A: 'リード文', B: '記事', C: 'アンケートの結果', D: '資料' }[m4[1].toUpperCase()];
    if (part) return `第4問（${part}）`;
  }
  const m3m = s.match(/^3M([12])$/i);
  if (m3m) {
    const part = { 1: '第1段落', 2: '第2段落' }[m3m[1]];
    if (part) return `第3問（${part}）`;
  }
  const m5m = s.match(/^5M([12])$/i);
  if (m5m) {
    const part = { 1: '記事', 2: '調査結果' }[m5m[1]];
    if (part) return `第5問（${part}）`;
  }
  const m5t = s.match(/^5T([1-3])$/i);
  if (m5t) {
    const part = {
      1: 'リード文',
      2: '「あなた」のメール',
      3: 'ライアン教授のメール',
    }[m5t[1]];
    if (part) return `第5問（${part}）`;
  }
  const m5 = s.match(/^5([A-G])$/i);
  if (m5) {
    const part = {
      A: '§1',
      B: '§2',
      C: '§3',
      D: '§4前',
      E: '§4',
      F: '§5',
      G: '§6',
    }[m5[1].toUpperCase()];
    if (part) return `第5問（${part}）`;
  }
  const m6n = s.match(/^6N([1-3])$/i);
  if (m6n) {
    const part = {
      1: '物語',
      2: 'ワークシート',
      3: '設問文・選択肢',
    }[m6n[1]];
    if (part) return `第6問（${part}）`;
  }
  const m6m = s.match(/^6M([1-4])$/i);
  if (m6m) {
    const part = { 1: '§1', 2: '§2', 3: '§3', 4: '§4' }[m6m[1]];
    if (part) return `第6問（${part}）`;
  }
  const m7p = s.match(/^7P([1-9])$/i);
  if (m7p) {
    const part = {
      1: '第1段落',
      2: '第2段落',
      3: '第3段落',
      4: '第4段落',
      5: '第5段落',
      6: '第6段落',
      7: '最終段落',
      8: '発表のアウトライン',
      9: '設問文・選択肢',
    }[m7p[1]];
    if (part) return `第7問（${part}）`;
  }
  const m7m = s.match(/^7M([1-8])$/i);
  if (m7m) {
    const n = m7m[1];
    if (n === '8') return '第7問（最終段落）';
    const part = { 1: '§1', 2: '§2', 3: '§3', 4: '§4', 5: '§5', 6: '§6', 7: '§7' }[n];
    if (part) return `第7問（${part}）`;
  }
  const m8m = s.match(/^8M([1-6])$/i);
  if (m8m) {
    const part = {
      1: 'Apu',
      2: 'Christine',
      3: 'Meilin',
      4: '中盤',
      5: 'Naomi',
      6: 'Victor',
    }[m8m[1]];
    if (part) return `第8問（${part}）`;
  }
  const m8n = s.match(/^8N([1-3])$/i);
  if (m8n) {
    const part = {
      1: 'エッセイのアウトライン',
      2: '資料A',
      3: '資料B',
    }[m8n[1]];
    if (part) return `第8問（${part}）`;
  }
  const m8u = s.match(/^8U([1-8])$/i);
  if (m8u) {
    const part = {
      1: '冒頭',
      2: 'ステップ1・Aya',
      3: 'ステップ1・David',
      4: 'Indira',
      5: 'Kenyatta',
      6: 'Yo',
      7: '設問文・選択肢',
      8: 'ステップ2',
    }[m8u[1]];
    if (part) return `第8問（${part}）`;
  }
  const m8v = s.match(/^8V([1-4])$/i);
  if (m8v) {
    const part = {
      1: 'エッセイのアウトライン',
      2: '資料A',
      3: '資料B',
      4: '設問文・選択肢',
    }[m8v[1]];
    if (part) return `第8問（${part}）`;
  }
  const m6a = s.match(/^6A([a-f])$/i);
  if (m6a) {
    const part = {
      a: '第1段落',
      b: '第2段落',
      c: '第3段落',
      d: '第4段落',
      e: '第5段落',
      f: '最終段落',
    }[m6a[1].toLowerCase()];
    if (part) return `第6A問（${part}）`;
  }
  const m6b = s.match(/^6B([a-h])$/i);
  if (m6b) {
    const part = {
      a: '第1段落',
      b: '第2段落',
      c: '第3段落',
      d: '第4段落',
      e: '第5段落',
      f: '第6段落',
      g: '第7段落',
      h: '最終段落',
    }[m6b[1].toLowerCase()];
    if (part) return `第6B問（${part}）`;
  }
  return `第${s}問`;
}

function buildSectionCounts(cards) {
  const counts = new Map();
  for (const c of cards) {
    const sec = normalizeSectionValue(c.section);
    if (!sec) continue;
    counts.set(sec, (counts.get(sec) || 0) + 1);
  }
  return new Map(
    [...counts.entries()].sort((a, b) => compareSectionOrder(a[0], b[0]))
  );
}

function parseSectionOrder(value) {
  const raw = normalizeSectionValue(value);
  const m = raw.match(/^(\d+)([A-Za-z]*)$/);
  if (!m) {
    return { main: Number.MAX_SAFE_INTEGER, suffix: raw.toUpperCase(), raw };
  }
  return {
    main: Number(m[1]),
    suffix: (m[2] || '').toUpperCase(),
    raw,
  };
}

function compareSectionOrder(a, b) {
  const pa = parseSectionOrder(a);
  const pb = parseSectionOrder(b);
  if (pa.main !== pb.main) return pa.main - pb.main;
  if (pa.suffix !== pb.suffix) return pa.suffix.localeCompare(pb.suffix, 'en');
  return pa.raw.localeCompare(pb.raw, 'ja');
}

function getCardsBySelectedSections(cards) {
  return cards.filter(c => vocabState.selectedSections.has(normalizeSectionValue(c.section)));
}

function renderSectionPicker() {
  const m = vocabState.modal;
  if (!m) return;
  const listEl = m.querySelector('.vocab-section-list');
  const allEl = m.querySelector('.vocab-section-all');
  const allCntEl = m.querySelector('.section-count-all');
  const sections = [...vocabState.sectionCounts.entries()];
  listEl.innerHTML = sections
    .map(([sec, cnt]) => {
      const checked = vocabState.selectedSections.has(sec) ? 'checked' : '';
      return `<label class="vocab-section-item"><input type="checkbox" class="vocab-section-check" value="${sec}" ${checked} /><span>${formatVocabSectionLabel(sec)}</span><span class="vocab-section-count">${cnt}語</span></label>`;
    })
    .join('');
  const selectedCount = vocabState.selectedSections.size;
  allEl.checked = selectedCount === sections.length;
  allEl.indeterminate = selectedCount > 0 && selectedCount < sections.length;
  allCntEl.textContent = `${vocabState.allCards.length}語`;
}

function handleToggleAllSections(ev) {
  const checked = !!ev.target.checked;
  vocabState.selectedSections = checked
    ? new Set([...vocabState.sectionCounts.keys()])
    : new Set();
  showVocabSetup();
}

function handleToggleSectionItem(ev) {
  const target = ev.target;
  if (!(target instanceof HTMLInputElement)) return;
  if (!target.classList.contains('vocab-section-check')) return;
  const sec = normalizeSectionValue(target.value);
  if (!sec) return;
  if (target.checked) vocabState.selectedSections.add(sec);
  else vocabState.selectedSections.delete(sec);
  showVocabSetup();
}
