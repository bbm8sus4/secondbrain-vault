/**
 * Course Intake Kit (MASTER) — สร้าง Google Forms กลาง 4 ตัว
 *   ฟอร์ม 1: แบบสอบถามผู้ว่าจ้าง (Needs Analysis)
 *   ฟอร์ม 2: แบบสำรวจผู้เรียนก่อนอบรม (Pre-training)
 *   ฟอร์ม 3: แบบประเมินหลังอบรม (Post-training)
 *   ฟอร์ม 4: แบบติดตามผล 30–60 วัน (Follow-up)
 *
 * วิธีใช้ต่อลูกค้า 1 ราย: เปิดฟอร์ม MASTER ใน Drive → "ทำสำเนา" → แก้ [ค่ากลาง] ให้ตรงลูกค้า
 * ห้ามส่งฟอร์ม MASTER ให้ลูกค้าตอบตรงๆ
 *
 * create-only: รัน createAllForms ครั้งเดียว — มี property lock กันสร้างซ้ำ
 * ถ้าต้องการสร้างชุดใหม่จริงๆ ให้รัน createAllFormsForce
 */

var PROP_KEY = 'KIT_FORM_URLS';

// ===== ค่ากลาง — แก้ตอน "ทำสำเนา" ต่อลูกค้าแต่ละราย =====

var TOPICS = [
  'พื้นฐานการใช้ AI / Claude (ติดตั้ง สั่งงาน prompt)',
  'AI ช่วยงานเอกสาร/สรุป/วิเคราะห์ข้อมูล (Excel, รายงาน)',
  'AI ช่วยงานการตลาด (คอนเทนต์ ภาพ แผนแคมเปญ)',
  'ทำเว็บไซต์ขึ้น production (GitHub, Vercel/Netlify)',
  'ฐานข้อมูล (Supabase, Firebase ฯลฯ)',
  'Automation / เชื่อมระบบ (API, chatbot, workflow)'
];

var DEPARTMENTS = [
  'บัญชี/การเงิน',
  'การตลาด/ขาย',
  'HR/ธุรการ',
  'IT',
  'ปฏิบัติการ/ผลิต/ช่าง',
  'บริหาร'
];

// ===== helpers =====

function addHeader(f, title, help) {
  var it = f.addSectionHeaderItem().setTitle(title);
  if (help) it.setHelpText(help);
  return it;
}

function addText(f, title, required, help) {
  var it = f.addTextItem().setTitle(title);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function addPara(f, title, required, help) {
  var it = f.addParagraphTextItem().setTitle(title);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function addMC(f, title, choices, required, other, help) {
  var it = f.addMultipleChoiceItem().setTitle(title).setChoiceValues(choices);
  if (other) it.showOtherOption(true);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function addCB(f, title, choices, required, other, help) {
  var it = f.addCheckboxItem().setTitle(title).setChoiceValues(choices);
  if (other) it.showOtherOption(true);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function addScale(f, title, lowLabel, highLabel, required, help, low, high) {
  var it = f.addScaleItem().setTitle(title)
    .setBounds(low || 1, high || 5)
    .setLabels(lowLabel, highLabel);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function addGrid(f, title, rows, cols, required, help) {
  var it = f.addGridItem().setTitle(title).setRows(rows).setColumns(cols);
  if (help) it.setHelpText(help);
  if (required) it.setRequired(true);
  return it;
}

function tryPublish(f) {
  try { if (typeof f.setPublished === 'function') f.setPublished(true); } catch (e) {}
}

// ===== ฟอร์ม 1 — ผู้ว่าจ้าง (Needs Analysis) =====

function createHirerForm() {
  var f = FormApp.create('[MASTER] ฟอร์ม 1 — แบบสอบถามผู้ว่าจ้าง (Needs Analysis)');
  f.setDescription(
    'แบบสอบถามนี้ช่วยให้เราออกแบบหลักสูตรให้ตรงเป้าหมายของบริษัทมากที่สุด ' +
    'รบกวนตอบตามความต้องการจริงครับ ข้อมูลใช้เพื่อการออกแบบหลักสูตรเท่านั้น'
  );

  addHeader(f, 'ส่วน A — ภาพรวมธุรกิจ & เป้าหมาย');
  addText(f, 'บริษัท / ชื่อผู้ตอบ / ตำแหน่ง', true);
  addText(f, 'ประเภทธุรกิจ/อุตสาหกรรม + ธุรกิจทำอะไรโดยย่อ', true);
  addMC(f, 'ขนาดองค์กรโดยประมาณ',
    ['น้อยกว่า 10 คน', '10–50 คน', '51–200 คน', 'มากกว่า 200 คน'], true);
  addCB(f, 'ทำไมถึงอยากจัดอบรม AI ตอนนี้ — มีปัญหา/โอกาสอะไรที่อยากแก้', [
    'อยากลดเวลางานซ้ำๆ',
    'คู่แข่งเริ่มใช้ AI',
    'พนักงานอยากเรียน',
    'ผู้บริหารมีนโยบาย',
    'มีโปรเจกต์เฉพาะที่อยากทำ'
  ], true, true);
  addCB(f, 'เป้าหมายหลักหลังอบรม — อยากให้เกิดอะไรกับทีม/ธุรกิจ', [
    'ลดเวลางานประจำ / เพิ่ม productivity',
    'พนักงานใช้ AI เป็นในงานของตัวเอง',
    'สร้างผลงาน/ระบบที่ใช้จริงได้',
    'ต่อยอดสู่โปรเจกต์ AI ภายในบริษัท',
    'ยกระดับภาพลักษณ์/ความสามารถองค์กร'
  ], true, true);
  addCB(f, 'ถ้าอบรมนี้ "สำเร็จ" ภายใน 3 เดือน จะเห็นอะไรเปลี่ยน (วัดผลอย่างไร)', [
    'พนักงานใช้ AI ในงานประจำสม่ำเสมอ',
    'เวลาทำงานบางอย่างลดลงแบบวัดได้',
    'มีผลงาน/ระบบที่ใช้จริงในบริษัท',
    'ลดค่าใช้จ่าย/งาน outsource',
    'มีทีมภายในที่สอนต่อกันเองได้'
  ], true, true);

  addHeader(f, 'ส่วน B — ขอบเขตหลักสูตร');
  addCB(f, 'หัวข้อที่ต้องการ', TOPICS, true, true);
  addGrid(f, 'ระดับผลลัพธ์ที่คาดหวัง "ต่อหัวข้อ" — เลือกที่ใกล้สุด',
    TOPICS,
    ['รู้จัก/เข้าใจภาพรวม', 'ทำตามขั้นตอนได้', 'ทำเองได้จริงหลังจบ'],
    true,
    'คำถามสำคัญที่สุดของฟอร์ม — ใช้กำหนดความลึกและจำนวนวันของคอร์ส');
  addCB(f, 'มีโปรเจกต์/ผลงานจริงที่อยากให้พนักงาน "ทำได้" หลังจบไหม', [
    'เว็บไซต์ / landing page ของบริษัท',
    'ระบบภายใน / เครื่องมือช่วยงาน',
    'รายงาน / dashboard อัตโนมัติ',
    'คอนเทนต์การตลาด',
    'Chatbot / ระบบตอบลูกค้า',
    'ยังไม่มีโปรเจกต์เฉพาะ — เน้นทักษะ'
  ], false, true);
  addMC(f, 'หัวข้อไหน "สำคัญสุด" / อยากเน้นเป็นพิเศษ', TOPICS, false, true);

  addHeader(f, 'ส่วน C — กลุ่มผู้เรียน');
  addText(f, 'จำนวนผู้เรียน + มาจากแผนก/สายงานไหนบ้าง', true);
  addCB(f, 'ทำไมเลือกผู้เรียนกลุ่มนี้', [
    'งานของกลุ่มนี้เกี่ยวข้องกับ AI มากที่สุด',
    'เป็นตัวแทนไปสอนต่อทีม',
    'อาสาสมัคร / สนใจเอง',
    'ผู้บริหารเลือกให้',
    'อบรมทั้งบริษัท/ทั้งแผนก'
  ], false, true);
  addMC(f, 'หัวข้อสายเทคนิค (ถ้ามี) คาดหวังให้ "ทุกคน" ทำได้ หรือ "เฉพาะบางกลุ่ม"', [
    'ทุกคนต้องทำได้เท่ากัน',
    'แบ่งระดับ: กลุ่มเทคนิคลงลึก / กลุ่มอื่นเรียนภาพรวม',
    'เฉพาะทีมเทคนิคเรียนหัวข้อลึก ที่เหลือเรียนพื้นฐาน'
  ], true);
  addMC(f, 'รับได้ไหมถ้าผู้สอนแนะนำให้ "แบ่งกลุ่มตามพื้นฐาน" หรือปรับเนื้อหาตามแผนก',
    ['ได้', 'ขอคุยก่อน'], false);
  addMC(f, 'ผู้เรียนอ่านภาษาอังกฤษได้ระดับไหนโดยรวม (สื่อการสอนบางส่วนเป็นภาษาอังกฤษ)',
    ['น้อย', 'พอได้', 'ดี', 'คละกัน'], false);

  addHeader(f, 'ส่วน D — เครื่องมือ & งบประมาณ');
  addMC(f, 'ใครออกค่าเครื่องมือ (AI plan รายเดือน, บริการ cloud)',
    ['บริษัทออก', 'ผู้เรียนใช้แบบฟรี / ของตัวเอง', 'ยังไม่ได้คิด'], true);
  addCB(f, 'บริษัทมีบัญชี/โครงสร้างเดิมอะไรบ้าง', [
    'GitHub organization',
    'โดเมนเว็บไซต์',
    'Google Workspace',
    'Microsoft 365',
    'AI plan ที่ซื้อแล้ว (ChatGPT / Claude / Gemini ฯลฯ)',
    'ยังไม่มีเลย'
  ], false, true);
  addMC(f, 'งบประมาณโดยประมาณ', [
    'ไม่เกิน 50,000 บาท (รวม)',
    '50,000–100,000 บาท (รวม)',
    '100,000–300,000 บาท (รวม)',
    'มากกว่า 300,000 บาท (รวม)',
    'ยังไม่กำหนด'
  ], false, true, 'ถ้าคิดเป็นงบต่อหัว ระบุใน "อื่นๆ"');
  addMC(f, 'รูปแบบการจัด',
    ['ที่บริษัท (in-house)', 'นอกสถานที่', 'ออนไลน์', 'ผสม'], true);

  addHeader(f, 'ส่วน E — โลจิสติกส์ & ความพร้อม IT');
  addMC(f, 'จำนวนวัน + ช่วงเวลาที่คาดหวัง',
    ['ครึ่งวัน', '1 วัน', '2 วัน', 'มากกว่า 2 วัน', 'แล้วแต่แนะนำ'], true);
  addText(f, 'ช่วงวันที่สะดวก', true);
  addMC(f, 'สถานที่มี WiFi รองรับผู้เรียนทุกเครื่องพร้อมกันไหม',
    ['มี', 'ไม่แน่ใจ', 'ให้ผู้สอนช่วยจัด'], true);
  addMC(f, 'ผู้เรียนใช้โน้ตบุ๊ก + มีสิทธิ์ "ติดตั้งโปรแกรมเอง" (admin) ไหม',
    ['มีสิทธิ์ติดตั้งเอง', 'ต้องให้ IT ลงให้', 'ไม่แน่ใจ'], true,
    false, 'จำเป็นมากถ้าคอร์สมีการติดตั้งเครื่องมือ');
  addMC(f, 'ระบบ IT บริษัทมีบล็อกเว็บ / proxy / firewall ที่อาจกั้นเครื่องมือ (AI, GitHub, cloud) ไหม',
    ['ไม่มี', 'มี', 'ไม่แน่ใจ'], false,
    false, 'ถ้ามี รบกวนแจ้งชื่อผู้ดูแล IT ไว้ประสานล่วงหน้า');
  addMC(f, 'ผู้เรียนมีอีเมลบริษัท (corporate) สำหรับสมัครบริการไหม',
    ['มีอีเมลบริษัท', 'ใช้อีเมลส่วนตัว', 'คละกัน'], false);
  addText(f, 'ชื่อผู้ประสานงานฝั่งบริษัท + ช่องทางติดต่อ (LINE / โทร)', true);

  addHeader(f, 'ส่วน F — นโยบายข้อมูล & ความปลอดภัย');
  addCB(f, 'มีข้อมูลบริษัทที่ "ห้าม" นำเข้า AI ไหม', [
    'ข้อมูลลูกค้า / ข้อมูลส่วนบุคคล',
    'ข้อมูลการเงิน',
    'ความลับการค้า / สูตร / แบบ',
    'สัญญา / เอกสารกฎหมาย',
    'ไม่มีข้อห้าม'
  ], true, true);
  addMC(f, 'บริษัทมีนโยบาย/ข้อกำหนดการใช้ AI อยู่แล้วไหม', [
    'มีเป็นลายลักษณ์อักษร',
    'มีแนวปฏิบัติแบบปากเปล่า',
    'ยังไม่มี — อยากให้ช่วยร่าง',
    'ยังไม่มี'
  ], false);

  addHeader(f, 'ส่วน G — หลังอบรม & ความคาดหวังผลลัพธ์');
  addMC(f, 'ต้องการสื่อ/คู่มือ (SOP) + ติดตามผลหลังอบรมไหม',
    ['ต้องการ', 'ไม่ต้องการ', 'แล้วแต่แนะนำ'], false);
  addMC(f, 'ผู้เรียนพื้นฐานต่างกัน ผลลัพธ์หลังอบรมย่อมไม่เท่ากัน — ยอมรับผลลัพธ์แบบ "ไม่เท่ากันตามพื้นฐาน" ได้ไหม', [
    'ยอมรับได้',
    'อยากให้ทุกคนถึงเส้นเดียวกัน (อาจต้องเพิ่มวัน/แบ่งรุ่น)'
  ], true);

  tryPublish(f);
  return f;
}

// ===== ฟอร์ม 2 — ผู้เรียน (Pre-training) =====

function createLearnerForm() {
  var f = FormApp.create('[MASTER] ฟอร์ม 2 — แบบสำรวจผู้เรียนก่อนอบรม (Pre-training)');
  f.setDescription(
    'แบบสอบถามนี้ใช้เพื่อเตรียมหลักสูตรให้ตรงกับงานและพื้นฐานของทุกท่าน ' +
    'รบกวนตอบตามจริงครับ ไม่มีถูกผิด — ใช้เพื่อออกแบบการอบรมเท่านั้น (ตอบ ~5 นาที)'
  );

  addHeader(f, 'ส่วนที่ 1 — ข้อมูลทั่วไป');
  addText(f, 'ชื่อ–นามสกุล', true, 'ใช้จับคู่กับแบบประเมินหลังเรียน เพื่อดูพัฒนาการรายคน');
  addMC(f, 'แผนก', DEPARTMENTS, true, true);
  addText(f, 'ตำแหน่ง / หน้าที่หลักโดยย่อ', true);
  addText(f, 'อีเมล (สำหรับส่งสื่อ/เกียรติบัตร/ติดตามผล)', false);

  addHeader(f, 'ส่วนที่ 2 — พื้นฐานทั่วไป');
  addScale(f, 'ความคล่องในการใช้คอมพิวเตอร์', 'เริ่มต้น', 'คล่องมาก', true,
    '1 = ใช้งานพื้นฐาน · 3 = ใช้งานทั่วไปได้คล่อง · 5 = คล่องมาก ช่วยคนอื่นได้');
  addMC(f, 'ระดับการอ่านภาษาอังกฤษ', ['น้อย', 'พอได้', 'ดี'], true);

  addHeader(f, 'ส่วนที่ 3 — ความพร้อมด้านเทคนิค',
    'ใช้เพื่อจัดกลุ่ม/ปรับเนื้อหาให้เหมาะกับพื้นฐาน — ตอบตามจริงได้เลย');
  addMC(f, 'ระบบปฏิบัติการเครื่องที่จะใช้ในวันอบรม',
    ['Windows', 'macOS', 'Linux', 'ไม่แน่ใจ'], true);
  addMC(f, 'สิทธิ์ติดตั้งโปรแกรมบนเครื่อง',
    ['ติดตั้งเองได้', 'ต้องให้ IT ลงให้', 'ไม่แน่ใจ'], true);
  addMC(f, 'ประสบการณ์เขียนโค้ด / ทำเว็บ',
    ['ไม่เคยเลย', 'เคยเห็น HTML/CSS นิดหน่อย', 'เขียนโปรแกรม/ทำเว็บได้'], true);
  addCB(f, 'เคยใช้เครื่องมือเหล่านี้ไหม', [
    'GitHub / Git',
    'Command line (Terminal)',
    'ฐานข้อมูล SQL',
    'ฐานข้อมูล NoSQL',
    'ยังไม่เคยเลย'
  ], false);
  addCB(f, 'มีบัญชีเหล่านี้แล้วหรือยัง', [
    'GitHub', 'Vercel', 'Netlify', 'Supabase', 'Firebase', 'ยังไม่มีเลย'
  ], false, false, 'ปรับรายการตามบริการที่คอร์สใช้จริง');
  addCB(f, 'เคยใช้ทักษะเหล่านี้ไหม', [
    'สูตร Excel ซับซ้อน (VLOOKUP / Pivot)',
    'Macro / Apps Script',
    'ตั้งค่า automation (Zapier / Make ฯลฯ)',
    'เขียน SQL query',
    'ยังไม่เคยเลย'
  ], false);
  addMC(f, 'ยินดีทำ pre-task สั้นๆ ก่อนวันงานไหม (เช่น สมัครบัญชี ติดตั้งโปรแกรมล่วงหน้า)',
    ['ยินดี', 'ขอทำหน้างาน', 'ไม่แน่ใจ'], false);
  addScale(f, 'ความสบายใจกับเครื่องมือสายเทคนิค (Git, Terminal, ฐานข้อมูล)',
    'อึดอัดมาก', 'สบายมาก', true,
    '1 = ไม่อยากแตะเลย · 3 = ลองได้ถ้ามีคนช่วย · 5 = สนุก อยากลอง');

  addHeader(f, 'ส่วนที่ 4 — ประสบการณ์ AI');
  addCB(f, 'เคยใช้ AI ตัวไหนมาบ้าง',
    ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'ยังไม่เคย'], false, true);
  addMC(f, 'ระดับการใช้ Claude',
    ['ไม่เคย', 'เคยลองเล่น', 'ใช้บ้าง', 'ใช้ประจำ'], true);
  addCB(f, 'เคยเอา AI ไปช่วยงานอะไรบ้าง', [
    'ร่าง/สรุปเอกสาร',
    'แปลภาษา',
    'เขียนอีเมล / ตอบแชท',
    'วิเคราะห์ข้อมูล / Excel',
    'ทำภาพ / คอนเทนต์',
    'เขียนโค้ด',
    'ยังไม่เคยใช้กับงาน'
  ], false, true);
  addScale(f, 'ความมั่นใจในการใช้ AI ช่วยงาน "ตอนนี้"', 'ไม่มั่นใจเลย', 'มั่นใจมาก', true,
    'ตอบตามความรู้สึกจริงตอนนี้ — จะถามอีกครั้งหลังอบรมเพื่อดูพัฒนาการ');

  addHeader(f, 'ส่วนที่ 5 — งานจริง & สิ่งที่อยากได้');
  addCB(f, 'งานประจำที่ "กินเวลา" มากที่สุด', [
    'งานเอกสาร / รายงาน',
    'ตอบอีเมล / แชท / ลูกค้า',
    'คีย์ข้อมูล / จัดการไฟล์',
    'วิเคราะห์ข้อมูล / สรุปตัวเลข',
    'ประชุม / ประสานงาน',
    'งานคอนเทนต์ / ออกแบบ'
  ], true, true);
  addCB(f, 'งานที่อยากให้ AI ช่วยมากที่สุด', [
    'งานเอกสาร / รายงาน',
    'ตอบอีเมล / แชท / ลูกค้า',
    'คีย์ข้อมูล / จัดการไฟล์',
    'วิเคราะห์ข้อมูล / สรุปตัวเลข',
    'ประชุม / ประสานงาน',
    'งานคอนเทนต์ / ออกแบบ'
  ], true, true);
  addText(f, 'โปรแกรม/เครื่องมือที่ใช้ประจำ (เช่น Excel, โปรแกรมบัญชี, ระบบภายใน)', false);
  addCB(f, 'หลังอบรมจบ อยากทำอะไรได้', [
    'ใช้ AI ทำงานประจำได้เร็วขึ้น',
    'สร้างเอกสาร/รายงานอัตโนมัติ',
    'ทำเว็บ/ระบบเองได้',
    'วิเคราะห์ข้อมูลเองได้',
    'สอนต่อเพื่อนร่วมงานได้'
  ], true, true);

  addHeader(f, 'ส่วนที่ 6 — อื่นๆ');
  addCB(f, 'มีข้อกังวล/อุปสรรคเรื่องการใช้ AI ไหม', [
    'กลัวใช้ไม่เป็น / ตามไม่ทัน',
    'กลัว AI แทนที่งาน',
    'กังวลความปลอดภัยข้อมูล',
    'ภาษาอังกฤษ',
    'เวลาไม่พอฝึก',
    'ไม่มีข้อกังวล'
  ], false, true);
  addText(f, 'ข้อจำกัดด้านอาหาร (มังสวิรัติ / แพ้อาหาร) — ถ้ามี', false,
    'ตัดข้อนี้ออกถ้างานไม่ได้จัดอาหาร');

  tryPublish(f);
  return f;
}

// ===== ฟอร์ม 3 — หลังอบรม (Post-training) =====

function createPostForm() {
  var f = FormApp.create('[MASTER] ฟอร์ม 3 — แบบประเมินหลังอบรม (Post-training)');
  f.setDescription(
    'ขอบคุณที่ร่วมอบรมครับ รบกวนสะท้อนความเห็นตามจริง ' +
    'เพื่อพัฒนาหลักสูตรและช่วยให้ทีมงานสนับสนุนท่านได้ตรงจุด (ตอบ ~5 นาที)'
  );

  addHeader(f, 'ส่วนที่ 1 — ข้อมูลผู้ตอบ');
  addText(f, 'ชื่อ–นามสกุล', true, 'ใช้จับคู่กับแบบก่อนเรียน เพื่อดูพัฒนาการรายคน');
  addMC(f, 'แผนก', DEPARTMENTS, true, true);

  addHeader(f, 'ส่วนที่ 2 — ความพึงพอใจ');
  addScale(f, 'ความพึงพอใจโดยรวมต่อการอบรม', 'น้อยที่สุด', 'มากที่สุด', true);
  addScale(f, 'เนื้อหาตรงกับงาน / ความคาดหวัง', 'ไม่ตรงเลย', 'ตรงมาก', true);
  addScale(f, 'วิทยากร (ความชัดเจน + ความรู้)', 'ควรปรับปรุง', 'ดีมาก', true);
  addMC(f, 'จังหวะ/ความเร็วในการสอน', ['ช้าไป', 'พอดี', 'เร็วไป'], true);
  addScale(f, 'สื่อ / ใบงาน / ตัวอย่าง', 'ควรปรับปรุง', 'ดีมาก', false);
  addScale(f, 'สถานที่ / อาหาร / การจัดการ', 'ควรปรับปรุง', 'ดีมาก', false,
    'ตัดข้อนี้ออกถ้าจัดออนไลน์');
  addMC(f, 'ระยะเวลาการอบรม', ['สั้นไป', 'พอดี', 'ยาวไป'], false);

  addHeader(f, 'ส่วนที่ 3 — การเรียนรู้');
  addScale(f, 'ความมั่นใจในการใช้ AI ช่วยงาน "หลังเรียน"', 'ไม่มั่นใจเลย', 'มั่นใจมาก', true,
    'เทียบกับที่ตอบไว้ก่อนเรียน — ใช้วัดพัฒนาการ');
  addGrid(f, 'ประเมินตัวเอง — ทำได้แค่ไหนในแต่ละหัวข้อ',
    TOPICS,
    ['ยังทำไม่ได้', 'ทำตามได้', 'ทำเองได้'],
    true,
    'ตอนทำสำเนาต่อลูกค้า: แก้แถวให้เหลือเฉพาะหัวข้อที่สอนจริง');
  addMC(f, 'หัวข้อที่เข้าใจชัดเจนที่สุด', TOPICS, false, true);
  addCB(f, 'หัวข้อที่ยัง "งง" / อยากทบทวนเพิ่ม', TOPICS.concat(['ไม่มี']), true, true);

  addHeader(f, 'ส่วนที่ 4 — การนำไปใช้');
  addPara(f, 'ตั้งใจจะนำไปใช้กับงานอะไรบ้าง', true);
  addPara(f, 'ภายใน 30 วันนี้ จะลองทำอะไรเป็นอย่างแรก', false);
  addCB(f, 'คาดว่าจะเจออุปสรรคอะไรตอนเอาไปใช้จริง', [
    'ไม่มีเวลาฝึก',
    'ลืมขั้นตอน',
    'เครื่องมือ / สิทธิ์ไม่พร้อม',
    'ไม่มีคนถาม',
    'นโยบายบริษัท'
  ], false, true);
  addCB(f, 'อยากให้สนับสนุนอะไรเพิ่มหลังอบรม', [
    'คู่มือ / SOP',
    'คลิปทบทวน',
    'กลุ่มถาม-ตอบ',
    'Coaching ตัวต่อตัว',
    'คลาสต่อยอด'
  ], false, true);

  addHeader(f, 'ส่วนที่ 5 — ภาพรวม & ข้อเสนอแนะ');
  addScale(f, 'จะแนะนำคอร์สนี้ให้เพื่อนร่วมงานไหม', 'ไม่แนะนำเลย', 'แนะนำแน่นอน', true,
    '0 = ไม่แนะนำเลย · 10 = แนะนำแน่นอน', 0, 10);
  addPara(f, 'สิ่งที่ "ชอบที่สุด"', false);
  addPara(f, 'สิ่งที่ "ควรปรับปรุง"', false);
  addText(f, 'หัวข้อที่อยากเรียนเพิ่มในอนาคต', false);
  addPara(f, 'ความคิดเห็นเพิ่มเติม', false);

  tryPublish(f);
  return f;
}

// ===== ฟอร์ม 4 — ติดตามผล 30–60 วัน (Follow-up) =====

function createFollowupForm() {
  var f = FormApp.create('[MASTER] ฟอร์ม 4 — แบบติดตามผล 30–60 วัน (Follow-up)');
  f.setDescription(
    'ผ่านมา 1–2 เดือนแล้ว อยากทราบว่า AI ช่วยงานจริงของท่านได้แค่ไหน ' +
    'คำตอบช่วยให้เราสนับสนุนต่อได้ตรงจุดครับ (ตอบ ~3 นาที)'
  );

  addHeader(f, 'ส่วนที่ 1 — ข้อมูลผู้ตอบ');
  addText(f, 'ชื่อ–นามสกุล', true);
  addMC(f, 'แผนก', DEPARTMENTS, true, true);

  addHeader(f, 'ส่วนที่ 2 — การใช้งานจริง');
  addMC(f, 'หลังอบรม ได้ใช้ AI กับงานจริงบ่อยแค่ไหน', [
    'ทุกวัน',
    'สัปดาห์ละหลายครั้ง',
    'สัปดาห์ละครั้ง',
    'นานๆ ครั้ง',
    'ยังไม่ได้ใช้เลย'
  ], true);
  addCB(f, 'ใช้กับงานอะไรบ้าง', [
    'งานเอกสาร / สรุป / รายงาน',
    'วิเคราะห์ข้อมูล / Excel',
    'คอนเทนต์ / การตลาด',
    'ทำเว็บ / ระบบ',
    'Automation / เชื่อมระบบ',
    'ยังไม่ได้ใช้'
  ], false, true);
  addMC(f, 'มีผลงานที่ทำด้วย AI แล้วใช้จริงไหม (เอกสาร เว็บ ระบบ ฯลฯ)',
    ['มี', 'กำลังทำ', 'ยังไม่มี'], false, true,
    'ถ้ามี เล่าสั้นๆ ใน "อื่นๆ" ได้เลย');
  addMC(f, 'ประมาณเวลาที่ประหยัดได้ต่อสัปดาห์', [
    'ยังไม่เห็นผล',
    'น้อยกว่า 1 ชั่วโมง',
    '1–3 ชั่วโมง',
    '3–8 ชั่วโมง',
    'มากกว่า 8 ชั่วโมง'
  ], true);

  addHeader(f, 'ส่วนที่ 3 — อุปสรรค & การสนับสนุน');
  addCB(f, 'ถ้าใช้น้อย/ไม่ได้ใช้ — ติดอะไร', [
    'ไม่มีเวลา',
    'ลืมวิธีใช้',
    'เครื่องมือ / บัญชี / สิทธิ์ไม่พร้อม',
    'งานไม่เอื้อ',
    'นโยบายบริษัท',
    'ไม่มีคนถาม',
    'ไม่ติดอะไร'
  ], false, true);
  addScale(f, 'ความมั่นใจในการใช้ AI ช่วยงาน "ตอนนี้"', 'ไม่มั่นใจเลย', 'มั่นใจมาก', true,
    'จุดที่ 3 ของเส้นวัดผล: ก่อนเรียน → หลังเรียน → 30–60 วัน');
  addCB(f, 'อยากได้การสนับสนุนอะไรต่อ', [
    'คลาสทบทวน',
    'คลาสต่อยอด',
    'Coaching',
    'คู่มือเพิ่ม',
    'ไม่ต้องการ'
  ], false);
  addPara(f, 'ความคิดเห็นเพิ่มเติม / ผลงานที่อยากอวด', false);

  tryPublish(f);
  return f;
}

// ===== entry points =====

function createAllForms() {
  // LockService = atomic check-then-create (property check เดี่ยวๆ กัน concurrent doGet ไม่ได้ — พิสูจน์แล้ว 2026-07-15 ได้ 3 ชุดซ้อน)
  var lock = LockService.getScriptLock();
  lock.waitLock(120000);
  try {
    var props = PropertiesService.getScriptProperties();
    var existing = props.getProperty(PROP_KEY);
    if (existing) {
      Logger.log('ฟอร์มถูกสร้างไปแล้ว — ไม่สร้างซ้ำ (กัน duplicate)');
      Logger.log(existing);
      return JSON.parse(existing);
    }
    return doCreate_();
  } finally {
    lock.releaseLock();
  }
}

// duplicate จากเหตุการณ์ doGet ซ้อน 2026-07-15 — trash ผ่าน ?action=cleanup (ย้ายลงถังขยะ กู้คืนได้)
var DUPLICATE_IDS_20260715 = [
  '1-LpYW5FVSIfPRXNYCPoeu8gtLcFcG2-BNZQ3IVwWFOc',
  '1pfF6YJEzo1fYFiNDQxyUXRpl4KwZnXGNFRdw9ajbugE',
  '1tNNLaeVR5xzbkw3VcLqSp1ufhKr4_0Ekm1_0M-0NRKI',
  '1qKGv564SOxsbJrbAiB0W2x7AUGBw9-UUmlTLhNIxgsU',
  '15yENqX5lQD7YBXXYHGO328RaZKMVIxNKXhgm7OSzYl8',
  '1UOcg1WwoD5GDrewttzEEoIfYQWB7UXpagB5GsegKge4',
  '1Yk92Qgdpk5xCAJWio7otR9tOwg-VgDXPGbZnnJzp9DQ',
  '1PWSJXFPJWFhNkUol_lQldlQHV0VlD-h77FzbnHLIkkw'
];

function cleanupDuplicates() {
  var keep = {};
  var stored = PropertiesService.getScriptProperties().getProperty(PROP_KEY);
  if (stored) {
    var out = JSON.parse(stored);
    for (var k in out) {
      var m = out[k].editUrl.match(/\/d\/([^\/]+)\//);
      if (m) keep[m[1]] = true;
    }
  }
  var results = [];
  DUPLICATE_IDS_20260715.forEach(function (id) {
    if (keep[id]) { results.push(id + ': SKIP (ชุดที่ใช้อยู่)'); return; }
    try {
      var file = DriveApp.getFileById(id);
      if (file.getName().indexOf('[MASTER]') !== 0) {
        results.push(id + ': SKIP (ชื่อไม่ใช่ [MASTER])');
        return;
      }
      file.setTrashed(true);
      results.push(id + ': trashed');
    } catch (e) {
      results.push(id + ': ERROR ' + e);
    }
  });
  Logger.log(results.join('\n'));
  return results;
}

function createAllFormsForce() {
  return doCreate_();
}

function doCreate_() {
  var forms = [
    ['form1_hirer', createHirerForm()],
    ['form2_learner', createLearnerForm()],
    ['form3_post', createPostForm()],
    ['form4_followup', createFollowupForm()]
  ];
  var out = {};
  forms.forEach(function (pair) {
    var key = pair[0], f = pair[1];
    out[key] = {
      title: f.getTitle(),
      editUrl: f.getEditUrl(),
      publishedUrl: f.getPublishedUrl()
    };
  });
  PropertiesService.getScriptProperties().setProperty(PROP_KEY, JSON.stringify(out));
  Logger.log(JSON.stringify(out, null, 2));
  return out;
}

function doGet(e) {
  if (e && e.parameter && e.parameter.action === 'cleanup') {
    var res = cleanupDuplicates();
    return HtmlService.createHtmlOutput('<h2>Cleanup</h2><pre>' + res.join('\n') + '</pre>');
  }
  var out = createAllForms(); // LockService + property กันสร้างซ้ำเมื่อ doGet ถูก trigger ซ้อน
  var html = '<h2>Course Intake Kit — MASTER Forms</h2><ol>';
  for (var k in out) {
    html += '<li><b>' + out[k].title + '</b><br>' +
      'แก้ไข: <a href="' + out[k].editUrl + '">' + out[k].editUrl + '</a><br>' +
      'ตอบ: <a href="' + out[k].publishedUrl + '">' + out[k].publishedUrl + '</a></li>';
  }
  html += '</ol><p>ใช้งานต่อลูกค้า: เปิดฟอร์มใน Drive แล้ว "ทำสำเนา" — ห้ามส่ง MASTER ให้ลูกค้าตอบตรง</p>';
  return HtmlService.createHtmlOutput(html);
}
