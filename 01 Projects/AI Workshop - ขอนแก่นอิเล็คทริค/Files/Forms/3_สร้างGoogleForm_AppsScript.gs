/**
 * สร้าง Google Form 3 ชุด สำหรับ Claude AI Workshop (บ.ขอนแก่นอิเล็คทริค)
 *   - createOwnerForm()   : แบบสอบถามเจ้าของธุรกิจ (Needs Analysis)
 *   - createLearnerForm() : แบบสำรวจผู้เรียน 15 ท่าน (พื้นฐาน + ความพร้อมเทคนิค)
 *   - createPostForm()    : แบบประเมินหลังอบรม (Kirkpatrick L1–L2)
 *
 * วิธีใช้:
 *  1) เปิด https://script.google.com -> New project
 *  2) ลบโค้ดเดิม วางทั้งหมดนี้
 *  3) เลือกฟังก์ชันที่จะรัน -> กด Run
 *  4) อนุญาตสิทธิ์ครั้งแรก -> ดูลิงก์ที่ View > Logs
 *  (รัน createAllForms() เพื่อสร้างทั้ง 3 ฟอร์มรวดเดียว)
 */

function createAllForms() {
  createOwnerForm();
  createLearnerForm();
  createPostForm();
}

/* ============ ชุดที่ 1: เจ้าของธุรกิจ ============ */
function createOwnerForm() {
  var f = FormApp.create('แบบสอบถามเจ้าของธุรกิจ — Claude AI Workshop (Needs Analysis)');
  f.setDescription('แบบสอบถามนี้ช่วยให้เราออกแบบหลักสูตรให้ตรงเป้าหมายของบริษัทมากที่สุด รบกวนตอบตามความต้องการจริงครับ');
  f.setProgressBar(true);

  f.addSectionHeaderItem().setTitle('ส่วน A — ภาพรวมธุรกิจ & เป้าหมาย');
  f.addTextItem().setTitle('บริษัท / ผู้ตอบ / ตำแหน่ง').setRequired(true);
  f.addTextItem().setTitle('ธุรกิจของบริษัททำอะไรโดยย่อ').setRequired(true);
  f.addParagraphTextItem().setTitle('ทำไมถึงอยากจัดอบรม AI ตอนนี้ — มีปัญหา/โอกาสอะไรที่อยากแก้').setRequired(true);
  f.addParagraphTextItem().setTitle('เป้าหมายหลักหลังอบรม — อยากให้เกิดอะไรกับทีม/ธุรกิจ').setRequired(true);
  f.addParagraphTextItem().setTitle('ถ้าอบรมนี้ "สำเร็จ" ภายใน 3 เดือน จะเห็นอะไรเปลี่ยน (วัดผลอย่างไร)').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วน B — ขอบเขตหลักสูตร');
  f.addCheckboxItem().setTitle('ยืนยันหัวข้อที่ต้องการ')
    .setChoiceValues(['พื้นฐานการใช้ Claude (ติดตั้ง สั่งงาน ฟังก์ชัน)',
                      'ทำเว็บไซต์ขึ้น production (GitHub · Vercel · Netlify)',
                      'ฐานข้อมูล (Supabase · Firebase · MongoDB)',
                      'GitHub (เวอร์ชันคอนโทรล)'])
    .showOtherOption(true).setRequired(true);
  f.addGridItem().setTitle('ระดับผลลัพธ์ที่คาดหวัง "ต่อหัวข้อ" (สำคัญที่สุด — กำหนดความลึก)')
    .setRows(['Claude พื้นฐาน', 'ทำเว็บ deploy', 'ฐานข้อมูล', 'GitHub'])
    .setColumns(['รู้จัก/เข้าใจภาพรวม', 'ทำตามขั้นตอนได้', 'ทำเองได้จริง'])
    .setRequired(true);
  f.addParagraphTextItem().setTitle('มีโปรเจกต์/ผลงานจริงที่อยากให้พนักงานทำได้หลังจบไหม (เช่น เว็บบริษัท, ระบบภายใน)');
  f.addTextItem().setTitle('หัวข้อไหนสำคัญสุด / อยากเน้นเป็นพิเศษ');

  f.addSectionHeaderItem().setTitle('ส่วน C — กลุ่มผู้เรียน')
    .setHelpText('ผู้เรียนคละแผนก (บัญชี/การตลาด/วิศวกร/ช่าง) แต่หัวข้อ 2–4 เป็นสายเทคนิค');
  f.addParagraphTextItem().setTitle('ทำไมถึงเลือกผู้เรียน 15 ท่านกลุ่มนี้');
  f.addMultipleChoiceItem().setTitle('หัวข้อสายเทคนิค (deploy เว็บ, ฐานข้อมูล, GitHub) คาดหวังให้ใครทำได้')
    .setChoiceValues(['ทุกคนต้องทำได้เท่ากัน',
                      'แบ่งระดับ: กลุ่มเทคนิคลงลึก / กลุ่มอื่นเรียนภาพรวม',
                      'เฉพาะทีมเทคนิคลงลึก ที่เหลือเรียน Claude พื้นฐาน'])
    .setRequired(true);
  f.addMultipleChoiceItem().setTitle('รับได้ไหมถ้าแนะนำให้แบ่งกลุ่มตามพื้นฐาน / ปรับเนื้อหาบางส่วน')
    .setChoiceValues(['ได้', 'ขอคุยรายละเอียดก่อน']);

  f.addSectionHeaderItem().setTitle('ส่วน D — เครื่องมือ & งบประมาณ');
  f.addMultipleChoiceItem().setTitle('ใครออกค่าเครื่องมือ (Claude plan, GitHub, Vercel/Netlify, ฐานข้อมูล)')
    .setChoiceValues(['บริษัทออกให้', 'ผู้เรียนใช้ฟรี/ของตัวเอง', 'ยังไม่ได้คิด'])
    .showOtherOption(true).setRequired(true);
  f.addTextItem().setTitle('บริษัทมีบัญชี/โดเมน/โครงสร้างที่ใช้อยู่แล้วไหม (เช่น GitHub org, โดเมน)');
  f.addTextItem().setTitle('งบประมาณโดยประมาณ — ต่อหัว หรือ งบรวม');
  f.addMultipleChoiceItem().setTitle('รูปแบบการจัด')
    .setChoiceValues(['ที่บริษัท (in-house)', 'นอกสถานที่', 'ออนไลน์']).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วน E — โลจิสติกส์ & หลังอบรม');
  f.addMultipleChoiceItem().setTitle('จำนวนวัน + ช่วงเวลาที่คาดหวัง')
    .setChoiceValues(['ครึ่งวัน', '1 วัน', '2 วัน', 'มากกว่า 2 วัน']).showOtherOption(true).setRequired(true);
  f.addTextItem().setTitle('วันที่สะดวก (ช่วงเดือน/สัปดาห์ไหน)').setRequired(true);
  f.addMultipleChoiceItem().setTitle('สถานที่อบรม มี WiFi รองรับ 15 เครื่องพร้อมกันไหม')
    .setChoiceValues(['มี', 'ไม่แน่ใจ', 'ให้ผู้จัดช่วยจัด']).setRequired(true);
  f.addMultipleChoiceItem().setTitle('ผู้เรียนมีสิทธิ์ติดตั้งโปรแกรมเอง (admin) บนเครื่องไหม — จำเป็นต่อการลง Claude/Git/Node')
    .setChoiceValues(['มีสิทธิ์', 'ต้องให้ IT ลงให้', 'ไม่แน่ใจ']).setRequired(true);
  f.addParagraphTextItem().setTitle('มีข้อมูลบริษัทที่ "ห้าม" นำเข้า AI ไหม (นโยบายความปลอดภัย/ลูกค้า)');
  f.addMultipleChoiceItem().setTitle('อยากได้สื่อ/คู่มือ (SOP) + ติดตามผลหลังอบรมไหม')
    .setChoiceValues(['ต้องการ', 'ไม่ต้องการ', 'แล้วแต่แนะนำ']);

  Logger.log('✅ ฟอร์มเจ้าของธุรกิจ');
  Logger.log('✏️  แก้ไข: ' + f.getEditUrl());
  Logger.log('📨 ส่งตอบ: ' + f.getPublishedUrl());
}

/* ============ ชุดที่ 2: ผู้เรียน ============ */
function createLearnerForm() {
  var f = FormApp.create('แบบสำรวจผู้เรียน — Claude AI Workshop');
  f.setDescription('แบบสอบถามนี้ใช้เพื่อเตรียมหลักสูตรให้ตรงกับงานและพื้นฐานของทุกท่าน รบกวนตอบตามจริงครับ ไม่มีถูกผิด');
  f.setProgressBar(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 1 — ข้อมูลทั่วไป');
  f.addTextItem().setTitle('ชื่อ–นามสกุล').setRequired(true);
  f.addMultipleChoiceItem().setTitle('แผนก')
    .setChoiceValues(['บัญชี / การเงิน', 'การตลาด', 'วิศวกร', 'ช่าง / เทคนิค']).showOtherOption(true).setRequired(true);
  f.addTextItem().setTitle('ตำแหน่ง / หน้าที่หลักโดยย่อ').setRequired(true);
  f.addTextItem().setTitle('อีเมล (สำหรับส่งสื่อ / เกียรติบัตร / ติดตามผล)');

  f.addSectionHeaderItem().setTitle('ส่วนที่ 2 — พื้นฐานทั่วไป');
  f.addScaleItem().setTitle('ความคล่องในการใช้คอมพิวเตอร์').setBounds(1, 5).setLabels('เริ่มต้น', 'คล่องมาก').setRequired(true);
  f.addMultipleChoiceItem().setTitle('ระดับการอ่านภาษาอังกฤษ').setChoiceValues(['น้อย (อ่านไม่ค่อยออก)', 'พอได้', 'ดี']).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 3 — ความพร้อมด้านเทคนิค')
    .setHelpText('คอร์สมีการ deploy เว็บ + ฐานข้อมูล จึงขอประเมินพื้นฐานส่วนนี้');
  f.addMultipleChoiceItem().setTitle('ระบบปฏิบัติการเครื่องที่จะใช้ในวันอบรม')
    .setChoiceValues(['Windows', 'macOS', 'Linux', 'ไม่แน่ใจ']).setRequired(true);
  f.addMultipleChoiceItem().setTitle('สิทธิ์ติดตั้งโปรแกรมบนเครื่อง (ลง Claude/Git/Node)')
    .setChoiceValues(['ติดตั้งเองได้', 'ต้องให้ IT ลงให้', 'ไม่แน่ใจ']).setRequired(true);
  f.addMultipleChoiceItem().setTitle('ประสบการณ์เขียนโค้ด / ทำเว็บ')
    .setChoiceValues(['ไม่เคยเลย', 'เคยเห็น HTML/CSS นิดหน่อย', 'เขียนโปรแกรม/ทำเว็บได้']).setRequired(true);
  f.addCheckboxItem().setTitle('เคยใช้เครื่องมือเหล่านี้ไหม (เลือกที่เคยใช้)')
    .setChoiceValues(['GitHub / Git', 'Command line (Terminal)', 'ฐานข้อมูล SQL', 'ฐานข้อมูล NoSQL', 'ยังไม่เคยเลย']);
  f.addCheckboxItem().setTitle('มีบัญชีเหล่านี้แล้วหรือยัง')
    .setChoiceValues(['GitHub', 'Vercel', 'Netlify', 'Supabase', 'Firebase', 'MongoDB', 'ยังไม่มีเลย']);
  f.addScaleItem().setTitle('ความสบายใจกับเครื่องมือสายเทคนิค (Git, Terminal, ฐานข้อมูล)').setBounds(1, 5).setLabels('อึดอัดมาก', 'สบายมาก').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 4 — ประสบการณ์ AI');
  f.addCheckboxItem().setTitle('เคยใช้ AI ตัวไหนมาบ้าง')
    .setChoiceValues(['ChatGPT', 'Claude', 'Gemini', 'Microsoft Copilot', 'ยังไม่เคยใช้เลย']).showOtherOption(true);
  f.addMultipleChoiceItem().setTitle('ระดับการใช้ Claude')
    .setChoiceValues(['ไม่เคย', 'เคยลองเล่น', 'ใช้บ้างเป็นครั้งคราว', 'ใช้ประจำ']).setRequired(true);
  f.addParagraphTextItem().setTitle('ถ้าเคยใช้ AI เคยเอาไปช่วยงานอะไรบ้าง');
  f.addScaleItem().setTitle('ความมั่นใจในการใช้ AI ช่วยงาน "ตอนนี้" (จะถามซ้ำหลังอบรม)').setBounds(1, 5).setLabels('ไม่มั่นใจเลย', 'มั่นใจมาก').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 5 — งานจริง & สิ่งที่อยากได้');
  f.addParagraphTextItem().setTitle('งานประจำที่ "กินเวลา" มากที่สุด 1–2 อย่าง').setRequired(true);
  f.addParagraphTextItem().setTitle('งานที่อยากให้ AI ช่วยมากที่สุด').setRequired(true);
  f.addTextItem().setTitle('โปรแกรม/เครื่องมือที่ใช้ประจำ (เช่น Excel, easyslip, โปรแกรมบัญชี)');
  f.addParagraphTextItem().setTitle('หลังอบรมจบ อยากทำอะไรได้').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 6 — อื่นๆ');
  f.addParagraphTextItem().setTitle('มีข้อกังวล/อุปสรรคเรื่องการใช้ AI หรือเครื่องมือเทคนิคไหม');
  f.addTextItem().setTitle('ข้อจำกัดด้านอาหาร (มังสวิรัติ/แพ้อาหาร)');

  Logger.log('✅ ฟอร์มผู้เรียน');
  Logger.log('✏️  แก้ไข: ' + f.getEditUrl());
  Logger.log('📨 ส่งผู้เรียน: ' + f.getPublishedUrl());
}

/* ============ ชุดที่ 4: หลังอบรม (Kirkpatrick L1–L2) ============ */
function createPostForm() {
  var f = FormApp.create('แบบประเมินหลังการอบรม — Claude AI Workshop');
  f.setDescription('ขอบคุณที่ร่วมอบรมครับ รบกวนสะท้อนความเห็นตามจริง เพื่อพัฒนาหลักสูตรและช่วยสนับสนุนท่านได้ตรงจุด');
  f.setProgressBar(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 1 — ข้อมูลผู้ตอบ');
  f.addTextItem().setTitle('ชื่อ–นามสกุล (เพื่อจับคู่กับแบบก่อนเรียน)').setRequired(true);
  f.addMultipleChoiceItem().setTitle('แผนก')
    .setChoiceValues(['บัญชี / การเงิน', 'การตลาด', 'วิศวกร', 'ช่าง / เทคนิค']).showOtherOption(true).setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 2 — ความพึงพอใจ (Reaction)');
  f.addScaleItem().setTitle('ความพึงพอใจโดยรวมต่อการอบรม').setBounds(1, 5).setLabels('น้อยมาก', 'มากที่สุด').setRequired(true);
  f.addScaleItem().setTitle('เนื้อหาตรงกับงาน / ความคาดหวัง').setBounds(1, 5).setLabels('ไม่ตรง', 'ตรงมาก').setRequired(true);
  f.addScaleItem().setTitle('วิทยากร (ความชัดเจน + ความรู้)').setBounds(1, 5).setLabels('ควรปรับ', 'ดีมาก').setRequired(true);
  f.addMultipleChoiceItem().setTitle('จังหวะ/ความเร็วในการสอน').setChoiceValues(['ช้าไป', 'พอดี', 'เร็วไป']).setRequired(true);
  f.addScaleItem().setTitle('สื่อ / ใบงาน / ตัวอย่าง').setBounds(1, 5).setLabels('น้อยมาก', 'ดีมาก');
  f.addScaleItem().setTitle('สถานที่ / อาหาร / การจัดการ').setBounds(1, 5).setLabels('น้อยมาก', 'ดีมาก');
  f.addMultipleChoiceItem().setTitle('ระยะเวลาการอบรม').setChoiceValues(['สั้นไป', 'พอดี', 'ยาวไป']);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 3 — การเรียนรู้ (Learning)');
  f.addScaleItem().setTitle('ความมั่นใจในการใช้ AI ช่วยงาน "หลังเรียน" (เทียบกับก่อนเรียน)').setBounds(1, 5).setLabels('ไม่มั่นใจเลย', 'มั่นใจมาก').setRequired(true);
  f.addGridItem().setTitle('ประเมินตัวเอง — ทำได้แค่ไหนในแต่ละหัวข้อ')
    .setRows(['Claude พื้นฐาน', 'ทำเว็บ deploy', 'ฐานข้อมูล', 'GitHub'])
    .setColumns(['ยังทำไม่ได้', 'ทำตามได้', 'ทำเองได้']).setRequired(true);
  f.addTextItem().setTitle('หัวข้อที่เข้าใจชัดเจนที่สุด');
  f.addTextItem().setTitle('หัวข้อที่ยัง "งง" / อยากทบทวนเพิ่ม').setRequired(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 4 — การนำไปใช้ (Application)');
  f.addParagraphTextItem().setTitle('ตั้งใจจะนำไปใช้กับงานอะไรบ้าง').setRequired(true);
  f.addParagraphTextItem().setTitle('ภายใน 30 วันนี้ จะลองทำอะไรเป็นอย่างแรก');
  f.addParagraphTextItem().setTitle('คาดว่าจะเจออุปสรรคอะไรตอนเอาไปใช้จริง');
  f.addCheckboxItem().setTitle('อยากให้สนับสนุนอะไรเพิ่มหลังอบรม')
    .setChoiceValues(['คู่มือ/SOP', 'คลิปทบทวน', 'กลุ่มถาม-ตอบ', 'coaching ตัวต่อตัว', 'คลาสต่อยอด']).showOtherOption(true);

  f.addSectionHeaderItem().setTitle('ส่วนที่ 5 — ภาพรวม & ข้อเสนอแนะ');
  f.addScaleItem().setTitle('จะแนะนำคอร์สนี้ให้เพื่อนร่วมงานไหม (0–10)').setBounds(0, 10).setLabels('ไม่แนะนำ', 'แนะนำมาก').setRequired(true);
  f.addParagraphTextItem().setTitle('สิ่งที่ "ชอบที่สุด"');
  f.addParagraphTextItem().setTitle('สิ่งที่ "ควรปรับปรุง"');
  f.addTextItem().setTitle('หัวข้อที่อยากเรียนเพิ่มในอนาคต');
  f.addParagraphTextItem().setTitle('ความคิดเห็นเพิ่มเติม');

  Logger.log('✅ ฟอร์มหลังอบรม');
  Logger.log('✏️  แก้ไข: ' + f.getEditUrl());
  Logger.log('📨 ส่งผู้เรียน: ' + f.getPublishedUrl());
}
