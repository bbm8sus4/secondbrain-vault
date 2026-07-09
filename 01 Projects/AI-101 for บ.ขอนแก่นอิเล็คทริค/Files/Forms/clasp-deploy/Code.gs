/**
 * Google Forms สำหรับ Claude AI Workshop (บ.ขอนแก่นอิเล็คทริค) — 2 ฟอร์ม
 *   createOwnerForm()   : เจ้าของธุรกิจ (Needs Analysis)
 *   createLearnerForm() : ผู้เรียน 15 ท่าน (Pre-training Survey)
 * Deploy เป็น Web App → เปิด URL → doGet() จะ rewrite ทั้ง 2 ฟอร์ม
 */

const OWNER_FORM_ID = '1oEUefpyYqe1MQPpbwyM_lrkzReq02ZaETM50rUf-bvw';
const LEARNER_FORM_ID = '1ekrJsyjnlVluHixcDwyJy0AcTnwO9vuYYfzfkw81G7o';

function clearAllItems(f) {
  var items = f.getItems();
  for (var i = items.length - 1; i >= 0; i--) f.deleteItem(items[i]);
}

function tryPublish(f) {
  try { if (typeof f.setPublished === 'function') f.setPublished(true); } catch (e) {}
  try { if (typeof f.publish === 'function') f.publish(); } catch (e) {}
}

function trashManagerFormIfExists() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('MANAGER_FORM_ID');
  if (!id) return null;
  try {
    DriveApp.getFileById(id).setTrashed(true);
    props.deleteProperty('MANAGER_FORM_ID');
    return id;
  } catch (e) {
    props.deleteProperty('MANAGER_FORM_ID');
    return null;
  }
}

function createBothForms() {
  createOwnerForm();
  createLearnerForm();
}

// GCP project ที่เปิด Forms API ไว้ (ใช้เป็น quota project)
var QUOTA_PROJECT = 'extreme-voice-462512-d0';

/**
 * ★★★ กู้ข้อมูล — รันฟังก์ชันนี้จาก editor ★★★
 * ดึง raw response (answers keyed by questionId เดิม) ผ่าน Forms REST API
 * แล้วเขียนลงชีตใหม่ พร้อม map questionId → ชื่อคำถามเดิม (จาก schema ปัจจุบัน + ที่เหลือโชว์ ID)
 */
function recoverResponses() {
  var token = ScriptApp.getOAuthToken();
  var ss = SpreadsheetApp.create('★ RECOVERED RESPONSES — AI Workshop ' + new Date().toISOString());
  var forms = [['LEARNER', LEARNER_FORM_ID], ['OWNER', OWNER_FORM_ID]];
  var summary = [];

  for (var fi = 0; fi < forms.length; fi++) {
    var label = forms[fi][0], fid = forms[fi][1];
    // 1) schema: questionId -> title
    var qmap = {};
    try {
      var sres = UrlFetchApp.fetch('https://forms.googleapis.com/v1/forms/' + fid, {
        headers: { Authorization: 'Bearer ' + token, 'x-goog-user-project': QUOTA_PROJECT },
        muteHttpExceptions: true
      });
      if (sres.getResponseCode() === 200) {
        var sj = JSON.parse(sres.getContentText());
        (sj.items || []).forEach(function (it) {
          if (it.questionItem && it.questionItem.question)
            qmap[it.questionItem.question.questionId] = it.title || '';
          if (it.questionGroupItem && it.questionGroupItem.questions)
            it.questionGroupItem.questions.forEach(function (q) { qmap[q.questionId] = it.title || ''; });
        });
      }
    } catch (e) {}

    // 2) responses
    var rres = UrlFetchApp.fetch('https://forms.googleapis.com/v1/forms/' + fid + '/responses?pageSize=5000', {
      headers: { Authorization: 'Bearer ' + token, 'x-goog-user-project': QUOTA_PROJECT },
      muteHttpExceptions: true
    });
    var sh = ss.insertSheet(label);
    if (rres.getResponseCode() !== 200) {
      sh.appendRow(['ERROR http=' + rres.getResponseCode(), rres.getContentText().slice(0, 500)]);
      summary.push(label + ': HTTP ' + rres.getResponseCode());
      continue;
    }
    var rj = JSON.parse(rres.getContentText());
    var responses = rj.responses || [];

    // เก็บทุก questionId ที่เจอใน responses (รวม ID เก่าที่ schema ปัจจุบันไม่มี)
    var allQ = {};
    responses.forEach(function (r) {
      var ans = r.answers || {};
      for (var qid in ans) allQ[qid] = true;
    });
    var qids = Object.keys(allQ);

    // header
    var header = ['responseId', 'submittedTime'];
    qids.forEach(function (qid) { header.push((qmap[qid] || '[deleted q]') + ' (' + qid + ')'); });
    sh.appendRow(header);

    // rows
    responses.forEach(function (r) {
      var row = [r.responseId || '', r.lastSubmittedTime || r.createTime || ''];
      var ans = r.answers || {};
      qids.forEach(function (qid) {
        var v = '';
        if (ans[qid] && ans[qid].textAnswers && ans[qid].textAnswers.answers) {
          v = ans[qid].textAnswers.answers.map(function (a) { return a.value; }).join(' | ');
        }
        row.push(v);
      });
      sh.appendRow(row);
    });

    summary.push(label + ': ' + responses.length + ' responses, ' + qids.length + ' answered questions');
  }

  // ลบ default sheet
  var def = ss.getSheetByName('Sheet1') || ss.getSheetByName('ชีต1');
  if (def && ss.getSheets().length > 1) ss.deleteSheet(def);

  var url = ss.getUrl();
  Logger.log('=================================');
  Logger.log('RECOVERY DONE: ' + summary.join(' | '));
  Logger.log('SHEET: ' + url);
  Logger.log('SHEET_ID: ' + ss.getId());
  Logger.log('=================================');
  // เก็บ id ไว้ให้ web app อ่านได้
  PropertiesService.getScriptProperties().setProperty('RECOVERY_SHEET_ID', ss.getId());
  return url;
}

function doGet(e) {
  if (e && e.parameter && e.parameter.action === 'tab') {
    // อ่านแท็บใน spreadsheet ผ่าน Sheets API REST (token deployer มี drive scope)
    var token = ScriptApp.getOAuthToken();
    var sid = e.parameter.sid;
    var gid = e.parameter.gid;
    var hdr = { headers: { Authorization: 'Bearer ' + token }, muteHttpExceptions: true };
    // หา title ของแท็บจาก gid
    var meta = UrlFetchApp.fetch('https://sheets.googleapis.com/v4/spreadsheets/' + sid + '?fields=sheets(properties(sheetId,title))', hdr);
    if (meta.getResponseCode() !== 200) return ContentService.createTextOutput('META ' + meta.getResponseCode() + ' ' + meta.getContentText().slice(0, 300));
    var sheets = JSON.parse(meta.getContentText()).sheets || [];
    var title = null;
    for (var i = 0; i < sheets.length; i++) {
      if (String(sheets[i].properties.sheetId) === String(gid)) { title = sheets[i].properties.title; break; }
    }
    if (!title && sheets.length) title = sheets[sheets.length - 1].properties.title; // เผื่อ gid ไม่ตรง เอาแท็บล่าสุด
    var vres = UrlFetchApp.fetch('https://sheets.googleapis.com/v4/spreadsheets/' + sid + '/values/' + encodeURIComponent(title) + '?majorDimension=ROWS', hdr);
    if (vres.getResponseCode() !== 200) return ContentService.createTextOutput('VALUES ' + vres.getResponseCode() + ' ' + vres.getContentText().slice(0, 300));
    var rows = JSON.parse(vres.getContentText()).values || [];
    // ส่งกลับเป็น TSV (กัน comma ในคำตอบ)
    var out = ['TAB: ' + title + ' | rows: ' + rows.length];
    for (var r = 0; r < rows.length; r++) out.push(rows[r].join('\t'));
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'removemenu') {
    // ลบเฉพาะ 5 ข้อของส่วนเมนู (ไม่ใช้ clearAllItems — ข้ออื่น + item ID เดิมไม่แตะ)
    var f = FormApp.openById(LEARNER_FORM_ID);
    var kill = [
      'ส่วนที่ 7: เลือกเมนูอาหาร & เบรค สำหรับวันอบรม',
      'เมนูอาหารกลางวัน (เซตละ 190 บาท)',
      'เครื่องดื่มเย็น เบรค (70 บาท)',
      'ขนมเบรค (Break Set 49 บาท) — เลือกขนม 1 ชิ้น',
      'นม / น้ำผลไม้ ที่มาคู่ Break Set'
    ];
    var items = f.getItems();
    var deleted = [];
    for (var i = items.length - 1; i >= 0; i--) {
      if (kill.indexOf(items[i].getTitle()) >= 0) {
        deleted.push(items[i].getTitle());
        f.deleteItem(items[i]);
      }
    }
    return ContentService.createTextOutput('DELETED ' + deleted.length + ' menu items:\n' + deleted.join('\n')
      + '\n\nremaining items: ' + f.getItems().length);
  }
  if (e && e.parameter && e.parameter.action === 'setdest') {
    // ผูกฟอร์มกับชีต (สร้าง response tab สำหรับคนใหม่ในไฟล์เดียวกับข้อมูลกู้คืน)
    var LEARNER_SHEET = '1fQmT7RUO_YVLyZVQP3e9jowYv5TgotU56XEvFE0LpUQ';
    var OWNER_SHEET = '1l9Z_IiQ-VGO8dZAH6XJzuLZXa_CYraG2gnJ7NxrbLBE';
    var out = [];
    var jobs = [['LEARNER', LEARNER_FORM_ID, LEARNER_SHEET], ['OWNER', OWNER_FORM_ID, OWNER_SHEET]];
    for (var i = 0; i < jobs.length; i++) {
      var nm = jobs[i][0], fid = jobs[i][1], sid = jobs[i][2];
      try {
        var f = FormApp.openById(fid);
        f.setDestination(FormApp.DestinationType.SPREADSHEET, sid);
        out.push(nm + ': linked OK -> sheet ' + sid + ' | dest=' + f.getDestinationId());
      } catch (er) {
        out.push(nm + ': ERROR ' + er);
      }
    }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'getrecovery') {
    var rid = PropertiesService.getScriptProperties().getProperty('RECOVERY_SHEET_ID');
    if (!rid) return ContentService.createTextOutput('NO_RECOVERY_YET');
    var token = ScriptApp.getOAuthToken();
    var out = ['RECOVERY_SHEET_ID: ' + rid, ''];
    var ss = SpreadsheetApp.openById(rid);
    var sheets = ss.getSheets();
    for (var s = 0; s < sheets.length; s++) {
      var sh = sheets[s];
      var data = sh.getDataRange().getValues();
      out.push('===== TAB: ' + sh.getName() + ' (' + data.length + ' rows) =====');
      for (var r = 0; r < data.length; r++) out.push(data[r].join(' | '));
      out.push('');
    }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'rest') {
    // กู้ข้อมูลดิบจาก Forms REST API (answers keyed by questionId — อาจเก็บไว้แม้ item ถูกลบ)
    var token = ScriptApp.getOAuthToken();
    var which = (e.parameter.f === 'o') ? OWNER_FORM_ID : LEARNER_FORM_ID;
    var hdr = { Authorization: 'Bearer ' + token, 'x-goog-user-project': QUOTA_PROJECT };
    var out = [];
    // ดึง responses ดิบ
    try {
      var r = UrlFetchApp.fetch(
        'https://forms.googleapis.com/v1/forms/' + which + '/responses?pageSize=100',
        { headers: hdr, muteHttpExceptions: true });
      out.push('RESPONSES http=' + r.getResponseCode());
      out.push(r.getContentText());
    } catch (er) { out.push('RESPONSES ERROR ' + er); }
    // ดึง form schema (questionId → title) เพื่อ map
    try {
      var s = UrlFetchApp.fetch(
        'https://forms.googleapis.com/v1/forms/' + which,
        { headers: hdr, muteHttpExceptions: true });
      out.push('=== FORM SCHEMA http=' + s.getResponseCode() + ' ===');
      out.push(s.getContentText());
    } catch (er2) { out.push('SCHEMA ERROR ' + er2); }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'export') {
    // กู้ข้อมูล: export ทุก response source ผ่าน OAuth token ของ deployer (มี drive scope เต็ม)
    var token = ScriptApp.getOAuthToken();
    var out = [];
    var targets = {};
    // 1) sheet ที่รู้ว่า link ไว้
    targets['linked-14F0'] = '14F0ZIX07pB2qNI808IYpX-EQ81DFVsqP1wxVHwfvpL8';
    // 2) destination ของแต่ละฟอร์ม (เผื่อมี sheet อื่น)
    var formIds = {
      'owner': OWNER_FORM_ID,
      'learner': LEARNER_FORM_ID,
      'owner-dup': '1mLALx74_5yf0i51LlJuI_1E72vBhT4iED-NqTaecJgo',
      'learner-dup': '1hLEg4Jmh8dp6zQvo8PWRgIJwJ-c5LRxMNOmxjD5bAMI'
    };
    for (var k in formIds) {
      try {
        var ff = FormApp.openById(formIds[k]);
        var d = ff.getDestinationId();
        if (d) targets['dest-' + k] = d;
      } catch (er) {}
    }
    // export แต่ละ target เป็น CSV ผ่าน Drive API
    for (var name in targets) {
      var sid = targets[name];
      out.push('========== ' + name + ' (' + sid + ') ==========');
      try {
        var resp = UrlFetchApp.fetch(
          'https://www.googleapis.com/drive/v3/files/' + sid + '/export?mimeType=text/csv',
          { headers: { Authorization: 'Bearer ' + token }, muteHttpExceptions: true });
        var code = resp.getResponseCode();
        if (code === 200) {
          out.push(resp.getContentText());
        } else {
          // อาจเป็น spreadsheet ที่มีหลาย tab — ลอง list แล้ว export ทีละ gid
          out.push('[export csv code=' + code + '] ' + resp.getContentText().slice(0, 300));
        }
      } catch (er2) {
        out.push('[ERROR] ' + er2);
      }
      out.push('');
    }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'sheet') {
    // ดึงข้อมูลจาก linked spreadsheet (response เก่าก่อน rewrite อยู่ที่นี่)
    var SHEET_ID = '14F0ZIX07pB2qNI808IYpX-EQ81DFVsqP1wxVHwfvpL8';
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sheets = ss.getSheets();
    var out = ['Spreadsheet: ' + ss.getName(), 'Sheets: ' + sheets.length, '====='];
    for (var s = 0; s < sheets.length; s++) {
      var sh = sheets[s];
      var data = sh.getDataRange().getValues();
      out.push('');
      out.push('=== TAB: ' + sh.getName() + ' (' + data.length + ' rows x ' + (data[0]||[]).length + ' cols) ===');
      for (var r = 0; r < data.length; r++) {
        out.push('R' + (r+1) + ': ' + data[r].join(' | '));
      }
    }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'dump') {
    // Dump คำตอบทั้งหมดของ learner form
    var f = FormApp.openById(LEARNER_FORM_ID);
    var resp = f.getResponses();
    var out = ['LEARNER form — ' + resp.length + ' responses', '====='];
    for (var i = 0; i < resp.length; i++) {
      out.push('');
      out.push('=== #' + (i+1) + ' ' + resp[i].getTimestamp() + ' ===');
      var items = resp[i].getItemResponses();
      for (var j = 0; j < items.length; j++) {
        var ans = items[j].getResponse();
        if (Array.isArray(ans)) ans = ans.join(', ');
        out.push('  ' + items[j].getItem().getTitle() + ' → ' + ans);
      }
    }
    return ContentService.createTextOutput(out.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'responses') {
    // ตรวจ response count ของฟอร์มทุกใบที่รู้จัก (รวม duplicate + active)
    var ids = [
      ['Owner (active)', OWNER_FORM_ID],
      ['Learner (active)', LEARNER_FORM_ID],
      ['Owner DUP rd1', '1mLALx74_5yf0i51LlJuI_1E72vBhT4iED-NqTaecJgo'],
      ['Learner DUP rd1', '1hLEg4Jmh8dp6zQvo8PWRgIJwJ-c5LRxMNOmxjD5bAMI'],
      ['Manager (trashed)', '1Cfru3TdRoDEcLZ4Uidqf28sKxXJWufrD2q3uZFPlfwU'],
    ];
    var lines = [];
    for (var i = 0; i < ids.length; i++) {
      try {
        var f = FormApp.openById(ids[i][1]);
        var resp = f.getResponses();
        var dest = '(no linked sheet)';
        try { dest = f.getDestinationId() || '(no destination)'; } catch (e2) {}
        lines.push(ids[i][0] + ' [' + ids[i][1] + ']: ' + resp.length + ' responses | dest=' + dest);
        if (resp.length > 0) {
          for (var j = 0; j < Math.min(resp.length, 3); j++) {
            lines.push('  - ' + resp[j].getTimestamp() + ' by ' + (resp[j].getRespondentEmail() || 'anonymous'));
          }
        }
      } catch (err) {
        lines.push(ids[i][0] + ' [' + ids[i][1] + ']: ERROR ' + err);
      }
    }
    return ContentService.createTextOutput(lines.join('\n'));
  }
  if (e && e.parameter && e.parameter.action === 'status') {
    var which = (e.parameter.f === 'l') ? LEARNER_FORM_ID : OWNER_FORM_ID;
    var f = FormApp.openById(which);
    var items = f.getItems();
    var lines = ['TITLE: ' + f.getTitle(), 'ITEMS: ' + items.length, 'PUBLISHED: ' + f.getPublishedUrl(), '---'];
    for (var i = 0; i < items.length; i++) {
      lines.push((i+1) + '. [' + items[i].getType() + '] ' + items[i].getTitle());
    }
    return ContentService.createTextOutput(lines.join('\n'));
  }
  // STOP — disable all rewrite via doGet หลังพบ data loss issue
  return ContentService.createTextOutput('REWRITE DISABLED. Use ?action=responses or ?action=status');
  var which = (e && e.parameter && e.parameter.form) || 'both';
  var trashed = trashManagerFormIfExists();
  var owner = (which === 'both' || which === 'owner') ? createOwnerForm() : { edit: '(skipped)', publish: '(skipped)' };
  var learner = (which === 'both' || which === 'learner') ? createLearnerForm() : { edit: '(skipped)', publish: '(skipped)' };
  var html = '<!doctype html><meta charset="utf-8"><title>เสร็จแล้ว</title>'
    + '<style>body{font-family:-apple-system,system-ui,sans-serif;max-width:760px;margin:40px auto;padding:0 20px;line-height:1.7}h1{font-size:22px}h2{font-size:16px;margin-top:28px}a{color:#06c;word-break:break-all}.box{background:#f6f8fa;padding:14px 18px;border-radius:8px;margin:8px 0}.note{color:#888;font-size:13px}</style>'
    + '<h1>สร้างฟอร์มเรียบร้อย (2 ฟอร์ม)</h1>'
    + (trashed ? '<p class="note">ลบฟอร์มหัวหน้าแผนกเก่าไปเรียบร้อย (id: ' + trashed + ')</p>' : '')
    + '<h2>ฟอร์ม 1 — เจ้าของธุรกิจ (Needs Analysis)</h2>'
    + '<div class="box"><b>ส่งให้ตอบ:</b><br><a href="' + owner.publish + '" target="_blank">' + owner.publish + '</a></div>'
    + '<div class="box"><b>แก้ไข:</b><br><a href="' + owner.edit + '" target="_blank">' + owner.edit + '</a></div>'
    + '<h2>ฟอร์ม 2 — ผู้เรียน 15 ท่าน (Pre-training Survey)</h2>'
    + '<div class="box"><b>ส่งให้ตอบ:</b><br><a href="' + learner.publish + '" target="_blank">' + learner.publish + '</a></div>'
    + '<div class="box"><b>แก้ไข:</b><br><a href="' + learner.edit + '" target="_blank">' + learner.edit + '</a></div>';
  return HtmlService.createHtmlOutput(html);
}

/* ============ ฟอร์ม 1: เจ้าของธุรกิจ ============ */
function createOwnerForm() {
  var f = FormApp.openById(OWNER_FORM_ID); clearAllItems(f);
  f.setDescription('แบบสอบถามนี้ช่วยให้เราออกแบบหลักสูตรให้ตรงเป้าหมายของบริษัทมากที่สุด รบกวนตอบตามจริงครับ ส่วนใหญ่เป็นตัวเลือก กดเลือกได้เลย ใช้เวลา ~5 นาที');
  f.setProgressBar(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 1: ภาพรวมธุรกิจ & เป้าหมาย');
  f.addTextItem().setTitle('บริษัท, ชื่อผู้ตอบ, ตำแหน่ง').setRequired(true);
  f.addTextItem().setTitle('ธุรกิจของบริษัททำเกี่ยวกับอะไร (สั้นๆ 1 บรรทัด)').setRequired(true);

  f.addCheckboxItem().setTitle('เหตุผลที่อยากจัดอบรม AI ตอนนี้ (เลือกได้หลายข้อ)')
    .setHelpText('เลือกที่ตรงกับ pain point จริง — ผู้สอนจะใช้คัดเนื้อหา')
    .setChoiceValues([
      'งานซ้ำๆ ในทีมกินเวลามากเกินไป',
      'คู่แข่ง/ตลาดเริ่มใช้ AI แล้ว',
      'อยากให้ทีมเรียนรู้สิ่งใหม่ ทันยุค',
      'มีโปรเจกต์/ระบบใหม่ที่จะใช้ AI',
      'อยากลดต้นทุน/headcount',
      'เป็นนโยบายของบริษัท/ผู้บริหาร',
      'ลูกค้าเริ่มถามถึง AI'
    ]).showOtherOption(true).setRequired(true);

  f.addCheckboxItem().setTitle('เป้าหมายหลักหลังอบรม (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'ทีมใช้ AI ในงานประจำได้คล่อง',
      'มี internal tool ใช้จริง 1+ ตัว',
      'ลดเวลาทำงานซ้ำๆ ของทีม',
      'มีคน deploy เว็บไซต์เองได้',
      'ใช้ฐานข้อมูลในงานได้',
      'มี dashboard / automation ใหม่',
      'เปิดทาง self-service ในแผนก'
    ]).showOtherOption(true).setRequired(true);

  f.addCheckboxItem().setTitle('ตัวชี้วัดความสำเร็จที่ 3 เดือน (เลือก 1-3 ข้อ)')
    .setHelpText('ใช้วัดผลหลังคลาส ไม่ใช่แค่ความพอใจ — เลือกที่บริษัทยอม commit ได้')
    .setChoiceValues([
      'มี internal tool ใช้จริง 1+ ตัว',
      'ลดเวลาทำรายงานลง 30%+',
      'พนักงาน 5+ คนใช้ AI ในงานประจำ',
      'มี prototype 1+ ตัวขึ้น production',
      'มีคนในทีมทำเว็บ deploy เองได้',
      'มี automation ใหม่ 2+ ตัว',
      'ยังไม่แน่ใจ ขอผู้สอนช่วยกำหนด'
    ]).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 2: ขอบเขตหลักสูตร');
  f.addCheckboxItem().setTitle('หัวข้อที่ต้องการเรียน (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'พื้นฐาน Claude (ติดตั้ง สั่งงาน ฟังก์ชัน)',
      'ทำเว็บไซต์ขึ้น production (GitHub · Vercel · Netlify)',
      'ฐานข้อมูล (Supabase · Firebase · MongoDB)',
      'GitHub (เวอร์ชันคอนโทรล)'
    ]).showOtherOption(true).setRequired(true);

  f.addGridItem().setTitle('ระดับความคาดหวังในแต่ละหัวข้อ (สำคัญที่สุด — กำหนดความลึก)')
    .setHelpText('เข้าใจภาพรวม = ฟังบรรยายเข้าใจ · ทำตามขั้นตอน = follow tutorial ได้ · ทำเองได้ = สร้างใหม่ได้ตั้งแต่ต้น')
    .setRows(['Claude พื้นฐาน', 'deploy เว็บ', 'ฐานข้อมูล', 'GitHub'])
    .setColumns(['เข้าใจภาพรวม', 'ทำตามขั้นตอน', 'ทำเองได้จริง'])
    .setRequired(true);

  f.addCheckboxItem().setTitle('โปรเจกต์/ผลงานที่อยากให้พนักงานทำได้หลังจบ (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'เว็บบริษัท / landing page',
      'ระบบภายใน (internal tool)',
      'Dashboard ดูข้อมูล',
      'Bot / automation งานซ้ำ',
      'เดโมสำหรับลูกค้า',
      'ยังไม่มีไอเดียชัดเจน'
    ]).showOtherOption(true);

  f.addMultipleChoiceItem().setTitle('หัวข้อไหนสำคัญสุด อยากเน้นเป็นพิเศษ')
    .setChoiceValues([
      'Claude พื้นฐาน',
      'ทำเว็บ deploy',
      'ฐานข้อมูล',
      'GitHub',
      'เน้นเท่ากันทุกหัวข้อ'
    ]).showOtherOption(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 3: กลุ่มผู้เรียน')
    .setHelpText('ผู้เรียนคละแผนก (บัญชี/การตลาด/วิศวกร/ช่าง) หัวข้อ deploy เว็บ/DB/GitHub เน้นสายเทคนิค');

  f.addCheckboxItem().setTitle('เหตุผลที่เลือกผู้เรียนกลุ่มนี้ (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'หัวหน้าแต่ละแผนกคัดเลือกให้',
      'คนที่สนใจสมัครเข้ามาเอง',
      'คนที่มีพื้นฐานคอมพิวเตอร์อยู่แล้ว',
      'คนที่ทำงานเกี่ยวกับ pain point ที่อยากแก้',
      'คนที่จะใช้/ต่อยอดได้จริง',
      'ตามตำแหน่ง/แผนก ไม่ได้คัดพิเศษ'
    ]).showOtherOption(true);

  f.addMultipleChoiceItem().setTitle('หัวข้อสายเทคนิค (deploy/DB/GitHub) คาดหวังให้ใครทำได้')
    .setChoiceValues([
      'ทุกคนต้องทำได้เท่ากัน',
      'แบ่งระดับ: ทีมเทคนิคเรียนลึก / ทีมอื่นเรียนภาพรวม',
      'เฉพาะทีมเทคนิคเรียนลึก ที่เหลือเรียน Claude พื้นฐาน'
    ]).setRequired(true);

  f.addMultipleChoiceItem().setTitle('สะดวกไหมหากแบ่งกลุ่มตามพื้นฐาน + ปรับเนื้อหาให้เหมาะ')
    .setChoiceValues(['สะดวก', 'ขอรายละเอียดเพิ่มเติมก่อน']);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 4: เครื่องมือ & งบประมาณ');

  f.addMultipleChoiceItem().setTitle('ใครออกค่าเครื่องมือ (Claude/GitHub/Vercel/DB)')
    .setHelpText('ค่าใช้จ่ายโดยประมาณ: Claude ~฿700/คน/เดือน · GitHub ฟรี · Vercel/Netlify มี free tier · Supabase/Firebase มี free tier')
    .setChoiceValues([
      'บริษัทออกให้ทั้งหมด',
      'บริษัทออกบางส่วน (เช่น Claude เท่านั้น)',
      'ผู้เรียนใช้ฟรี-tier ของตัวเอง',
      'ยังไม่ได้วางแผน'
    ]).setRequired(true);

  f.addCheckboxItem().setTitle('บริษัทมีบัญชี/โครงสร้างเดิมอะไรบ้าง (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'GitHub organization',
      'โดเมนเว็บบริษัท',
      'Cloud (AWS / GCP / Azure)',
      'Vercel / Netlify',
      'ฐานข้อมูลที่ใช้อยู่ (SQL / NoSQL)',
      'ระบบ ERP / WMS / CRM',
      'ยังไม่มี'
    ]).showOtherOption(true);

  f.addMultipleChoiceItem().setTitle('งบประมาณโดยประมาณ')
    .setHelpText('ใช้กำหนด scope ของคอร์ส — ระบุคร่าวๆ ได้ จะปรับให้ลงตัว')
    .setChoiceValues([
      'น้อยกว่า ฿30,000 รวม',
      '฿30,000-50,000 รวม',
      '฿50,000-100,000 รวม',
      '฿100,000-200,000 รวม',
      'มากกว่า ฿200,000 รวม',
      'ยังไม่มีกรอบ ขอผู้สอนเสนอ option'
    ]).setRequired(true);

  f.addMultipleChoiceItem().setTitle('รูปแบบการจัด')
    .setChoiceValues(['ในออฟฟิศบริษัท (in-house)', 'นอกสถานที่', 'ออนไลน์'])
    .setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 5: โลจิสติกส์ & หลังอบรม');

  f.addMultipleChoiceItem().setTitle('จำนวนวัน + ช่วงเวลาที่คาดหวัง')
    .setChoiceValues(['ครึ่งวัน', '1 วัน', '2 วัน', 'มากกว่า 2 วัน'])
    .showOtherOption(true).setRequired(true);

  f.addCheckboxItem().setTitle('ช่วงเวลาที่สะดวก (เลือกได้หลายช่วง)')
    .setHelpText('เลือก 2-3 ช่วงให้ผู้สอนเลือกวันที่ลงตัว')
    .setChoiceValues([
      'กรกฎาคม 2026',
      'สิงหาคม 2026',
      'กันยายน 2026',
      'ตุลาคม 2026',
      'พฤศจิกายน 2026',
      'หลังจากนั้น',
      'ยังไม่แน่นอน'
    ]).setRequired(true);

  f.addMultipleChoiceItem().setTitle('สถานที่อบรมมี WiFi รองรับ 15 เครื่องพร้อมกันไหม')
    .setChoiceValues(['มี เสถียรพอ', 'ไม่แน่ใจ', 'ให้ผู้จัดเตรียมให้'])
    .setRequired(true);

  f.addMultipleChoiceItem().setTitle('ผู้เรียนติดตั้งโปรแกรมเองได้ (admin) ไหม')
    .setHelpText('จำเป็นมาก สำหรับ Claude/Git/Node — ถ้าไม่มีสิทธิ์ ต้องมี IT ช่วยล่วงหน้า')
    .setChoiceValues(['ติดตั้งเองได้', 'ต้องให้ IT ติดตั้งให้', 'ไม่แน่ใจ'])
    .setRequired(true);

  f.addCheckboxItem().setTitle('ข้อมูลบริษัทที่ห้ามนำไปใช้กับ AI (เลือกได้หลายข้อ)')
    .setHelpText('ใช้กำหนด data policy + guardrail ในคลาส')
    .setChoiceValues([
      'ข้อมูลลูกค้า (PII, เบอร์, ที่อยู่)',
      'งบการเงิน / ตัวเลขที่ไม่เปิดเผย',
      'source code ระบบหลัก',
      'ข้อมูล production',
      'สัญญา / เอกสารกฎหมาย',
      'ไม่มีข้อจำกัดพิเศษ',
      'ยังไม่ได้กำหนดนโยบาย'
    ]);

  f.addMultipleChoiceItem().setTitle('ต้องการสื่อ/SOP + ติดตามผลหลังอบรมไหม')
    .setChoiceValues(['ต้องการ', 'ไม่ต้องการ', 'แล้วแต่ผู้สอนแนะนำ']);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 6: ผลลัพธ์แบบ Tiered (สำคัญต่อการออกแบบหลักสูตร)')
    .setHelpText('ผู้เรียนคละแผนกที่ความต่างระดับสูง การยอมรับผลลัพธ์ไม่เท่ากันจะช่วยปลดล็อกการออกแบบ pace + ความลึก');

  f.addMultipleChoiceItem().setTitle('ยอมรับผลลัพธ์ของผู้เรียนแบบไม่เท่ากันได้ไหม')
    .setChoiceValues([
      'ทุกคนต้องได้ผลเท่ากัน (ต้องลดเพดานทั้งห้องตามคนช้าสุด)',
      'ยอมแบ่ง track ตามความเร็ว (คนเก่ง stretch / คนเริ่มต้นเวอร์ชันย่อ)',
      'แบ่งตามแผนก (สายเทคนิคทำเต็ม / สาย business เวอร์ชันย่อ)',
      'ขอคุยรายละเอียดก่อนตัดสินใจ'
    ]).setRequired(true);

  tryPublish(f);
  Logger.log('OK owner form');
  return { edit: f.getEditUrl(), publish: f.getPublishedUrl() };
}

/* ============ ฟอร์ม 2: ผู้เรียน ============ */
function createLearnerForm() {
  var f = FormApp.openById(LEARNER_FORM_ID); clearAllItems(f);
  f.setDescription('แบบสำรวจนี้ใช้เตรียมหลักสูตรให้ตรงกับงานและพื้นฐานของท่าน รบกวนตอบตามจริงครับ ไม่มีถูกผิด ส่วนใหญ่กดเลือกได้เลย ใช้เวลา ~5 นาที');
  f.setProgressBar(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 1: ข้อมูลทั่วไป');
  f.addTextItem().setTitle('ชื่อ-นามสกุล').setRequired(true);
  f.addMultipleChoiceItem().setTitle('แผนก')
    .setChoiceValues(['บัญชี / การเงิน', 'การตลาด', 'วิศวกร', 'ช่าง / เทคนิค'])
    .showOtherOption(true).setRequired(true);
  f.addTextItem().setTitle('ตำแหน่ง / หน้าที่หลัก').setRequired(true);
  f.addTextItem().setTitle('อีเมล (สำหรับส่งสื่อ/เกียรติบัตร/ติดตามผล)');

  f.addSectionHeaderItem().setTitle('ส่วนที่ 2: พื้นฐานทั่วไป');
  f.addScaleItem().setTitle('ความคล่องในการใช้คอมพิวเตอร์')
    .setHelpText('1 = พิมพ์งาน เปิดเว็บได้ · 3 = ใช้ Excel จัดไฟล์คล่อง · 5 = ติดตั้งโปรแกรม แก้ปัญหาคอมเองได้')
    .setBounds(1, 5).setLabels('เริ่มต้น', 'คล่องมาก').setRequired(true);

  f.addMultipleChoiceItem().setTitle('ระดับการอ่านภาษาอังกฤษ')
    .setHelpText('ไม่ต้องเก่ง — แต่ถ้าอ่าน error message อังกฤษได้จะเรียนเร็วกว่ามาก')
    .setChoiceValues(['น้อย (อ่านไม่ค่อยออก)', 'พอได้', 'ดี']).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 3: ความพร้อมด้านเทคนิค')
    .setHelpText('คอร์สมี deploy เว็บ + ฐานข้อมูล จึงขอประเมินส่วนนี้');

  f.addMultipleChoiceItem().setTitle('ระบบปฏิบัติการของเครื่องที่จะใช้ในวันอบรม')
    .setChoiceValues(['Windows', 'macOS', 'Linux', 'ไม่แน่ใจ']).setRequired(true);

  f.addMultipleChoiceItem().setTitle('สิทธิ์ติดตั้งโปรแกรมบนเครื่อง (Claude/Git/Node)')
    .setHelpText('ถ้าไม่แน่ใจ ลองดูว่าเคยลงโปรแกรมเอง (Zoom, Chrome, LINE) ได้ไหม')
    .setChoiceValues(['ติดตั้งเองได้', 'ต้องให้ IT ติดตั้งให้', 'ไม่แน่ใจ']).setRequired(true);

  f.addMultipleChoiceItem().setTitle('ประสบการณ์เขียนโค้ด / ทำเว็บ')
    .setChoiceValues(['ไม่เคยเลย', 'เคยเห็น HTML/CSS', 'เขียนโปรแกรม/ทำเว็บได้']).setRequired(true);

  f.addCheckboxItem().setTitle('เคยใช้เครื่องมือเหล่านี้ไหม (เลือกที่เคยใช้)')
    .setChoiceValues(['GitHub / Git', 'Command line (Terminal)', 'ฐานข้อมูล SQL', 'ฐานข้อมูล NoSQL', 'ไม่เคยเลย']);

  f.addCheckboxItem().setTitle('มีบัญชีเหล่านี้แล้วหรือยัง')
    .setChoiceValues(['GitHub', 'Vercel', 'Netlify', 'Supabase', 'Firebase', 'MongoDB', 'ยังไม่มีเลย']);

  f.addCheckboxItem().setTitle('เคยใช้ทักษะเหล่านี้บ้างไหม (เลือกที่เคยใช้จริง)')
    .setHelpText('คนที่ใช้สูตร Excel หรือ automation เก่ง มักเรียน AI ได้เร็ว แม้ไม่เคยเขียนโปรแกรม')
    .setChoiceValues([
      'สูตร Excel/Sheets แบบ IF, VLOOKUP, INDEX/MATCH',
      'Pivot Table',
      'เครื่องมือ automation (Zapier, Make, Power Automate)',
      'เขียน SQL / query ฐานข้อมูล',
      'เขียน macro (VBA, Google Apps Script)',
      'ยังไม่เคยใช้เลย'
    ]);

  f.addMultipleChoiceItem().setTitle('ยินดีทำ pre-task เบาๆ ก่อนวันงาน 3 วัน (~30 นาที) ไหม')
    .setHelpText('ใช้เป็น baseline + เตรียมเครื่องให้พร้อม จะช่วยลดเวลาติดตั้งในห้อง')
    .setChoiceValues(['ยินดี', 'จะพยายามทำ', 'ไม่ค่อยมีเวลา']).setRequired(true);

  f.addScaleItem().setTitle('ความสบายใจในการใช้เครื่องมือเทคนิค (Git, Terminal, ฐานข้อมูล)')
    .setHelpText('1 = ไม่เคยใช้ ไม่อยากแตะ · 3 = ใช้ได้แต่ต้องมีคนสอน · 5 = ใช้ประจำ สบายมาก')
    .setBounds(1, 5).setLabels('อึดอัดมาก', 'สบายมาก').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 4: ประสบการณ์ AI');

  f.addCheckboxItem().setTitle('เคยใช้ AI ตัวไหนบ้าง')
    .setChoiceValues(['ChatGPT', 'Claude', 'Gemini', 'Microsoft Copilot', 'ไม่เคยใช้เลย'])
    .showOtherOption(true);

  f.addMultipleChoiceItem().setTitle('ระดับการใช้ Claude')
    .setChoiceValues(['ไม่เคย', 'เคยลองเล่น', 'ใช้บ้างเป็นครั้งคราว', 'ใช้ประจำ']).setRequired(true);

  f.addCheckboxItem().setTitle('ถ้าเคยใช้ AI เคยนำไปช่วยงานอะไรบ้าง (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'เขียน/แก้ภาษาไทย-อังกฤษ',
      'สรุปข้อความ / เอกสาร',
      'แปลภาษา',
      'ค้นคว้าข้อมูล',
      'ตอบลูกค้า / chatbot',
      'สร้าง content (caption, blog)',
      'วิเคราะห์ Excel / data',
      'เขียนโค้ด / script',
      'สร้างภาพ',
      'ยังไม่เคยใช้'
    ]).showOtherOption(true);

  f.addScaleItem().setTitle('ความมั่นใจในการใช้ AI ช่วยงานตอนนี้ (จะถามซ้ำหลังอบรม)')
    .setHelpText('1 = ยังไม่กล้าใช้เลย · 3 = ใช้บ้างแต่ไม่แน่ใจคำตอบ · 5 = ใช้คล่อง สั่งงานได้หลายแบบ')
    .setBounds(1, 5).setLabels('ไม่มั่นใจ', 'มั่นใจมาก').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 5: งานจริง & สิ่งที่อยากได้');

  f.addCheckboxItem().setTitle('งานประจำที่กินเวลามากที่สุด (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'ทำรายงาน / สรุปข้อมูล',
      'กรอกข้อมูลซ้ำๆ (copy-paste)',
      'ตอบลูกค้า / chat',
      'ตรวจสอบ / approve เอกสาร',
      'ประชุม / ตามงาน',
      'สร้าง content social',
      'ทำ invoice / slip / เอกสาร',
      'วิเคราะห์ข้อมูล / Excel',
      'ค้นหาข้อมูล',
      'งานช่าง / หน้างาน'
    ]).showOtherOption(true).setRequired(true);

  f.addCheckboxItem().setTitle('งานที่อยากให้ AI ช่วยมากที่สุด (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'สรุปประชุม / chat',
      'แปล / เขียนภาษาอังกฤษ',
      'ตอบลูกค้า',
      'สร้าง content social',
      'วิเคราะห์ Excel',
      'ตรวจสอบ / แก้เอกสาร',
      'ค้นหาข้อมูล',
      'สร้างเว็บ / landing page',
      'สร้างภาพประกอบ',
      'automation งานซ้ำๆ'
    ]).showOtherOption(true).setRequired(true);

  f.addCheckboxItem().setTitle('โปรแกรม/เครื่องมือที่ใช้ประจำ (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'Excel / Google Sheets',
      'Word / Google Docs',
      'PowerPoint / Slides',
      'LINE / LINE OA',
      'Facebook / Instagram',
      'Email (Outlook / Gmail)',
      'โปรแกรมบัญชี (Express, Peak, ฯลฯ)',
      'EasySlip',
      'ERP / WMS',
      'Photoshop / Canva',
      'Notion / Trello'
    ]).showOtherOption(true);

  f.addCheckboxItem().setTitle('หลังอบรมจบ อยากทำอะไรได้ (เลือกได้หลายข้อ)')
    .setChoiceValues([
      'ใช้ AI ช่วยงานประจำได้คล่อง',
      'สร้าง prompt ที่ใช้ซ้ำได้',
      'ทำหน้าเว็บโปรไฟล์ / landing page เองได้',
      'ทำ internal tool / dashboard ของแผนก',
      'เชื่อม AI กับ Excel / ฐานข้อมูล',
      'สอนเพื่อนต่อได้',
      'ยังไม่ชัด ขอเรียนในคลาส'
    ]).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 6: อื่นๆ');

  f.addCheckboxItem().setTitle('มีข้อกังวล / อุปสรรค (เลือกที่ตรง)')
    .setChoiceValues([
      'กลัวข้อมูลรั่วไหล',
      'กลัวเรียนไม่ทัน',
      'กังวลภาษาอังกฤษ',
      'ไม่เคยใช้ command line',
      'ไม่มีสิทธิ์ติดตั้งโปรแกรม',
      'ไม่มีเวลาฝึก',
      'ไม่กังวลอะไรเป็นพิเศษ'
    ]).showOtherOption(true);

  f.addCheckboxItem().setTitle('ข้อจำกัดด้านอาหาร (เลือกที่ตรง)')
    .setChoiceValues([
      'ไม่มี / กินทุกอย่าง',
      'มังสวิรัติ',
      'เจ',
      'ไม่กินหมู',
      'ไม่กินเนื้อ',
      'แพ้อาหารทะเล',
      'แพ้นม (lactose intolerant)',
      'แพ้กลูเตน',
      'แพ้ถั่ว'
    ]).showOtherOption(true);

  // [ลบส่วนที่ 7 เมนูอาหาร/เครื่องดื่ม/ขนม ออกตามคำสั่ง user 2026-06-30 — ย้อนกลับเป็นเวอร์ชันก่อนเพิ่มเมนู]

  tryPublish(f);
  Logger.log('OK learner form');
  return { edit: f.getEditUrl(), publish: f.getPublishedUrl() };
}
