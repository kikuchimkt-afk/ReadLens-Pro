/**
 * 共通テスト英語問題DB - Viewer
 * 見開きページ型学習ビューア
 */

// ===== レジストリ（app.jsと共通） =====
const EXAM_PATHS = {
  kyotsu_2025_honshiken: 'data/kyotsu/2025/honshiken/data.json',
  kyotsu_2025_tsuishiken: 'data/kyotsu/2025/tsuishiken/data.json',
  zkai_2026_01: 'data/zkai/2026/round01/data.json',
  zkai_2026_02: 'data/zkai/2026/round02/data.json',
  zkai_2026_03: 'data/zkai/2026/round03/data.json',
  zkai_2026_04: 'data/zkai/2026/round04/data.json',
  zkai_2026_05: 'data/zkai/2026/round05/data.json',
  zkai_2026_06: 'data/zkai/2026/round06/data.json',
  sundai_2026_01: 'data/sundai/2026/round01/data.json',
  sundai_2026_02: 'data/sundai/2026/round02/data.json',
  sundai_2026_03: 'data/sundai/2026/round03/data.json',
  sundai_2026_04: 'data/sundai/2026/round04/data.json',
  sundai_2026_05: 'data/sundai/2026/round05/data.json',
  sundai_2025_01: 'data/sundai/2025/round01/data.json',
  sundai_2025_02: 'data/sundai/2025/round02/data.json',
  sundai_2025_03: 'data/sundai/2025/round03/data.json',
  sundai_2025_04: 'data/sundai/2025/round04/data.json',
  kakomon_2025: 'data/kakomon/2025/data.json',
  kyotsu_2024_honshiken: 'data/kyotsu/2024/honshiken/data.json',
  kyotsu_2023_honshiken: 'data/kyotsu/2023/honshiken/data.json'
};

/**
 * 教師コメント付きエッセイ表：和文1行。英語側と同じ (1)∧・下線を再現する。
 * @param {object} sent
 * @returns {string} HTML
 */
function formatEssayMarginJaHtml(sent) {
  const hasUw = Boolean(sent.underline_word || sent.underline_word_ja);
  let text = String(sent.ja || '');

  if (sent.comment_marker && sent.marker_position !== 'after' && !hasUw) {
    const caret = sent.marker_type === 'caret' ? ' <span class="caret-mark">∧</span>' : '';
    text = '<sup class="comment-marker">' + sent.comment_marker + '</sup>' + caret + ' ' + text;
  }

  if (hasUw) {
    const uw =
      sent.underline_word_ja != null
        ? String(sent.underline_word_ja)
        : String(sent.underline_word || '');
    if (uw && text.includes(uw)) {
      const fullUnderline = String(text).trim() === uw.trim();
      const avoidDupMarker =
        uw.startsWith('(') &&
        text.includes(uw) &&
        sent.comment_marker &&
        uw.startsWith(String(sent.comment_marker));
      const markerHtml =
        sent.comment_marker &&
        sent.marker_position !== 'after' &&
        !fullUnderline &&
        !avoidDupMarker
          ? '<sup class="comment-marker">' + sent.comment_marker + '</sup>'
          : '';
      text = text.replace(uw, markerHtml + '<span class="underline-word">' + uw + '</span>');
    }
  }

  if (sent.comment_marker && sent.marker_position === 'after') {
    const caret = sent.marker_type === 'caret' ? ' <span class="caret-mark">∧</span>' : '';
    text += '<sup class="comment-marker">' + sent.comment_marker + '</sup>' + caret;
  }

  return String(text).replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>');
}

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
    const resp = await fetch(dataPath + '?v=' + new Date().getTime());
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
        for (const q of sub.questions) {
          q._subsectionLabel = sub.label;
          q._displayLabel = q.question_id;
          q.question_id = sub.label + '_' + q.question_id;
        }
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

  // Situation (skip for subsections — each subsection has its own).
  // 各英文を .sentence span でラップし、本文と同じクリック→和訳ポップアップ機能に対応させる。
  if (sec.situation && !sec.subsections) {
    let sitHtml = '<div class="situation-box">';
    const introSents = sec.situation.intro_sentences;
    if (introSents && introSents.length) {
      sitHtml += '<div class="situation-intro">';
      for (const s of introSents) {
        sitHtml += `<span class="sentence" data-sid="${s.id}">${s.en || ''}</span> `;
      }
      sitHtml += '</div>';
      sitHtml += '<div class="passage-ja-block situation-intro-sentences-ja">';
      for (const s of introSents) {
        sitHtml += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja || ''}</div>`;
      }
      sitHtml += '</div>';
    } else {
      sitHtml += `<div class="situation-intro"><span class="sentence" data-sid="__sit_intro">${sec.situation.en}</span></div>`;
    }
    if (sec.situation.steps && sec.situation.steps.length) {
      sitHtml += '<ul class="situation-steps">';
      sec.situation.steps.forEach((step, i) => {
        const sid = `__sit_step_${i}`;
        sitHtml += `<li><span class="sentence" data-sid="${sid}">${step.en || ''}</span>`;
        if (step.ja) sitHtml += `<div class="choice-text-ja">${step.ja}</div>`;
        sitHtml += '</li>';
      });
      sitHtml += '</ul>';
    }
    if (sec.situation.ja && !(introSents && introSents.length)) {
      sitHtml += `<div class="situation-intro-ja choice-text-ja">${sec.situation.ja}</div>`;
    }
    sitHtml += '</div>';
    html += sitHtml;
  }

  // Passages — grouped in one bordered container like the original exam
  const passageContainerExtra =
    sec.passage_ui && sec.passage_ui.outer_container_border === false
      ? ' passage-container--no-outer-border'
      : '';
  html += `<div class="passage-container${passageContainerExtra}">`;

  const passages = sec.passages;
  for (let i = 0; i < passages.length; i++) {
    const passage = passages[i];
    const isHeader = passage.id === 'header' || (passage.id && passage.id.startsWith('header_'));
    const isFirst = i === 0;

    // Subsection header (A/B separator for 6AB format).
    // サブセクションの situation も .sentence でラップしてクリック→和訳ポップアップに対応。
    if (passage.is_subsection_header) {
      if (!isFirst) html += '</div>'; // close previous passage-container
      html += `<div class="subsection-label">${sec.title} ${passage.subsection_label}</div>`;
      if (passage.situation) {
        const subLabel = passage.subsection_label || '';
        if (typeof passage.situation === 'string') {
          html += `<div class="situation-box"><span class="sentence" data-sid="__sit_sub_${subLabel}">${passage.situation}</span></div>`;
        } else {
          const sitEn = passage.situation.en || '';
          const sitJa = passage.situation.ja || '';
          html += `<div class="situation-box">`;
          html += `<div class="situation-intro"><span class="sentence" data-sid="__sit_sub_${subLabel}">${sitEn}</span></div>`;
          if (sitJa) {
            html += `<div class="situation-intro-ja choice-text-ja">${sitJa}</div>`;
          }
          html += `</div>`;
        }
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
    const framedCls = passage.framed ? ' passage-section--framed' : '';
    const pamphletCls = passage.pamphlet_layout ? ' passage-section--pamphlet' : '';
    const floatWrapCls =
      (passage.image && passage.image.placement === 'before_subtitle') || passage.floating_aside
        ? ' passage-section--float-wrap'
        : '';
    const emailWinCls = passage.layout === 'email_window' ? ' passage-section--email-window' : '';
    html += `<div class="passage-section${isHeader ? ' passage-section--header' : ''}${hasPortrait}${framedCls}${floatWrapCls}${pamphletCls}${emailWinCls}">`;

    if (
      passage.title &&
      !(passage.margin_comments && passage.margin_comments.length > 0) &&
      passage.layout !== 'email_window'
    ) {
      const titlePamphletCls = passage.pamphlet_layout ? ' passage-title--pamphlet-main' : '';
      let titleAlignCls = '';
      if (passage.title.align === 'center') titleAlignCls = ' passage-title--center';
      else if (passage.title.align === 'right') titleAlignCls = ' passage-title--right';
      if (passage.title.ja) {
        const tid = passage.title.id || `__title_${passage.id || 'p'}`;
        html += `<div class="passage-title${titlePamphletCls}${titleAlignCls}"><span class="sentence" data-sid="${tid}">${passage.title.en}</span></div>`;
        html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${tid}">${passage.title.ja}</div></div>`;
      } else {
        html += `<div class="passage-title${titlePamphletCls}${titleAlignCls}">${passage.title.en}</div>`;
      }
    }

    // 見出し直後に画像（記事ヘッダ横のイラスト：追試験 大問2 など）
    if (passage.image && passage.image.placement === 'before_subtitle') {
      const imgBaseEarly = currentDataPath.replace(/data\.json$/, '');
      const rawEarly = passage.image.src || '';
      const imgSrcEarly = /^https?:\/\//.test(rawEarly)
        ? rawEarly
        : rawEarly.startsWith('data/')
          ? rawEarly
          : imgBaseEarly + rawEarly;
      const layoutFullEarly =
        passage.image.layout === 'full' || passage.image.float === 'none' || passage.image.float === 'block';
      const floatClassEarly = layoutFullEarly
        ? 'passage-img--full'
        : passage.image.float === 'left'
          ? 'passage-img--left'
          : 'passage-img--right';
      html += `<img class="passage-img ${floatClassEarly}" src="${imgSrcEarly}" alt="${passage.image.alt || ''}">`;
    }

    // ロゴ＋導入枠（第5回 第1問 YCW など）— 見出しより先に置く
    if (passage.ad_top && passage.ad_top.image && passage.sentences) {
      const sentMapTop = {};
      for (const s of passage.sentences) sentMapTop[s.id] = s;
      const imgBaseTop = currentDataPath.replace(/data\.json$/, '');
      const rawTopSrc = passage.ad_top.image.src || '';
      const imgTopSrc = /^https?:\/\//.test(rawTopSrc) ? rawTopSrc : (rawTopSrc.startsWith('data/') ? rawTopSrc : imgBaseTop + rawTopSrc);
      html += '<div class="ad-top-row">';
      html += `<div class="ad-top-logo"><img src="${imgTopSrc}" alt="${passage.ad_top.image.alt || ''}"></div>`;
      html += '<div class="ad-top-intro-box">';
      html += '<p class="passage-paragraph">';
      for (const sid of passage.ad_top.sentence_ids || []) {
        const s = sentMapTop[sid];
        if (s) html += `<span class="sentence" data-sid="${s.id}">${s.en}</span> `;
      }
      html += '</p>';
      html += '<div class="passage-ja-block">';
      for (const sid of passage.ad_top.sentence_ids || []) {
        const s = sentMapTop[sid];
        if (s) html += `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div>`;
      }
      html += '</div></div></div>';
    }

    if (passage.subtitle) {
      let subAlign = '';
      if (passage.subtitle.align === 'center') subAlign = ' passage-subtitle--center';
      else if (passage.subtitle.align === 'left') subAlign = ' passage-subtitle--left';
      else if (passage.subtitle.align === 'right') subAlign = ' passage-subtitle--right';
      const subPamphlet = passage.pamphlet_layout ? ' passage-subtitle--pamphlet' : '';
      if (passage.subtitle.ja) {
        const sidSub = passage.subtitle.id || `__sub_${passage.id || 'p'}`;
        html += `<div class="passage-subtitle${subAlign}${subPamphlet}"><span class="sentence" data-sid="${sidSub}">${passage.subtitle.en}</span></div>`;
        html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${sidSub}">${passage.subtitle.ja}</div></div>`;
      } else {
        html += `<div class="passage-subtitle${subAlign}${subPamphlet}">${passage.subtitle.en}</div>`;
      }
    }

    // Image (float right/left like original exam, or full-width flyer scan)
    if (passage.image && passage.image.placement !== 'before_subtitle') {
      const imgBase = currentDataPath.replace(/data\.json$/, '');
      const rawSrc = passage.image.src || '';
      const imgSrc = /^https?:\/\//.test(rawSrc)
        ? rawSrc
        : rawSrc.startsWith('data/')
          ? rawSrc
          : imgBase + rawSrc;
      const layoutFull = passage.image.layout === 'full' || passage.image.float === 'none' || passage.image.float === 'block';
      const floatClass = layoutFull
        ? 'passage-img--full'
        : passage.image.float === 'left'
          ? 'passage-img--left'
          : 'passage-img--right';
      html += `<img class="passage-img ${floatClass}" src="${imgSrc}" alt="${passage.image.alt || ''}">`;
    }
    // Flyer layout (e.g. 2025年追試験 第1問: 文房具店チラシ)
    if (passage.is_flyer && passage.flyer) {
      html += renderFlyer(passage);
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

    if (passage.floating_aside) {
      const aside = passage.floating_aside;
      html += `<div class="passage-floating-aside" style="float:right; width:45%; border:1px solid #333; margin:0 0 15px 15px; padding:15px; border-radius:2px; background:#fff; clear:right;">`;
      if (aside.title) {
        html += `<div style="font-weight:bold; text-align:center; margin-bottom:10px;">${aside.title.en}</div>`;
      }
      if (aside.sentences) {
        html += `<ul style="list-style-type:disc; padding-left:20px; margin:0;">`;
        for (const s of aside.sentences) {
          html += `<li style="margin-bottom:6px;"><span class="sentence" data-sid="${s.id}">${s.en}</span><div class="passage-ja-block"><span class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</span></div></li>`;
        }
        html += `</ul>`;
      }
      html += `</div>`;
    }

    // Sentences rendering — skip when a custom layout (e.g. is_flyer) already
    // consumed the sentences pool to avoid dumping a duplicate wall of text.
    if (passage.sentences && !passage.is_flyer) {
      const audioFile = `${audioBase}s${secNum}_${passage.id}.mp3`;

      if (passage.advertisement_sections) {
        // ===== Structured advertisement rendering =====
        const sentMap = {};
        for (const s of passage.sentences) sentMap[s.id] = s;

        html += '<div class="para-audio-row">';
        html += '<div class="para-content">';
        const adBoxClass = passage.framed ? 'ad-box ad-box--in-framed' : 'ad-box';
        html += `<div class="${adBoxClass}">`;

        for (const adSec of passage.advertisement_sections) {
          // Section heading with separator
          if (adSec.heading) {
            html += '<hr class="ad-separator">';
            const hAlign = adSec.heading_align === 'center' ? ' ad-section-heading--center' : '';
            html += `<div class="ad-section-heading${hAlign}"><strong>${adSec.heading.en}</strong></div>`;
            if (adSec.heading.ja) {
              html += `<div class="choice-text-ja ad-section-heading-ja${hAlign}">${adSec.heading.ja}</div>`;
            }
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
          } else if (adSec.type === 'diamond_blocks') {
            // ◆見出し付きコースのまとまり（1コース＝複数文・◆は1つ）
            for (const block of adSec.blocks || []) {
              html += '<div class="ad-diamond-block">';
              html += '<span class="ad-diamond-mark" aria-hidden="true">◆</span>';
              html += '<div class="ad-diamond-body">';
              for (const sid of block.sentence_ids || []) {
                const s = sentMap[sid];
                if (s) {
                  html += `<p class="passage-paragraph ad-diamond-para"><span class="sentence" data-sid="${s.id}">${s.en}</span></p>`;
                  html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${s.id}">${s.ja}</div></div>`;
                }
              }
              html += '</div></div>';
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
        const flatSents = passage.sentences;
        const stripLeadBullet = t =>
          String(t || '')
            .replace(/^●\s*/, '')
            .replace(/^・\s*/, '');
        const useBulletList =
          Array.isArray(flatSents) &&
          flatSents.length > 0 &&
          (passage.list_style === 'bullet' || flatSents.every(s => s.role === 'bullet'));
        if (useBulletList) {
          html += '<ul class="passage-bullet-list">';
          for (const sent of flatSents) {
            const enLine = stripLeadBullet(sent.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<li class="sentence passage-bullet-item" data-sid="${sent.id}">${enLine}</li>`;
          }
          html += '</ul>';
          html += '<div class="passage-ja-block">';
          for (const sent of flatSents) {
            const jaLine = stripLeadBullet(sent.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja sentence-ja-bullet" data-sid-ja="${sent.id}">${jaLine}</div>`;
          }
          html += '</div>';
        } else {
          html += '<p class="passage-paragraph">';
          for (const sent of flatSents) {
            html += `<span class="sentence" data-sid="${sent.id}">${sent.en}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const sent of flatSents) {
            html += `<span class="sentence-ja" data-sid-ja="${sent.id}">${sent.ja}</span>`;
          }
          html += '</div>';
        }
        html += '</div>';
        html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
        html += '</div>';
      }
    }

    // Hotel brochure sheet（第4回 第2問 The Imgya など：見出し・2段ダッシュ列・料金・レビュー）
    if (passage.hotel_sheet) {
      const hs = passage.hotel_sheet;
      const imgBaseHs = currentDataPath.replace(/data\.json$/, '');
      const audioFileHs = `${audioBase}s${secNum}_${passage.id}.mp3`;
      html += '<div class="para-audio-row">';
      html += '<div class="para-content">';
      html += '<div class="hotel-sheet">';
      if (hs.banner) {
        html += '<div class="hotel-sheet-banner">';
        html += `<div class="hotel-sheet-title-en">${hs.banner.title.en}</div>`;
        if (hs.banner.image && hs.banner.image.src) {
          html += `<img class="hotel-sheet-banner-img" src="${imgBaseHs}${hs.banner.image.src}" alt="${hs.banner.image.alt || ''}" />`;
        }
        html += '</div>';
        if (hs.banner.title.ja) {
          html += `<div class="hotel-sheet-title-ja choice-text-ja">${hs.banner.title.ja}</div>`;
        }
      }
      for (const hsec of hs.sections || []) {
        const k = hsec.kind;
        if (k === 'heading_paragraph') {
          html += `<div class="hotel-sheet-strong">${hsec.heading.en}</div>`;
          if (hsec.heading.ja) {
            html += `<div class="choice-text-ja hotel-sheet-heading-ja">${hsec.heading.ja}</div>`;
          }
          const pRaw = hsec.paragraph;
          const pList = Array.isArray(pRaw) ? pRaw : (pRaw ? [pRaw] : []);
          html += '<p class="passage-paragraph hotel-sheet-para-indent">';
          for (const p of pList) {
            const enHp = String(p.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<span class="sentence" data-sid="${p.id}">${enHp}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const p of pList) {
            const jaHp = String(p.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja" data-sid-ja="${p.id}">${jaHp}</div>`;
          }
          html += '</div>';
        } else if (k === 'two_column_dashes') {
          html += `<div class="hotel-sheet-strong">${hsec.heading.en}</div>`;
          if (hsec.heading.ja) {
            html += `<div class="choice-text-ja hotel-sheet-heading-ja">${hsec.heading.ja}</div>`;
          }
          html += '<div class="hotel-sheet-two-col">';
          html += '<div class="hotel-sheet-col">';
          for (const item of hsec.left || []) {
            const t = String(item.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="hotel-sheet-dash-line"><span class="sentence" data-sid="${item.id}">\u2013 ${t}</span></div>`;
          }
          html += '</div><div class="hotel-sheet-col">';
          for (const item of hsec.right || []) {
            const t = String(item.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="hotel-sheet-dash-line"><span class="sentence" data-sid="${item.id}">\u2013 ${t}</span></div>`;
          }
          html += '</div></div>';
          html += '<div class="passage-ja-block hotel-sheet-two-col-ja">';
          html += '<div class="hotel-sheet-col">';
          for (const item of hsec.left || []) {
            const tj = String(item.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja" data-sid-ja="${item.id}">${tj}</div>`;
          }
          html += '</div><div class="hotel-sheet-col">';
          for (const item of hsec.right || []) {
            const tj = String(item.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja" data-sid-ja="${item.id}">${tj}</div>`;
          }
          html += '</div></div>';
        } else if (k === 'prices') {
          html += '<div class="hotel-sheet-prices-wrap">';
          html += `<div class="hotel-sheet-strong">${hsec.heading.en}</div>`;
          if (hsec.heading.ja) {
            html += `<div class="choice-text-ja hotel-sheet-heading-ja">${hsec.heading.ja}</div>`;
          }
          html += '<ul class="hotel-sheet-price-list">';
          for (const line of hsec.lines || []) {
            const t = String(line.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<li><span class="sentence" data-sid="${line.id}">\u2013 ${t}</span></li>`;
          }
          html += '</ul>';
          html += '<div class="passage-ja-block">';
          for (const line of hsec.lines || []) {
            const tj = String(line.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja" data-sid-ja="${line.id}">${tj}</div>`;
          }
          html += '</div></div>';
        } else if (k === 'guest_review') {
          html += '<div class="hotel-sheet-review">';
          html += '<div class="hotel-sheet-review-header">';
          html += `<span class="hotel-sheet-review-left">${hsec.header_left.en}</span>`;
          const starN = typeof hsec.stars === 'number' ? hsec.stars : 5;
          html += `<span class="hotel-sheet-review-rating">${'\u2605'.repeat(starN)} ${hsec.rating_right.en}</span>`;
          html += '</div>';
          if (hsec.header_left.ja || hsec.rating_right.ja) {
            html += '<div class="hotel-sheet-review-header-ja choice-text-ja">';
            html += `<span>${hsec.header_left.ja || ''}</span> <span>${hsec.rating_right.ja || ''}</span>`;
            html += '</div>';
          }
          html += `<div class="hotel-sheet-reviewer">${hsec.reviewer.en}</div>`;
          if (hsec.reviewer.ja) html += `<div class="choice-text-ja">${hsec.reviewer.ja}</div>`;
          const bRaw = hsec.body;
          const bList = Array.isArray(bRaw) ? bRaw : (bRaw ? [bRaw] : []);
          html += '<p class="passage-paragraph">';
          for (const b of bList) {
            const enB = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<span class="sentence" data-sid="${b.id}">${enB}</span> `;
          }
          html += '</p>';
          html += '<div class="passage-ja-block">';
          for (const b of bList) {
            const jaB = String(b.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="sentence-ja" data-sid-ja="${b.id}">${jaB}</div>`;
          }
          html += '</div>';
          html += '</div>';
        }
      }
      html += '</div>';
      html += '</div>';
      html += `<button class="btn-audio" data-audio="${audioFileHs}" title="読み上げ">🔊</button>`;
      html += '</div>';
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
        if (po.header_right && Array.isArray(po.header_right.lines_en)) {
          html += '<div class="presentation-notes-banner">';
          html += '<div class="presentation-notes-banner-main">';
          html += `<div class="presentation-outline-inner-title">${po.title.en}</div>`;
          if (po.title.ja) {
            html += `<div class="presentation-outline-inner-title-ja choice-text-ja">${po.title.ja}</div>`;
          }
          html += '</div>';
          html += '<div class="presentation-notes-header-right">';
          const hrs = po.header_right.lines_en || [];
          const hrj = po.header_right.lines_ja || [];
          for (let hi = 0; hi < hrs.length; hi++) {
            html += `<div class="presentation-notes-hand">${hrs[hi]}</div>`;
            if (hrj[hi]) html += `<div class="presentation-notes-hand choice-text-ja">${hrj[hi]}</div>`;
          }
          html += '</div></div>';
        } else {
          html += `<div class="presentation-outline-inner-title">${po.title.en}</div>`;
          if (po.title.ja) {
            html += `<div class="presentation-outline-inner-title-ja choice-text-ja">${po.title.ja}</div>`;
          }
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
        } else if (btype === 'story_outline') {
          // Story outline block: lead text → sequential answer slots with arrows → tail text
          html += `<div class="presentation-outline-strong">${bl.heading.en}</div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          if (bl.lead_en) {
            html += `<div class="story-outline-lead">${bl.lead_en}</div>`;
            if (bl.lead_ja) html += `<div class="choice-text-ja">${bl.lead_ja}</div>`;
          }
          html += '<div class="story-outline-sequential">';
          const slots = bl.sequential_slots || [];
          for (let si = 0; si < slots.length; si++) {
            html += `<div class="story-outline-slot-row"><span class="answer-slot">${slots[si]}</span></div>`;
            if (si < slots.length - 1) {
              html += '<div class="story-outline-arrow">↓</div>';
            }
          }
          html += '</div>';
          if (bl.tail_en) {
            html += `<div class="story-outline-tail">${bl.tail_en}</div>`;
            if (bl.tail_ja) html += `<div class="choice-text-ja">${bl.tail_ja}</div>`;
          }
        } else if (btype === 'underlined_heading') {
          html += `<div class="presentation-underline-heading"><span>${bl.heading.en}</span></div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
        } else if (btype === 'whos_who_brace') {
          html += `<div class="presentation-underline-heading pres-ww-title"><span>${bl.heading.en}</span></div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          html += '<div class="pres-whoswho-row">';
          html += '<div class="pres-whoswho-lines">';
          for (const row of bl.rows || []) {
            const blank =
              row.blank_slot != null
                ? `<span class="answer-slot">${row.blank_slot}</span>`
                : '<span class="notes-blank-box"></span>';
            html += `<div class="pres-whoswho-line"><strong>${row.label}:</strong> ${blank}</div>`;
          }
          html += '</div>';
          html += '<div class="pres-whoswho-brace" aria-hidden="true">}</div>';
          if (bl.brace_target_slot != null) {
            html += `<div class="pres-whoswho-target"><span class="answer-slot">${bl.brace_target_slot}</span></div>`;
          }
          html += '</div>';
        } else if (btype === 'storyline_horizontal') {
          html += `<div class="presentation-underline-heading"><span>${bl.heading.en}</span></div>`;
          if (bl.heading.ja) {
            html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
          }
          for (const line of bl.lead_lines || []) {
            html += `<div class="pres-story-lead">${line.en}</div>`;
            if (line.ja) html += `<div class="choice-text-ja">${line.ja}</div>`;
          }
          html += '<div class="pres-story-flow">';
          const hslots = bl.horizontal_slots || [];
          for (let hi = 0; hi < hslots.length; hi++) {
            if (hi > 0) {
              html += '<span class="pres-story-arrow">→</span>';
            }
            html += `<span class="answer-slot">${hslots[hi]}</span>`;
          }
          html += '</div>';
        } else if (btype === 'bullets_lead_slots') {
          if (bl.heading && bl.heading.en) {
            html += `<div class="presentation-underline-heading"><span>${bl.heading.en}</span></div>`;
            if (bl.heading.ja) {
              html += `<div class="choice-text-ja presentation-outline-heading-ja">${bl.heading.ja}</div>`;
            }
          }
          if (bl.intro && bl.intro.en) {
            html += `<div class="pres-bullets-intro">${bl.intro.en}</div>`;
            if (bl.intro.ja) html += `<div class="choice-text-ja">${bl.intro.ja}</div>`;
          }
          html += '<ul class="pres-bullets-slot-list">';
          for (const it of bl.items || []) {
            const t = String(it.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += '<li>';
            if (it.slot != null) {
              html += `<span class="answer-slot">${it.slot}</span> `;
            }
            html += t;
            if (it.ja) {
              const tj = String(it.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="choice-text-ja">${tj}</div>`;
            }
            html += '</li>';
          }
          html += '</ul>';
        }
      }
      html += '</div>'; // .presentation-outline-box
    }

    // Presentation slides grid (大問7: 6 枚のスライドを 3×2 グリッドで表示)
    if (passage.presentation_slides) {
      const ps = passage.presentation_slides;
      if (ps.label_outside_box && ps.label_outside_box.en) {
        html += `<div class="presentation-outline-label">${ps.label_outside_box.en}</div>`;
        if (ps.label_outside_box.ja) {
          html += `<div class="choice-text-ja">${ps.label_outside_box.ja}</div>`;
        }
      }
      html += '<div class="slides-grid">';
      for (const slide of ps.slides || []) {
        html += '<div class="slide-card">';
        // Slide title (centered, bold)
        if (slide.title) {
          html += `<div class="slide-title">${slide.title.en}</div>`;
          if (slide.title.ja) {
            html += `<div class="slide-title-ja choice-text-ja">${slide.title.ja}</div>`;
          }
        }
        // Image (Slide 1 など) — data.json と同じディレクトリ基準で相対パスを解決
        if (slide.image) {
          const imgBaseSlide = currentDataPath.replace(/data\.json$/, '');
          const rawSlide = slide.image.src || '';
          const slideImgSrc = /^https?:\/\//.test(rawSlide)
            ? rawSlide
            : rawSlide.startsWith('data/')
              ? rawSlide
              : imgBaseSlide + rawSlide;
          html += `<div class="slide-image-wrap"><img class="slide-image" src="${slideImgSrc}" alt="${slide.image.alt || ''}" /></div>`;
        }
        // Lead text (e.g., "The silkworm ..." or "Silk ...")
        if (slide.lead) {
          let leadHtml = slide.lead.en || '';
          if (typeof slide.lead.trailing_slot === 'number') {
            leadHtml += ` <span class="answer-slot">${slide.lead.trailing_slot}</span>`;
          }
          html += `<div class="slide-lead">${leadHtml}</div>`;
          if (slide.lead.ja) {
            const jaTrail = typeof slide.lead.trailing_slot === 'number'
              ? ` <span class="answer-slot">${slide.lead.trailing_slot}</span>` : '';
            html += `<div class="slide-lead-ja choice-text-ja">${slide.lead.ja}${jaTrail}</div>`;
          }
        }
        // Compare table (大問6B Slide 2: 2列比較表)
        if (slide.compare_table) {
          const ct = slide.compare_table;
          const cols = ct.columns || {};
          html += '<table class="slide-compare-table">';
          if (cols.en && cols.en.length === 2) {
            html += `<thead><tr><th>${cols.en[0]}</th><th>${cols.en[1]}</th></tr>`;
            if (cols.ja && cols.ja.length === 2) {
              html += `<tr class="compare-table-ja"><th><span class="choice-text-ja">${cols.ja[0]}</span></th>`
                + `<th><span class="choice-text-ja">${cols.ja[1]}</span></th></tr>`;
            }
            html += '</thead>';
          }
          html += '<tbody>';
          for (const row of (ct.rows || [])) {
            const left = String((row.left && row.left.en) || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            const right = String((row.right && row.right.en) || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<tr><td>${left}</td><td>${right}</td></tr>`;
            if ((row.left && row.left.ja) || (row.right && row.right.ja)) {
              const lja = String((row.left && row.left.ja) || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              const rja = String((row.right && row.right.ja) || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<tr class="compare-table-ja"><td><span class="choice-text-ja">${lja}</span></td>`
                + `<td><span class="choice-text-ja">${rja}</span></td></tr>`;
            }
          }
          html += '</tbody></table>';
        }
        // Bullets (•付き、スロットも含む)
        if (slide.bullets && slide.bullets.length) {
          html += '<ul class="slide-bullets">';
          for (const b of slide.bullets) {
            if (b.is_slot && typeof b.slot === 'number') {
              html += `<li><span class="answer-slot">${b.slot}</span></li>`;
            } else {
              const t = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<li>${t}`;
              if (b.ja) {
                const tj = String(b.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="choice-text-ja">${tj}</div>`;
              }
              html += '</li>';
            }
          }
          html += '</ul>';
        }
        // Lettered bullets (A. B. C. ... 形式; 大問7 Slide 3 など)
        if (slide.lettered_bullets && slide.lettered_bullets.length) {
          html += '<ul class="slide-lettered-bullets">';
          for (const lb of slide.lettered_bullets) {
            html += `<li><span class="slide-letter">${lb.letter}.</span> ${lb.en || ''}`;
            if (lb.ja) html += `<div class="choice-text-ja">${lb.ja}</div>`;
            html += '</li>';
          }
          html += '</ul>';
        }
        // Center slot (Slide 4, 6 のように [34] や [37] だけが中央にあるタイプ)
        if (typeof slide.center_slot === 'number') {
          html += `<div class="slide-center-slot"><span class="answer-slot">${slide.center_slot}</span></div>`;
        }
        // Slide number (右下)
        html += `<div class="slide-no">${slide.slide_no}</div>`;
        html += '</div>'; // .slide-card
      }
      html += '</div>'; // .slides-grid
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
      const isEmailWindow = passage.layout === 'email_window';

      if (isEmailWindow) {
        const tid = (passage.title && passage.title.id) || `__email_subj_${passage.id}`;
        const subEn = (passage.title && passage.title.en) || '';
        const subJa = (passage.title && passage.title.ja) || '';
        const dateSid = `__email_date_${passage.id}`;
        const salSid = `__email_sal_${passage.id}`;
        let salEn = (passage.salutation && passage.salutation.en) || '';
        const salJa = (passage.salutation && passage.salutation.ja) || '';
        if (!salEn && passage.to) {
          salEn = /^Dear\s/i.test(passage.to)
            ? passage.to.endsWith(',')
              ? passage.to
              : `${passage.to},`
            : `Dear ${passage.to},`;
        }
        html += '<div class="email-window">';
        html +=
          '<div class="email-window__chrome" aria-hidden="true"><span class="email-window__chrome-btn"></span><span class="email-window__chrome-btn email-window__chrome-btn--sq"></span><span class="email-window__chrome-btn email-window__chrome-btn--close"></span></div>';
        html += '<div class="email-window__header">';
        html += `<div class="email-window__date"><span class="sentence" data-sid="${dateSid}">${passage.date || ''}</span></div>`;
        html += `<div class="email-window__subject"><span class="sentence" data-sid="${tid}">${subEn}</span></div>`;
        html += '</div>';
        if (passage.date_ja || subJa) {
          html += '<div class="passage-ja-block email-window__header-ja">';
          if (passage.date && passage.date_ja) {
            html += `<div class="sentence-ja" data-sid-ja="${dateSid}">${passage.date_ja}</div>`;
          }
          if (subJa) {
            html += `<div class="sentence-ja" data-sid-ja="${tid}">${subJa}</div>`;
          }
          html += '</div>';
        }
        html += '<hr class="email-window__sep" />';
        html += `<div class="email-window__salutation"><span class="sentence" data-sid="${salSid}">${salEn}</span></div>`;
        if (salJa) {
          html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${salSid}">${salJa}</div></div>`;
        }
        html += '<div class="email-window__body">';
      }

      if (hasComments) {
        html += '<table class="essay-table"><thead><tr>';
        html += '<th class="essay-col-main">' + (passage.title ? passage.title.en : '') + '</th>';
        html += '<th class="essay-col-comments">Comments</th>';
        html += '</tr></thead><tbody>';
      }

      // essay_outline_box レイアウト用の枠開閉フラグ
      let outlineBoxOpen = false;

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
          const essayParaClass =
            passage.paragraph_classes && passage.paragraph_classes[pi]
              ? ' ' + passage.paragraph_classes[pi]
              : '';
          html += '<p class="passage-paragraph' + essayParaClass + '">';
          for (const sent of para) {
            // Show marker BEFORE sentence (default) unless marker_position is 'after'
            // But if underline_word is set, inject marker right before the underline
            if (sent.comment_marker && sent.marker_position !== 'after' && !sent.underline_word) {
              const caret = sent.marker_type === 'caret' ? ' <span class="caret-mark">∧</span>' : '';
              html += '<sup class="comment-marker">' + sent.comment_marker + '</sup>' + caret + ' ';
            }
            // Render sentence text with optional underline word
            let sentText = sent.en;
            if (sent.underline_word) {
              const fullUnderline =
                String(sent.en || '').trim() === String(sent.underline_word || '').trim();
              const uw = String(sent.underline_word || '');
              const avoidDupMarker =
                uw.startsWith('(') &&
                String(sent.en || '').includes(uw) &&
                sent.comment_marker &&
                uw.startsWith(String(sent.comment_marker));
              const markerHtml =
                sent.comment_marker &&
                sent.marker_position !== 'after' &&
                !fullUnderline &&
                !avoidDupMarker
                  ? '<sup class="comment-marker">' + sent.comment_marker + '</sup>'
                  : '';
              sentText = sentText.replace(sent.underline_word, markerHtml + '<span class="underline-word">' + sent.underline_word + '</span>');
            }
            sentText = String(sentText).replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>');
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
            html +=
              '<div class="sentence-ja" data-sid-ja="' + sent.id + '">' + formatEssayMarginJaHtml(sent) + '</div>';
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
        } else if (passage.layout === 'essay_outline_box') {
          // Essay outline (Section 8 Step 3) — PDF と同じ「ラベル＋枠囲みボックス」レイアウト
          const head = (Array.isArray(para) && para.length > 0) ? para[0] : null;
          const role = head && head.role;

          // タイトル行の手前で枠を開く
          if (!outlineBoxOpen && role === 'outline_title') {
            html += '<div class="essay-outline-box">';
            outlineBoxOpen = true;
          }

          if (role === 'outline_label') {
            html += '<div class="essay-outline-label">';
            html += `<span class="sentence" data-sid="${head.id}">${head.en}</span>`;
            html += '</div>';
            html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${head.id}">${head.ja}</div></div>`;
          } else if (role === 'outline_title') {
            html += '<div class="essay-outline-title">';
            html += `<span class="sentence" data-sid="${head.id}">${head.en}</span>`;
            html += '</div>';
            html += `<div class="passage-ja-block essay-outline-title-ja"><div class="sentence-ja" data-sid-ja="${head.id}">${head.ja}</div></div>`;
          } else if (role === 'outline_subheader') {
            html += '<div class="essay-outline-subheader">';
            html += `<span class="sentence" data-sid="${head.id}">${head.en}</span>`;
            html += '</div>';
            html += `<div class="passage-ja-block essay-outline-subheader-ja"><div class="sentence-ja" data-sid-ja="${head.id}">${head.ja}</div></div>`;
          } else if (role === 'outline_line') {
            const enText = String(head.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            const jaText = String(head.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += '<div class="essay-outline-line">';
            html += `<span class="sentence" data-sid="${head.id}">${enText}</span>`;
            html += '</div>';
            html += `<div class="passage-ja-block"><div class="sentence-ja" data-sid-ja="${head.id}">${jaText}</div></div>`;
          } else {
            html += '<div class="essay-outline-body">';
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
            html += '</div>';
          }

          // 最後の段落を描画したら枠を閉じる
          if (outlineBoxOpen && pi === passage.paragraphs.length - 1) {
            html += '</div>';
            outlineBoxOpen = false;
          }
        } else {
          const bulletParaList = passage.list_style === 'bullet';
          // Block separator before this paragraph if it's the start of a new block
          if (passage.block_separators && passage.block_separators.includes(i) && i > 0) {
            html += '<div class="block-separator">◆◆◆◆◆</div>';
          }

          // Normal paragraph rendering (no blocks)
          if (passage.pamphlet_layout && pi >= 1) {
            html += '<hr class="pamphlet-step-rule" />';
            html += '<div class="pamphlet-step-wrap">';
          }
          if (bulletParaList && pi === 0) {
            html += '<ul class="passage-bullet-list passage-bullet-para-list">';
          }
          if (bulletParaList) {
            html += '<li class="passage-bullet-audio-item">';
          }
          html += '<div class="para-audio-row">';
          html += '<div class="para-content">';
          // Insert passage images that target this paragraph
          if (passage.images) {
            const imgBase = currentDataPath.replace(/data\.json$/, '');
            for (const img of passage.images) {
              if (img.paragraph_index === pi) {
                let floatClass = 'passage-img-float-right';
                if (img.position === 'float-left') floatClass = 'passage-img-float-left';
                else if (img.position === 'block' || img.position === 'center') floatClass = 'passage-img-block';
                const styleAttr = img.max_width ? ` style="max-width:${img.max_width}px"` : '';
                const rawSrc = img.src || '';
                const imgSrc =
                  /^https?:\/\//.test(rawSrc)
                    ? rawSrc
                    : rawSrc.startsWith('data/')
                      ? rawSrc
                      : imgBase + rawSrc;
                html += `<img src="${imgSrc}" alt="${img.alt || ''}" class="passage-img ${floatClass}"${styleAttr}>`;
              }
            }
          }
          // Optional per-paragraph CSS classes (e.g. "para-indent" for first-line indent), parallel to paragraphs[]
          const paraExtraClass =
            passage.paragraph_classes && passage.paragraph_classes[pi]
              ? ' ' + passage.paragraph_classes[pi]
              : '';
          // ☆ 付き箇条書き（問題冊子のオープンスター・リスト）
          if (!Array.isArray(para) && para.list_style === 'star' && Array.isArray(para.items)) {
            html += `<ul class="passage-star-bullets${paraExtraClass}">`;
            for (const it of para.items) {
              const enText = String(it.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<li><span class="sentence" data-sid="${it.id}">${enText}</span></li>`;
            }
            html += '</ul>';
            html += '<div class="passage-ja-block passage-star-bullets-ja">';
            for (const it of para.items) {
              const jaText = String(it.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<div class="sentence-ja sentence-ja-star-line" data-sid-ja="${it.id}">${jaText}</div>`;
            }
            html += '</div>';
          } else if (!Array.isArray(para) && para.id && para.en) {
            // Object paragraph: render as a single paragraph block
            html += `<p class="passage-paragraph${paraExtraClass}">`;
            html += `<span class="sentence" data-sid="${para.id}">${para.en}</span>`;
            html += '</p>';
            html += '<div class="passage-ja-block">';
            html += `<div class="sentence-ja" data-sid-ja="${para.id}">${para.ja}</div>`;
            html += '</div>';
          } else {
            // Array of sentences — check if any have role:'bullet'
            const hasBullet = para.some(s => s.role === 'bullet');
            if (hasBullet) {
              // Group: normal sentences first, then bullets in <ul>, then normal again
              let inList = false;
              for (const sent of para) {
                const enText = String(sent.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                if (sent.role === 'bullet') {
                  if (!inList) { html += '<ul class="passage-bullet-list">'; inList = true; }
                  html += `<li class="sentence passage-bullet-item" data-sid="${sent.id}">${enText}</li>`;
                } else {
                  if (inList) { html += '</ul>'; inList = false; }
                  html += `<p class="passage-paragraph${paraExtraClass}"><span class="sentence" data-sid="${sent.id}">${enText}</span></p>`;
                }
              }
              if (inList) { html += '</ul>'; }
              html += '<div class="passage-ja-block">';
              for (const sent of para) {
                const jaText = String(sent.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                const cls = sent.role === 'bullet' ? 'sentence-ja sentence-ja-bullet' : 'sentence-ja';
                html += `<div class="${cls}" data-sid-ja="${sent.id}">${jaText}</div>`;
              }
              html += '</div>';
            } else {
              const phHead =
                passage.pamphlet_layout && Array.isArray(para)
                  ? para.find(s => s.role === 'pamphlet_heading')
                  : null;
              const phRest = phHead ? para.filter(s => s !== phHead) : para;
              if (phHead) {
                const hEn = String(phHead.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="pamphlet-step-head"><strong><span class="sentence" data-sid="${phHead.id}">${hEn}</span></strong></div>`;
              }
              html += `<p class="passage-paragraph${paraExtraClass}">`;
              for (const sent of phRest) {
                const enText = String(sent.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<span class="sentence" data-sid="${sent.id}">${enText}</span> `;
              }
              html += '</p>';
              html += '<div class="passage-ja-block">';
              if (phHead) {
                const hJa = String(phHead.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="sentence-ja" data-sid-ja="${phHead.id}">${hJa}</div>`;
              }
              for (const sent of phRest) {
                const jaText = String(sent.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="sentence-ja" data-sid-ja="${sent.id}">${jaText}</div>`;
              }
              html += '</div>';
            }
          }
          html += '</div>';
          html += `<button class="btn-audio" data-audio="${audioFile}" title="読み上げ">🔊</button>`;
          html += '</div>';
          if (bulletParaList) {
            html += '</li>';
          }
          if (bulletParaList && pi === passage.paragraphs.length - 1) {
            html += '</ul>';
          }
          if (passage.pamphlet_layout && pi >= 1) {
            html += '</div>'; // .pamphlet-step-wrap
          }
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
            // Section header row (shaded full-width label)
            if (row && row.type === 'section_header') {
              const lbl = (window._showJa && row.label_ja) ? row.label_ja : row.label;
              html += `<tr class="tbl-section-header"><td colspan="${tbl.headers.length}">${lbl}</td></tr>`;
              continue;
            }
            // Span row (Break / Lunch / End — second cell spans and centers)
            if (row && row.type === 'span') {
              const spanCells = (window._showJa && row.cells_ja) ? row.cells_ja : (row.cells || []);
              html += `<tr class="tbl-span-row"><td>${spanCells[0]}</td><td class="tbl-span-cell">${spanCells[1]}</td></tr>`;
              continue;
            }
            const rawCells = (window._showJa && row.cells_ja) ? row.cells_ja : (row.cells || []);
            const cells = Array.isArray(row) ? row : rawCells;
            const naCells = (row && row.na_cells) || [];
            html += '<tr>';
            for (let ci = 0; ci < cells.length; ci++) {
              const isNA = naCells.includes(ci);
              html += `<td${isNA ? ' class="na-cell"' : ''}>${String(cells[ci]).replace(/\n/g, '<br>')}</td>`;
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

        // Inline solve markers: 第8問のように本文を連続表示するセクションで、
        // 学習者に「次にやるべきこと」だけをシンプルに示すバッジ。
        // ヒントや設問のステムは一切表示しない（解説欄の instructor_note に集約）。
        // marker_type:
        //   "solve"  (既定) — ここで設問を解く。「ここで [問X][問Y] を解いてください」+ 解答番号バッジ。
        //   "navigate"      — 本文に戻る／次の本文へ進む等の遷移。「↳ <action_ja>」のみ。
        if (Array.isArray(passage.inline_solve_markers)) {
          for (const marker of passage.inline_solve_markers) {
            if (marker && marker.after_paragraph === pi) {
              const isNav = marker.marker_type === 'navigate';
              if (isNav) {
                // navigate: 「↳ 本文に戻る」等のシンプルな矢印行
                const text = marker.action_ja || marker.next_action_ja || '本文に戻る';
                html += '<div class="solve-marker solve-marker-nav">';
                html += '<div class="solve-marker-nav-row">';
                html += '<span class="solve-marker-nav-arrow">↩</span>';
                html += `<span class="solve-marker-nav-text">${text}</span>`;
                html += '</div>';
                html += '</div>';
              } else {
                // solve: 「ここで [問1] [問2] を解いてください」+ 解答番号バッジ
                const qids = Array.isArray(marker.question_ids)
                  ? marker.question_ids
                  : (marker.question_id ? [marker.question_id] : []);
                const nums = Array.isArray(marker.answer_numbers) ? marker.answer_numbers : [];
                const qHtml = qids.map(q => `<span class="solve-marker-q">${q}</span>`).join('');
                const numHtml = nums.map(n => `<span class="solve-marker-num">[${n}]</span>`).join(' ');
                html += '<div class="solve-marker">';
                html += '<div class="solve-marker-title">';
                html += `<span class="solve-marker-qs">${qHtml}</span>`;
                html += '<span class="solve-marker-label">を解いてください</span>';
                if (numHtml) html += ` <span class="solve-marker-nums">${numHtml}</span>`;
                html += '</div>';
                html += '</div>';
              }
            }
          }
        }
      }

      if (isEmailWindow) {
        html += '</div>';
      }



      // Teacher's comment (optional title: title_en / title_ja — 第4問「Overall Comments」など)
      if (passage.teacher_comment) {
        const tc = passage.teacher_comment;
        if (hasComments) {
          html += '<tr><td colspan="2" class="essay-teacher-comment">';
        } else {
          html += '<div class="essay-teacher-comment">';
        }
        const tcTitleEn = tc.title_en != null ? tc.title_en : "Teacher's Comment";
        html += '<strong class="essay-teacher-comment-title">' + tcTitleEn + '</strong>';
        if (tc.title_ja) {
          html += '<div class="choice-text-ja essay-teacher-comment-title-ja">' + tc.title_ja + '</div>';
        }
        html += '<br>';
        html += tc.en;
        html += '<div class="choice-text-ja">' + tc.ja + '</div>';
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

      if (isEmailWindow) {
        html += '</div>';
      }
    }

    // ===== Questionnaire rendering =====
    if (passage.id === 'questionnaire') {
      if (passage.survey_title) {
        const st = passage.survey_title;
        if (st.en) {
          html += `<div class="questionnaire-survey-title">${st.en}</div>`;
        }
        if (st.ja) {
          html += `<div class="passage-ja-block questionnaire-survey-title-ja"><div class="sentence-ja">${st.ja}</div></div>`;
        }
      }
      // Q1 title
      if (passage.q1_title) {
        html += `<div class="questionnaire-q-title">${passage.q1_title.en}</div>`;
      }
      // Bar chart image (user-provided screenshot)
      if (passage.chart_image) {
        const chartBase = currentDataPath.replace(/data\.json$/, '');
        const chartSrc = passage.chart_image.src.startsWith('http')
          ? passage.chart_image.src
          : chartBase + passage.chart_image.src;
        html += `<div class="chart-image-container"><img class="chart-image" src="${chartSrc}" alt="${passage.chart_image.alt || 'Chart'}"></div>`;
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
          html += '<div class="student-comment">';
          const parts = c.sentences && c.sentences.length ? c.sentences : null;
          if (parts) {
            for (let pi = 0; pi < parts.length; pi++) {
              const ps = parts[pi];
              const lab = pi === 0
                ? (c.label === 'S1' ? 'Student 1 (S1)' : c.label)
                : '';
              const prefix = lab ? `<strong>${lab}:</strong> ` : '';
              html += `<span class="sentence" data-sid="${ps.id}">${prefix}${ps.en}</span> `;
            }
            html += '<div class="passage-ja-block questionnaire-comment-ja">';
            for (const ps of parts) {
              html += `<div class="sentence-ja" data-sid-ja="${ps.id}">${ps.ja}</div>`;
            }
            html += '</div>';
          } else {
            html += `<span class="sentence" data-sid="${c.id}"><strong>${c.label === 'S1' ? 'Student 1 (S1)' : c.label}:</strong> ${c.en}</span>`;
            html += `<div class="sentence-ja" data-sid-ja="${c.id}">${c.ja}</div>`;
          }
          html += '</div>';
        }
      }
    }

    // ===== Handout rendering =====
    if (passage.is_handout) {
      if (passage.sections_content) {
        for (const sec of passage.sections_content) {
          html += `<div class="handout-section">`;
          const headEn = String(sec.heading.en || '').replace(
            /\[(\d+)\]/g,
            '<span class="answer-slot">$1</span>'
          );
          html += `<div class="handout-heading">■ ${headEn}</div>`;
          if (sec.heading.ja) {
            const headJa = String(sec.heading.ja).replace(
              /［(\d+)］/g,
              '<span class="answer-slot">$1</span>'
            );
            html += `<div class="choice-text-ja handout-heading-ja">${headJa}</div>`;
          }
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
              if (sub.content && sub.content.en != null && String(sub.content.en).trim() !== '') {
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
      html += `<div class="step-nav-cue" data-target-qids="問3">
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
      if (passage.notes_caption) {
        html += `<div class="notes-caption">${passage.notes_caption.en}</div>`;
        if (passage.notes_caption.ja) {
          html += `<div class="notes-caption-ja choice-text-ja">${passage.notes_caption.ja}</div>`;
        }
      }
      html += `<div class="notes-title">${passage.notes_title.en}</div>`;
      if (passage.notes_title.ja) {
        html += `<div class="passage-ja-block"><div class="choice-text-ja notes-title-ja">${passage.notes_title.ja}</div></div>`;
      }

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

      // About Maki (大問5: 主人公が女性のストーリー型)
      if (passage.about_maki) {
        const am = passage.about_maki;
        const heading = (am.heading && am.heading.en) || 'About Maki';
        html += `<div class="notes-heading">${heading}</div>`;
        if (am.heading && am.heading.ja) {
          html += `<div class="passage-ja-block"><div class="choice-text-ja notes-heading-ja">${am.heading.ja}</div></div>`;
        }
        html += '<ul class="notes-list">';
        const ageSlot = `<span class="answer-slot">${am.age_slot}</span>`;
        html += `<li>Age: ${ageSlot}</li>`;
        html += `<li>Occupation: ${am.occupation.en}</li>`;
        const supportLabel = (am.support_heading && am.support_heading.en) || 'How she supported her friends:';
        html += `<li>${supportLabel}`;
        for (const item of am.support) {
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

      // Outline by paragraph (大問6A: 番号付きリスト + サブ▸アイテム)
      if (passage.outline_by_paragraph) {
        const obp = passage.outline_by_paragraph;
        const heading = (obp.header && obp.header.en) || 'Outline by paragraph';
        html += `<div class="notes-heading">${heading}</div>`;
        if (obp.header && obp.header.ja) {
          html += `<div class="passage-ja-block"><div class="choice-text-ja notes-heading-ja">${obp.header.ja}</div></div>`;
        }
        html += '<ol class="notes-numbered">';
        for (const item of (obp.items || [])) {
          const t = String(item.text && item.text.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<li value="${item.number}">${t}`;
          if (item.text && item.text.ja) {
            const tja = String(item.text.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="choice-text-ja">${tja}</div>`;
          }
          if (item.sub_items && item.sub_items.length) {
            html += '<ul class="notes-sub-bullets">';
            for (const sub of item.sub_items) {
              const subT = String(sub.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
              html += `<li>${subT}`;
              if (sub.ja) {
                const subJa = String(sub.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
                html += `<div class="choice-text-ja">${subJa}</div>`;
              }
              html += '</li>';
            }
            html += '</ul>';
          }
          html += '</li>';
        }
        html += '</ol>';
      }

      // Original examples (大問6A: A./B. ヘッダ付き例)
      if (passage.original_examples) {
        const oe = passage.original_examples;
        const heading = (oe.header && oe.header.en) || 'My original examples';
        html += `<div class="notes-heading">${heading}</div>`;
        if (oe.header && oe.header.ja) {
          html += `<div class="passage-ja-block"><div class="choice-text-ja notes-heading-ja">${oe.header.ja}</div></div>`;
        }
        for (const item of (oe.items || [])) {
          html += '<div class="notes-original-example">';
          html += `<div class="notes-original-label"><strong>${item.label}.</strong> ${item.heading && item.heading.en || ''}</div>`;
          if (item.heading && item.heading.ja) {
            html += `<div class="passage-ja-block"><div class="choice-text-ja">${item.heading.ja}</div></div>`;
          }
          const t = String(item.text && item.text.en || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
          html += `<div class="notes-original-text">${t}</div>`;
          if (item.text && item.text.ja) {
            const tja = String(item.text.ja).replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>');
            html += `<div class="passage-ja-block"><div class="choice-text-ja">${tja}</div></div>`;
          }
          html += '</div>';
        }
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

// ===== Flyer Layout Renderer (2025年追試験 第1問: 文房具店チラシ) =====
function renderFlyer(passage) {
  const sentMap = {};
  for (const s of (passage.sentences || [])) sentMap[s.id] = s;
  const imgBase = currentDataPath.replace(/data\.json$/, '');
  const resolveSrc = (src) => /^https?:\/\//.test(src) || src.startsWith('data/') ? src : imgBase + src;

  const sentEN = (sid) => {
    const s = sentMap[sid];
    return s ? `<span class="sentence" data-sid="${s.id}">${s.en || ''}</span>` : '';
  };
  const sentJA = (sid) => {
    const s = sentMap[sid];
    return s ? `<div class="sentence-ja" data-sid-ja="${s.id}">${s.ja || ''}</div>` : '';
  };
  const sentLine = (sid) => `<div class="flyer-line">${sentEN(sid)}${sentJA(sid)}</div>`;

  const f = passage.flyer;
  let h = '<div class="flyer-frame">';

  // Top section: header (badge / logo / special-gift)
  h += '<div class="flyer-top">';

  // Header row with three columns
  h += '<div class="flyer-header-row">';
  // Badge (Celebrating 50 years!)
  if (f.header && f.header.badge_image) {
    h += `<div class="flyer-badge"><img src="${resolveSrc(f.header.badge_image)}" alt="Celebrating 50 years!"></div>`;
  }
  // Center logo (Stationery Supplies / Arigato / Established 1975)
  if (f.header && f.header.logo_image) {
    h += `<div class="flyer-logo"><img src="${resolveSrc(f.header.logo_image)}" alt="Arigato"></div>`;
  }
  // Special Gift dashed box
  if (f.header && f.header.special_gift) {
    const sg = f.header.special_gift;
    h += '<div class="flyer-special-gift">';
    h += '<div class="flyer-sg-title">Special Gift</div>';
    for (const sid of sg.line_ids || []) h += sentLine(sid);
    h += '</div>';
  }
  h += '</div>'; // .flyer-header-row

  // Store info (centered lines under header)
  if (f.header && Array.isArray(f.header.store_info_ids)) {
    h += '<div class="flyer-store-info">';
    for (const sid of f.header.store_info_ids) h += sentLine(sid);
    h += '</div>';
  }

  h += '</div>'; // .flyer-top

  // Monthly specials banner
  if (f.specials_banner) {
    h += '<div class="flyer-specials-banner">';
    if (f.specials_banner.title_id) {
      h += `<div class="flyer-specials-title">${sentEN(f.specials_banner.title_id)}</div>`;
      h += sentJA(f.specials_banner.title_id);
    }
    if (f.specials_banner.subtitle_id) {
      h += `<div class="flyer-specials-subtitle">**${sentEN(f.specials_banner.subtitle_id)}**</div>`;
      h += sentJA(f.specials_banner.subtitle_id);
    }
    h += '</div>';
  }

  // Product table
  if (Array.isArray(f.products) && f.products.length) {
    h += '<table class="flyer-products"><tbody>';
    for (const p of f.products) {
      h += '<tr class="flyer-product-row">';
      h += '<td class="flyer-product-illus">';
      if (p.price) h += `<div class="flyer-product-price">${p.price}</div>`;
      if (p.image) h += `<img src="${resolveSrc(p.image)}" alt="${p.name_id || ''}">`;
      if (p.name_id) {
        h += `<div class="flyer-product-name">${sentEN(p.name_id)}</div>`;
        h += sentJA(p.name_id);
      }
      h += '</td>';
      h += '<td class="flyer-product-desc">';
      if (p.desc_id) {
        h += sentEN(p.desc_id);
        h += sentJA(p.desc_id);
      }
      h += '</td>';
      h += '</tr>';
    }
    h += '</tbody></table>';
  }

  h += '</div>'; // .flyer-frame
  return h;
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
  // ── 合成 ID（situation 系）— リード文の click→和訳ポップアップ用
  if (typeof sid === 'string' && sid.startsWith('__sit_')) {
    const sit = currentSection && currentSection.situation;
    if (sid === '__sit_intro') return (sit && sit.ja) || null;
    const stepMatch = sid.match(/^__sit_step_(\d+)$/);
    if (stepMatch && sit && Array.isArray(sit.steps)) {
      const idx = parseInt(stepMatch[1], 10);
      return (sit.steps[idx] && sit.steps[idx].ja) || null;
    }
    // サブセクション header の situation: __sit_sub_<label>
    const subMatch = sid.match(/^__sit_sub_(.+)$/);
    if (subMatch) {
      const label = subMatch[1];
      // currentSection.subsections から探す（sub.label 一致 → sub.situation.ja）
      if (currentSection && Array.isArray(currentSection.subsections)) {
        const sub = currentSection.subsections.find(s => s.label === label);
        if (sub && sub.situation) {
          return (typeof sub.situation === 'object' && sub.situation.ja) || null;
        }
      }
      return null;
    }
    return null;
  }

  // ── situation.intro_sentences
  if (currentSection.situation && currentSection.situation.intro_sentences) {
    for (const s of currentSection.situation.intro_sentences) {
      if (s.id === sid) return s.ja;
    }
  }

  // ── 設問 stem.sentences
  for (const q of currentSection.questions || []) {
    const stem = q.stem || q.question_text;
    if (stem && stem.sentences) {
      const hit = stem.sentences.find(s => s.id === sid);
      if (hit) return hit.ja;
    }
  }

  // ── questionnaire のコメント（複数文）
  for (const passage of currentSection.passages || []) {
    if (passage.id === 'questionnaire' && passage.comments) {
      for (const c of passage.comments) {
        if (c.sentences) {
          const hit = c.sentences.find(s => s.id === sid);
          if (hit) return hit.ja;
        }
        if (c.id === sid) return c.ja;
      }
    }
  }

  // ── 通常の本文 sentence ID
  for (const passage of currentSection.passages) {
    if (passage.layout === 'email_window') {
      if (sid === `__email_date_${passage.id}`) return passage.date_ja || null;
      if (sid === `__email_sal_${passage.id}`) return (passage.salutation && passage.salutation.ja) || null;
      if (
        passage.title &&
        (sid === passage.title.id || sid === `__email_subj_${passage.id}`)
      ) {
        return passage.title.ja || null;
      }
    }
    if (passage.subtitle && passage.subtitle.id === sid) {
      return passage.subtitle.ja || null;
    }
    if (passage.sentences) {
      const sent = passage.sentences.find(s => s.id === sid);
      if (sent) return sent.ja;
    }
    if (passage.paragraphs) {
      for (const para of passage.paragraphs) {
        if (Array.isArray(para)) {
          const sent = para.find(s => s.id === sid);
          if (sent) return sent.ja;
        } else if (para && para.list_style === 'star' && Array.isArray(para.items)) {
          const sent = para.items.find(s => s.id === sid);
          if (sent) return sent.ja;
        } else if (para && para.id === sid) {
          return para.ja;
        }
      }
    }
    if (passage.authors) {
      for (const author of passage.authors) {
        for (const para of author.paragraphs || []) {
          for (const s of para) {
            if (s.id === sid) return s.ja;
          }
        }
      }
    }
    if (passage.sources) {
      for (const source of passage.sources) {
        for (const para of source.paragraphs || []) {
          for (const s of para) {
            if (s.id === sid) return s.ja;
          }
        }
      }
    }
    if (passage.hotel_sheet && passage.hotel_sheet.sections) {
      for (const hsec of passage.hotel_sheet.sections) {
        if (hsec.kind === 'heading_paragraph' && hsec.paragraph) {
          const plist = Array.isArray(hsec.paragraph) ? hsec.paragraph : [hsec.paragraph];
          for (const p of plist) {
            if (p.id === sid) return p.ja;
          }
        }
        if (hsec.kind === 'two_column_dashes') {
          for (const item of [...(hsec.left || []), ...(hsec.right || [])]) {
            if (item.id === sid) return item.ja;
          }
        }
        if (hsec.kind === 'prices') {
          for (const line of hsec.lines || []) {
            if (line.id === sid) return line.ja;
          }
        }
        if (hsec.kind === 'guest_review' && hsec.body) {
          const blist = Array.isArray(hsec.body) ? hsec.body : [hsec.body];
          for (const b of blist) {
            if (b.id === sid) return b.ja;
          }
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
const audioBarSpeed = document.getElementById('audio-bar-speed');
let seekAnimFrame = null;

let currentPlaybackRate = parseFloat(localStorage.getItem('readlensPlaybackRate')) || 1.0;
if (audioBarSpeed) {
  audioBarSpeed.textContent = currentPlaybackRate.toFixed(1) + 'x';
  audioBarSpeed.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    currentPlaybackRate = Math.abs(currentPlaybackRate - 1.0) < 0.01 ? 0.9 : 1.0;
    audioBarSpeed.textContent = currentPlaybackRate.toFixed(1) + 'x';
    localStorage.setItem('readlensPlaybackRate', currentPlaybackRate.toString());
    if (currentAudio) {
      currentAudio.defaultPlaybackRate = currentPlaybackRate;
      currentAudio.playbackRate = currentPlaybackRate;
    }
  });
}

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
  currentAudio.defaultPlaybackRate = currentPlaybackRate;
  currentAudio.playbackRate = currentPlaybackRate;
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

  currentAudio.addEventListener('play', () => {
    currentAudio.playbackRate = currentPlaybackRate;
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

/** choices_N 付きの複数空欄。answer_numbers が無い場合は answer のキーと choices_N から導出する */
function deriveMultiSlotAnswerNumbers(q) {
  if (Array.isArray(q.answer_numbers) && q.answer_numbers.length) return q.answer_numbers;
  if (q.answer && typeof q.answer === 'object' && !Array.isArray(q.answer)) {
    const nums = Object.keys(q.answer)
      .map(k => parseInt(k, 10))
      .filter(
        n =>
          !isNaN(n) &&
          Array.isArray(q['choices_' + n]) &&
          q['choices_' + n].length > 0
      );
    nums.sort((a, b) => a - b);
    if (nums.length) return nums;
  }
  return null;
}

/** 複数空欄の正解を UI の選択肢ラベル（① 等）に揃える（データが 1 始まりの番号のときは choices から変換） */
function normalizeSlotAnswerLabel(q, slotNum, raw) {
  if (raw == null || raw === '') return raw;
  if (typeof raw === 'string' && !/^\d+$/.test(raw)) return raw;
  const idx = typeof raw === 'number' ? raw : parseInt(String(raw), 10);
  if (isNaN(idx) || idx < 1) return String(raw);
  const slotChoices = q['choices_' + slotNum];
  const arr =
    Array.isArray(slotChoices) && slotChoices.length
      ? slotChoices
      : Array.isArray(q.choices) && q.choices.length
        ? q.choices
        : null;
  const choice = arr && arr[idx - 1];
  return (choice && choice.label) ? choice.label : String(raw);
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
    // Optional Step / phase header rendered above this question
    // (e.g. "Step 2: Take a position ..." inserted before 問3 of 第8問)
    if (q.pre_header && (q.pre_header.en || q.pre_header.ja)) {
      html += `<div class="question-pre-header">`;
      if (q.pre_header.en) html += `<div class="question-pre-header-en">${q.pre_header.en}</div>`;
      if (q.pre_header.ja) html += `<div class="question-pre-header-ja choice-text-ja">${q.pre_header.ja}</div>`;
      html += `</div>`;
    }
    const qIdx = getQuestionIndex(q.question_id);
    html += `<div class="question-block" data-qid="${q.question_id}">`;

    // Question label + per-question evidence button
    html += `<div class="question-label-row">
      <span class="question-label">${q._displayLabel || q.question_id}</span>
      <button class="btn-evidence-q" data-qid="${q.question_id}" data-qidx="${qIdx}" title="根拠箇所をヒント表示">ヒント</button>
    </div>`;

    // Stem (support both "stem" and "question_text" field names)
    const stemObj = q.stem || q.question_text;
    if (stemObj && stemObj.sentences && stemObj.sentences.length) {
      html += '<div class="question-stem">';
      for (const s of stemObj.sentences) {
        const enLine = String(s.en || '').replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>');
        html += `<span class="sentence" data-sid="${s.id}">${enLine}</span> `;
      }
      html += '</div>';
      html += '<div class="passage-ja-block question-stem-ja">';
      for (const s of stemObj.sentences) {
        const jaLine = String(s.ja || '')
          .replace(/［\s*(\d+)\s*］/g, '<span class="answer-slot">$1</span>')
          .replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>');
        html += `<div class="sentence-ja" data-sid-ja="${s.id}">${jaLine}</div>`;
      }
      html += '</div>';
    } else if (stemObj && stemObj.en) {
      const stemEn = String(stemObj.en || '')
        .replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>')
        .replace(/\n/g, '<br>');
      html += `<div class="question-stem">${stemEn}</div>`;
    }

    // Stem ja (hidden by default) — single-block stems only
    if (stemObj && stemObj.ja && !(stemObj.sentences && stemObj.sentences.length)) {
      const stemJa = String(stemObj.ja || '')
        .replace(/［\s*(\d+)\s*］/g, '<span class="answer-slot">$1</span>')
        .replace(/\[\s*(\d+)\s*\]/g, '<span class="answer-slot">$1</span>')
        .replace(/\n/g, '<br>');
      html += `<div class="choice-text-ja" style="margin-bottom:10px; margin-top:-8px;">${stemJa}</div>`;
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
      let cap = '';
      if (qFig.caption_en && String(qFig.caption_en).trim()) {
        cap += `<div class="question-figure-caption question-figure-caption-en">${qFig.caption_en}</div>`;
      }
      if (qFig.caption_ja && String(qFig.caption_ja).trim()) {
        cap += `<div class="question-figure-caption choice-text-ja">${qFig.caption_ja}</div>`;
      }
      const qFigBase = currentDataPath.replace(/data\.json$/, '');
      const rawFigSrc = qFig.src || '';
      const finalFigSrc = /^https?:\/\//.test(rawFigSrc) ? rawFigSrc : (rawFigSrc.startsWith('data/') ? rawFigSrc : qFigBase + rawFigSrc);
      html += `<figure class="question-figure">
        <img src="${finalFigSrc}" alt="${qFig.alt || ''}" />
        ${cap}
      </figure>`;
    }

    // Position box (Step 2 のメモ枠: Your position / Authors [X] and [Y] / main argument [Z])
    if (q.position_box && (q.position_box.en || q.position_box.ja)) {
      const pbEn = (q.position_box.en || '')
        .replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>')
        .replace(/\n/g, '<br>');
      const pbJa = (q.position_box.ja || '').replace(/\[(\d+)\]/g, '<span class="answer-slot">$1</span>').replace(/\n/g, '<br>');
      html += `<div class="position-box">`;
      html += `<div class="position-box-en">${pbEn}</div>`;
      if (pbJa) html += `<div class="position-box-ja choice-text-ja">${pbJa}</div>`;
      html += `</div>`;
    }

    // Question-level table/chart image (uses imgBase path like graph_image)
    if (q.question_image && q.question_image.src) {
      const qImgBase = currentDataPath.replace(/data\.json$/, '');
      const qImgCap = q.question_image.caption_ja
        ? `<div class="question-figure-caption">${q.question_image.caption_ja}</div>` : '';
      html += `<figure class="question-figure">
        <img class="chart-image" src="${qImgBase}${q.question_image.src}" alt="${q.question_image.alt || ''}" />
        ${qImgCap}
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

    const multiSlotNums = deriveMultiSlotAnswerNumbers(q);

    // Two-column combination choices (e.g. 第6問 問1: Anais | Samantha)
    if (q.choice_pair_headers && q.choices && q.choices.some(c => c.pair_left && c.pair_right)) {
      html += '<div class="choice-pairs-wrap">';
      html += '<div class="choice-pairs-head" role="row">';
      html += '<div class="choice-pairs-head-spacer" aria-hidden="true"></div>';
      for (const h of q.choice_pair_headers) {
        html += `<div class="choice-pairs-head-col"><span class="choice-pairs-head-underline">${h.en || ''}</span>`;
        if (h.ja) html += `<div class="choice-text-ja choice-pairs-head-ja">${h.ja}</div>`;
        html += '</div>';
      }
      html += '</div>';
      html += '<div class="choice-pairs-body">';
      for (let i = 0; i < q.choices.length; i++) {
        const choice = q.choices[i];
        if (!choice.pair_left || !choice.pair_right) continue;
        let isCorrect = choice.is_correct;
        if (isCorrect === undefined && q.answer !== undefined) {
          if (Array.isArray(q.answer)) {
            isCorrect = q.answer.includes(i + 1);
          } else {
            isCorrect = (q.answer === (i + 1));
          }
        }
        const dc = isCorrect === true ? 'true' : 'false';
        html += `<div class="choice-item choice-pair-row" data-qid="${q.question_id}" data-label="${choice.label}" data-correct="${dc}">`;
        html += `<div class="choice-pair-label-wrap"><span class="choice-pair-label-badge">${choice.label}</span></div>`;
        html += '<div class="choice-pair-cell-box">';
        html += `<span class="choice-text">${choice.pair_left.en || ''}</span>`;
        if (choice.pair_left.ja) {
          html += `<div class="choice-text-ja">${choice.pair_left.ja}</div>`;
        }
        html += '</div>';
        html += '<div class="choice-pair-cell-box">';
        html += `<span class="choice-text">${choice.pair_right.en || ''}</span>`;
        if (choice.pair_right.ja) {
          html += `<div class="choice-text-ja">${choice.pair_right.ja}</div>`;
        }
        html += '</div></div>';
      }
      html += '</div></div>';
    } else if (q.question_type === 'ordering') {
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
    } else if (multiSlotNums) {
      // Multiple answer: slot-based UI (select all before checking)
      html += '<div class="multi-answer-slots" data-qid="' + q.question_id + '">';
      for (let ai = 0; ai < multiSlotNums.length; ai++) {
        const ansNum = multiSlotNums[ai];
        if (ai > 0) html += '<span class="ordering-arrow">＋</span>';
        html += '<span class="ordering-slot multi-slot" data-slot="' + ansNum + '">[' + ansNum + ']</span>';
      }
      html += '</div>';
      const anySlotSpecificChoices = multiSlotNums.some(
        n => Array.isArray(q['choices_' + n]) && q['choices_' + n].length > 0
      );
      for (const ansNum of multiSlotNums) {
        const choicesKey = `choices_${ansNum}`;
        let choices = q[choicesKey];
        if (!Array.isArray(choices) || !choices.length) {
          if (!anySlotSpecificChoices && Array.isArray(q.choices) && q.choices.length) {
            choices = q.choices;
          }
        }
        if (!Array.isArray(choices) || !choices.length) continue;
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
      for (let i = 0; i < q.choices.length; i++) {
        const choice = q.choices[i];
        let isCorrect = choice.is_correct;
        if (isCorrect === undefined && q.answer !== undefined) {
          if (Array.isArray(q.answer)) {
            isCorrect = q.answer.includes(i + 1);
          } else {
            isCorrect = (q.answer === (i + 1));
          }
        }
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
        html += `<li class="choice-item${liExtra}" data-qid="${q.question_id}" data-label="${choice.label}" data-correct="${isCorrect}">
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
  html += `<div class="explanation-header">📖 解説（${q._displayLabel || q.question_id}）</div>`;

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
    // Compare by raw labels (e.g. "①","②"...) to match answer_sequence which is character-form.
    const userLabels = [...slots].map(s => s.dataset.label);
    const isCorrect = JSON.stringify(userLabels) === JSON.stringify(q.answer_sequence);

    slotsContainer.classList.add('judged', isCorrect ? 'correct' : 'wrong');
    undoBtn.style.display = 'none';

    // If wrong, show correct answer
    if (!isCorrect) {
      let correctText;
      if (q.answer && typeof q.answer === 'object') {
        // Multi-slot dict: {"25": "⑤", "26": "②", ...}
        const parts = Object.entries(q.answer).map(([k, v]) => `[${k}] ${v}`);
        correctText = parts.join('  ');
        if (q.answer_note) correctText += `（${q.answer_note}）`;
      } else if (Array.isArray(q.answer_sequence)) {
        correctText = q.answer_sequence.join(' → ');
        if (q.answer_note) correctText += `（${q.answer_note}）`;
      } else {
        correctText = String(q.answer || '');
      }
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
  const slotNums = deriveMultiSlotAnswerNumbers(q);
  if (!slotNums || !slotNums.length) return;

  // Determine which slots are unordered (e.g. [27] and [28] are interchangeable)
  let unorderedSlots = Array.isArray(q.unordered_slots) && q.unordered_slots.length
    ? q.unordered_slots.map(Number)
    : [];
  if (!unorderedSlots.length && q.unordered === true && slotNums.length >= 2) {
    unorderedSlots = slotNums.map(Number);
  }
  const userAnswers = {};
  for (const s of allSlots) {
    userAnswers[s.dataset.slot] = s.dataset.label;
  }

  let allCorrect = true;
  if (unorderedSlots.length > 0) {
    // For unordered slots: collect correct labels and user labels, then compare as sets
    const unorderedCorrect = unorderedSlots
      .map(n => normalizeSlotAnswerLabel(q, n, q.answer[String(n)]))
      .sort();
    const unorderedUser = unorderedSlots.map(n => userAnswers[String(n)]).sort();
    if (JSON.stringify(unorderedCorrect) !== JSON.stringify(unorderedUser)) {
      allCorrect = false;
    }
    // Check remaining (ordered) slots
    for (const s of allSlots) {
      const num = s.dataset.slot;
      if (unorderedSlots.includes(Number(num))) continue;
      const correctLabel = normalizeSlotAnswerLabel(q, Number(num), q.answer[String(num)]);
      if (userAnswers[num] !== correctLabel) {
        allCorrect = false;
        break;
      }
    }
  } else {
    for (const s of allSlots) {
      const num = s.dataset.slot;
      const correctLabel = q.answer && normalizeSlotAnswerLabel(q, Number(num), q.answer[String(num)]);
      if (userAnswers[num] !== correctLabel) {
        allCorrect = false;
        break;
      }
    }
  }

  slotsContainer.classList.add('judged', allCorrect ? 'correct' : 'wrong');
  if (undoBtn) undoBtn.style.display = 'none';

  // Mark choices as correct/wrong
  for (const num of slotNums) {
    const isUnordered = unorderedSlots.includes(Number(num));
    const selectedEl = document.querySelector(`.multi-choice[data-qid="${qid}"][data-ans-num="${num}"].selected`);
    if (selectedEl) {
      if (isUnordered) {
        // For unordered: check if user's label is among any of the unordered correct labels
        const unorderedCorrectLabels = unorderedSlots.map(n =>
          normalizeSlotAnswerLabel(q, n, q.answer[String(n)])
        );
        if (unorderedCorrectLabels.includes(selectedEl.dataset.label)) {
          selectedEl.classList.add('correct');
        } else {
          selectedEl.classList.add('wrong');
        }
      } else {
        const correctLabel = normalizeSlotAnswerLabel(q, Number(num), q.answer[String(num)]);
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
    for (const num of slotNums) {
      correctText += `[${num}] ${normalizeSlotAnswerLabel(q, Number(num), q.answer[String(num)])}  `;
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
  const q = currentSection.questions.find(q => q.question_id === qid);
  if (!q) return 1;
  const subLabel = q._subsectionLabel;
  if (subLabel) {
    const subQuestions = currentSection.questions.filter(q2 => q2._subsectionLabel === subLabel);
    const idx = subQuestions.findIndex(q2 => q2.question_id === qid);
    return idx >= 0 ? idx + 1 : 1;
  }
  const idx = currentSection.questions.findIndex(q2 => q2.question_id === qid);
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
      const displayLabel = q._displayLabel || qid;
      addEvidenceTag(el, displayLabel, qIdx);
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
        addEvidenceTag(el, q._displayLabel || q.question_id, qIdx);
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
