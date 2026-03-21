/**
 * 共通テスト英語問題DB - Print Module
 * URL params:
 *   exam=sundai_2025_01
 *   mode=passage|questions|all
 *   section=1  (for passage/questions mode)
 */

const EXAM_PATHS = {
  sundai_2025_01: 'data/sundai/2025/round01/data.json'
};

document.addEventListener('DOMContentLoaded', async () => {
  const params = new URLSearchParams(location.search);
  const examId = params.get('exam') || 'sundai_2025_01';
  const mode = params.get('mode') || 'all';
  const sectionNum = parseInt(params.get('section') || '0');

  const dataPath = EXAM_PATHS[examId];
  if (!dataPath) {
    document.getElementById('print-content').innerHTML = '<p>データが見つかりません。</p>';
    return;
  }

  const res = await fetch(dataPath);
  const data = await res.json();

  document.title = data.exam_name + ' — 印刷';
  document.getElementById('print-title').textContent = data.exam_name + ' — 印刷プレビュー';

  let html = '';

  if (mode === 'passage' && sectionNum > 0) {
    const sec = data.sections.find(s => s.section_number === sectionNum);
    if (sec) html = renderPassagePage(sec);
  } else if (mode === 'questions' && sectionNum > 0) {
    const sec = data.sections.find(s => s.section_number === sectionNum);
    if (sec) html = renderQuestionsPage(sec);
  } else {
    // all: 大問1問題→大問1設問→大問2問題→…
    for (const sec of data.sections) {
      html += renderPassagePage(sec);
      html += renderQuestionsPage(sec);
    }
  }

  document.getElementById('print-content').innerHTML = html;
});

// ===== Render Passage Page =====
function renderPassagePage(sec) {
  let html = '<div class="print-section">';

  // Header
  html += '<div class="print-section-header">';
  html += '<div class="print-section-title">' + sec.title + '</div>';
  if (sec.points) {
    html += '<div class="print-section-subtitle">配点 ' + sec.points + '点';
    if (sec.points_per_question) {
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

    if (hasComments) {
      // Essay table layout
      html += '<table class="print-essay-table">';
      html += '<thead><tr>';
      html += '<th class="print-essay-col-main">' + (passage.title ? passage.title.en : '') + '</th>';
      html += '<th class="print-essay-col-comments">Comments</th>';
      html += '</tr></thead><tbody>';

      for (const para of passage.paragraphs) {
        const paraComments = [];
        for (const sent of para) {
          if (sent.comment_marker) {
            const mc = passage.margin_comments.find(c => c.marker === sent.comment_marker);
            if (mc) paraComments.push(mc);
          }
        }

        html += '<tr><td>';
        html += '<p class="print-paragraph">';
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
      }

      // Teacher's comment
      if (passage.teacher_comment) {
        html += '<tr><td colspan="2" class="print-teacher-comment">';
        html += '<strong>Teacher\'s Comment</strong><br>';
        html += passage.teacher_comment.en;
        html += '</td></tr>';
      }

      html += '</tbody></table>';
    } else {
      // Standard passage
      html += '<div class="print-passage">';
      if (passage.title) {
        html += '<div class="print-passage-title">' + passage.title.en + '</div>';
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
        for (const para of passage.paragraphs) {
          html += '<p class="print-paragraph">';
          for (const sent of para) {
            html += sent.en + ' ';
          }
          html += '</p>';
        }
      }
      html += '</div>';
    }
  }

  html += '</div>'; // .print-section
  return html;
}

// ===== Render Questions Page =====
function renderQuestionsPage(sec) {
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

    // Stem
    const stemText = q.stem.en.replace(
      /\[(\d+)\]/g,
      '<span class="print-answer-slot">$1</span>'
    );
    html += '<div class="print-question-stem">' + stemText + '</div>';

    // Choices
    if (q.question_type === 'ordering') {
      // Ordering question - show choices with numbers
      html += '<ul class="print-choices">';
      for (const choice of q.choices) {
        html += '<li><span class="print-choice-label">' + choice.label + '</span> ' + choice.en + '</li>';
      }
      html += '</ul>';
    } else {
      html += '<ul class="print-choices">';
      for (const choice of q.choices) {
        html += '<li><span class="print-choice-label">' + choice.label + '</span> ' + choice.en + '</li>';
      }
      html += '</ul>';
    }

    html += '</div>';
  }

  html += '</div>'; // .print-section
  return html;
}
