/**
 * สร้าง Google Form — เลือกอาหารเบรก & อาหารกลางวัน
 * สำหรับผู้เข้าอบรม Claude AI Workshop (บ.ขอนแก่นอิเล็คทริค · 15 ท่าน)
 * อิงเมนูจริงจากร้าน SHIFT (ดู 04-Menu-Catering.md)
 *
 * วิธีใช้:
 *  1) เปิด https://script.google.com -> New project
 *  2) ลบโค้ดเดิม วางไฟล์นี้ทั้งหมด
 *  3) เลือกฟังก์ชัน createFoodForm -> กด Run
 *  4) อนุญาตสิทธิ์ครั้งแรก -> ดูลิงก์ที่ View > Logs (Ctrl/Cmd+Enter)
 *
 * ⚠️ ปลอดภัย: สคริปต์นี้ "สร้างฟอร์มใหม่" อย่างเดียว (FormApp.create)
 *    ไม่มี clearAllItems / deleteItem / delete ใด ๆ — รันซ้ำ = ได้ฟอร์มใหม่อีกใบ
 *    ห้ามเอา logic ลบ item ไปใส่ทับฟอร์มที่มี response แล้ว (เคยมี incident ข้อมูลหาย)
 */

/* ---------- เมนูจริง (แก้ที่นี่ที่เดียว) ---------- */

// อาหารกลางวัน 190.-/เซต (กับข้าว 2 อย่าง + ข้าว + ผลไม้ + น้ำผลไม้ + น้ำเปล่า)
var LUNCH = [
  'ข้าวกะเพราหมู', 'ข้าวกะเพราไก่',
  'ข้าวผัดพริกหมู', 'ข้าวผัดพริกไก่',
  'ข้าวแกงจืดหมู', 'ข้าวแกงจืดไก่',
  'ข้าวผัดหมู', 'ข้าวผัดไก่', 'ข้าวผัดไส้กรอก',
  'ไข่เจียวหมูสับ', 'ไข่เจียวไก่สับ',
  'ข้าวหมูเกาหลี', 'ข้าวไก่เกาหลี',
  'ข้าวหมูสับผัดซีอิ๊ว', 'ข้าวไก่สับผัดซีอิ๊ว'
];

// เครื่องดื่มเย็นเบรค 70.-/แก้ว
var DRINKS = [
  'Americano (เย็น)', 'Iced Milk', 'Matcha Pure',
  'Matcha Latte', 'Thai Tea', 'Lychee Soda'
];

// ขนม Break Set 49.- (ใส่หมวดกำกับกันชื่อซ้ำ เช่น ช็อกโกแลต/ฝอยทอง มีทั้ง Bread และเค้กฟอยล์)
var SNACKS = [
  '[เค้กไข่ 18.-] เค้กไข่เคลือบช็อกโกแลต',
  '[เค้กไข่ 18.-] เค้กไข่เคลือบไวท์ช็อกโกแลต',
  '[Bread 20.-] ฝอยทอง',
  '[Bread 20.-] ลูกเกด',
  '[Bread 20.-] แยมสตรอว์เบอรี่',
  '[Bread 20.-] ไวท์ช็อกโกแลต',
  '[Bread 20.-] ช็อกโกแลต',
  '[Bread 20.-] ใบเตย',
  '[ขนมปังปั้น 20.-] แฮมชีส',
  '[ขนมปังปั้น 20.-] หมูหยองเนย',
  '[ขนมปังปั้น 20.-] ปูอัดไส้กุ้ง',
  '[ขนมปังปั้น 20.-] ผักโขมอบชีส',
  '[ขนมปังปั้น 20.-] หน้าพิซซ่า',
  '[ขนมปังปั้น 20.-] ข้าวโพด',
  '[ขนมปังปั้น 20.-] หมูหยองพริกเผา',
  '[เค้กฟอยล์ 25.-] ช็อกโกแลต',
  '[เค้กฟอยล์ 25.-] บลูเบอรี่',
  '[เค้กฟอยล์ 25.-] เผือก',
  '[เค้กฟอยล์ 25.-] ชาไทย',
  '[เค้กฟอยล์ 25.-] สตรอว์เบอรี่',
  '[เค้กฟอยล์ 25.-] มะพร้าว',
  '[เค้กฟอยล์ 25.-] ฝอยทอง',
  '[เค้กฟอยล์ 25.-] วานิลา',
  '[เค้กฟอยล์ 25.-] โอริโอ้'
];

// นม/น้ำผลไม้ คู่ Break Set
var MILK = ['นมจืด', 'นมรสช็อกโกแลต', 'น้ำส้ม', 'น้ำแอปเปิ้ล'];


/* ---------- สร้างฟอร์ม ---------- */
function createFoodForm() {
  var f = FormApp.create('เลือกอาหารเบรก & อาหารกลางวัน — Claude AI Workshop');
  f.setDescription(
    'สำหรับผู้เข้าอบรม 15 ท่าน — เลือกเมนูอาหารกลางวัน เครื่องดื่มเบรก เช้า/บ่าย และขนม\n' +
    'มื้อกลางวัน 1 เซต = กับข้าว 2 อย่าง + ข้าวเปล่า + ผลไม้ + น้ำผลไม้ 1 กล่อง + น้ำเปล่า 1 ขวด\n' +
    'รบกวนกรอกให้ครบก่อนวันอบรม เพื่อให้เราสั่งอาหารได้ถูกต้องครับ'
  );
  f.setProgressBar(true);
  f.setCollectEmail(true);              // เก็บอีเมลกันกรอกซ้ำ/ระบุตัวตน
  f.setLimitOneResponsePerUser(false);  // เผื่อกรอกแทนกัน/แก้ทีหลัง

  /* ส่วน 1 — ระบุตัวผู้กรอก */
  f.addSectionHeaderItem().setTitle('ส่วนที่ 1 — ข้อมูลผู้เข้าอบรม');
  f.addTextItem().setTitle('ชื่อ–นามสกุล').setRequired(true);
  f.addTextItem().setTitle('แผนก / ทีม').setRequired(true);

  /* ส่วน 2 — อาหารกลางวัน */
  f.addSectionHeaderItem().setTitle('ส่วนที่ 2 — อาหารกลางวัน (190.-/เซต)')
    .setHelpText('เลือก 1 เมนู');
  f.addMultipleChoiceItem()
    .setTitle('เมนูอาหารกลางวันที่เลือก')
    .setChoiceValues(LUNCH)
    .setRequired(true);

  /* ส่วน 3 — เบรกเช้า */
  f.addSectionHeaderItem().setTitle('ส่วนที่ 3 — เบรกเช้า')
    .setHelpText('เครื่องดื่มเย็น 1 แก้ว + ขนม 1 ชิ้น + นม/น้ำผลไม้ 1 กล่อง');
  f.addMultipleChoiceItem()
    .setTitle('เครื่องดื่มเย็น (เบรกเช้า)')
    .setChoiceValues(DRINKS).setRequired(true);
  f.addListItem()
    .setTitle('ขนม (เบรกเช้า)')
    .setChoiceValues(SNACKS).setRequired(true);
  f.addMultipleChoiceItem()
    .setTitle('นม / น้ำผลไม้ (เบรกเช้า)')
    .setChoiceValues(MILK).setRequired(true);

  /* ส่วน 4 — เบรกบ่าย */
  f.addSectionHeaderItem().setTitle('ส่วนที่ 4 — เบรกบ่าย')
    .setHelpText('เครื่องดื่มเย็น 1 แก้ว + ขนม 1 ชิ้น + นม/น้ำผลไม้ 1 กล่อง');
  f.addMultipleChoiceItem()
    .setTitle('เครื่องดื่มเย็น (เบรกบ่าย)')
    .setChoiceValues(DRINKS).setRequired(true);
  f.addListItem()
    .setTitle('ขนม (เบรกบ่าย)')
    .setChoiceValues(SNACKS).setRequired(true);
  f.addMultipleChoiceItem()
    .setTitle('นม / น้ำผลไม้ (เบรกบ่าย)')
    .setChoiceValues(MILK).setRequired(true);

  /* ส่วน 5 — ข้อจำกัดด้านอาหาร */
  f.addSectionHeaderItem().setTitle('ส่วนที่ 5 — ข้อจำกัด / คำขอเพิ่มเติม');
  f.addCheckboxItem()
    .setTitle('ข้อจำกัดด้านอาหาร (เลือกได้หลายข้อ)')
    .setChoiceValues(['ไม่มี', 'ทานมังสวิรัติ / เจ', 'อิสลาม (ฮาลาล — ไม่ทานหมู)', 'ไม่ทานเนื้อสัตว์บางชนิด'])
    .showOtherOption(true);
  f.addTextItem()
    .setTitle('อาหารที่แพ้ (ถ้ามี ระบุให้ชัด เช่น กุ้ง ถั่ว นม)');
  f.addParagraphTextItem()
    .setTitle('หมายเหตุอื่น ๆ ถึงทีมจัดงาน');

  f.setConfirmationMessage('บันทึกเรียบร้อยครับ ขอบคุณที่กรอก แล้วเจอกันวันอบรม 🙌');

  Logger.log('=== สร้างฟอร์มอาหารเรียบร้อย ===');
  Logger.log('ลิงก์ให้ผู้เข้าอบรมกรอก (published): ' + f.getPublishedUrl());
  Logger.log('ลิงก์แก้ไขฟอร์ม (edit):          ' + f.getEditUrl());
  Logger.log('เก็บผลตอบใน Sheet: เปิดฟอร์ม -> Responses -> Link to Sheets');
}
