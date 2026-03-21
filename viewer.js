/**
 * 共通テスト英語問題DB - Viewer
 * 見開きページ型学習ビューア
 */

// ===== レジストリ（app.jsと共通） =====
const EXAM_PATHS = {
  sundai_2025_01: 'data/sundai/2025/round01/data.json'
};

// ===== State =====
let currentData = null;
let currentSection = null;
let currentDataPath = '';
let showJa = false;
let showExplain = false;

// ===== Init =====
document.addEventListener('DOMContentLoaded', async () => {
  const params = new URLSearchParams(location.search);
  const examId = params.get('exam') || 'sundai_2025_01';
  const sectionNum = parseInt(params.get('section') || '1');

  const dataPath = EXAM_PATHS[examId];
  currentDataPath = dataPath;
  if (!dataPath) {
    document.getElementById('passage-content').innerHTML = '<p class="pane-loading">試験データが見つかりません。</p>';
    return;
  }

  try {
    const resp = await fetch(dataPath);
    currentData = await resp.json();
  } catch (e) {
    document.getElementById('passage-content').innerHTML = '<p class="pane-loading">データの読み込みに失敗しました。</p>';
    return;
  }

  currentSection = currentData.sections.find(s => s.section_number === sectionNum);
  if (!currentSection) {
    document.getElementById('passage-content').innerHTML = '<p class="pane-loading">この大問のデータはまだありません。</p>';
    return;
  }

  // Set title
  const info = currentData.exam_info;
  document.getElementById('viewer-title').textContent =
    `${info.title} 第${info.round}回 — ${currentSection.title}`;
  document.title = `${currentSection.title} — 共通テスト英語問題DB`;

  // Render
  renderPassage();
  renderQuestions();

  // Setup controls
  setupControls();
  setupDivider();
});

// ===== Render Passage (Left Pane) =====
function renderPassage() {
  const sec = currentSection;
  const secNum = sec.section_number;
  // Audio base path: derive from exam data path
  const audioBase = currentDataPath.replace(/data\.json$/, 'audio/');
  let html = '';

  // Section header
  html += `<div class="passage-header">
    <div class="section-label">${sec.title}</div>
    <div class="section-points">配点 ${sec.points}点（各${sec.points_per_question}点×${sec.questions.length}問）</div>
  </div>`;

  // Situation
  if (sec.situation) {
    html += `<div class="situation-box">${sec.situation.en}</div>`;
  }

  // Passages — grouped in one bordered container like the original exam
  html += '<div class="passage-container">';

  const passages = sec.passages;
  for (let i = 0; i < passages.length; i++) {
    const passage = passages[i];
    const isHeader = passage.id === 'header';
    const isFirst = i === 0;

    // Separator between tour sections (not before first)
    if (!isFirst) {
      html += '<hr class="passage-divider">';
    }

    // Section within the passage box
    html += `<div class="passage-section${isHeader ? ' passage-section--header' : ''}">`;

    if (passage.title && !(passage.margin_comments && passage.margin_comments.length > 0)) {
      html += `<div class="passage-title">${passage.title.en}</div>`;
    }
    if (passage.subtitle) {
      html += `<div class="passage-subtitle">${passage.subtitle.en}</div>`;
    }

    // Image (float right/left like original exam)
    if (passage.image) {
      const floatClass = passage.image.float === 'left' ? 'passage-img--left' : 'passage-img--right';
      html += `<img class="passage-img ${floatClass}" src="${passage.image.src}" alt="${passage.image.alt || ''}">`;
    }

    // Sentences as flowing paragraph (inline spans) + audio button
    if (passage.sentences) {
      const audioFile = `${audioBase}s${secNum}_${passage.id}.mp3`;
      html += '<div class="para-audio-row">';
      html += '<div class="para-content">';
      html += '<p class="passage-paragraph">';
      for (const sent of passage.sentences) {
        html += `<span class="sentence" data-sid="${sent.id}">${sent.en}</span> `;
      }
      html += '</p>';
      html += '<div class="passage-ja-block">';
      for (const sent of passage.sentences) {
        html += `<span class="sentence-ja" data-sid-ja="${sent.id}">${sent.ja}</span>`;
      }
      html += '</div>';
      html += '</div>';
      html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
      html += '</div>';
    }

    // Paragraphs: multiple <p> blocks with per-paragraph audio buttons
    if (passage.paragraphs) {
      // If margin_comments exist, use two-column table layout
      const hasComments = passage.margin_comments && passage.margin_comments.length > 0;

      if (hasComments) {
        html += '<table class="essay-table"><thead><tr>';
        html += '<th class="essay-col-main">' + (passage.title ? passage.title.en : '') + '</th>';
        html += '<th class="essay-col-comments">Comments</th>';
        html += '</tr></thead><tbody>';
      }

      for (let pi = 0; pi < passage.paragraphs.length; pi++) {
        const para = passage.paragraphs[pi];
        const audioFile = `${audioBase}s${secNum}_${passage.id}_p${pi + 1}.mp3`;

        if (hasComments) {
          // Find comment markers in this paragraph
          const paraComments = [];
          for (const sent of para) {
            if (sent.comment_marker) {
              const mc = passage.margin_comments.find(c => c.marker === sent.comment_marker);
              if (mc) paraComments.push(mc);
            }
          }

          html += '<tr><td class="essay-cell-main">';
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          html += '<p class="passage-paragraph">';
          for (const sent of para) {
            if (sent.comment_marker) {
              html += '<sup class="comment-marker">' + sent.comment_marker + '</sup>';
            }
            html += '<span class="sentence" data-sid="' + sent.id + '">' + sent.en + '</span> ';
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const sent of para) {
            html += '<div class="sentence-ja" data-sid-ja="' + sent.id + '">' + sent.ja + '</div>';
          }
          html += '</div>';
          html += '</div>';
          html += '<button class="btn-audio" data-audio="' + audioFile + '" title="読み上げ">🔊</button>';
          html += '</div>';
          html += '</td>';

          // Comments column
          html += '<td class="essay-cell-comments">';
          for (const mc of paraComments) {
            html += '<div class="margin-comment">';
            html += '<em>' + mc.marker + ' ' + mc.en + '</em>';
            html += '<div class="choice-text-ja">' + mc.ja + '</div>';
            html += '</div>';
          }
          html += '</td></tr>';
        } else {
          // Normal paragraph rendering
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          html += '<p class="passage-paragraph">';
          for (const sent of para) {
            html += `<span class="sentence" data-sid="${sent.id}">${sent.en}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const sent of para) {
            html += `<div class="sentence-ja" data-sid-ja="${sent.id}">${sent.ja}</div>`;
          }
          html += '</div>';
          html += '</div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
        }
      }

      // Teacher's comment
      if (passage.teacher_comment) {
        if (hasComments) {
          html += '<tr><td colspan="2" class="essay-teacher-comment">';
        } else {
          html += '<div class="essay-teacher-comment">';
        }
        html += '<strong>Teacher\'s Comment</strong><br>';
        html += passage.teacher_comment.en;
        html += '<div class="choice-text-ja">' + passage.teacher_comment.ja + '</div>';
        if (hasComments) {
          html += '</td></tr>';
        } else {
          html += '</div>';
        }
      }

      if (hasComments) {
        html += '</tbody></table>';
      }
    }

    // ===== Questionnaire rendering =====
    if (passage.id === 'questionnaire') {
      // Q1 title
      if (passage.q1_title) {
        html += `<div class="questionnaire-q-title">${passage.q1_title.en}</div>`;
      }
      // Bar chart image (user-provided screenshot)
      if (passage.chart_image) {
        html += `<div class="chart-image-container"><img class="chart-image" src="${passage.chart_image.src}" alt="${passage.chart_image.alt || 'Chart'}"></div>`;
      } else if (passage.chart_data) {
        // Fallback: simple image if chart_image not set
        const imgBase = currentDataPath.replace(/data\.json$/, 'images/');
        html += `<div class="chart-image-container"><img class="chart-image" src="${imgBase}s5_questionnaire_chart.png" alt="Questionnaire Chart"></div>`;
      }
      // Q2 title + comments
      if (passage.q2_title) {
        html += `<div class="questionnaire-q-title" style="margin-top:20px;">${passage.q2_title.en}</div>`;
      }
      if (passage.comments) {
        html += `<div class="questionnaire-comments-label">Main comments:</div>`;
        for (const c of passage.comments) {
          html += `<div class="student-comment">
            <span class="sentence" data-sid="${c.id}"><strong>${c.label === 'S1' ? 'Student 1 (S1)' : c.label}:</strong> ${c.en}</span>
            <div class="sentence-ja" data-sid-ja="${c.id}">${c.ja}</div>
          </div>`;
        }
      }
    }

    // ===== Handout rendering =====
    if (passage.is_handout) {
      if (passage.sections_content) {
        for (const sec of passage.sections_content) {
          html += `<div class="handout-section">`;
          html += `<div class="handout-heading">■ ${sec.heading.en}</div>`;
          if (sec.items) {
            for (const item of sec.items) {
              const itemEn = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="handout-item">－ ${itemEn}</div>`;
            }
          }
          if (sec.sub_items) {
            for (const sub of sec.sub_items) {
              html += `<div class="handout-sub-item">`;
              html += `<div class="handout-sub-label">－ ${sub.label.en}</div>`;
              if (sub.content) {
                const contentEn = sub.content.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="handout-sub-content">${contentEn}</div>`;
              }
              if (sub.options) {
                html += `<div class="handout-options">`;
                if (sub.blank_number) {
                  html += `<div class="answer-slot" style="margin-bottom:6px;">${sub.blank_number}</div>`;
                }
                for (const opt of sub.options) {
                  html += `<div class="handout-option">${opt.label}.  ${opt.en}</div>`;
                }
                html += `</div>`;
              }
              html += `</div>`;
            }
          }
          html += `</div>`;
        }
      }
    }

    html += '</div>';
  }

  html += '</div>'; // .passage-container

  document.getElementById('passage-content').innerHTML = html;

  // Bind sentence click for translation popup
  setupSentencePopup();

  // Bind audio play buttons
  setupAudioButtons();
}

// ===== Sentence Translation Popup =====
function setupSentencePopup() {
  const pane = document.getElementById('pane-passage');

  pane.addEventListener('click', (e) => {
    const sent = e.target.closest('.sentence.highlighted');

    // Close existing popup
    const existing = document.querySelector('.sentence-popup');
    if (existing) existing.remove();

    if (!sent) return;

    const sid = sent.dataset.sid;
    if (!sid) return;

    // Find the Japanese translation from the data
    const ja = findSentenceJa(sid);
    if (!ja) return;

    // Create popup
    const popup = document.createElement('div');
    popup.className = 'sentence-popup';
    popup.innerHTML = `<span class="popup-close">✕</span>${ja}`;

    // Position relative to sentence
    const rect = sent.getBoundingClientRect();
    const paneRect = pane.getBoundingClientRect();
    popup.style.left = `${rect.left - paneRect.left + pane.scrollLeft}px`;
    popup.style.top = `${rect.bottom - paneRect.top + pane.scrollTop + 8}px`;

    pane.querySelector('.pane-inner').appendChild(popup);

    // Close on button click
    popup.querySelector('.popup-close').addEventListener('click', (ev) => {
      ev.stopPropagation();
      popup.remove();
    });
  });

  // Close popup when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.sentence.highlighted') && !e.target.closest('.sentence-popup')) {
      const existing = document.querySelector('.sentence-popup');
      if (existing) existing.remove();
    }
  });
}

// ===== Find sentence Japanese translation =====
function findSentenceJa(sid) {
  for (const passage of currentSection.passages) {
    if (passage.sentences) {
      const sent = passage.sentences.find(s => s.id === sid);
      if (sent) return sent.ja;
    }
    if (passage.paragraphs) {
      for (const para of passage.paragraphs) {
        const sent = para.find(s => s.id === sid);
        if (sent) return sent.ja;
      }
    }
  }
  return null;
}

// ===== Audio Playback =====
let currentAudio = null;
let currentAudioBtn = null;

function setupAudioButtons() {
  document.querySelectorAll('.btn-audio').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const src = btn.dataset.audio;

      // If same button clicked again, stop
      if (currentAudio && currentAudioBtn === btn) {
        currentAudio.pause();
        currentAudio = null;
        btn.textContent = '🔊';
        btn.classList.remove('playing');
        currentAudioBtn = null;
        return;
      }

      // Stop any playing audio
      if (currentAudio) {
        currentAudio.pause();
        currentAudioBtn.textContent = '🔊';
        currentAudioBtn.classList.remove('playing');
      }

      // Play new
      currentAudio = new Audio(src);
      currentAudioBtn = btn;
      btn.textContent = '⏸';
      btn.classList.add('playing');

      currentAudio.play().catch(() => {
        btn.textContent = '🔊';
        btn.classList.remove('playing');
      });

      currentAudio.addEventListener('ended', () => {
        btn.textContent = '🔊';
        btn.classList.remove('playing');
        currentAudio = null;
        currentAudioBtn = null;
      });
    });
  });
}

// ===== Render Questions (Right Pane) =====
function renderQuestions() {
  const sec = currentSection;
  let html = '';

  for (const q of sec.questions) {
    const qIdx = getQuestionIndex(q.question_id);
    html += `<div class="question-block" data-qid="${q.question_id}">`;

    // Question label + per-question evidence button
    html += `<div class="question-label-row">
      <span class="question-label">${q.question_id}</span>
      <button class="btn-evidence-q" data-qid="${q.question_id}" data-qidx="${qIdx}" title="根拠箇所をヒント表示">ヒント</button>
    </div>`;

    // Stem
    const stemEn = q.stem.en.replace(
      /\[(\d+)\]/g,
      '<span class="answer-slot">$1</span>'
    );
    html += `<div class="question-stem">${stemEn}</div>`;

    // Stem ja (hidden by default)
    if (q.stem.ja) {
      html += `<div class="choice-text-ja" style="margin-bottom:10px; margin-top:-8px;">${q.stem.ja}</div>`;
    }

    // Choices — ordering vs normal
    if (q.question_type === 'ordering') {
      // Ordering slots row
      const slotCount = q.answer_sequence.length;
      html += '<div class="ordering-slots" data-qid="' + q.question_id + '">';
      for (let si = 0; si < slotCount; si++) {
        if (si > 0) html += '<span class="ordering-arrow">→</span>';
        html += '<span class="ordering-slot" data-slot="' + si + '"></span>';
      }
      html += '</div>';

      // Ordering choice buttons
      html += '<div class="ordering-choices" data-qid="' + q.question_id + '">';
      for (const choice of q.choices) {
        html += '<button class="ordering-btn" data-qid="' + q.question_id + '" data-label="' + choice.label + '">'
          + '<span class="ordering-btn-label">' + choice.label + '</span>'
          + '<span class="ordering-btn-text">' + choice.en + '</span>'
          + '<div class="choice-text-ja">' + (choice.ja || '') + '</div>'
          + '</button>';
      }
      html += '</div>';
      // Undo button
      html += '<button class="ordering-undo" data-qid="' + q.question_id + '" title="取り消し" style="display:none;">↩ 戻す</button>';
    } else if (q.answer_numbers) {
      // Multiple answer: slot-based UI (select all before checking)
      html += '<div class="multi-answer-slots" data-qid="' + q.question_id + '">';
      for (let ai = 0; ai < q.answer_numbers.length; ai++) {
        const ansNum = q.answer_numbers[ai];
        if (ai > 0) html += '<span class="ordering-arrow">＋</span>';
        html += '<span class="ordering-slot multi-slot" data-slot="' + ansNum + '">[' + ansNum + ']</span>';
      }
      html += '</div>';
      for (const ansNum of q.answer_numbers) {
        const choicesKey = `choices_${ansNum}`;
        const choices = q[choicesKey];
        if (!choices) continue;
        html += `<div class="multi-answer-group" data-ans-num="${ansNum}">`;
        html += `<div class="multi-answer-label">[${ansNum}]</div>`;
        html += '<ul class="choices">';
        for (const choice of choices) {
          html += `<li class="choice-item multi-choice" data-qid="${q.question_id}" data-ans-num="${ansNum}" data-label="${choice.label}">
            <span class="choice-label">${choice.label}</span>
            <span class="choice-text">
              ${choice.en}
              <div class="choice-text-ja">${choice.ja || ''}</div>
            </span>
          </li>`;
        }
        html += '</ul></div>';
      }
      html += '<button class="ordering-undo multi-undo" data-qid="' + q.question_id + '" title="取り消し" style="display:none;">↩ 戻す</button>';
    } else if (q.choices) {
      // Normal choices
      html += '<ul class="choices">';
      for (const choice of q.choices) {
        html += `<li class="choice-item" data-qid="${q.question_id}" data-label="${choice.label}" data-correct="${choice.is_correct}">
          <span class="choice-label">${choice.label}</span>
          <span class="choice-text">
            ${choice.en}
            <div class="choice-text-ja">${choice.ja || ''}</div>
          </span>
        </li>`;
      }
      html += '</ul>';
    }

    // Explanation
    html += renderExplanation(q);

    html += '</div>';
  }

  document.getElementById('questions-content').innerHTML = html;

  // Bind choice click events (exclude multi-choice items)
  document.querySelectorAll('.choice-item:not(.multi-choice)').forEach(el => {
    el.addEventListener('click', handleChoiceClick);
  });

  // Bind per-question evidence buttons
  document.querySelectorAll('.btn-evidence-q').forEach(el => {
    el.addEventListener('click', handlePerQuestionEvidence);
  });

  // Bind ordering buttons (excluding multi-btn)
  document.querySelectorAll('.ordering-btn:not(.multi-btn)').forEach(btn => {
    btn.addEventListener('click', handleOrderingClick);
  });
  document.querySelectorAll('.ordering-undo:not(.multi-undo)').forEach(btn => {
    btn.addEventListener('click', handleOrderingUndo);
  });

  // Bind multi-answer choices
  document.querySelectorAll('.multi-choice').forEach(el => {
    el.addEventListener('click', handleMultiAnswerClick);
  });
  document.querySelectorAll('.multi-undo').forEach(btn => {
    btn.addEventListener('click', handleMultiAnswerUndo);
  });
}

// ===== Render Explanation =====
function renderExplanation(q) {
  if (!q.explanation) return '';

  let html = `<div class="explanation-box" data-qid="${q.question_id}">`;
  html += `<div class="explanation-header">📖 解説（${q.question_id}）</div>`;
  html += `<div class="explanation-text">
    <strong>正解: ${q.answer}</strong> ─ ${q.explanation.ja}
  </div>`;

  // Others wrong
  if (q.explanation.why_others_wrong && q.explanation.why_others_wrong.length > 0) {
    html += `<div class="explanation-toggle" data-qid="${q.question_id}">▶ 他の選択肢の解説</div>`;
    html += `<div class="others-wrong" data-qid="${q.question_id}">`;
    for (const ow of q.explanation.why_others_wrong) {
      html += `<div class="wrong-reason"><strong>${ow.choice}</strong> ${ow.reason}</div>`;
    }
    html += '</div>';
  }

  html += '</div>';
  return html;
}

// ===== Ordering Click Handler =====
function handleOrderingClick(e) {
  const btn = e.currentTarget;
  const qid = btn.dataset.qid;
  const label = btn.dataset.label;

  // Already used or already judged
  if (btn.classList.contains('used')) return;
  const slotsContainer = document.querySelector(`.ordering-slots[data-qid="${qid}"]`);
  if (slotsContainer.classList.contains('judged')) return;

  // Find next empty slot
  const slots = slotsContainer.querySelectorAll('.ordering-slot');
  let targetSlot = null;
  for (const s of slots) {
    if (!s.dataset.label) { targetSlot = s; break; }
  }
  if (!targetSlot) return;

  // Fill slot
  targetSlot.textContent = label;
  targetSlot.dataset.label = label;
  targetSlot.classList.add('filled');
  btn.classList.add('used');

  // Show undo
  const undoBtn = document.querySelector(`.ordering-undo[data-qid="${qid}"]`);
  undoBtn.style.display = 'inline-block';

  // Check if all slots filled
  const allFilled = [...slots].every(s => s.dataset.label);
  if (allFilled) {
    // Judge
    const q = currentSection.questions.find(q => q.question_id === qid);
    const userSeq = [...slots].map(s => {
      // Extract number from label like "①" → 1
      const m = s.dataset.label.match(/[①②③④⑤⑥⑦⑧]/);
      if (m) return '①②③④⑤⑥⑦⑧'.indexOf(m[0]) + 1;
      return parseInt(s.dataset.label);
    });
    const isCorrect = JSON.stringify(userSeq) === JSON.stringify(q.answer_sequence);

    slotsContainer.classList.add('judged', isCorrect ? 'correct' : 'wrong');
    undoBtn.style.display = 'none';

    // If wrong, show correct answer
    if (!isCorrect) {
      const correctText = q.answer;
      const correctDiv = document.createElement('div');
      correctDiv.className = 'ordering-correct-answer';
      correctDiv.textContent = '正解: ' + correctText;
      slotsContainer.parentNode.insertBefore(correctDiv, slotsContainer.nextSibling);
    }

    // Show explanation
    const explBox = document.querySelector(`.explanation-box[data-qid="${qid}"]`);
    if (explBox) explBox.classList.add('visible');

    // Highlight evidence
    highlightEvidence(qid);
  }
}

// ===== Ordering Undo =====
function handleOrderingUndo(e) {
  const qid = e.currentTarget.dataset.qid;
  const slotsContainer = document.querySelector(`.ordering-slots[data-qid="${qid}"]`);
  if (slotsContainer.classList.contains('judged')) return;

  const slots = [...slotsContainer.querySelectorAll('.ordering-slot')];
  // Find last filled slot
  for (let i = slots.length - 1; i >= 0; i--) {
    if (slots[i].dataset.label) {
      const label = slots[i].dataset.label;
      slots[i].textContent = '';
      delete slots[i].dataset.label;
      slots[i].classList.remove('filled');
      // Re-enable button
      const btn = document.querySelector(`.ordering-btn[data-qid="${qid}"][data-label="${label}"]`);
      if (btn) btn.classList.remove('used');
      break;
    }
  }

  // Hide undo if no slots filled
  const anyFilled = slots.some(s => s.dataset.label);
  if (!anyFilled) {
    e.currentTarget.style.display = 'none';
  }
}

// ===== Multi-Answer Click Handler =====
function handleMultiAnswerClick(e) {
  const btn = e.currentTarget;
  const qid = btn.dataset.qid;
  const ansNum = btn.dataset.ansNum;
  const label = btn.dataset.label;

  const slotsContainer = document.querySelector(`.multi-answer-slots[data-qid="${qid}"]`);
  if (slotsContainer && slotsContainer.classList.contains('judged')) return;

  // Remove previous selection in this group
  document.querySelectorAll(`.multi-choice[data-qid="${qid}"][data-ans-num="${ansNum}"]`).forEach(el => {
    el.classList.remove('selected');
  });
  btn.classList.add('selected');

  // Fill the corresponding slot
  const slot = slotsContainer.querySelector(`.multi-slot[data-slot="${ansNum}"]`);
  if (slot) {
    slot.textContent = label;
    slot.dataset.label = label;
    slot.classList.add('filled');
  }

  // Show undo
  const undoBtn = document.querySelector(`.multi-undo[data-qid="${qid}"]`);
  if (undoBtn) undoBtn.style.display = 'inline-block';

  // Check if all slots filled
  const allSlots = slotsContainer.querySelectorAll('.multi-slot');
  const allFilled = [...allSlots].every(s => s.dataset.label);
  if (!allFilled) return;

  // Judge all answers
  const q = currentSection.questions.find(q => q.question_id === qid);
  if (!q) return;

  let allCorrect = true;
  for (const s of allSlots) {
    const num = s.dataset.slot;
    const userLabel = s.dataset.label;
    const correctLabel = q.answer && q.answer[String(num)];
    if (userLabel !== correctLabel) {
      allCorrect = false;
      break;
    }
  }

  slotsContainer.classList.add('judged', allCorrect ? 'correct' : 'wrong');
  if (undoBtn) undoBtn.style.display = 'none';

  // Mark choices as correct/wrong
  for (const num of q.answer_numbers) {
    const correctLabel = q.answer[String(num)];
    const selectedEl = document.querySelector(`.multi-choice[data-qid="${qid}"][data-ans-num="${num}"].selected`);
    if (selectedEl) {
      if (selectedEl.dataset.label === correctLabel) {
        selectedEl.classList.add('correct');
      } else {
        selectedEl.classList.add('wrong');
        // Also highlight the correct one
        document.querySelectorAll(`.multi-choice[data-qid="${qid}"][data-ans-num="${num}"]`).forEach(el => {
          if (el.dataset.label === correctLabel) el.classList.add('correct');
        });
      }
    }
  }

  // If wrong, show correct
  if (!allCorrect) {
    let correctText = '正解: ';
    for (const num of q.answer_numbers) {
      correctText += `[${num}] ${q.answer[String(num)]}  `;
    }
    const correctDiv = document.createElement('div');
    correctDiv.className = 'ordering-correct-answer';
    correctDiv.textContent = correctText;
    slotsContainer.parentNode.insertBefore(correctDiv, slotsContainer.nextSibling);
  }

  // Show explanation
  const explBox = document.querySelector(`.explanation-box[data-qid="${qid}"]`);
  if (explBox) explBox.classList.add('visible');

  // Highlight evidence
  highlightEvidence(qid);
}

// ===== Multi-Answer Undo =====
function handleMultiAnswerUndo(e) {
  const qid = e.currentTarget.dataset.qid;
  const slotsContainer = document.querySelector(`.multi-answer-slots[data-qid="${qid}"]`);
  if (!slotsContainer || slotsContainer.classList.contains('judged')) return;

  const slots = [...slotsContainer.querySelectorAll('.multi-slot')];
  // Find last filled slot
  for (let i = slots.length - 1; i >= 0; i--) {
    if (slots[i].dataset.label) {
      const ansNum = slots[i].dataset.slot;
      const label = slots[i].dataset.label;
      slots[i].textContent = '[' + ansNum + ']';
      delete slots[i].dataset.label;
      slots[i].classList.remove('filled');
      // Un-select the choice
      document.querySelectorAll(`.multi-choice[data-qid="${qid}"][data-ans-num="${ansNum}"]`).forEach(el => {
        el.classList.remove('selected');
      });
      break;
    }
  }

  const anyFilled = slots.some(s => s.dataset.label);
  if (!anyFilled) e.currentTarget.style.display = 'none';
}

// ===== Choice Click Handler =====
function handleChoiceClick(e) {
  const item = e.currentTarget;
  const qid = item.dataset.qid;
  const isCorrect = item.dataset.correct === 'true';

  // Remove previous selections for this question
  document.querySelectorAll(`.choice-item[data-qid="${qid}"]`).forEach(el => {
    el.classList.remove('selected', 'correct', 'wrong');
  });

  // Mark selected
  if (isCorrect) {
    item.classList.add('correct');
  } else {
    item.classList.add('wrong');
    // Also highlight the correct answer
    document.querySelectorAll(`.choice-item[data-qid="${qid}"][data-correct="true"]`).forEach(el => {
      el.classList.add('correct');
    });
  }

  // Show explanation for this question
  const explBox = document.querySelector(`.explanation-box[data-qid="${qid}"]`);
  if (explBox) {
    explBox.classList.add('visible');
  }

  // Highlight evidence sentences in the passage
  highlightEvidence(qid);
}

// ===== Question index (for color mapping) =====
function getQuestionIndex(qid) {
  if (!currentSection) return 0;
  const idx = currentSection.questions.findIndex(q => q.question_id === qid);
  return idx >= 0 ? idx + 1 : 1;
}

// ===== Per-question hint (evidence) button handler =====
let activeHintQid = null;

function handlePerQuestionEvidence(e) {
  const btn = e.currentTarget;
  const qid = btn.dataset.qid;

  // Toggle off if same question
  if (activeHintQid === qid) {
    clearAllEvidence();
    btn.classList.remove('active');
    activeHintQid = null;
    return;
  }

  // Clear previous and deactivate old button
  clearAllEvidence();
  document.querySelectorAll('.btn-evidence-q.active').forEach(b => b.classList.remove('active'));

  // Highlight this question's evidence
  highlightEvidence(qid);
  btn.classList.add('active');
  activeHintQid = qid;
}

// ===== Highlight Evidence Sentences (single question) =====
function highlightEvidence(qid) {
  clearAllEvidence();

  const q = currentSection.questions.find(q => q.question_id === qid);
  if (!q || !q.explanation || !q.explanation.evidence_sentences) return;

  const qIdx = getQuestionIndex(qid);
  for (const sid of q.explanation.evidence_sentences) {
    const el = document.querySelector(`.sentence[data-sid="${sid}"]`);
    if (el) {
      el.classList.add('highlighted', `evidence-q${qIdx}`);
      addEvidenceTag(el, qid, qIdx);
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
}

// ===== Show ALL evidence for ALL questions at once =====
function showAllEvidence() {
  clearAllEvidence();

  for (const q of currentSection.questions) {
    if (!q.explanation || !q.explanation.evidence_sentences) continue;
    const qIdx = getQuestionIndex(q.question_id);

    for (const sid of q.explanation.evidence_sentences) {
      const el = document.querySelector(`.sentence[data-sid="${sid}"]`);
      if (el) {
        el.classList.add('highlighted', `evidence-q${qIdx}`);
        addEvidenceTag(el, q.question_id, qIdx);
      }
    }
  }
}

// ===== Add colored tag to an evidence sentence =====
function addEvidenceTag(el, qid, qIdx) {
  // Don't add duplicate tags
  if (el.querySelector(`.evidence-tag.tag-q${qIdx}`)) return;
  const tag = document.createElement('span');
  tag.className = `evidence-tag tag-q${qIdx}`;
  tag.textContent = qid;
  el.appendChild(tag);
}

// ===== Clear all evidence highlights =====
function clearAllEvidence() {
  document.querySelectorAll('.sentence.highlighted').forEach(el => {
    el.classList.remove('highlighted',
      'evidence-q1','evidence-q2','evidence-q3','evidence-q4',
      'evidence-q5','evidence-q6','evidence-q7','evidence-q8');
    el.querySelectorAll('.evidence-tag').forEach(t => t.remove());
  });
}

// ===== Controls =====
let showEvidence = false;

function setupControls() {
  const btnFullscreen = document.getElementById('btn-fullscreen');
  const btnReset = document.getElementById('btn-reset');
  const btnJa = document.getElementById('btn-toggle-ja');
  const btnEvidence = document.getElementById('btn-toggle-evidence');
  const btnExplain = document.getElementById('btn-toggle-explain');

  // Fullscreen toggle
  btnFullscreen.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen();
    }
  });
  document.addEventListener('fullscreenchange', () => {
    if (document.fullscreenElement) {
      btnFullscreen.textContent = '✕';
      btnFullscreen.title = '全画面を終了';
    } else {
      btnFullscreen.textContent = '⛶';
      btnFullscreen.title = '全画面表示';
    }
  });

  // Reset everything
  btnReset.addEventListener('click', () => {
    // Clear choice selections
    document.querySelectorAll('.choice-item').forEach(el => {
      el.classList.remove('selected', 'correct', 'wrong');
    });
    // Hide explanations
    showExplain = false;
    btnExplain.classList.remove('active');
    document.querySelectorAll('.explanation-box').forEach(el => el.classList.remove('visible'));
    // Clear evidence
    showEvidence = false;
    btnEvidence.classList.remove('active');
    clearAllEvidence();
    // Clear per-question hint buttons
    activeHintQid = null;
    document.querySelectorAll('.btn-evidence-q.active').forEach(b => b.classList.remove('active'));
    // Hide translations
    showJa = false;
    btnJa.classList.remove('active');
    document.body.classList.remove('show-ja');
    // Remove popups
    document.querySelectorAll('.sentence-popup').forEach(p => p.remove());
    // Reset ordering questions
    document.querySelectorAll('.ordering-slots').forEach(sc => {
      sc.classList.remove('judged', 'correct', 'wrong');
      sc.querySelectorAll('.ordering-slot').forEach(s => {
        s.textContent = '';
        delete s.dataset.label;
        s.classList.remove('filled');
      });
    });
    document.querySelectorAll('.ordering-btn').forEach(b => b.classList.remove('used'));
    document.querySelectorAll('.ordering-undo').forEach(b => { b.style.display = 'none'; });
    document.querySelectorAll('.ordering-correct-answer').forEach(el => el.remove());
    // Reset multi-answer questions
    document.querySelectorAll('.multi-answer-slots').forEach(sc => {
      sc.classList.remove('judged', 'correct', 'wrong');
      sc.querySelectorAll('.multi-slot').forEach(s => {
        const ansNum = s.dataset.slot;
        s.textContent = '[' + ansNum + ']';
        delete s.dataset.label;
        s.classList.remove('filled');
      });
    });
    document.querySelectorAll('.multi-choice').forEach(el => el.classList.remove('selected', 'correct', 'wrong'));
    document.querySelectorAll('.multi-undo').forEach(b => { b.style.display = 'none'; });
    // Collapse others-wrong
    document.querySelectorAll('.others-wrong.open').forEach(el => el.classList.remove('open'));
    document.querySelectorAll('.explanation-toggle').forEach(el => el.textContent = '▶ 他の選択肢の解説');
    // Stop audio
    if (currentAudio) {
      currentAudio.pause();
      currentAudio = null;
    }
    if (currentAudioBtn) {
      currentAudioBtn.textContent = '🔊';
      currentAudioBtn.classList.remove('playing');
      currentAudioBtn = null;
    }
    // Scroll both panes to top
    document.getElementById('pane-passage').scrollTop = 0;
    document.getElementById('pane-questions').scrollTop = 0;
  });

  btnJa.addEventListener('click', () => {
    showJa = !showJa;
    btnJa.classList.toggle('active', showJa);
    document.body.classList.toggle('show-ja', showJa);
  });

  // Evidence only (no explanations)
  btnEvidence.addEventListener('click', () => {
    showEvidence = !showEvidence;
    btnEvidence.classList.toggle('active', showEvidence);
    if (showEvidence) {
      showAllEvidence();
    } else {
      clearAllEvidence();
    }
  });

  btnExplain.addEventListener('click', () => {
    showExplain = !showExplain;
    btnExplain.classList.toggle('active', showExplain);
    document.querySelectorAll('.explanation-box').forEach(el => {
      el.classList.toggle('visible', showExplain);
    });
    // Show/hide correct answers
    if (showExplain) {
      document.querySelectorAll('.choice-item[data-correct="true"]').forEach(el => {
        el.classList.add('correct');
      });
    } else {
      // Only remove correct class if not individually answered
      document.querySelectorAll('.choice-item.correct').forEach(el => {
        const qid = el.dataset.qid;
        const hasWrong = document.querySelector(`.choice-item.wrong[data-qid="${qid}"]`);
        if (!hasWrong) el.classList.remove('correct');
      });
    }
    // Also show/hide evidence
    if (showExplain) {
      showEvidence = true;
      btnEvidence.classList.add('active');
      showAllEvidence();
    } else {
      showEvidence = false;
      btnEvidence.classList.remove('active');
      clearAllEvidence();
    }
  });

  // Others-wrong toggles (delegated)
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('explanation-toggle')) {
      const qid = e.target.dataset.qid;
      const panel = document.querySelector(`.others-wrong[data-qid="${qid}"]`);
      if (panel) {
        panel.classList.toggle('open');
        e.target.textContent = panel.classList.contains('open')
          ? '▼ 他の選択肢の解説'
          : '▶ 他の選択肢の解説';
      }
    }
  });
}

// ===== Draggable Divider =====
function setupDivider() {
  const divider = document.getElementById('pane-divider');
  const leftPane = document.getElementById('pane-passage');
  const container = document.querySelector('.viewer-split');
  let isDragging = false;

  divider.addEventListener('mousedown', (e) => {
    isDragging = true;
    divider.classList.add('dragging');
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
    e.preventDefault();
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const containerRect = container.getBoundingClientRect();
    const newWidth = e.clientX - containerRect.left;
    const pct = (newWidth / containerRect.width) * 100;
    if (pct > 20 && pct < 80) {
      leftPane.style.flex = `0 0 ${pct}%`;
    }
  });

  document.addEventListener('mouseup', () => {
    if (isDragging) {
      isDragging = false;
      divider.classList.remove('dragging');
      document.body.style.cursor = '';
      document.body.style.userSelect = '';
    }
  });
}
