/**
 * 共通テスト英語問題DB - Landing Page Application
 * レジストリからデータを読み込みカード一覧を描画
 */

// ===== レジストリ: 問題集・回の一覧 =====
const EXAM_REGISTRY = [
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
    icon: "📖"
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
  {
    id: "kakomon_2025",
    publisher: "共通テスト",
    series: "過去問",
    year: 2025,
    round: "本試験",
    label: "共通テスト 2025年度 本試験",
    dataPath: "data/kakomon/2025/data.json",
    icon: "🏛"
  },
  {
    id: "kakomon_2024",
    publisher: "共通テスト",
    series: "過去問",
    year: 2024,
    round: "本試験",
    label: "共通テスト 2024年度 本試験",
    dataPath: "data/kakomon/2024/data.json",
    icon: "🏫"
  },
  {
    id: "kakomon_2023",
    publisher: "共通テスト",
    series: "過去問",
    year: 2023,
    round: "本試験",
    label: "共通テスト 2023年度 本試験",
    dataPath: "data/kakomon/2023/data.json",
    icon: "🏫"
  },
  {
    id: "kakomon_2022",
    publisher: "共通テスト",
    series: "過去問",
    year: 2022,
    round: "本試験",
    label: "共通テスト 2022年度 本試験",
    dataPath: "data/kakomon/2022/data.json",
    icon: "🏫"
  },
  {
    id: "kakomon_2021_1",
    publisher: "共通テスト",
    series: "過去問",
    year: 2021,
    round: "第1日程",
    label: "共通テスト 2021年度 第1日程",
    dataPath: "data/kakomon/2021_1/data.json",
    icon: "🏫"
  }
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
    const key = `${ex.publisher}__${ex.year}`;
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
  const pdfBase = `original_PDFs/${exam.publisher === '駿台' ? 'sundai' : exam.publisher}${exam.year}/`;
  const pdfMondai = data?.exam_info?.source_pdf_mondai;
  const pdfKaitou = data?.exam_info?.source_pdf_kaitou;
  let pdfLinksHtml = '';
  if (pdfMondai) {
    pdfLinksHtml += `<a href="${pdfBase}${pdfMondai}" target="_blank" class="btn-pdf-link" onclick="event.stopPropagation()" title="原本PDF（問題）">📄 問題PDF</a>`;
  }
  if (pdfKaitou) {
    pdfLinksHtml += `<a href="${pdfBase}${pdfKaitou}" target="_blank" class="btn-pdf-link" onclick="event.stopPropagation()" title="原本PDF（解説）">📖 解説PDF</a>`;
  }

  const isOpen = (lastExamId && exam.id === lastExamId) ? 'open' : '';
  return `
    <section class="exam-block">
      <details class="exam-details" data-exam-id="${exam.id}" ${isOpen}>
        <summary class="exam-block-header">
          <h2 class="exam-block-title"><span class="icon">${exam.icon}</span>${exam.label}</h2>
          <div class="exam-header-actions">
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
