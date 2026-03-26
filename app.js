/**
 * 共通テスト英語問題DB - Landing Page Application
 * レジストリからデータを読み込みカード一覧を描画
 */

// ===== レジストリ: 問題集・回の一覧 =====
const EXAM_REGISTRY = [
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

  try {
    let html = '';
    for (let i = 0; i < EXAM_REGISTRY.length; i++) {
      html += await renderExamBlock(EXAM_REGISTRY[i], i);
    }
    loading.style.display = 'none';
    app.insertAdjacentHTML('beforeend', html);
  } catch (err) {
    loading.textContent = 'データの読み込みに失敗しました。';
    console.error(err);
  }
});

// ===== 問題集ブロックの描画 =====
async function renderExamBlock(exam, index) {
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

    const clickHandler = isReady ? `onclick="location.href='viewer.html?exam=${exam.id}&section=${num}'"` : '';

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

  const isOpen = index === 0 ? 'open' : '';
  return `
    <section class="exam-block">
      <details class="exam-details" ${isOpen}>
        <summary class="exam-block-header">
          <h2 class="exam-block-title"><span class="icon">${exam.icon}</span>${exam.label}</h2>
          <a href="print.html?exam=${exam.id}&mode=all" class="btn-print-all" onclick="event.stopPropagation()" title="全問題を印刷">🖨 全問題印刷</a>
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
