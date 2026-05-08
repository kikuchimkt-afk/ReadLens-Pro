/**
 * 共通テスト英語問題DB - Print Module
 * URL params:
 *   exam=sundai_2025_01
 *   mode=passage|questions|all
 *   section=1  (for passage/questions mode)
 */

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
  sundai_2025_01: 'data/sundai/2025/round01/data.json',
  sundai_2025_02: 'data/sundai/2025/round02/data.json',
  sundai_2025_03: 'data/sundai/2025/round03/data.json',
  sundai_2025_04: 'data/sundai/2025/round04/data.json',
  kakomon_2025: 'data/kakomon/2025/data.json',
  kakomon_2024: 'data/kakomon/2024/data.json',
  kyotsu_2024_honshiken: 'data/kyotsu/2024/honshiken/data.json'
};

document.addEventListener('DOMContentLoaded', async () => {
  const params = new URLSearchParams(location.search);
  const examId = params.get('exam') || 'sundai_2025_01';
  const mode = params.get('mode') || 'all';
  const sectionParam = params.get('section') || '0';
  const sectionNum = /^\d+$/.test(sectionParam) ? parseInt(sectionParam) : sectionParam;

  const dataPath = EXAM_PATHS[examId];
  if (!dataPath) {
    document.getElementById('print-content').innerHTML = '<p>データが見つかりません。</p>';
    return;
  }

  const res = await fetch(dataPath);
  const data = await res.json();

  const examName = (data.exam_info && data.exam_info.title) || 'Exam';
  document.title = examName + ' — 印刷';
  document.getElementById('print-title').textContent = examName + ' — 印刷プレビュー';

  let html = '';

  if (mode === 'passage' && sectionNum) {
    const sec = data.sections.find(s => String(s.section_number) === String(sectionNum));
    if (sec) html = renderPassagePage(sec, dataPath);
  } else if (mode === 'questions' && sectionNum) {
    const sec = data.sections.find(s => String(s.section_number) === String(sectionNum));
    if (sec) html = renderQuestionsPage(sec, dataPath);
  } else {
    // all: 大問1問題→大問1設問→大問2問題→…
    for (const sec of data.sections) {
      html += renderPassagePage(sec, dataPath);
      html += renderQuestionsPage(sec, dataPath);
    }
  }

  document.getElementById('print-content').innerHTML = html;
});

// ===== Render Passage Page =====
function renderPassagePage(sec, dataPath) {
  let html = '<div class="print-section">';

  // Header
  html += '<div class="print-section-header">';
  html += '<div class="print-section-title">' + sec.title + '</div>';
  if (sec.points) {
    html += '<div class="print-section-subtitle">配点 ' + sec.points + '点';
    if (sec.points_per_question && typeof sec.points_per_question === 'number') {
      html += '（各' + sec.points_per_question + '点×' + sec.questions.length + '問）';
    }
    html += '</div>';
  }
  html += '<div class="print-section-type">― 問題 ―</div>';
  html += '</div>';

  // Situation
  if (sec.situation) {
    html += '<div class="print-situation">' + sec.situation.en + '</div>';
  }

  // Passages
  for (const passage of sec.passages) {
    const hasComments = passage.margin_comments && passage.margin_comments.length > 0;

    if (passage.hotel_sheet) {
      const hs = passage.hotel_sheet;
      const imgBase = dataPath ? dataPath.replace(/data\.json$/, '') : '';
      html += '<div class="print-passage print-hotel-sheet" style="border:1px solid #333;padding:12px;">';
      if (hs.banner) {
        html += '<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">';
        html += '<div style="font-weight:700;font-size:14pt;">' + hs.banner.title.en + '</div>';
        if (hs.banner.image && hs.banner.image.src) {
          html +=
            '<img class="print-img" src="' +
            imgBase +
            hs.banner.image.src +
            '" style="max-width:110px;" alt="">';
        }
        html += '</div>';
      }
      for (const hsec of hs.sections || []) {
        const k = hsec.kind;
        if (k === 'heading_paragraph') {
          html += '<div style="font-weight:700;margin-top:10px;">' + hsec.heading.en + '</div>';
          html +=
            '<p style="text-indent:1.5em;margin:6px 0;">' +
            hsec.paragraph.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
            '</p>';
        } else if (k === 'two_column_dashes') {
          html += '<div style="font-weight:700;margin-top:10px;">' + hsec.heading.en + '</div>';
          html += '<table style="width:100%;margin-top:6px;"><tr>';
          html += '<td style="width:50%;vertical-align:top;padding-right:8px;">';
          for (const item of hsec.left || []) {
            html +=
              '<div>\u2013 ' +
              String(item.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
              '</div>';
          }
          html += '</td><td style="width:50%;vertical-align:top;">';
          for (const item of hsec.right || []) {
            html +=
              '<div>\u2013 ' +
              String(item.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
              '</div>';
          }
          html += '</td></tr></table>';
        } else if (k === 'prices') {
          html += '<div style="margin-top:12px;padding-bottom:8px;border-bottom:1px dashed #999;">';
          html += '<div style="font-weight:700;">' + hsec.heading.en + '</div>';
          html += '<ul style="margin:6px 0;padding-left:18px;list-style:none;">';
          for (const line of hsec.lines || []) {
            html +=
              '<li>\u2013 ' +
              String(line.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
              '</li>';
          }
          html += '</ul></div>';
        } else if (k === 'guest_review') {
          html += '<div style="margin-top:12px;border:1px solid #666;padding:10px;">';
          html +=
            '<div style="display:flex;justify-content:space-between;flex-wrap:wrap;"><span>' +
            hsec.header_left.en +
            '</span><span>';
          const starN = typeof hsec.stars === 'number' ? hsec.stars : 5;
          html += '\u2605'.repeat(starN) + ' ' + hsec.rating_right.en + '</span></div>';
          html += '<div style="font-weight:600;margin:8px 0;">' + hsec.reviewer.en + '</div>';
          html +=
            '<p>' +
            hsec.body.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
            '</p>';
          html += '</div>';
        }
      }
      html += '</div>';
    } else if (passage.is_presentation && passage.slides) {
      // Presentation slides (大問8)
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      html += '<div class="print-slides-grid">';
      for (const slide of passage.slides) {
        html += '<div class="print-slide-card">';
        html += '<div class="print-slide-title">' + (slide.title ? slide.title.en.replace(/\n/g, '<br>') : '') + '</div>';
        if (slide.has_image && dataPath) {
          html += '<img class="print-slide-img" src="' + dataPath.replace(/data\.json$/, 'images/s8_slide1.png') + '" alt="Vegetables">';
        }
        if (slide.columns) {
          html += '<table class="print-slide-columns"><tr>';
          for (const col of slide.columns) {
            html += '<td><div class="print-slide-col-heading">' + col.heading.en + '</div><ul>';
            for (const item of col.items) {
              html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
            }
            html += '</ul></td>';
          }
          html += '</tr></table>';
        }
        if (slide.content) {
          html += '<p class="print-slide-content">' + slide.content.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</p>';
        }
        if (slide.options) {
          html += '<div class="print-slide-options">';
          for (const opt of slide.options) {
            html += '<div>' + opt.label + '. ' + opt.en + '</div>';
          }
          html += '</div>';
        }
        if (slide.items) {
          html += '<ul class="print-slide-items">';
          for (const item of slide.items) {
            html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
          }
          html += '</ul>';
        }
        html += '<div class="print-slide-number">' + slide.number + '</div>';
        html += '</div>';
      }
      html += '</div></div>';

    } else if (passage.presentation_outline) {
      // 駿台第7問など — 発表の概要ボックス（問題冊子の下段）
      const po = passage.presentation_outline;
      html += '<div class="print-passage print-presentation-outline">';
      if (po.label_outside_box && po.label_outside_box.en) {
        html += '<div class="print-outline-outside-label">' + po.label_outside_box.en + '</div>';
      }
      html += '<div class="print-outline-box">';
      if (po.title && po.title.en) {
        html += '<div class="print-outline-inner-title">' + po.title.en + '</div>';
      }
      const blocks = po.blocks || [];
      for (const bl of blocks) {
        const btype = bl.type;
        if (btype === 'adaptations_heading') {
          html += '<div class="print-outline-section-heading">';
          html += '<strong>' + bl.heading.en + '</strong>';
          if (typeof bl.slot_after_heading === 'number') {
            html += ' <span class="print-answer-slot">' + bl.slot_after_heading + '</span>';
          }
          html += '</div>';
          html += '<ul class="print-outline-list">';
          for (const line of bl.lines || []) {
            html += '<li>' + line.en + '</li>';
          }
          html += '</ul>';
        } else if (btype === 'section_heading_lines') {
          html += '<div class="print-outline-section-heading"><strong>' + bl.heading.en + '</strong></div>';
          html += '<div class="print-outline-bullets">';
          for (const b of bl.bullets || []) {
            const t = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>');
            html += '<div class="print-outline-bullet">— ' + t + '</div>';
          }
          html += '</div>';
        } else if (btype === 'center_slot') {
          html += '<div class="print-outline-section-heading"><strong>' + bl.heading.en + '</strong></div>';
          if (typeof bl.center_slot === 'number') {
            html += '<div class="print-outline-center-slot"><span class="print-answer-slot">' + bl.center_slot + '</span></div>';
          }
        } else if (btype === 'function_slot') {
          html += '<div class="print-outline-section-heading"><strong>' + bl.heading.en + '</strong></div>';
          html += '<div class="print-outline-bullets">';
          for (const b of bl.bullets || []) {
            const t = String(b.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>');
            html += '<div class="print-outline-bullet">— ' + t + '</div>';
          }
          html += '</div>';
        } else if (btype === 'slot_heading_list') {
          html += '<div class="print-outline-slot-row"><span class="print-answer-slot">' + bl.slot + '</span></div>';
          html += '<ul class="print-outline-list print-outline-muted">';
          for (const line of bl.lines || []) {
            html += '<li>' + line.en + '</li>';
          }
          html += '</ul>';
        }
      }
      html += '</div></div>';

    } else if (passage.presentation_slides && passage.presentation_slides.slides) {
      // 共通テスト 第6問B 等 — viewer.js と同形式の presentation_slides（グリッドスライド）
      const ps = passage.presentation_slides;
      const imgBase = dataPath ? dataPath.replace(/data\.json$/, '') : '';
      html += '<div class="print-passage">';
      if (ps.label_outside_box && ps.label_outside_box.en) {
        html += '<div style="font-weight:700;margin-bottom:6px;">' + ps.label_outside_box.en + '</div>';
      }
      if (ps.label_outside_box && ps.label_outside_box.ja) {
        html += '<div style="font-size:0.88rem;margin-bottom:10px;">' + ps.label_outside_box.ja + '</div>';
      }
      html += '<div class="print-slides-grid">';
      for (const slide of ps.slides || []) {
        html += '<div class="print-slide-card" style="position:relative;">';
        if (slide.title) {
          html +=
            '<div class="print-slide-title">' +
            (slide.title.en || '').replace(/\n/g, '<br>') +
            '</div>';
          if (slide.title.ja) {
            html +=
              '<div style="font-size:0.85rem;text-align:center;margin-bottom:8px;">' +
              slide.title.ja +
              '</div>';
          }
        }
        if (slide.image && slide.image.src) {
          const raw = slide.image.src;
          const src =
            raw.startsWith('http') || raw.startsWith('data:') || raw.startsWith('/')
              ? raw
              : raw.startsWith('data/')
                ? raw
                : imgBase + raw;
          html +=
            '<div style="text-align:center;margin:6px 0;"><img class="print-slide-img" src="' +
            src +
            '" alt="' +
            (slide.image.alt || '') +
            '" style="max-width:88%;max-height:170px;" /></div>';
        }
        if (slide.compare_table) {
          const ct = slide.compare_table;
          const cols = ct.columns || {};
          html +=
            '<table style="width:100%;border-collapse:collapse;font-size:0.88rem;margin:6px 0;"><thead><tr>';
          if (cols.en && cols.en.length === 2) {
            html +=
              '<th style="border:1px solid #333;padding:4px 6px;text-align:center;">' +
              cols.en[0] +
              '</th>';
            html +=
              '<th style="border:1px solid #333;padding:4px 6px;text-align:center;">' +
              cols.en[1] +
              '</th>';
          }
          html += '</tr></thead><tbody>';
          for (const row of ct.rows || []) {
            const left = String((row.left && row.left.en) || '').replace(
              /\[(\d+)\]/g,
              '<span class="print-answer-slot">$1</span>'
            );
            const right = String((row.right && row.right.en) || '').replace(
              /\[(\d+)\]/g,
              '<span class="print-answer-slot">$1</span>'
            );
            html +=
              '<tr><td style="border:1px solid #333;padding:6px;vertical-align:top;">• ' +
              left +
              '</td>';
            html +=
              '<td style="border:1px solid #333;padding:6px;vertical-align:top;">• ' +
              right +
              '</td></tr>';
          }
          html += '</tbody></table>';
        }
        if (slide.lead) {
          let leadEn = slide.lead.en || '';
          if (typeof slide.lead.trailing_slot === 'number') {
            leadEn += ' <span class="print-answer-slot">' + slide.lead.trailing_slot + '</span>';
          }
          html += '<p class="print-slide-content" style="margin:6px 0;">' + leadEn + '</p>';
          if (slide.lead.ja) {
            let leadJa = slide.lead.ja;
            if (typeof slide.lead.trailing_slot === 'number') {
              leadJa += ' <span class="print-answer-slot">' + slide.lead.trailing_slot + '</span>';
            }
            html += '<div style="font-size:0.85rem;margin-bottom:6px;">' + leadJa + '</div>';
          }
        }
        if (slide.lettered_bullets && slide.lettered_bullets.length) {
          html += '<ul class="print-slide-items">';
          for (const lb of slide.lettered_bullets) {
            html += '<li><strong>' + lb.letter + '.</strong> ' + (lb.en || '') + '</li>';
          }
          html += '</ul>';
        }
        if (slide.bullets && slide.bullets.length) {
          html += '<ul class="print-slide-items">';
          for (const b of slide.bullets) {
            if (b.is_slot && typeof b.slot === 'number') {
              html += '<li><span class="print-answer-slot">' + b.slot + '</span></li>';
            } else {
              html +=
                '<li>' +
                String(b.en || '').replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') +
                '</li>';
            }
          }
          html += '</ul>';
        }
        if (typeof slide.center_slot === 'number') {
          html +=
            '<div style="text-align:center;margin:14px 0;"><span class="print-answer-slot">' +
            slide.center_slot +
            '</span></div>';
        }
        html += '<div class="print-slide-number">' + slide.slide_no + '</div>';
        html += '</div>';
      }
      html += '</div></div>';

    } else if (hasComments) {
      // Essay table layout (大問4)
      html += '<table class="print-essay-table">';
      html += '<thead><tr>';
      html += '<th class="print-essay-col-main">' + (passage.title ? passage.title.en : '') + '</th>';
      html += '<th class="print-essay-col-comments">Comments</th>';
      html += '</tr></thead><tbody>';

      passage.paragraphs.forEach((para, pi) => {
        const paraComments = [];
        for (const sent of para) {
          if (sent.comment_marker) {
            const mc = passage.margin_comments.find(c => c.marker === sent.comment_marker);
            if (mc) paraComments.push(mc);
          }
        }

        const printParaClass =
          passage.paragraph_classes && passage.paragraph_classes[pi]
            ? ' ' + passage.paragraph_classes[pi]
            : '';
        html += '<tr><td>';
        html += '<p class="print-paragraph' + printParaClass + '">';
        for (const sent of para) {
          if (sent.comment_marker) {
            html += '<sup class="print-comment-marker">' + sent.comment_marker + '</sup>';
          }
          html += sent.en + ' ';
        }
        html += '</p>';
        html += '</td><td>';
        for (const mc of paraComments) {
          html += '<div class="print-margin-comment">' + mc.marker + ' ' + mc.en + '</div>';
        }
        html += '</td></tr>';
      });

      // Teacher's comment
      if (passage.teacher_comment) {
        html += '<tr><td colspan="2" class="print-teacher-comment">';
        html += '<strong>Teacher\'s Comment</strong><br>';
        html += passage.teacher_comment.en;
        html += '</td></tr>';
      }

      html += '</tbody></table>';

    } else if (passage.authors) {
      // Authors format (大問6 Step1)
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      for (const author of passage.authors) {
        html += '<div style="margin-bottom:10px;">';
        html += '<div><strong>' + author.label.en + '</strong></div>';
        html += '<p class="print-paragraph">';
        for (const s of author.sentences) html += s.en + ' ';
        html += '</p></div>';
      }
      html += '</div>';
      // Navigation cue: answer 問1 and 問2 after Step 1
      html += '<div class="print-nav-cue">📝 ここまで読んだら <strong>問1</strong> と <strong>問2</strong> を解答</div>';

    } else if (passage.is_step2) {
      // Step2: Take a position (大問6)
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      if (passage.position) {
        html += '<p class="print-paragraph"><strong><u>' + passage.position.en + '</u></strong></p>';
      }
      if (passage.position_details) {
        html += '<ul>';
        for (const d of passage.position_details) {
          html += '<li>' + d.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
        }
        html += '</ul>';
      }
      html += '</div>';
      // Navigation cue: answer 問3 after Step 2
      html += '<div class="print-nav-cue">📝 ここまで読んだら <strong>問3</strong> を解答</div>';

    } else if (passage.is_step3) {
      // Step3: Essay outline (大問6)
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      if (passage.outline) {
        const o = passage.outline;
        html += '<p class="print-paragraph"><strong>' + o.essay_title.en + '</strong></p>';
        html += '<p class="print-paragraph"><em>Introduction:</em> ' + o.introduction.en + '</p>';
        for (const b of o.body) {
          html += '<p class="print-paragraph">' + b.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</p>';
        }
        html += '<p class="print-paragraph"><em>Conclusion:</em> ' + o.conclusion.en + '</p>';
      }
      html += '</div>';
      // Navigation cue: answer 問4 and 問5 after Step 3
      html += '<div class="print-nav-cue">📝 ここまで読んだら <strong>問4</strong> と <strong>問5</strong> を解答</div>';

    } else if (passage.is_source_with_chart) {
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      if (passage.sentences) {
        html += '<p class="print-paragraph">';
        for (const s of passage.sentences) html += s.en + ' ';
        html += '</p>';
      }
      if (passage.paragraphs) {
        for (const para of passage.paragraphs) {
          html += '<p class="print-paragraph">';
          for (const sent of para) html += sent.en + ' ';
          html += '</p>';
        }
      }
      if (passage.chart_image) {
        html += '<img class="print-img" src="' + passage.chart_image.src + '" alt="' + (passage.chart_image.alt || '') + '">';
      }
      html += '</div>';

    } else if (passage.id === 'questionnaire') {
      // Questionnaire (大問5: chart + comments)
      html += '<div class="print-passage">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      if (passage.q1_title) html += '<p class="print-paragraph"><strong>' + passage.q1_title.en + '</strong></p>';
      if (passage.chart_image) {
        html += '<img class="print-img" src="' + passage.chart_image.src + '" alt="' + (passage.chart_image.alt || '') + '">';
      } else if (passage.chart_data && dataPath) {
        // Fallback: derive image path from data path
        const imgBase = dataPath.replace(/data\.json$/, 'images/');
        html += '<img class="print-img" src="' + imgBase + 's5_questionnaire_chart.png" alt="Questionnaire Chart">';
      }
      if (passage.q2_title) html += '<p class="print-paragraph" style="margin-top:12px;"><strong>' + passage.q2_title.en + '</strong></p>';
      if (passage.comments) {
        html += '<p class="print-paragraph"><em>Main comments:</em></p>';
        for (const c of passage.comments) {
          html += '<div style="margin:4px 0 4px 16px;">• <strong>' + (c.label === 'S1' ? 'Student 1 (S1)' : c.label) + ':</strong> ' + c.en + '</div>';
        }
      }
      html += '</div>';

    } else if (passage.is_handout) {
      // Handout (大問5: sections with items/sub_items/options)
      html += '<div class="print-passage" style="border:1px solid #333;padding:16px;">';
      if (passage.title) html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      if (passage.sections_content) {
        for (const sec of passage.sections_content) {
          html += '<div style="margin:10px 0;">';
          html += '<div><strong>■ ' + sec.heading.en + '</strong></div>';
          if (sec.items) {
            for (const item of sec.items) {
              const itemEn = item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>');
              html += '<div style="margin-left:16px;">－ ' + itemEn + '</div>';
            }
          }
          if (sec.sub_items) {
            for (const sub of sec.sub_items) {
              html += '<div style="margin-left:16px;">－ ' + sub.label.en + '</div>';
              if (sub.content) {
                const contentEn = sub.content.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>');
                html += '<div style="margin-left:32px;">' + contentEn + '</div>';
              }
              if (sub.options) {
                if (sub.blank_number) {
                  html += '<div style="margin-left:32px;"><span class="print-answer-slot">' + sub.blank_number + '</span></div>';
                }
                for (const opt of sub.options) {
                  html += '<div style="margin-left:40px;">' + opt.label + '. ' + opt.en + '</div>';
                }
              }
            }
          }
          html += '</div>';
        }
      }
      html += '</div>';

    } else if (passage.is_notes) {
      // Notes section (大問7)
      html += '<div class="print-passage" style="border:1px solid #333;padding:16px;">';
      if (passage.notes_caption && passage.notes_caption.en) {
        html += '<div style="font-size:0.9rem;font-style:italic;margin-bottom:4px;">' + passage.notes_caption.en + '</div>';
      }
      html += '<div class="print-passage-title" style="text-align:center;">' + (passage.notes_title ? passage.notes_title.en : 'Your notes') + '</div>';
      if (passage.story_outline) {
        const so = passage.story_outline;
        html += '<p class="print-paragraph"><strong><em>Story outline</em></strong></p>';
        html += '<p class="print-paragraph">' + so.start.en + '</p>';
        html += '<div style="margin:4px 0 4px 16px;padding-left:8px;border-left:2px solid #555;">';
        for (const slot of so.slots) {
          html += '<div><span class="print-answer-slot">' + slot + '</span></div>';
        }
        html += '</div>';
        if (so.end) {
          html += '<p class="print-paragraph">' + so.end.en + '</p>';
        }
      }
      if (passage.about_sam) {
        const as_ = passage.about_sam;
        html += '<p class="print-paragraph"><strong><em>About Sam</em></strong></p>';
        html += '<ul style="list-style:disc;padding-left:22px;">';
        html += '<li>Nationality: ' + as_.nationality.en + '</li>';
        html += '<li>Age: <span class="print-answer-slot">' + as_.age_slot + '</span></li>';
        html += '<li>Occupation: ' + as_.occupation.en + '</li>';
        html += '<li>How his friends and family supported him:';
        for (const item of as_.support) {
          html += '<div style="margin-left:14px;">' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</div>';
        }
        html += '</li></ul>';
      }
      if (passage.interpretation) {
        html += '<p class="print-paragraph"><strong><em>Interpretation of key moments</em></strong></p>';
        html += '<ul style="list-style:disc;padding-left:22px;">';
        for (const item of passage.interpretation) {
          html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
        }
        html += '</ul>';
      }
      // Research sections
      if (passage.research_sections) {
        for (const rsec of passage.research_sections) {
          html += '<p class="print-paragraph"><strong><em>' + rsec.heading.en + '</em></strong></p>';
          html += '<ul style="list-style:disc;padding-left:22px;">';
          for (const item of rsec.items) {
            html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
          }
          html += '</ul>';
        }
      }
      // Event sequence
      if (passage.event_sequence) {
        const es = passage.event_sequence;
        html += '<p class="print-paragraph"><strong><em>' + es.heading.en + '</em></strong></p>';
        html += '<p class="print-paragraph">' + es.start.en + '</p>';
        html += '<div style="margin:4px 0 4px 16px;padding-left:8px;border-left:2px solid #555;">';
        for (const slot of es.slots) {
          html += '<div><span class="print-answer-slot">' + slot + '</span></div>';
        }
        html += '</div>';
      }
      // Legacy section
      if (passage.legacy_section) {
        const ls = passage.legacy_section;
        html += '<p class="print-paragraph"><strong><em>' + ls.heading.en + '</em></strong></p>';
        html += '<p class="print-paragraph">' + ls.content.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</p>';
      }
      // Lessons
      if (passage.lessons) {
        const ll = passage.lessons;
        html += '<p class="print-paragraph"><strong><em>' + ll.heading.en + '</em></strong></p>';
        html += '<ul style="list-style:disc;padding-left:22px;">';
        for (const item of ll.items) {
          html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
        }
        html += '</ul>';
      }
      // Note sections (大問7: 発表ノートの各セクション)
      if (passage.note_sections) {
        for (const ns of passage.note_sections) {
          html += '<p class="print-paragraph"><strong><em>' + ns.heading.en + '</em></strong></p>';
          if (ns.is_timeline) {
            html += '<div style="margin:4px 0 4px 16px;padding-left:8px;border-left:2px solid #555;">';
            for (const item of ns.items) {
              if (item.is_slot) {
                html += '<div><span class="print-answer-slot">' + item.en.replace(/[\[\]]/g, '') + '</span></div>';
              } else {
                html += '<div style="margin:4px 0;">' + item.en + '</div>';
              }
            }
            html += '</div>';
          } else {
            html += '<ul style="list-style:disc;padding-left:22px;">';
            for (const item of ns.items) {
              html += '<li>' + item.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</li>';
            }
            html += '</ul>';
          }
        }
      }
      html += '</div>';

    } else if (passage.is_poster) {
      // Poster (大問8: ポスター表+イラスト)
      const imgBase = dataPath.replace(/data\.json$/, '');
      html += '<div class="print-passage" style="border:1px solid #333;padding:16px;">';
      if (passage.poster_title) {
        html += '<div style="text-align:center;margin-bottom:12px;"><span style="display:inline-block;font-weight:700;padding:4px 16px;background:#666;color:#fff;border-radius:16px;">' + passage.poster_title.en + '</span></div>';
      }
      if (passage.poster_intro_slot) {
        html += '<p>' + passage.poster_intro_slot.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</p>';
      }
      if (passage.poster_section_label) {
        html += '<div style="display:inline-block;border:1px solid #666;border-radius:14px;padding:2px 12px;font-weight:700;font-size:0.9rem;margin:8px 0;">' + passage.poster_section_label.en + '</div>';
      }
      if (passage.poster_table) {
        const pt = passage.poster_table;
        html += '<table class="print-poster-table" style="width:100%;border-collapse:collapse;margin:8px 0;font-size:0.88rem;"><tr>';
        for (const h of pt.headers) {
          html += '<th style="border:1px solid #666;padding:6px;text-align:left;background:#eee;">' + h + '</th>';
        }
        html += '</tr>';
        for (const row of pt.rows) {
          html += '<tr>';
          html += '<td style="border:1px solid #666;padding:6px;text-align:center;">' + row.type_num + '</td>';
          html += '<td style="border:1px solid #666;padding:6px;">' + row.cause.en;
          if (row.cause_image) {
            html += '<br><img src="' + imgBase + row.cause_image + '" alt="' + row.cause.en + '" style="max-width:50px;margin-top:4px;">';
          }
          html += '</td>';
          html += '<td style="border:1px solid #666;padding:6px;">' + row.theory.en.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</td>';
          html += '<td style="border:1px solid #666;padding:6px;">' + row.origins.en + '</td>';
          html += '</tr>';
        }
        html += '</table>';
      }
      if (passage.poster_solutions_label) {
        html += '<div style="display:inline-block;border:1px solid #666;border-radius:14px;padding:2px 12px;font-weight:700;font-size:0.9rem;margin:8px 0;">' + passage.poster_solutions_label.en + '</div>';
        html += '<div style="border:1px solid #666;padding:10px;margin:4px 0;">';
        for (const slot of passage.poster_solutions_slots) {
          html += '<div>' + slot.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>') + '</div>';
        }
        html += '</div>';
      }
      html += '</div>';

    } else if (passage.pamphlet_layout && passage.paragraphs) {
      const imgBase = dataPath.replace(/data\.json$/, '');
      html +=
        '<div class="print-passage" style="border:1px solid #222;padding:16px 18px;font-family:Times New Roman,Times,serif;">';
      if (passage.title) {
        html += '<div class="print-passage-title" style="text-align:center;">' + passage.title.en + '</div>';
      }
      if (passage.subtitle && passage.subtitle.en) {
        html +=
          '<div style="text-align:center;color:#555;font-weight:600;font-size:0.95rem;margin-bottom:12px;">' +
          passage.subtitle.en +
          '</div>';
      }
      for (let pi = 0; pi < passage.paragraphs.length; pi++) {
        const para = passage.paragraphs[pi];
        if (pi >= 1) {
          html += '<hr style="border:none;border-top:1px solid #1a1a1a;margin:12px 0;" />';
        }
        const phHead = Array.isArray(para) ? para.find(s => s.role === 'pamphlet_heading') : null;
        const phRest = phHead ? para.filter(s => s !== phHead) : para;
        if (phHead) {
          html += '<p style="font-weight:700;margin:0 0 6px 0;">' + phHead.en + '</p>';
        }
        html += '<div style="overflow:auto;">';
        if (passage.images) {
          for (const img of passage.images) {
            if (img.paragraph_index === pi) {
              const raw = img.src || '';
              const src =
                raw.startsWith('data/') || raw.startsWith('http') ? raw : imgBase + raw;
              const mw = img.max_width ? Math.min(img.max_width, 220) : 200;
              html +=
                '<img src="' +
                src +
                '" alt="" style="float:right;max-width:' +
                mw +
                'px;margin:0 0 8px 12px;" />';
            }
          }
        }
        html += '<p class="print-paragraph" style="text-align:left;margin-top:0;">';
        for (const sent of phRest) {
          let t = sent.en;
          t = t.replace(/\[(\d+)\]/g, '<span class="print-answer-slot">$1</span>');
          html += t + ' ';
        }
        html += '</p><div style="clear:both;"></div></div>';
      }
      html += '</div>';

    } else {
      // Standard passage
      html += '<div class="print-passage">';
      if (passage.title) {
        html += '<div class="print-passage-title">' + passage.title.en + '</div>';
      }
      if (passage.subtitle && passage.subtitle.en) {
        html +=
          '<div class="print-passage-subtitle" style="text-align:center;margin-bottom:10px;">' +
          passage.subtitle.en +
          '</div>';
      }
      if (passage.image) {
        html += '<img class="print-img" src="' + passage.image.src + '" alt="' + (passage.image.alt || '') + '">';
      }

      if (passage.sentences) {
        html += '<p class="print-paragraph">';
        for (const sent of passage.sentences) {
          html += sent.en + ' ';
        }
        html += '</p>';
      }

      if (passage.paragraphs) {
        if (passage.block_separators && passage.block_separators.length > 0) {
          // Block-based rendering with ◆◆◆◆◆ separators (大問7)
          for (let pi = 0; pi < passage.paragraphs.length; pi++) {
            const para = passage.paragraphs[pi];
            html += '<p class="print-paragraph" style="text-indent:1.5em;">';
            for (const sent of para) html += sent.en + ' ';
            html += '</p>';
            if (passage.block_separators.includes(pi)) {
              html += '<div style="text-align:center;margin:12px 0;letter-spacing:0.3em;">◆◆◆◆◆</div>';
            }
          }
        } else {
          for (let pi = 0; pi < passage.paragraphs.length; pi++) {
            const para = passage.paragraphs[pi];
            const pc =
              passage.paragraph_classes && passage.paragraph_classes[pi] === 'para-indent';
            const indentAttr = pc ? ' style="text-indent:1.5em;"' : '';
            html += '<p class="print-paragraph"' + indentAttr + '>';
            for (const sent of para) {
              html += sent.en + ' ';
            }
            html += '</p>';
            // Graph image after specified paragraph (1-indexed)
            if (passage.graph_image && passage.graph_image.after_paragraph === (pi + 1)) {
              const imgBase = dataPath.replace(/data\.json$/, '');
              html += '<img class="print-img" src="' + imgBase + passage.graph_image.src + '" alt="' + (passage.graph_image.alt || 'Graph') + '">';
            }
          }
        }
      }
      html += '</div>';
    }
  }

  html += '</div>'; // .print-section
  return html;
}

/** viewer.js の deriveMultiSlotAnswerNumbers と同ロジック（印刷用） */
function deriveMultiSlotAnswerNumbersPrint(q) {
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

// ===== Render Questions Page =====
function renderQuestionsPage(sec, dataPath) {
  const imgBase = dataPath ? dataPath.replace(/data\.json$/, '') : '';

  function resolveImgSrc(src) {
    if (!src) return '';
    if (src.startsWith('http') || src.startsWith('data:') || src.startsWith('/')) return src;
    if (src.startsWith('data/')) return src;
    return imgBase + src;
  }

  let html = '<div class="print-section">';

  // Header
  html += '<div class="print-section-header">';
  html += '<div class="print-section-title">' + sec.title + '</div>';
  html += '<div class="print-section-type">― 設問 ―</div>';
  html += '</div>';

  for (const q of sec.questions) {
    html += '<div class="print-question-block">';

    // Label
    html += '<div class="print-question-label">' + q.question_id + '</div>';

    // Stem (with fallback to question_text)
    const stemObj = q.stem || q.question_text;
    if (stemObj) {
      const stemText = stemObj.en.replace(
        /\[(\d+)\]/g,
        '<span class="print-answer-slot">$1</span>'
      );
      html += '<div class="print-question-stem">' + stemText + '</div>';
    }

    if (Array.isArray(q.info_options) && q.info_options.length > 0) {
      html += '<ul class="print-info-options">';
      for (const opt of q.info_options) {
        const lab = opt.label || '';
        const en = opt.en || '';
        html +=
          '<li class="print-info-option-item">' +
          '<span class="print-info-option-letter">' + lab + '</span>' +
          '<span class="print-info-option-colon"> : </span>' +
          '<span>' + en + '</span></li>';
      }
      html += '</ul>';
    }

    const qFig = q.figure_image || q.choice_grid_image;
    if (qFig && qFig.src) {
      html +=
        '<figure class="print-question-figure">' +
        '<img class="print-img print-question-choice-figure" src="' +
        resolveImgSrc(qFig.src) +
        '" alt="' +
        (qFig.alt || '').replace(/"/g, '&quot;') +
        '">' +
        '</figure>';
    }

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

    // Choices: multi-answer (choices_27, choices_28, etc.) or standard
    const printMultiSlots = deriveMultiSlotAnswerNumbersPrint(q);
    if (printMultiSlots && printMultiSlots.length > 0) {
      // Multi-answer question (大問6問3, 大問7問3 etc.)
      const anySlotSpecificChoices = printMultiSlots.some(
        n => Array.isArray(q['choices_' + n]) && q['choices_' + n].length > 0
      );
      for (const num of printMultiSlots) {
        const choicesKey = 'choices_' + num;
        let choices = q[choicesKey];
        if (!Array.isArray(choices) || !choices.length) {
          if (!anySlotSpecificChoices && Array.isArray(q.choices) && q.choices.length) {
            choices = q.choices;
          }
        }
        if (choices && choices.length) {
          html += '<div style="font-weight:600;margin:8px 0 4px;">[' + num + ']</div>';
          html += '<ul class="print-choices">';
          for (const choice of choices) {
            const cImg =
              choice.image && choice.image.src
                ? '<br><img class="print-img print-choice-inline-img" src="' +
                  resolveImgSrc(choice.image.src) +
                  '" alt="' +
                  (choice.image.alt || '').replace(/"/g, '&quot;') +
                  '">'
                : '';
            html +=
              '<li><span class="print-choice-label">' +
              choice.label +
              '</span> ' +
              (choice.en || '') +
              cImg +
              '</li>';
          }
          html += '</ul>';
        }
      }
    } else if (q.choices) {
      const ulCls = pictureTierChoices ? 'print-choices print-choices-picture-tier' : 'print-choices';
      html += '<ul class="' + ulCls + '">';
      for (const choice of q.choices) {
        const cImg =
          choice.image && choice.image.src
            ? '<img class="print-img print-choice-inline-img" src="' +
              resolveImgSrc(choice.image.src) +
              '" alt="' +
              (choice.image.alt || '').replace(/"/g, '&quot;') +
              '"> '
            : '';
        if (pictureTierChoices) {
          html += '<li><span class="print-choice-label">' + choice.label + '</span></li>';
        } else {
          html +=
            '<li><span class="print-choice-label">' + choice.label + '</span> ' + cImg + (choice.en || '') + '</li>';
        }
      }
      html += '</ul>';
    }

    html += '</div>';
  }

  html += '</div>'; // .print-section
  return html;
}
