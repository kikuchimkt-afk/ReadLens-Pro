/**
 * 共通テスト英語問題DB - Viewer
 * 見開きページ型学習ビューア
 */

// ===== レジストリ（app.jsと共通） =====
const EXAM_PATHS = {
  sundai_2026_01: 'data/sundai/2026/round01/data.json',
  sundai_2025_01: 'data/sundai/2025/round01/data.json',
  sundai_2025_02: 'data/sundai/2025/round02/data.json',
  sundai_2025_03: 'data/sundai/2025/round03/data.json',
  sundai_2025_04: 'data/sundai/2025/round04/data.json',
  kakomon_2025: 'data/kakomon/2025/data.json',
  kakomon_2024: 'data/kakomon/2024/data.json',
  kakomon_2023: 'data/kakomon/2023/data.json',
  kakomon_2022: 'data/kakomon/2022/data.json',
  kakomon_2021_1: 'data/kakomon/2021_1/data.json'
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
  const sectionParam = params.get('section') || '1';
  const sectionNum = /^\d+$/.test(sectionParam) ? parseInt(sectionParam) : sectionParam;

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

  currentSection = currentData.sections.find(s => String(s.section_number) === String(sectionNum));
  if (!currentSection) {
    document.getElementById('passage-content').innerHTML = '<p class="pane-loading">この大問のデータはまだありません。</p>';
    return;
  }

  // Set title
  const info = currentData.exam_info;
  const roundLabel = typeof info.round === 'number' ? `第${info.round}回` : info.round;
  document.getElementById('viewer-title').textContent =
    `${info.title} ${roundLabel} — ${currentSection.title}`;
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

  // Flatten subsections if present (6AB format: sections 1-5 have A/B subsections)
  if (sec.subsections && !sec._flattened) {
    sec.passages = [];
    sec.questions = [];
    for (const sub of sec.subsections) {
      // Add situation as a separator passage
      if (sub.situation) {
        sec.passages.push({
          id: `subsection_${sub.label}_header`,
          is_subsection_header: true,
          subsection_label: sub.label,
          situation: sub.situation
        });
      }
      if (sub.passages) sec.passages.push(...sub.passages);
      if (sub.questions) {
        for (const q of sub.questions) q._subsectionLabel = sub.label;
        sec.questions.push(...sub.questions);
      }
    }
    sec._flattened = true;
  }

  // Section header
  const allQuestions = sec.questions || [];
  html += `<div class="passage-header">
    <div class="section-label">${sec.title}</div>
    <div class="section-points">配点 ${sec.points}点${sec.points_per_question ? `（各${sec.points_per_question}点×${allQuestions.length}問）` : `（${allQuestions.length}問）`}</div>
  </div>`;

  // Situation (skip for subsections — each subsection has its own)
  if (sec.situation && !sec.subsections) {
    html += `<div class="situation-box">${sec.situation.en}</div>`;
  }

  // Passages — grouped in one bordered container like the original exam
  html += '<div class="passage-container">';

  const passages = sec.passages;
  for (let i = 0; i < passages.length; i++) {
    const passage = passages[i];
    const isHeader = passage.id === 'header' || (passage.id && passage.id.startsWith('header_'));
    const isFirst = i === 0;

    // Subsection header (A/B separator for 6AB format)
    if (passage.is_subsection_header) {
      if (!isFirst) html += '</div>'; // close previous passage-container
      html += `<div class="subsection-label">${sec.title} ${passage.subsection_label}</div>`;
      if (passage.situation) {
        const sitText = typeof passage.situation === 'string' ? passage.situation : passage.situation.en;
        html += `<div class="situation-box">${sitText}</div>`;
      }
      html += '<div class="passage-container">';
      continue;
    }

    // Separator between tour sections (not before first, not if no_divider)
    if (!isFirst && !passages[i-1]?.is_subsection_header && !passage.no_divider) {
      html += '<hr class="passage-divider">';
    }

    // Section within the passage box
    const hasPortrait = passage.portrait_image ? ' has-portrait' : '';
    html += `<div class="passage-section${isHeader ? ' passage-section--header' : ''}${hasPortrait}">`;

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
    // Portrait image with caption (float, 大問7)
    if (passage.portrait_image) {
      const imgBase = currentDataPath.replace(/data\.json$/, '');
      const floatSide = passage.portrait_image.float === 'left' ? 'left' : 'right';
      html += `<div class="portrait-container" style="float:${floatSide};">`;
      html += `<img class="portrait-img" src="${imgBase}${passage.portrait_image.src}" alt="${passage.portrait_image.alt || ''}">`;
      if (passage.portrait_image.alt) {
        html += `<div class="portrait-caption">${passage.portrait_image.alt}</div>`;
      }
      html += `</div>`;
    }

    // Presentation slides (大問8)
    if (passage.is_presentation && passage.slides) {
      html += '<div class="slides-grid">';
      for (const slide of passage.slides) {
        html += '<div class="slide-card">';
        html += '<div class="slide-title">' + (slide.title ? slide.title.en.replace(/\n/g, '<br>') : '') + '</div>';
        // Slide 1: image
        if (slide.has_image) {
          html += '<img class="slide-img" src="' + currentDataPath.replace(/data\.json$/, 'images/s8_slide1.png') + '" alt="Vegetables">';
        }
        // Slide with two columns (e.g., Characteristics)
        if (slide.columns) {
          html += '<table class="slide-columns"><tr>';
          for (const col of slide.columns) {
            html += '<td><div class="slide-col-heading">' + col.heading.en + '</div><ul>';
            for (const item of col.items) {
              const txt = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += '<li>' + txt + '</li>';
            }
            html += '</ul></td>';
          }
          html += '</tr></table>';
        }
        // Slide with content text
        if (slide.content) {
          const txt = slide.content.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += '<p class="slide-content">' + txt + '</p>';
        }
        // Slide with options (A-E list)
        if (slide.options) {
          html += '<div class="slide-options">';
          for (const opt of slide.options) {
            html += '<div>' + opt.label + '. ' + opt.en + '</div>';
          }
          html += '</div>';
        }
        // Slide with bullet items
        if (slide.items) {
          html += '<ul class="slide-items">';
          for (const item of slide.items) {
            const txt = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += '<li>' + txt + '</li>';
          }
          html += '</ul>';
        }
        html += '<div class="slide-number">' + slide.number + '</div>';
        html += '</div>';
      }
      html += '</div>';
    }

    // Sentences rendering
    if (passage.sentences) {
      const audioFile = `${audioBase}s${secNum}_${passage.id}.mp3`;

      if (passage.advertisement_sections) {
        // ===== Structured advertisement rendering =====
        const sentMap = {};
        for (const s of passage.sentences) sentMap[s.id] = s;

        html += '<div class="para-audio-row">';
        html += '<div class="para-content">';
        html += '<div class="ad-box">';

        for (const adSec of passage.advertisement_sections) {
          // Section heading with separator
          if (adSec.heading) {
            html += '<hr class="ad-separator">';
            html += `<div class="ad-section-heading"><strong>${adSec.heading.en}</strong></div>`;
          }

          if (adSec.type === 'intro') {
            // Intro text as normal paragraph
            html += '<p class="passage-paragraph">';
            for (const sid of adSec.sentence_ids) {
              const s = sentMap[sid];
              if (s) html += `<span class="sentence" data-sid="${s.id}">${s.en}</span> `;
            }
            html += '</p>';
            html += '<div class="passage-ja-block">';
            for (const sid of adSec.sentence_ids) {
              const s = sentMap[sid];
              if (s) html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
            }
            html += '</div>';
          } else if (adSec.type === 'bullet') {
            // Bullet list items with ◆ marker
            html += '<ul class="ad-bullet-list">';
            for (const sid of adSec.sentence_ids) {
              const s = sentMap[sid];
              if (s) {
                html += `<li><span class="sentence" data-sid="${s.id}">${s.en}</span>`;
                html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
                html += '</li>';
              }
              // Links after specific sentence
              if (adSec.links && adSec.links_after_sentence_id === sid) {
                for (const link of adSec.links) {
                  html += `<div class="ad-link"><strong>${link.en}</strong></div>`;
                }
              }
            }
            html += '</ul>';
          } else if (adSec.type === 'text') {
            // Normal text block (e.g. Winners)
            for (const sid of adSec.sentence_ids) {
              const s = sentMap[sid];
              if (s) {
                html += `<p class="passage-paragraph"><span class="sentence" data-sid="${s.id}">${s.en}</span></p>`;
                html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div></div>`;
              }
            }
          }
        }
        html += '</div>'; // .ad-box
        html += '</div>'; // .para-content
        html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
        html += '</div>'; // .para-audio-row
      } else {
        // ===== Flat sentences rendering (fallback) =====
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
    }

    // Presentation outline in a box (駿台 第7問など)
    if (passage.presentation_outline) {
      const po = passage.presentation_outline;
      if (po.label_outside_box && po.label_outside_box.en) {
        html += `<div class="presentation-outline-label">${po.label_outside_box.en}</div>`;
        if (po.label_outside_box.ja) {
          html += `<div class="choice-text-ja">${po.label_outside_box.ja}</div>`;
        }
      }
      html += '<div class="presentation-outline-box">';
      if (po.title && po.title.en) {
        html += `<div class="presentation-outline-inner-title">${po.title.en}</div>`;
        if (po.title.ja) {
          html += `<div class="presentation-outline-inner-title-ja choice-text-ja">${po.title.ja}</div>`;
        }
      }
      const blocks = po.blocks || [];
      for (const bl of blocks) {
        const btype = bl.type;
        if (btype === 'adaptations_heading') {
          html += `<div class="presentation-outline-section-row">`;
          html += `<span class="presentation-outline-strong">${bl.heading.en}</span>`;
          const slotAfter = typeof bl.slot_after_heading === 'number' ? `<span class="answer-slot">${bl.slot_after_heading}</span>` : '';
          if (slotAfter) html += ` ${slotAfter}`;
          html += `</div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          html += `<ul class="presentation-outline-lines">`;
          for (const line of bl.lines || []) {
            html += `<li>${line.en}`;
            if (line.ja) html += `<div class="choice-text-ja">${line.ja}</div>`;
            html += '</li>';
          }
          html += '</ul>';
        } else if (btype === 'section_heading_lines') {
          html += `<div class="presentation-outline-strong">${bl.heading.en}</div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          html += `<div class="presentation-outline-bullets">`;
          for (const b of bl.bullets || []) {
            const t = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="presentation-outline-bullet">— ${t}`;
            if (b.ja) {
              const tj = String(b.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="choice-text-ja">${tj}</div>`;
            }
            html += '</div>';
          }
          html += '</div>';
        } else if (btype === 'center_slot') {
          html += `<div class="presentation-outline-strong">${bl.heading.en}</div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          if (typeof bl.center_slot === 'number') {
            html += `<div class="presentation-outline-center-slot"><span class="answer-slot">${bl.center_slot}</span></div>`;
          }
        } else if (btype === 'function_slot') {
          html += `<div class="presentation-outline-strong">${bl.heading.en}</div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          html += `<div class="presentation-outline-bullets">`;
          for (const b of bl.bullets || []) {
            const t = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="presentation-outline-bullet">— ${t}`;
            if (b.ja) {
              const tj = String(b.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="choice-text-ja">${tj}</div>`;
            }
            html += '</div>';
          }
          html += '</div>';
        } else if (btype === 'slot_heading_list') {
          html += `<div class="presentation-outline-slot-heading-row">`;
          html += `<span class="answer-slot">${bl.slot}</span>`;
          html += `</div>`;
          html += `<ul class="presentation-outline-lines presentation-outline-muted-bullets">`;
          for (const line of bl.lines || []) {
            html += `<li>${line.en}`;
            if (line.ja) html += `<div class="choice-text-ja">${line.ja}</div>`;
            html += '</li>';
          }
          html += '</ul>';
        }
      }
      html += '</div>'; // .presentation-outline-box
    }

    // Sections format: §1〜§6 with sentences inside each section (e.g., 2024 Section 5)
    if (passage.sections) {
      for (let si = 0; si < passage.sections.length; si++) {
        const section = passage.sections[si];
        const sectionAudioFile = `${audioBase}s${secNum}_${passage.id}_${section.id}.mp3`;

        // ◆◆◆◆◆ separator between sections
        if (si > 0) {
          html += '<div class="section-separator">◆◆◆◆◆</div>';
        }

        html += '<div class="para-audio-row">';
        html += '<div class="para-content">';
        html += '<p class="passage-paragraph">';
        for (const sent of section.sentences) {
          html += `<span class="sentence" data-sid="${sent.id}">${sent.en}</span> `;
        }
        html += '</p>';
        html += '<div class="passage-ja-block">';
        for (const sent of section.sentences) {
          html += `<div class="sentence-ja" data-sid-ja="${sent.id}">${sent.ja}</div>`;
        }
        html += '</div>';
        html += '</div>';
        html += `<button class="btn-audio" data-audio="${sectionAudioFile}" title="読み上げ">🔊</button>`;
        html += '</div>';
      }
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
            // Show marker BEFORE sentence (default) unless marker_position is 'after'
            if (sent.comment_marker && sent.marker_position !== 'after') {
              const caret = sent.marker_type === 'caret' ? ' <span class="caret-mark">∧</span>' : '';
              html += '<sup class="comment-marker">' + sent.comment_marker + '</sup>' + caret + ' ';
            }
            // Render sentence text with optional underline word
            let sentText = sent.en;
            if (sent.underline_word) {
              sentText = sentText.replace(sent.underline_word, '<span class="underline-word">' + sent.underline_word + '</span>');
            }
            html += '<span class="sentence" data-sid="' + sent.id + '">' + sentText + '</span> ';
            // Show marker AFTER sentence
            if (sent.comment_marker && sent.marker_position === 'after') {
              const caret = sent.marker_type === 'caret' ? ' <span class="caret-mark">∧</span>' : '';
              html += '<sup class="comment-marker">' + sent.comment_marker + '</sup>' + caret;
            }
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
        } else if (passage.layout === 'speaker_boxes') {
          // Speaker-boxed rendering: each paragraph (= one opinion) is wrapped in a bordered box.
          // The sentence whose id ends with _h is treated as the speaker name (bold header).
          html += '<div class="opinion-box">';
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          let headerSent = null;
          const bodySents = [];
          for (const s of para) {
            if (!headerSent && /_h$/.test(s.id || '')) {
              headerSent = s;
            } else {
              bodySents.push(s);
            }
          }
          if (headerSent) {
            html += '<div class="opinion-speaker">';
            html += `<span class="sentence" data-sid="${headerSent.id}">${headerSent.en}</span>`;
            html += '</div>';
            html += '<div class="passage-ja-block opinion-speaker-ja">';
            html += `<div class="sentence-ja" data-sid-ja="${headerSent.id}">${headerSent.ja}</div>`;
            html += '</div>';
          }
          html += '<p class="passage-paragraph">';
          for (const s of bodySents) {
            html += `<span class="sentence" data-sid="${s.id}">${s.en}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const s of bodySents) {
            html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
          }
          html += '</div>';
          html += '</div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
          html += '</div>';
        } else if (passage.block_separators && passage.block_separators.length > 0) {
          // Block-based rendering: group paragraphs into blocks separated by ◆◆◆◆◆
          // Handled below after the loop
        } else {
          // Normal paragraph rendering (no blocks)
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          // Insert passage images that target this paragraph
          if (passage.images) {
            const imgBase = currentDataPath.replace(/data\.json$/, '');
            for (const img of passage.images) {
              if (img.paragraph_index === pi) {
                const floatClass = img.position === 'float-left' ? 'passage-img-float-left' : 'passage-img-float-right';
                const styleAttr = img.max_width ? ` style="max-width:${img.max_width}px"` : '';
                html += `<img src="${imgBase}${img.src}" alt="${img.alt || ''}" class="passage-img ${floatClass}"${styleAttr}>`;
              }
            }
          }
          // Check if para is an object {id, en, ja} (6A/6B paragraph format) or an array of sentences
          if (!Array.isArray(para) && para.id && para.en) {
            // Object paragraph: render as a single paragraph block
            html += '<p class="passage-paragraph">';
            html += `<span class="sentence" data-sid="${para.id}">${para.en}</span>`;
            html += '</p>';
            html += '<div class="passage-ja-block">';
            html += `<div class="sentence-ja" data-sid-ja="${para.id}">${para.ja}</div>`;
            html += '</div>';
          } else {
            // Array of sentences (legacy format)
            html += '<p class="passage-paragraph">';
            for (const sent of para) {
              const enText = String(sent.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<span class="sentence" data-sid="${sent.id}">${enText}</span> `;
            }
            html += '</p>';
            html += '<div class="passage-ja-block">';
            for (const sent of para) {
              const jaText = String(sent.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="sentence-ja" data-sid-ja="${sent.id}">${jaText}</div>`;
            }
            html += '</div>';
          }
          html += '</div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
        }

        // Graph image after specified paragraph (1-indexed)
        if (passage.graph_image && passage.graph_image.after_paragraph === (pi + 1)) {
          const imgBase = currentDataPath.replace(/data\.json$/, '');
          html += `<div class="chart-image-container"><img class="chart-image" src="${imgBase}${passage.graph_image.src}" alt="${passage.graph_image.alt || 'Graph'}"></div>`;
        }
        // Inline data table after specified paragraph (1-indexed) — for schedule tables embedded in email body etc.
        if (passage.table && passage.table.after_paragraph === (pi + 1)) {
          const tbl = passage.table;
          html += '<div class="data-table-container">';
          if (tbl.title) {
            html += `<div class="data-table-title">${tbl.title.en}</div>`;
            if (tbl.title.ja) {
              html += `<div class="data-table-title-ja choice-text-ja">${tbl.title.ja}</div>`;
            }
          }
          html += '<table class="data-table"><thead><tr>';
          for (const h of tbl.headers) {
            html += `<th>${String(h).replace(/\n/g, '<br>')}</th>`;
          }
          html += '</tr></thead><tbody>';
          for (const row of tbl.rows) {
            const cells = Array.isArray(row) ? row : (row.cells || []);
            const naCells = (row && row.na_cells) || [];
            html += '<tr>';
            for (let ci = 0; ci < cells.length; ci++) {
              const isNA = naCells.includes(ci);
              html += `<td${isNA ? ' class="na-cell"' : ''}>${cells[ci]}</td>`;
            }
            html += '</tr>';
          }
          html += '</tbody></table></div>';
          // Mark so the bottom rendering doesn't repeat it
          tbl._renderedInline = true;
        }
        // Info box with image after specified paragraph (1-indexed)
        if (passage.info_box && passage.info_box.after_paragraph === (pi + 1)) {
          const imgBase = currentDataPath.replace(/data\.json$/, '');
          html += '<div class="info-box">';
          if (passage.info_box.title) {
            html += `<div class="info-box-title">${passage.info_box.title.en}</div>`;
          }
          if (passage.info_box.image_src) {
            html += `<div class="info-box-image"><img src="${imgBase}${passage.info_box.image_src}" alt="${passage.info_box.image_alt || ''}"></div>`;
          }
          html += '</div>';
        }
      }

      // Block-based rendering: paragraphs grouped by ◆◆◆◆◆ separators
      if (passage.block_separators && passage.block_separators.length > 0 && !hasComments) {
        // Clear the html we just added for paragraphs (we need to re-render in blocks)
        // Actually, since we skipped rendering in the else-if branch, we just add block html now
        const separators = passage.block_separators;
        const paragraphs = passage.paragraphs;
        let blockStart = 0;
        let blockNum = 1;

        for (let bi = 0; bi <= separators.length; bi++) {
          const blockEnd = bi < separators.length ? separators[bi] : paragraphs.length - 1;
          const blockAudioFile = `${audioBase}s${secNum}_${passage.id}_p${blockNum}.mp3`;

          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';

          for (let pi = blockStart; pi <= blockEnd; pi++) {
            const para = paragraphs[pi];
            html += `<p class="passage-paragraph para-indent">`;
            for (const sent of para) {
              const enText = String(sent.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<span class="sentence" data-sid="${sent.id}">${enText}</span> `;
            }
            html += '</p>';
            html += '<div class="passage-ja-block">';
            for (const sent of para) {
              const jaText = String(sent.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="sentence-ja" data-sid-ja="${sent.id}">${jaText}</div>`;
            }
            html += '</div>';
          }

          html += '</div>';
          html += `<button class="btn-audio" data-audio="${blockAudioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';

          // ◆◆◆◆◆ separator (not after the last block)
          if (bi < separators.length) {
            html += '<div class="block-separator">◆◆◆◆◆</div>';
          }

          blockStart = blockEnd + 1;
          blockNum++;
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

      // Data table (e.g. Monthly Rent) — skip if already rendered inline above via after_paragraph
      if (passage.table && !passage.table._renderedInline) {
        const tbl = passage.table;
        html += '<div class="data-table-container">';
        if (tbl.title) {
          html += `<div class="data-table-title">${tbl.title.en}</div>`;
        }
        html += '<table class="data-table"><thead><tr>';
        for (const h of tbl.headers) {
          html += `<th>${h.replace(/\n/g, '<br>')}</th>`;
        }
        html += '</tr></thead><tbody>';
        for (const row of tbl.rows) {
          html += '<tr>';
          for (let ci = 0; ci < row.cells.length; ci++) {
            const isNA = row.na_cells && row.na_cells.includes(ci);
            html += `<td${isNA ? ' class="na-cell"' : ''}>${row.cells[ci]}</td>`;
          }
          html += '</tr>';
        }
        html += '</tbody></table>';
        if (tbl.source_url) {
          html += `<div class="data-table-source">${tbl.source_url}</div>`;
        }
        html += '</div>';
      }

      // Footer note (e.g. deposits info)
      if (passage.footer_note) {
        html += `<div class="passage-footer-note"><strong>${passage.footer_note.en}</strong></div>`;
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

    // ===== Step label rendering =====
    if (passage.step_label) {
      html += `<div class="step-heading">${passage.step_label.en}</div>`;
    }

    // ===== Authors rendering (大問6: Step1) =====
    if (passage.authors) {
      for (const author of passage.authors) {
        const authorId = author.name.en.split('(')[0].trim().replace(/ /g, '_').toLowerCase();
        html += '<div class="author-block">';
        html += `<div class="author-label"><strong>${author.name.en}</strong></div>`;
        for (let pi = 0; pi < author.paragraphs.length; pi++) {
          const para = author.paragraphs[pi];
          const audioFile = `${audioBase}s${secNum}_${authorId}_p${pi + 1}.mp3`;
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          html += '<p class="passage-paragraph">';
          for (const s of para) {
            html += `<span class="sentence" data-sid="${s.id}">${s.en}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const s of para) {
            html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
          }
          html += '</div></div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
        }
        html += '</div>';
      }
      // Navigation cue: answer 問1 and 問2 after reading Step 1
      html += `<div class="step-nav-cue" data-target-qids="問1,問2">
        <span class="step-nav-icon">📝</span>
        <span class="step-nav-text">ここまで読んだら <strong>問1</strong> と <strong>問2</strong> を解答 →</span>
      </div>`;
    }

    // ===== Step2: Position rendering (大問6) =====
    if (passage.position) {
      const pos = passage.position;
      html += '<div class="position-box">';
      if (pos.title) {
        const titleText = pos.title.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
        html += `<div class="position-title"><strong><u>${titleText}</u></strong></div>`;
      }
      if (pos.bullets) {
        html += '<ul class="position-bullets">';
        for (const b of pos.bullets) {
          const bText = b.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<li>${bText}</li>`;
        }
        html += '</ul>';
      }
      html += '</div>';
      // Navigation cue: answer 問3 after Step 2
      html += `<div class="step-nav-cue" data-target-qids="問3a,問3b,問3c">
        <span class="step-nav-icon">📝</span>
        <span class="step-nav-text">ここまで読んだら <strong>問3</strong> を解答 →</span>
      </div>`;
    }

    // ===== Sources rendering (大問6: Step3 sources) =====
    if (passage.sources) {
      for (const source of passage.sources) {
        const sourceId = source.name.en.replace(/ /g, '_').toLowerCase();
        html += `<div class="source-block">`;
        html += `<div class="source-label"><strong>${source.name.en}</strong></div>`;
        for (let pi = 0; pi < source.paragraphs.length; pi++) {
          const para = source.paragraphs[pi];
          const audioFile = `${audioBase}s${secNum}_${sourceId}_p${pi + 1}.mp3`;
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          html += '<p class="passage-paragraph">';
          for (const s of para) {
            html += `<span class="sentence" data-sid="${s.id}">${s.en}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const s of para) {
            html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
          }
          html += '</div></div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
          // Graph image after specified paragraph
          if (source.graph_image && source.graph_image.after_paragraph === (pi + 1)) {
            const imgBase = currentDataPath.replace(/data\.json$/, '');
            html += `<div class="chart-image-container"><img class="chart-image" src="${imgBase}${source.graph_image.src}" alt="${source.graph_image.alt || 'Graph'}"></div>`;
          }
        }
        html += '</div>';
      }

      // Outline rendering
      if (passage.outline) {
        const o = passage.outline;
        html += '<div class="outline-box">';
        html += `<div class="outline-title">${o.title.en}</div>`;
        for (const sec2 of o.sections) {
          html += `<div class="outline-section"><strong><em>${sec2.label.en}</em></strong></div>`;
          if (sec2.content) {
            html += `<div class="outline-content">${sec2.content.en}</div>`;
          }
          if (sec2.reasons) {
            for (const reason of sec2.reasons) {
              const rText = reason.text.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="outline-reason">${reason.label}: ${rText}</div>`;
            }
          }
        }
        html += '</div>';
      }

      // Navigation cue: answer 問4 and 問5 after reading sources
      html += `<div class="step-nav-cue" data-target-qids="問4,問5">
        <span class="step-nav-icon">📝</span>
        <span class="step-nav-text">ここまで読んだら <strong>問4</strong> と <strong>問5</strong> を解答 →</span>
      </div>`;
    }

    // ===== Notes section (大問7: Your notes) =====
    if (passage.is_notes) {
      html += `<div class="notes-title">${passage.notes_title.en}</div>`;

      // Story outline
      if (passage.story_outline) {
        const so = passage.story_outline;
        html += '<div class="notes-heading">Story outline</div>';
        html += `<div class="notes-outline-start">${so.start.en}</div>`;
        html += '<div class="notes-outline-slots">';
        for (const slot of so.slots) {
          html += `<div class="notes-outline-slot"><span class="answer-slot">${slot}</span></div>`;
        }
        html += '</div>';
        if (so.end) {
          html += `<div class="notes-outline-end">${so.end.en}</div>`;
        }
      }

      // About Sam
      if (passage.about_sam) {
        const as_ = passage.about_sam;
        html += '<div class="notes-heading">About Sam</div>';
        html += '<ul class="notes-list">';
        html += `<li>Nationality: ${as_.nationality.en}</li>`;
        const ageSlot = `<span class="answer-slot">${as_.age_slot}</span>`;
        html += `<li>Age: ${ageSlot}</li>`;
        html += `<li>Occupation: ${as_.occupation.en}</li>`;
        html += '<li>How his friends and family supported him:';
        for (const item of as_.support) {
          const text = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<div class="notes-support-item">${text}</div>`;
        }
        html += '</li></ul>';
      }

      // Interpretation
      if (passage.interpretation) {
        html += '<div class="notes-heading">Interpretation of key moments</div>';
        html += '<ul class="notes-list">';
        for (const item of passage.interpretation) {
          const text = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<li>${text}</li>`;
        }
        html += '</ul>';
      }

      // Research notes (generic sections with heading + items)
      if (passage.research_sections) {
        for (const rsec of passage.research_sections) {
          html += `<div class="notes-heading">${rsec.heading.en}</div>`;
          html += '<ul class="notes-list">';
          for (const item of rsec.items) {
            const text = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<li>${text}</li>`;
          }
          html += '</ul>';
        }
      }

      // Event sequence (timeline with slots)
      if (passage.event_sequence) {
        const es = passage.event_sequence;
        html += `<div class="notes-heading">${es.heading.en}</div>`;
        html += '<div class="notes-outline-start">' + es.start.en + '</div>';
        html += '<div class="notes-outline-slots">';
        for (const slot of es.slots) {
          html += `<div class="notes-outline-slot"><span class="answer-slot">${slot}</span></div>`;
        }
        html += '</div>';
      }

      // Legacy sections (heading + single slot item)
      if (passage.legacy_section) {
        const ls = passage.legacy_section;
        html += `<div class="notes-heading">${ls.heading.en}</div>`;
        const text = ls.content.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
        html += `<div class="notes-outline-start">${text}</div>`;
      }

      // Lessons learned (heading + slot items)
      if (passage.lessons) {
        const ll = passage.lessons;
        html += `<div class="notes-heading">${ll.heading.en}</div>`;
        html += '<ul class="notes-list">';
        for (const item of ll.items) {
          const text = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<li>${text}</li>`;
        }
        html += '</ul>';
      }

      // Note sections (大問7: 発表ノートの各セクション)
      if (passage.note_sections) {
        if (passage.subtitle_slot) {
          html += `<div class="notes-subtitle-slot">${passage.subtitle_slot.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>')}</div>`;
        }
        for (const ns of passage.note_sections) {
          html += `<div class="notes-heading">${ns.heading.en}</div>`;
          if (ns.is_timeline) {
            html += '<div class="notes-timeline">';
            for (const item of ns.items) {
              if (item.is_slot) {
                html += `<div class="notes-timeline-slot"><span class="answer-slot">${item.en.replace(/[\[\]]/g, '')}</span></div>`;
              } else {
                html += `<div class="notes-timeline-item">${item.en}</div>`;
              }
            }
            html += '</div>';
          } else {
            html += '<ul class="notes-list">';
            for (const item of ns.items) {
              const text = item.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<li>${text}</li>`;
            }
            html += '</ul>';
          }
        }
      }
    }

    // Presentation slides (image-based, e.g. 大問8)
    if (passage.presentation_image) {
      const basePath = currentDataPath.replace(/[^/]*$/, '');
      const imgSrc = basePath + passage.presentation_image;
      html += `<div class="presentation-slides"><img src="${imgSrc}" alt="Presentation slides" style="max-width:100%; border:1px solid #ccc; border-radius:4px;"></div>`;
    }

    // ===== Poster rendering (大問8) =====
    if (passage.is_poster) {
      const imgBase = currentDataPath.replace(/data\.json$/, '');
      html += '<div class="poster-box">';
      // Poster title
      if (passage.poster_title) {
        html += `<div class="poster-title-wrap"><span class="poster-title">${passage.poster_title.en}</span></div>`;
      }
      // Intro slot ([41])
      if (passage.poster_intro_slot) {
        html += `<p>${passage.poster_intro_slot.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>')}</p>`;
      }
      // Section label + table
      if (passage.poster_section_label) {
        html += `<div class="poster-section-label">${passage.poster_section_label.en}</div>`;
      }
      if (passage.poster_table) {
        const pt = passage.poster_table;
        html += '<table class="poster-table"><tr>';
        for (const h of pt.headers) {
          html += `<th>${h}</th>`;
        }
        html += '</tr>';
        for (const row of pt.rows) {
          html += '<tr>';
          html += `<td style="text-align:center;">${row.type_num}</td>`;
          html += '<td>';
          html += `${row.cause.en}`;
          if (row.cause_image) {
            html += `<br><img src="${imgBase}${row.cause_image}" alt="${row.cause.en}" style="max-width:60px; margin-top:4px;">`;
          }
          html += '</td>';
          html += `<td>${row.theory.en.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>')}</td>`;
          html += `<td>${row.origins.en}</td>`;
          html += '</tr>';
        }
        html += '</table>';
      }
      // Solutions section
      if (passage.poster_solutions_label) {
        html += `<div class="poster-section-label">${passage.poster_solutions_label.en}</div>`;
        html += '<div class="poster-solutions">';
        for (const slot of passage.poster_solutions_slots) {
          html += `<div>${slot.replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>')}</div>`;
        }
        html += '</div>';
      }
      html += '</div>';
    }

    html += '</div>';
  }

  html += '</div>'; // .passage-container

  document.getElementById('passage-content').innerHTML = html;

  // Bind sentence click for translation popup
  setupSentencePopup();

  // Bind audio play buttons
  setupAudioButtons();

  // Bind step navigation cue clicks
  setupStepNavCues();
}

// ===== Step Navigation Cue (scroll to questions in right pane) =====
function setupStepNavCues() {
  document.querySelectorAll('.step-nav-cue').forEach(cue => {
    cue.addEventListener('click', () => {
      const qids = cue.dataset.targetQids.split(',');
      if (!qids.length) return;

      // Find the first target question block in the right pane
      const firstQBlock = document.querySelector(`.question-block[data-qid="${qids[0]}"]`);
      if (!firstQBlock) return;

      // Scroll right pane to the question
      const rightPane = document.getElementById('pane-questions');
      firstQBlock.scrollIntoView({ behavior: 'smooth', block: 'start' });

      // Flash highlight all target questions
      for (const qid of qids) {
        const qBlock = document.querySelector(`.question-block[data-qid="${qid}"]`);
        if (qBlock) {
          qBlock.classList.add('nav-flash');
          setTimeout(() => qBlock.classList.remove('nav-flash'), 1800);
        }
      }
    });
  });
}
function setupSentencePopup() {
  const pane = document.getElementById('pane-passage');

  pane.addEventListener('click', (e) => {
    // 解説モード（.sentence.highlighted）に限定せず，すべての .sentence でポップアップ表示。
    // ただし sentence 内に audio button などのインタラクティブ要素があれば，それは無視する。
    if (e.target.closest('.btn-audio, .popup-close')) return;
    const sent = e.target.closest('.sentence');

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
    if (!e.target.closest('.sentence') && !e.target.closest('.sentence-popup')) {
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
        if (Array.isArray(para)) {
          const sent = para.find(s => s.id === sid);
          if (sent) return sent.ja;
        } else if (para && para.id === sid) {
          return para.ja;
        }
      }
    }
  }
  return null;
}

// ===== Audio Playback =====
let currentAudio = null;
let currentAudioBtn = null;

// ===== Seek bar =====
const audioBar = document.getElementById('audio-bar');
const audioBarSeek = document.getElementById('audio-bar-seek');
const audioBarCurrent = document.getElementById('audio-bar-current');
const audioBarTotal = document.getElementById('audio-bar-total');
const audioBarPlayPause = document.getElementById('audio-bar-playpause');
const audioBarClose = document.getElementById('audio-bar-close');
let seekAnimFrame = null;

function fmtTime(s) {
  if (!isFinite(s)) return '0:00';
  const m = Math.floor(s / 60);
  const sec = Math.floor(s % 60);
  return `${m}:${sec.toString().padStart(2, '0')}`;
}

function updateSeekBar() {
  if (!currentAudio) return;
  const t = currentAudio.currentTime;
  const d = currentAudio.duration || 0;
  audioBarSeek.value = d ? (t / d) * 100 : 0;
  audioBarCurrent.textContent = fmtTime(t);
  seekAnimFrame = requestAnimationFrame(updateSeekBar);
}

function showAudioBar() {
  audioBar.classList.add('visible');
}
function hideAudioBar() {
  audioBar.classList.remove('visible');
  if (seekAnimFrame) { cancelAnimationFrame(seekAnimFrame); seekAnimFrame = null; }
}

audioBarSeek.addEventListener('input', () => {
  if (!currentAudio) return;
  const d = currentAudio.duration || 0;
  currentAudio.currentTime = (audioBarSeek.value / 100) * d;
});

audioBarPlayPause.addEventListener('click', () => {
  if (!currentAudio) return;
  if (currentAudio.paused) {
    currentAudio.play();
    audioBarPlayPause.textContent = '⏸';
    if (currentAudioBtn) { currentAudioBtn.textContent = '⏸'; currentAudioBtn.classList.add('playing'); }
  } else {
    currentAudio.pause();
    audioBarPlayPause.textContent = '▶';
    if (currentAudioBtn) { currentAudioBtn.textContent = '🔊'; currentAudioBtn.classList.remove('playing'); }
  }
});

audioBarClose.addEventListener('click', () => {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }
  if (currentAudioBtn) {
    currentAudioBtn.textContent = '🔊';
    currentAudioBtn.classList.remove('playing');
    currentAudioBtn = null;
  }
  hideAudioBar();
});

function startAudio(src, btn) {
  // Stop previous
  if (currentAudio) {
    currentAudio.pause();
    if (currentAudioBtn) { currentAudioBtn.textContent = '🔊'; currentAudioBtn.classList.remove('playing'); }
    if (seekAnimFrame) { cancelAnimationFrame(seekAnimFrame); seekAnimFrame = null; }
  }

  currentAudio = new Audio(src);
  currentAudioBtn = btn;
  btn.textContent = '⏸';
  btn.classList.add('playing');
  audioBarPlayPause.textContent = '⏸';
  audioBarSeek.value = 0;
  audioBarCurrent.textContent = '0:00';
  audioBarTotal.textContent = '0:00';

  currentAudio.addEventListener('loadedmetadata', () => {
    audioBarTotal.textContent = fmtTime(currentAudio.duration);
  });

  currentAudio.play().catch(() => {
    btn.textContent = '🔊';
    btn.classList.remove('playing');
    hideAudioBar();
  });

  currentAudio.addEventListener('ended', () => {
    btn.textContent = '🔊';
    btn.classList.remove('playing');
    currentAudio = null;
    currentAudioBtn = null;
    audioBarPlayPause.textContent = '▶';
    if (seekAnimFrame) { cancelAnimationFrame(seekAnimFrame); seekAnimFrame = null; }
  });

  showAudioBar();
  seekAnimFrame = requestAnimationFrame(updateSeekBar);
}

function setupAudioButtons() {
  document.querySelectorAll('.btn-audio').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const src = btn.dataset.audio;

      // If same button clicked again, toggle pause/play
      if (currentAudio && currentAudioBtn === btn) {
        if (currentAudio.paused) {
          currentAudio.play();
          btn.textContent = '⏸';
          audioBarPlayPause.textContent = '⏸';
          seekAnimFrame = requestAnimationFrame(updateSeekBar);
        } else {
          currentAudio.pause();
          btn.textContent = '🔊';
          btn.classList.remove('playing');
          audioBarPlayPause.textContent = '▶';
          if (seekAnimFrame) { cancelAnimationFrame(seekAnimFrame); seekAnimFrame = null; }
        }
        return;
      }

      startAudio(src, btn);
    });
  });
}

function escapeHtmlPreserve(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>')
    // 解説冊子の下線を再現するため <u>…</u> のみ復元（trusted ビルド済みデータ）
    .replace(/&lt;u&gt;([\s\S]*?)&lt;\/u&gt;/g, '<u>$1</u>');
}

// ===== Render Questions (Right Pane) =====
function renderQuestions() {
  const sec = currentSection;
  let html = '';

  let prevSubLabel = null;
  for (const q of sec.questions) {
    // Insert subsection label header when transitioning between A/B
    if (q._subsectionLabel && q._subsectionLabel !== prevSubLabel) {
      html += `<div class="subsection-label">${sec.title} ${q._subsectionLabel}</div>`;
      prevSubLabel = q._subsectionLabel;
    }
    const qIdx = getQuestionIndex(q.question_id);
    html += `<div class="question-block" data-qid="${q.question_id}">`;

    // Question label + per-question evidence button
    html += `<div class="question-label-row">
      <span class="question-label">${q.question_id}</span>
      <button class="btn-evidence-q" data-qid="${q.question_id}" data-qidx="${qIdx}" title="根拠箇所をヒント表示">ヒント</button>
    </div>`;

    // Stem (support both "stem" and "question_text" field names)
    const stemObj = q.stem || q.question_text;
    if (stemObj && stemObj.en) {
      const stemEn = stemObj.en.replace(
        /\[(\d+)\]/g,
        '<span class="answer-slot">$1</span>'
      );
      html += `<div class="question-stem">${stemEn}</div>`;
    }

    // Stem ja (hidden by default)
    if (stemObj && stemObj.ja) {
      html += `<div class="choice-text-ja" style="margin-bottom:10px; margin-top:-8px;">${stemObj.ja}</div>`;
    }

    // Letter-keyed definitions (e.g. A–F listed before 「組み合わせ」選択肢)
    if (Array.isArray(q.info_options) && q.info_options.length > 0) {
      html += '<ul class="info-options">';
      for (const opt of q.info_options) {
        const lab = escapeHtmlPreserve(opt.label || '');
        const en = escapeHtmlPreserve(opt.en || '');
        const ja = escapeHtmlPreserve(opt.ja || '');
        html +=
          `<li class="info-option-item">` +
          `<span class="info-option-letter">${lab}</span>` +
          `<span class="info-option-colon"> : </span>` +
          `<span class="info-option-en">${en}</span>`;
        if (ja) {
          html += `<div class="choice-text-ja info-option-ja">${ja}</div>`;
        }
        html += `</li>`;
      }
      html += '</ul>';
    }

    // Question-level figure (e.g. four-panel picture choices for problem 3)
    const qFig = q.figure_image || q.choice_grid_image;
    if (qFig && qFig.src) {
      const cap =
        qFig.caption_ja && String(qFig.caption_ja).trim()
          ? `<div class="question-figure-caption">${qFig.caption_ja}</div>`
          : '';
      html += `<figure class="question-figure">
        <img src="${qFig.src}" alt="${qFig.alt || ''}" />
        ${cap}
      </figure>`;
    }

    /** 画像で①〜④を示すのみで、選択肢テキストが空の設問か */
    const pictureTierChoices =
      q.choices &&
      qFig &&
      qFig.src &&
      q.choices.every(
        c =>
          !String(c.en || '').trim() &&
          !String(c.ja || '').trim() &&
          !c.image
      );

    // Choices — ordering vs normal
    if (q.question_type === 'ordering') {
      // Ordering slots row
      const slotCount = q.answer_sequence ? q.answer_sequence.length : (q.choices ? q.choices.length : 0);
      html += '<div class="ordering-slots" data-qid="' + q.question_id + '">';
      for (let si = 0; si < slotCount; si++) {
        if (si > 0) html += '<span class="ordering-arrow">→</span>';
        html += '<span class="ordering-slot" data-slot="' + si + '"></span>';
      }
      html += '</div>';

      // Ordering choice buttons
      const orderingChoices = q.choices || q.events || [];
      html += '<div class="ordering-choices" data-qid="' + q.question_id + '">';
      for (const choice of orderingChoices) {
        html += '<button class="ordering-btn" data-qid="' + q.question_id + '" data-label="' + choice.label + '">'
          + '<span class="ordering-btn-label">' + choice.label + '</span>'
          + '<span class="ordering-btn-text">' + (choice.en || '') + '</span>'
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
          const cEn = choice.en || '';
          const cJa = choice.ja || '';
          const cImg = choice.image
            ? `<img class="choice-image" src="${choice.image.src}" alt="${choice.image.alt || ''}" />`
            : '';
          html += `<li class="choice-item multi-choice" data-qid="${q.question_id}" data-ans-num="${ansNum}" data-label="${choice.label}">
            <span class="choice-label">${choice.label}</span>
            <span class="choice-text">
              ${cImg}${cEn}
              <div class="choice-text-ja">${cJa}</div>
            </span>
          </li>`;
        }
        html += '</ul></div>';
      }
      html += '<button class="ordering-undo multi-undo" data-qid="' + q.question_id + '" title="取り消し" style="display:none;">↩ 戻す</button>';
    } else if (q.choices) {
      // Normal choices
      const ulCls = pictureTierChoices ? 'choices choices-picture-tier' : 'choices';
      html += `<ul class="${ulCls}">`;
      for (const choice of q.choices) {
        const cEn = choice.en || '';
        const cJa = choice.ja || '';
        const cImg = choice.image
          ? `<img class="choice-image" src="${choice.image.src}" alt="${choice.image.alt || ''}" />`
          : '';
        const liExtra = pictureTierChoices ? ' choice-item-picture-tier' : '';
        const textBlock =
          pictureTierChoices
            ? ''
            : `<span class="choice-text">
              ${cImg}${cEn}
              <div class="choice-text-ja">${cJa}</div>
            </span>`;
        html += `<li class="choice-item${liExtra}" data-qid="${q.question_id}" data-label="${choice.label}" data-correct="${choice.is_correct}">
          <span class="choice-label">${choice.label}</span>${textBlock}
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

  // Build answer text
  let answerText;
  if (q.answer && typeof q.answer === 'object') {
    // Multi-answer: {"27": "①", "28": "④", ...}
    const parts = Object.entries(q.answer).map(([k, v]) => `[${k}] ${v}`);
    answerText = parts.join(' ');
    if (q.answer_note) answerText += `（${q.answer_note}）`;
  } else if (q.answer) {
    answerText = q.answer;
  } else if (q.choices) {
    // Derive from is_correct in choices
    const correct = q.choices.filter(c => c.is_correct);
    answerText = correct.map(c => c.label).join(', ');
  } else {
    answerText = '';
  }

  let html = `<div class="explanation-box" data-qid="${q.question_id}">`;
  html += `<div class="explanation-header">📖 解説（${q.question_id}）</div>`;

  // 解説PDF原文（逐語転載）優先。なければ legacy の ja を使う。
  const quotedBody = q.explanation.quoted_ja || q.explanation.ja || '';
  const quotedSource = q.explanation.quoted_source || '解説（駿台 2026 実戦問題集）';
  if (quotedBody) {
    html += `<div class="explanation-text explanation-quoted">
      <strong>正解: ${answerText}</strong>
      <div class="quoted-body">${escapeHtmlPreserve(quotedBody)}</div>
      <div class="quoted-source">— ${quotedSource} より引用</div>
    </div>`;
  } else {
    html += `<div class="explanation-text"><strong>正解: ${answerText}</strong></div>`;
  }

  // 「他の選択肢の解説」: 解説PDF原文に個別の不正解理由が書かれているとき
  if (q.explanation.why_others_wrong && q.explanation.why_others_wrong.length > 0) {
    html += `<div class="explanation-toggle" data-qid="${q.question_id}">▶ 他の選択肢の解説</div>`;
    html += `<div class="others-wrong" data-qid="${q.question_id}">`;
    for (const ow of q.explanation.why_others_wrong) {
      html += `<div class="wrong-reason"><strong>${ow.choice}</strong> ${ow.reason}</div>`;
    }
    html += '</div>';
  }

  // 講師からの＋α: 推論や補足を含む生成的記述（解説PDFに無い情報）
  const note = q.explanation.instructor_note;
  if (note && (note.ja || (note.points && note.points.length))) {
    html += `<div class="instructor-note">`;
    html += `<div class="instructor-note-header">📝 講師からの＋α（解説冊子にはない補足）</div>`;
    if (note.ja) {
      html += `<div class="instructor-note-body">${escapeHtmlPreserve(note.ja)}</div>`;
    }
    if (Array.isArray(note.points) && note.points.length > 0) {
      html += `<ul class="instructor-note-points">`;
      for (const p of note.points) {
        html += `<li>${escapeHtmlPreserve(p)}</li>`;
      }
      html += `</ul>`;
    }
    html += `</div>`;
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

  // Determine which slots are unordered (e.g. [27] and [28] are interchangeable)
  const unorderedSlots = q.unordered_slots || [];
  const userAnswers = {};
  for (const s of allSlots) {
    userAnswers[s.dataset.slot] = s.dataset.label;
  }

  let allCorrect = true;
  if (unorderedSlots.length > 0) {
    // For unordered slots: collect correct labels and user labels, then compare as sets
    const unorderedCorrect = unorderedSlots.map(n => q.answer[String(n)]).sort();
    const unorderedUser = unorderedSlots.map(n => userAnswers[String(n)]).sort();
    if (JSON.stringify(unorderedCorrect) !== JSON.stringify(unorderedUser)) {
      allCorrect = false;
    }
    // Check remaining (ordered) slots
    for (const s of allSlots) {
      const num = s.dataset.slot;
      if (unorderedSlots.includes(Number(num))) continue;
      if (userAnswers[num] !== q.answer[String(num)]) {
        allCorrect = false;
        break;
      }
    }
  } else {
    for (const s of allSlots) {
      const num = s.dataset.slot;
      const correctLabel = q.answer && q.answer[String(num)];
      if (userAnswers[num] !== correctLabel) {
        allCorrect = false;
        break;
      }
    }
  }

  slotsContainer.classList.add('judged', allCorrect ? 'correct' : 'wrong');
  if (undoBtn) undoBtn.style.display = 'none';

  // Mark choices as correct/wrong
  for (const num of q.answer_numbers) {
    const isUnordered = unorderedSlots.includes(Number(num));
    const selectedEl = document.querySelector(`.multi-choice[data-qid="${qid}"][data-ans-num="${num}"].selected`);
    if (selectedEl) {
      if (isUnordered) {
        // For unordered: check if user's label is among any of the unordered correct labels
        const unorderedCorrectLabels = unorderedSlots.map(n => q.answer[String(n)]);
        if (unorderedCorrectLabels.includes(selectedEl.dataset.label)) {
          selectedEl.classList.add('correct');
        } else {
          selectedEl.classList.add('wrong');
        }
      } else {
        const correctLabel = q.answer[String(num)];
        if (selectedEl.dataset.label === correctLabel) {
          selectedEl.classList.add('correct');
        } else {
          selectedEl.classList.add('wrong');
          document.querySelectorAll(`.multi-choice[data-qid="${qid}"][data-ans-num="${num}"]`).forEach(el => {
            if (el.dataset.label === correctLabel) el.classList.add('correct');
          });
        }
      }
    }
  }

  // If wrong, show correct
  if (!allCorrect) {
    let correctText = '正解: ';
    for (const num of q.answer_numbers) {
      correctText += `[${num}] ${q.answer[String(num)]}  `;
    }
    if (q.answer_note) correctText += `（${q.answer_note}）`;
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
  const btnPrintPassage = document.getElementById('btn-print-passage');
  const btnPrintQuestions = document.getElementById('btn-print-questions');

  // Print buttons
  const params = new URLSearchParams(location.search);
  const examId = params.get('exam') || 'sundai_2025_01';
  const sectionNum = params.get('section') || '1';

  btnPrintPassage.addEventListener('click', () => {
    window.open(`print.html?exam=${examId}&mode=passage&section=${sectionNum}`, '_blank');
  });
  btnPrintQuestions.addEventListener('click', () => {
    window.open(`print.html?exam=${examId}&mode=questions&section=${sectionNum}`, '_blank');
  });

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
