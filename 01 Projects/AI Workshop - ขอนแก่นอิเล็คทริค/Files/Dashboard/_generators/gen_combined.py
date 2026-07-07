#!/usr/bin/env python3
import json, math

BASE="/Users/aexgee/Documents/Claude/Projects/AI Workshop Management/RECOVERY"
QDATA=json.load(open('/tmp/qdata.json',encoding='utf-8'))
PEOPLE=json.load(open('/tmp/people.json',encoding='utf-8'))

# polish map (Typhoon) + overrides
pol={}
try:
    for p in json.load(open('/tmp/full_th_paired.json',encoding='utf-8')):
        if p.get('after') and p['before'].strip()!=p['after'].strip():
            pol[p['before']]=p['after']
except: pass
# overrides (reject Typhoon mistakes)
for k in ['เคยใช้ AI ตัวไหนบ้าง','17 คำถาม']: pol.pop(k,None)
pol['เคยใช้เครื่องมือเทคนิค']='เคยใช้เครื่องมือทางเทคนิค'
def P(s): return pol.get(s,s)

ANALYSIS={
 'ต่อ':{'v':'พร้อมที่สุดในกลุ่ม — ลงมือทำเองได้ทันที เหมาะเป็นผู้ช่วยสอนเพื่อน',
  's':['เขียนเว็บได้ + เคยใช้ Terminal และ SQL','ติดตั้งโปรแกรมเองได้ ใช้ macOS','ไม่มีข้อกังวล มีความมั่นใจในการใช้งาน'],
  'r':['อาจรู้สึกช้าถ้าคลาสเดินตามคนเริ่มต้น'],
  'p':['จัดเข้า advanced track — deploy จริง + ฐานข้อมูล','มอบบทบาท buddy/ผู้ช่วย ดูแลเพื่อนสายเทคนิค','ให้โจทย์ stretch กันเบื่อ']},
 'นัท':{'v':'พื้นฐานแน่น มั่นใจ AI สูงสุดในกลุ่ม — สายเทคนิคคนเดียว เป็นกำลังหลักได้',
  's':['ความมั่นใจในการใช้ AI สูงสุด (4/5)','เคยใช้ฐานข้อมูล SQL + ติดตั้งเองได้','ไม่มีข้อกังวล'],
  'r':['ยังไม่เคยเขียนโค้ดเต็มตัว (แต่พื้น SQL ช่วยได้มาก)'],
  'p':['เข้า advanced track คู่กับ ต่อ','เป็น buddy ช่วยเหลือเพื่อนที่ยังเริ่มต้น','ต่อยอดสู่งานช่าง/เทคนิคจริงของบริษัท']},
 'ฟ้า':{'v':'สายดีไซน์ที่ตรงกับ use case คอนเทนต์/ภาพพอดี — ไปได้ดีถ้าจังหวะเหมาะ',
  's':['ติดตั้งโปรแกรมเองได้','ทักษะกราฟิกตรงกับโจทย์การตลาด','ความมั่นใจปานกลาง (3/5)'],
  'r':['ยังไม่เคยเขียนโค้ด','กังวลว่าจะเรียนไม่ทัน'],
  'p':['core track เน้น content + ภาพ + landing page แบบ no-code','ใช้ทักษะดีไซน์เป็นแต้มต่อ ให้ทำงานจริงของตัวเอง']},
 'อาร์ม':{'v':'พื้นฐานพอมี (เคยเห็น HTML + ลองเล่น Claude) แต่ต้องเคลียร์เรื่องเครื่อง + ภาษา',
  's':['เคยเห็น HTML/CSS','เคยลองเล่น Claude มาก่อน'],
  'r':['สิทธิ์ติดตั้งโปรแกรมยังไม่แน่ใจ','กังวลเรียนไม่ทัน + ภาษาอังกฤษ'],
  'p':['เตรียม/ทดสอบเครื่องล่วงหน้า','แจก cheat sheet ศัพท์อังกฤษ + error','จัดเข้า core track']},
 'แม็ก':{'v':'สาย creative ตั้งเป้าสูง (อยากทำแอป) แต่ยังไม่ได้ตั้งเป้าชัดเจน ต้องช่วยให้โฟกัส',
  's':['เคยเห็น HTML/CSS','แรงจูงใจสูง อยากสร้างแอปจริง'],
  'r':['สิทธิ์ติดตั้งไม่แน่ใจ','เป้าหมายหลังเรียนยังไม่ชัด ควรช่วยให้โฟกัส'],
  'p':['ช่วยตั้งโจทย์ให้เป็นรูปธรรม 1 ชิ้น','เตรียมเครื่องล่วงหน้า','core track ต่อยอดสู่ prototype']},
 'เมย์':{'v':'ต้องการการสนับสนุนเพิ่ม — ยังไม่ค่อยมั่นใจในการใช้ AI + มีข้อกังวลหลายด้าน เหมาะกับการเรียนแบบประกบใกล้ชิด',
  's':['เคยใช้ ChatGPT/Gemini มาบ้าง'],
  'r':['ความมั่นใจในการใช้ AI ยังไม่สูง (2/5)','กังวล 3 เรื่อง: เรียนไม่ทัน · ภาษาอังกฤษ · command line','สิทธิ์ติดตั้งไม่แน่ใจ'],
  'p':['จับคู่ buddy ประกบ','เดินช้า มีจุดพัก','เตรียมเครื่อง + cheat sheet ก่อนวันงาน']},
 'ขิม':{'v':'ต้องการการสนับสนุนใกล้ชิด — มีข้อกังวลหลายด้าน (4 เรื่อง) + ต้องให้ IT ติดตั้ง',
  's':['ใช้ ChatGPT/Gemini + โปรแกรม office หลายตัว'],
  'r':['ความมั่นใจในการใช้ AI ยังไม่สูง (2/5)','มีข้อกังวลหลายด้าน (4 เรื่อง) รวมกลัวข้อมูลรั่วไหล','ต้องให้ IT ติดตั้งโปรแกรม (logistics)'],
  'p':['ประสาน IT ติดตั้งเครื่องล่วงหน้า','อธิบาย data policy เพื่อลดกังวลข้อมูลรั่ว','buddy ประกบ + เดินช้า']},
 'มอส':{'v':'เป็นผู้เริ่มต้นที่สุดในกลุ่ม — ยังอยู่ระดับเริ่มต้นในทุกด้าน และเป็นคนเดียวที่ยังไม่เคยใช้ AI มาก่อน เหมาะกับการเรียนแบบประกบใกล้ชิด 1:1',
  's':['มีความตั้งใจ (เลือกว่าอยากทำเว็บ/เชื่อม AI กับข้อมูลได้)'],
  'r':['ความคล่องคอมพิวเตอร์และความมั่นใจในการใช้ AI ยังอยู่ระดับเริ่มต้น (1/5)','ยังไม่เคยใช้ AI มาก่อน','ต้องให้ IT ติดตั้งโปรแกรม'],
 'p':['เรียนแบบประกบใกล้ชิด 1:1 โดยเริ่มจากพื้นฐาน','เริ่มจากใช้ AI แชทพื้นฐานก่อน ค่อยเป็นค่อยไป ไม่ต้องเร่งถึงขั้น deploy','เตรียมเครื่องผ่าน IT']},
 'เบนซ์':{'v':'พร้อมที่สุดในกลุ่มทั้งหมด — ใช้ Claude เป็นประจำอยู่แล้ว เขียนโปรแกรมได้ เป็นหัวหน้างานสายเทคนิค เหมาะเป็นแกนนำ/พี่เลี้ยงหลัก',
  's':['ใช้ Claude เป็นประจำ + มีบัญชี GitHub/Vercel/Claude พร้อม','เขียนโปรแกรม/ทำเว็บได้ · เคยใช้ Terminal + SQL','ความคล่องคอม 5/5 + ติดตั้งเองได้ · เป็นหัวหน้างาน'],
  'r':['มีพื้นฐานสูงกว่าค่าเฉลี่ยของกลุ่มมาก — ต้องมีโจทย์ท้าทายพอ เพื่อใช้ศักยภาพได้เต็มที่'],
  'p':['Advanced track เต็มรูปแบบ + เป็น co-trainer/พี่เลี้ยงหลัก','ช่วยออกแบบ internal tool ของบริษัทต่อจริง','ดึงเป็นแกนขับเคลื่อนการใช้ AI ในทีมหลังอบรม']},
 'เจ':{'v':'สาย creative (กราฟิก) พื้นฐานพอมี — คล้ายกลุ่มกลาง ต้องเคลียร์เครื่อง + ความกังวล',
  's':['เคยเห็น HTML/CSS','งานกราฟิกตรงกับ use case คอนเทนต์/ภาพ'],
  'r':['ยังไม่มีบัญชีเครื่องมือเลย · ติดตั้งไม่แน่ใจ','กังวล 2 เรื่อง (ข้อมูลรั่ว + เรียนไม่ทัน)'],
  'p':['core track เน้น content + ภาพ','เตรียมเครื่อง + เปิดบัญชีล่วงหน้า','อธิบาย data policy เพื่อลดกังวลข้อมูลรั่ว']},
 'โดนัท':{'v':'ต้องการการสนับสนุนเพิ่ม — ความสบายใจกับเครื่องมือเทคนิคยังอยู่ระดับเริ่มต้น (1/5) ไม่เคยเขียนโค้ด ตั้งเป้าพอประมาณ',
  's':['ใช้ ChatGPT/Gemini มาบ้าง','เป้าหมายชัด: อยากใช้ AI ช่วยงานประจำให้คล่อง'],
  'r':['ความสบายใจกับเครื่องมือเทคนิคยังอยู่ระดับเริ่มต้น (1/5)','ไม่เคยเขียนโค้ด · ยังไม่มีบัญชี · ติดตั้งไม่แน่ใจ','กังวลภาษาอังกฤษ'],
  'p':['core track เริ่มจากใช้ AI พื้นฐาน','ประกบใกล้ + cheat sheet อังกฤษ','เตรียมเครื่องล่วงหน้า']},
}

RANK=[
 ('top','1','เบนซ์','· ใช้ Claude ประจำ · เขียนโปรแกรมได้ · หัวหน้างาน','g',95),
 ('top','2','ต่อ','· เขียนเว็บได้ · สามารถติดตั้งเอง · ไม่กังวล','g',88),
 ('top','3','นัท','· มีความมั่นใจในการใช้ AI สูง · เคยใช้ SQL','g',80),
 ('','4','ฟ้า','· ออกแบบตรงตาม use case · สามารถติดตั้งเอง','',60),
 ('','5','อาร์ม','· เคยเห็น HTML · ทดลองใช้งาน Claude','',57),
 ('','6','แม็ก','· เคยเห็น HTML · ยังไม่ชัดเจนว่าเป้าหมายคืออะไร','',55),
 ('','7','เจ','· กราฟิก · เคยเห็น HTML · ยังไม่มีบัญชี','',52),
 ('','8','เมย์','· มีความมั่นใจในการใช้ AI ยังไม่สูง · มีข้อกังวล 3 เรื่อง','w',40),
 ('','9','โดนัท','· เริ่มต้นกับเครื่องมือเทคนิค · กังวลภาษาอังกฤษ','w',38),
 ('','10','ขิม','· มีข้อกังวลหลายด้าน (4 เรื่อง) · ต้องให้ IT ช่วยติดตั้ง','w',30),
 ('crit','11','มอส','· อยู่ในระดับเป็นผู้เริ่มต้นในทุกด้าน · ไม่เคยใช้ AI','r',15),
]

# accordion groups: (title, [qdata indices])
GROUPS=[
 ('ข้อมูลทั่วไป & พื้นฐาน',[0,1,2,3]),
 ('ทักษะ & เครื่องมือ',[6,7,15,16]),
 ('ประสบการณ์ใช้ AI',[5,4,8]),
 ('งานจริง & สิ่งที่อยากให้ AI ช่วย',[9,10,11,12]),
 ('ข้อกังวล & อื่นๆ',[13,14]),
]

HIGHLIGHTS=[
 'งานที่อยากให้ AI ช่วยอันดับ 1 คือ <b>สร้างภาพประกอบ (11/11 = 100%)</b> รองมาคือคอนเทนต์โซเชียลและทำเว็บ',
 '<b>มีเพียง 1 คนใช้ Claude เป็นประจำ (เบนซ์)</b> — อีก 10 คนต้อง onboard ตั้งแต่เริ่มต้น',
 '<b>6 ใน 11 ไม่เคยเขียนโค้ด</b> — หัวข้อทำเว็บควรใช้แนว no-code เป็นหลัก',
 '<b>7 ใน 11 กังวลว่าจะเรียนไม่ทัน</b> — ต้องเดินช้า มีจุดพัก และจับคู่ buddy',
 '<b>9 ใน 11 เป็นสายการตลาด</b> — โฟกัส use case การตลาด (คอนเทนต์/ภาพ/landing page)',
 'ติดตั้งโปรแกรมเองได้เพียง <b>4/11</b> — อีก 7 คนต้องเตรียมเครื่องล่วงหน้า',
]

def chart_h(q):
    if q['type']=='pie': return 250
    if q['type']=='scale': return 230
    return max(170,len(q['labels'])*30+46)

def qcard(i):
    q=QDATA[i]
    ans=f"จำนวนคำตอบ {q['answered']} ข้อ"
    return (f'<div class="qcard"><div class="qhead"><h3>{P(q["title"])}</h3>'
            f'<span class="qn">{ans}</span></div>'
            f'<div class="qchart" style="height:{chart_h(q)}px"><canvas id="q{i}"></canvas></div></div>')

acc_html=[]
for gi,(title,idxs) in enumerate(GROUPS):
    cards="\n          ".join(qcard(i) for i in idxs)
    acc_html.append(f'''      <div class="acc" data-qs="{json.dumps(idxs)}">
        <button class="acc-head" type="button">
          <span class="t">{title}</span><span class="c">{len(idxs)} คำถาม</span><span class="chev">▾</span>
        </button>
        <div class="acc-body"><div class="acc-grid">
          {cards}
        </div></div>
      </div>''')
acc_html="\n".join(acc_html)
insight_acc = '      <div class="acc" data-qs="[]">\n        <button class="acc-head" type="button"><span class="t">ภาพรวมกลุ่มผู้เรียน</span><span class="c">5 ข้อ</span><span class="chev">▾</span></button>\n        <div class="acc-body"><ul class="hi">\n          <li>ผู้เรียน 11 คน — สายการตลาด <b>9 คน</b> + สายช่าง/เทคนิค <b>2 คน</b></li>\n          <li>ระดับความพร้อมหลากหลาย: พร้อมสูง <b>3 คน</b> · ปานกลาง <b>4 คน</b> · ต้องการการสนับสนุน <b>4 คน</b></li>\n          <li>มีคนพร้อมเป็นพี่เลี้ยง 3 คน (<b>เบนซ์ · ต่อ · นัท</b>) — ใช้ระบบ buddy ได้</li>\n          <li>เบนซ์ใช้ Claude เป็นประจำ + เขียนโปรแกรมได้ เหมาะเป็นแกนหลักของทีม</li>\n          <li>ความคล่องคอมพิวเตอร์เฉลี่ย <b>3.0/5</b> · ความมั่นใจในการใช้ AI เฉลี่ย <b>2.7/5</b></li>\n        </ul></div>\n      </div>\n      <div class="acc" data-qs="[]">\n        <button class="acc-head" type="button"><span class="t">ความพร้อมด้านเทคนิค</span><span class="c">5 ข้อ</span><span class="chev">▾</span></button>\n        <div class="acc-body"><ul class="hi">\n          <li><b>6 ใน 11</b> ไม่เคยเขียนโค้ด · 3 คนเคยเห็น HTML/CSS · 2 คนเขียนโปรแกรมได้</li>\n          <li>ติดตั้งโปรแกรมเองได้ <b>4/11</b> — อีก 7 คนต้องให้ IT ช่วยหรือยังไม่แน่ใจ</li>\n          <li><b>10 ใน 11</b> ยังไม่มีบัญชี cloud (GitHub/Vercel ฯลฯ) — ต้องเปิดล่วงหน้า</li>\n          <li>ส่วนใหญ่ยังไม่เคยใช้เครื่องมือสายเทคนิค (Git · Terminal · SQL)</li>\n          <li>เครื่องที่ใช้: Windows <b>7</b> · macOS <b>4</b> — เตรียมคู่มือติดตั้งทั้ง 2 ระบบ</li>\n        </ul></div>\n      </div>\n      <div class="acc" data-qs="[]">\n        <button class="acc-head" type="button"><span class="t">ความต้องการ & งานจริง</span><span class="c">5 ข้อ</span><span class="chev">▾</span></button>\n        <div class="acc-body"><ul class="hi">\n          <li>งานที่อยากให้ AI ช่วยสูงสุด: <b>สร้างภาพประกอบ (11/11 = 100%)</b> · คอนเทนต์โซเชียล (9) · ทำเว็บ/landing page (8) · ค้นหาข้อมูล (7)</li>\n          <li>งานประจำที่ใช้เวลามากสุด: คอนเทนต์โซเชียล (8) · ทำรายงาน/สรุปข้อมูล (7) · ค้นหาข้อมูล (5)</li>\n          <li>โปรแกรมที่ใช้ประจำ: <b>Facebook/Instagram (10)</b> · Photoshop/Canva (7) · Office (6) — สาย marketing/creative ชัดเจน</li>\n          <li>เป้าหลังอบรม: ใช้ AI คล่อง (9) · prompt ใช้ซ้ำ (8) · ทำหน้าเว็บ/landing page เองได้ (7) · internal tool (6)</li>\n          <li>เคยใช้ AI ช่วยงาน สรุป/ค้นหา/สร้างภาพ ในระดับสูง — มีพื้นฐานการใช้ AI ทั่วไปอยู่บ้าง</li>\n        </ul></div>\n      </div>\n      <div class="acc" data-qs="[]">\n        <button class="acc-head" type="button"><span class="t">ความกังวล & สิ่งที่ต้องเตรียม</span><span class="c">5 ข้อ</span><span class="chev">▾</span></button>\n        <div class="acc-body"><ul class="hi">\n          <li><b>7 ใน 11</b> กังวลว่าจะเรียนไม่ทัน — เดินช้า มีจุดพัก จับคู่ buddy</li>\n          <li><b>5 ใน 11</b> กังวลภาษาอังกฤษ — แจก cheat sheet ศัพท์/error + สอนให้ AI ช่วยแปล</li>\n          <li>3 คนยังไม่เคยใช้ command line · 3 คนกังวลเรื่องความปลอดภัยข้อมูล — อธิบาย data policy ให้ชัด</li>\n          <li>ยังไม่มีใครใช้ Claude เป็นประจำ (ยกเว้นเบนซ์) — ต้องปูพื้น Claude ตั้งแต่เริ่มต้น</li>\n          <li><b>7 ใน 11</b> ต้องเตรียมเครื่อง/บัญชีล่วงหน้า (ประสานทีม IT)</li>\n        </ul></div>\n      </div>\n      <div class="acc" data-qs="[]">\n        <button class="acc-head" type="button"><span class="t">ข้อเสนอเชิงปฏิบัติ</span><span class="c">6 ข้อ</span><span class="chev">▾</span></button>\n        <div class="acc-body"><ul class="hi">\n          <li><b>แบ่ง tiered:</b> Core (ทุกคน) = Claude + คอนเทนต์ + landing page no-code · Advanced (เบนซ์/ต่อ/นัท) = deploy + ฐานข้อมูล</li>\n          <li><b>เน้น use case การตลาด</b> เป็นแกน (คอนเทนต์/ภาพ/landing page) — ตรงกับงานจริงของ 9 ใน 11 คน</li>\n          <li><b>ลดฐานข้อมูล + GitHub</b> เป็น "เข้าใจภาพรวม + ดู demo" สำหรับคนส่วนใหญ่</li>\n          <li><b>เตรียมก่อนวันงาน:</b> ติดตั้ง + เปิดบัญชี Claude/เครื่องมือ + cheat sheet ศัพท์อังกฤษ</li>\n          <li><b>buddy:</b> เบนซ์/ต่อ/นัท ประกบเพื่อนที่ยังเริ่มต้น · เรียนแบบประกบใกล้ชิด เมย์/ขิม/โดนัท/มอส</li>\n          <li><b>1 วันอาจไม่พอ</b>สำหรับ deploy + ฐานข้อมูลทุกคน → เพิ่ม clinic ครึ่งวัน follow-up</li>\n        </ul></div>\n      </div>'

rank_html="\n".join(
 f'          <div class="rrow" data-key="{nick}"><span class="rk {rk}">{num}</span>'
 f'<span class="rnm">{nick} <em>{desc}</em></span>'
 f'<span class="rbar"><i class="{bar}" style="width:{fit}%"></i></span>'
 f'<span class="rpct">{fit}</span></div>'
 for rk,num,nick,desc,bar,fit in RANK)

hi_html="\n".join(f'          <li>{x}</li>' for x in HIGHLIGHTS)
align_html = '\n    <div class="vbanner">\n      <span class="b">สอดคล้องบางส่วน — เป้าหมายตรงกัน แต่ความพร้อมยังห่างจากที่คาดหวัง</span>\n      <p>เจ้าของและผู้เรียน <b>เห็นตรงกันเรื่องเป้าหมาย</b> (ใช้ AI ในงาน · การตลาด · อยากทำเว็บได้เอง) แต่ระดับ <b>“ทำเองได้จริงทุกหัวข้อใน 1 วัน”</b> ยังห่างจากความพร้อมจริง โดยเฉพาะ <b>ฐานข้อมูล</b> และ <b>GitHub</b></p>\n    </div>\n    <div class="card" style="margin-bottom:16px">\n      <h3>ความคาดหวังของเจ้าของ เทียบ ความพร้อมจริงของผู้เรียน (0–3)</h3>\n      <div class="r2wrap"><canvas id="cRadar2"></canvas></div>\n      <p class="rhint" style="margin:10px 2px 0">ยิ่งเส้นสองเส้นห่างกัน = ช่องว่างที่ต้องปิดมากขึ้น — เห็นชัดที่ฐานข้อมูล / GitHub</p>\n    </div>\n    <table class="cmp">\n      <thead><tr><th>หัวข้อ</th><th>เจ้าของคาดหวัง</th><th>ความพร้อมจริงของผู้เรียน</th><th>ความสอดคล้อง</th></tr></thead>\n      <tbody>\n        <tr><td class="dim">ใช้ AI ในงานประจำ</td><td>ทีมใช้ AI ได้คล่อง</td><td>อยากได้มากที่สุด — สร้างภาพ 11/11 · คอนเทนต์ 9/11 <span class="sm">ตรงกับเป้า</span></td><td><span class="atag ok">สอดคล้องสูง</span></td></tr>\n        <tr><td class="dim">โฟกัสการตลาด</td><td>เพิ่ม AI กับการตลาด</td><td>9 ใน 11 เป็นสายการตลาด <span class="sm">use case ตรงกลุ่ม</span></td><td><span class="atag ok">สอดคล้องสูง</span></td></tr>\n        <tr><td class="dim">ทำเว็บ / landing page</td><td>deploy ขึ้น production เองได้</td><td>6/11 อยากทำได้ · 6/11 ยังไม่เคยเขียนโค้ด <span class="sm">ตรงเป้า แต่ทักษะยังไม่ถึง</span></td><td><span class="atag warn">ใช้แนว no-code</span></td></tr>\n        <tr><td class="dim">เครื่องมือ Claude</td><td>ใช้ Claude เป็นหลัก</td><td>มี 1 คนใช้ประจำ (เบนซ์) ที่เหลือยังไม่เคยใช้ <span class="sm">ต้อง onboard ตั้งแต่ต้น</span></td><td><span class="atag warn">ต้องปูพื้นก่อน</span></td></tr>\n        <tr><td class="dim">การติดตั้งโปรแกรม</td><td>ผู้เรียนติดตั้งเองได้</td><td>4/11 ติดตั้งเองได้ · อีก 7 คนต้องเตรียม <span class="sm">ปัญหา logistics</span></td><td><span class="atag warn">เตรียมก่อนวันงาน</span></td></tr>\n        <tr><td class="dim">ระดับ “ทำเองได้จริง” ทุกหัวข้อ</td><td>คาดหวังระดับสูงสุดทุกหัวข้อ</td><td>ส่วนใหญ่เป็นผู้เริ่มต้น <span class="sm">ความคาดหวังสูงกว่าความพร้อมปัจจุบัน</span></td><td><span class="atag risk">ช่องว่างสำคัญ</span></td></tr>\n        <tr><td class="dim">ฐานข้อมูล (Supabase ฯลฯ)</td><td>ใช้ฐานข้อมูลในงานได้</td><td>ไม่ใช่ความต้องการหลักของผู้เรียน · ความพร้อม ~0.9/3 <span class="sm">owner-push</span></td><td><span class="atag risk">ช่องว่างใหญ่</span></td></tr>\n        <tr><td class="dim">GitHub</td><td>อยากให้เรียนรู้</td><td>ไม่มีผู้เรียนระบุว่าต้องการ · ความพร้อม ~0.8/3</td><td><span class="atag risk">ช่องว่างใหญ่</span></td></tr>\n        <tr><td class="dim">เวลา 1 วัน เทียบขอบเขต</td><td>4+ หัวข้อ ภายใน 1 วัน</td><td>กลุ่มผู้เริ่มต้นต้องใช้จังหวะช้าลง <span class="sm">เนื้อหาแน่นเกินเวลา</span></td><td><span class="atag risk">เสี่ยงทำไม่ครบ</span></td></tr>\n      </tbody>\n    </table>\n    <div class="alegend">\n      <span><i style="background:#1a9e57"></i> สอดคล้อง — เดินหน้าได้</span>\n      <span><i style="background:#b5790a"></i> ต้องปรับวิธี / เตรียมก่อน</span>\n      <span><i style="background:#cc342b"></i> ต้องตัดสินใจเรื่องขอบเขต</span>\n    </div>\n    <div class="ownwhy" style="margin-top:16px"><b>ข้อเสนอเพื่อปิดช่องว่าง:</b> แบ่งหลักสูตรแบบ tiered (Core ทุกคน + Advanced สำหรับคนพร้อม) · เน้น use case การตลาด · ลดฐานข้อมูล/GitHub เป็น “เข้าใจภาพรวม + ดู demo” · เตรียมเครื่อง/บัญชีก่อนวันงาน · เพิ่ม clinic ครึ่งวัน follow-up เพื่อให้ตัวชี้วัด 3 เดือนเป็นจริง</div>'
owner_html = '\n    <div class="ometa">\n      <span class="pill">บริษัท <b>ขอนแก่นอิเล็คทริค</b></span>\n      <span class="pill">ผู้ตอบ <b>Ketthip · CEO</b></span>\n      <span class="pill">ธุรกิจ <b>ระบบไฟ · โซลาร์เซลล์</b></span>\n      <span class="pill">งบ <b>฿30,000–50,000</b> · <b>1 วัน</b></span>\n    </div>\n    <section class="s">\n      <div class="sh"><div class="no">★</div><h2>ระดับผลลัพธ์ที่คาดหวัง</h2></div>\n      <p class="lead">เจ้าของคาดหวังให้พนักงาน <b>“ทำเองได้จริง” (ระดับสูงสุด)</b> ในทุกหัวข้อ — ไม่ใช่แค่เข้าใจภาพรวม</p>\n      <div class="exp">\n        <div class="exprow"><span class="t">พื้นฐาน Claude</span><span class="ebar"><i style="width:100%"></i></span><span class="etag">ทำเองได้จริง</span></div>\n        <div class="exprow"><span class="t">ทำเว็บขึ้น production</span><span class="ebar"><i style="width:100%"></i></span><span class="etag">ทำเองได้จริง</span></div>\n        <div class="exprow"><span class="t">ฐานข้อมูล</span><span class="ebar"><i style="width:100%"></i></span><span class="etag">ทำเองได้จริง</span></div>\n        <div class="exprow"><span class="t">GitHub</span><span class="ebar"><i style="width:100%"></i></span><span class="etag">ทำเองได้จริง</span></div>\n      </div>\n      <div class="scalenote">มาตรวัด: เข้าใจภาพรวม → ทำตามขั้นตอนได้ → <b>ทำเองได้จริง</b> (สูงสุด) · เน้นทุกหัวข้อเท่ากัน</div>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">1</div><h2>ทำไมจัดอบรมตอนนี้</h2></div>\n      <ul class="o"><li>คู่แข่ง / ตลาดเริ่มใช้ AI แล้ว</li><li>อยากให้ทีมเรียนรู้สิ่งใหม่ ทันยุค</li><li>มีโปรเจกต์ / ระบบใหม่ที่จะใช้ AI</li></ul>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">2</div><h2>เป้าหมายหลังอบรม</h2></div>\n      <ul class="o"><li>ทีมใช้ AI ในงานประจำได้คล่อง</li><li>มี internal tool ใช้จริงอย่างน้อย 1 ตัว</li><li>มีคน deploy เว็บไซต์เองได้</li><li>ใช้ฐานข้อมูลในงานได้</li><li>มี dashboard / automation ใหม่</li></ul>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">3</div><h2>ตัวชี้วัดความสำเร็จ <span class="star">(วัดที่ 3 เดือน)</span></h2></div>\n      <ul class="o metric"><li>มี internal tool ใช้จริงอย่างน้อย <b>1 ตัว</b></li><li>พนักงาน <b>5 คนขึ้นไป</b> ใช้ AI ในงานประจำ</li><li>มี prototype อย่างน้อย <b>1 ตัวขึ้น production</b></li><li>มีคนในทีม <b>deploy เว็บเองได้</b></li></ul>\n      <div class="ownwhy"><b>หมายเหตุ:</b> ตัวชี้วัดเหล่านี้คือสิ่งที่เจ้าของใช้ตัดสินว่า “คุ้มค่า” — ควรผูกผลงานจากคลาสเข้ากับเป้าหมายเหล่านี้</div>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">4</div><h2>หัวข้อที่ต้องการให้เรียน</h2></div>\n      <div class="ochips"><span class="c">พื้นฐาน Claude</span><span class="c">ทำเว็บไซต์ขึ้น production (GitHub · Vercel · Netlify)</span><span class="c">ฐานข้อมูล (Supabase · Firebase · MongoDB)</span><span class="c">ใช้ AI ร่วมกับงานการตลาด</span></div>\n      <div class="ownwhy" style="margin-top:14px"><b>เน้นเป็นพิเศษ:</b> ทุกหัวข้อเท่ากัน (ไม่ได้ให้น้ำหนักหัวข้อใดมากกว่า)</div>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">5</div><h2>ผลงานที่อยากให้พนักงานทำได้</h2></div>\n      <ul class="o"><li>เว็บบริษัท / landing page</li><li>ระบบภายใน (internal tool)</li><li>Dashboard ดูข้อมูล</li></ul>\n    </section>\n    <section class="s">\n      <div class="sh"><div class="no">6</div><h2>กรอบการจัด &amp; งบประมาณ</h2></div>\n      <div class="kv"><div class="k">เหตุผลที่เลือกผู้เรียน</div><div>คนที่จะใช้ / ต่อยอดได้จริง</div><div class="k">ใครออกค่าเครื่องมือ</div><div>บริษัทออกให้ทั้งหมด</div><div class="k">งบประมาณ</div><div>฿30,000–50,000 (งบรวม)</div><div class="k">จำนวนวัน</div><div>1 วัน</div><div class="k">สิทธิ์ติดตั้งโปรแกรม</div><div>ผู้เรียนติดตั้งเองได้ (admin)</div></div>\n    </section>'

CSS='''
  :root{--bg:#f5f5f7;--card:#fff;--ink:#1d1d1f;--muted:#6e6e73;--line:#e5e5ea;--accent:#5b62e6;--accent2:#3257d6;--ok:#1a9e57;--warn:#b5790a;--risk:#cc342b;--track:#ececf0;--shadow:0 1px 2px rgba(0,0,0,.04),0 6px 20px rgba(0,0,0,.05)}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans","IBM Plex Sans Thai",-apple-system,BlinkMacSystemFont,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;font-kerning:normal;line-height:1.5}
  .wrap{max-width:1200px;margin:0 auto;padding:0 22px 70px}
  .hero-band{background:linear-gradient(160deg,#1f2e6b 0%,#2f49b8 60%,#3c5bd6 100%);color:#fff}
  .hero-inner{max-width:1200px;margin:0 auto;padding:44px 22px 26px}
  .eyebrow{display:inline-block;font-size:11.5px;font-weight:600;letter-spacing:1.3px;text-transform:uppercase;color:#dfe5fb;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:6px 13px}
  h1{font-size:clamp(26px,3.4vw,34px);font-weight:600;letter-spacing:-.5px;line-height:1.18;margin:16px 0 8px;color:#fff}
  .sub{color:#d7ddf6;font-size:15.5px;line-height:1.55;margin:0;max-width:760px}
  .kpi{display:grid;grid-template-columns:repeat(6,1fr);gap:13px;margin:26px 0 0}
  @media(max-width:880px){.kpi{grid-template-columns:repeat(3,1fr)}}
  .k{background:#fff;border:1px solid var(--line);border-radius:16px;padding:15px 17px 14px;box-shadow:0 1px 2px rgba(16,24,40,.04),0 6px 16px rgba(16,24,40,.05);display:flex;flex-direction:column;min-height:106px;position:relative;overflow:hidden;transition:transform .13s,box-shadow .13s}
  .k:hover{transform:translateY(-2px);box-shadow:0 4px 10px rgba(16,24,40,.06),0 14px 30px rgba(16,24,40,.09)}
  .k::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--accent2)}
  .k.acc-blue::before{background:#3257d6} .k.acc-amber::before{background:#b5790a} .k.acc-red::before{background:#cc342b} .k.acc-green::before{background:#1a9e57}
  .k .n{font-size:30px;font-weight:600;letter-spacing:-.7px;font-feature-settings:"tnum" 1;line-height:1.04}
  .k .n.r{color:var(--risk)} .k .n.w{color:var(--warn)} .k .n.a{color:var(--accent2)} .k .n.g{color:var(--ok)}
  .k .l{font-size:11.5px;color:var(--muted);margin-top:auto;padding-top:9px;line-height:1.35}
  section{margin-top:28px}
  .sec-head{display:flex;align-items:baseline;gap:10px;margin-bottom:14px;flex-wrap:wrap}
  .sec-head h2{font-size:20px;font-weight:600;margin:0;letter-spacing:-.2px}
  .sec-head .n{font-size:12px;font-weight:600;color:var(--accent2);background:#eef1fc;border-radius:8px;padding:3px 9px}
  .sec-head .tools{margin-left:auto;display:flex;gap:8px}
  .tbtn{font-family:inherit;font-size:12.5px;font-weight:500;color:var(--accent2);background:#eef1fc;border:0;border-radius:8px;padding:6px 12px;cursor:pointer}
  .tbtn:hover{background:#e3e8fb}
  .two{display:grid;grid-template-columns:1.05fr 1fr;gap:16px}
  .two > .card{display:flex;flex-direction:column}
  @media(max-width:880px){.two{grid-template-columns:1fr}}
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow);min-width:0}
  .card h3{margin:0 0 12px;font-size:13px;font-weight:600;color:var(--muted)}
  .rhint{font-size:11.5px;color:#a9a9b2;margin:2px 2px 12px}
  .rank{display:flex;flex-direction:column;gap:11px}
  .rrow{display:grid;grid-template-columns:26px 1fr 92px 32px;align-items:center;gap:10px;cursor:pointer;border-radius:8px;padding:3px 6px;margin:0 -6px;transition:background .12s}
  .rrow:hover{background:#f3f4f9}
  .rk{width:26px;height:26px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;background:#eef1fc;color:var(--accent2);font-feature-settings:"tnum" 1}
  .rk.top{background:#e6f6ec;color:var(--ok)} .rk.crit{background:#fdeceb;color:var(--risk)}
  .rnm{font-size:13px;font-weight:600;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .rnm em{font-style:normal;font-weight:400;color:var(--muted);font-size:11.5px}
  .rbar{height:7px;background:var(--track);border-radius:999px;overflow:hidden}
  .rbar i{display:block;height:100%;border-radius:999px;background:var(--accent2)}
  .rbar i.g{background:var(--ok)} .rbar i.w{background:var(--warn)} .rbar i.r{background:var(--risk)}
  .rpct{font-size:12px;font-weight:600;color:var(--muted);text-align:right;font-feature-settings:"tnum" 1}
  .exwrap{position:relative;flex:1 1 auto;min-height:340px}
  .exwrap canvas{position:absolute;inset:0;width:100%!important;height:100%!important}
  .hi{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:9px 20px}
  @media(max-width:880px){.hi{grid-template-columns:1fr}}
  .hi li{position:relative;padding-left:18px;font-size:13.5px;line-height:1.5;color:#3a3a40}
  .hi li::before{content:"";position:absolute;left:2px;top:8px;width:7px;height:7px;border-radius:2px;background:var(--accent2)}
  .hi li b{font-weight:600;color:var(--ink)}
  /* accordion */
  .acc{border:1px solid var(--line);border-radius:14px;background:#fff;box-shadow:var(--shadow);margin-bottom:14px;overflow:hidden}
  .acc-head{display:flex;align-items:center;gap:10px;width:100%;border:0;background:#fff;cursor:pointer;padding:16px 20px;font-family:inherit;text-align:left}
  .acc-head:hover{background:#fafafc}
  .acc-head .t{font-size:15.5px;font-weight:600;color:var(--ink)}
  .acc-head .c{font-size:12px;color:var(--muted);background:#f0f1f5;border-radius:8px;padding:2px 8px}
  .acc-head .chev{margin-left:auto;color:var(--muted);transition:transform .2s;font-size:14px}
  .acc.open .acc-head .chev{transform:rotate(180deg)}
  .acc-body{display:none;padding:4px 18px 18px}
  .acc.open .acc-body{display:block}
  .acc-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
  @media(max-width:880px){.acc-grid{grid-template-columns:1fr}}
  .qcard{border:1px solid var(--line);border-radius:14px;padding:14px 16px;min-width:0;background:#fff}
  .qhead{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:10px}
  .qhead h3{margin:0;font-size:14px;font-weight:600;line-height:1.35}
  .qhead .qn{font-size:11.5px;color:var(--muted);white-space:nowrap;flex:0 0 auto}
  .qchart{position:relative;min-width:0}
  .qchart canvas{position:absolute;inset:0;width:100%!important;height:100%!important}
  .subgroup-label{font-size:13px;font-weight:600;color:var(--muted);margin:20px 2px 11px}
  footer{margin-top:36px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
  /* modal */
  .pm-ov{position:fixed;inset:0;background:rgba(22,22,28,.46);display:none;align-items:center;justify-content:center;z-index:60;padding:20px}
  .pm-ov.open{display:flex}
  .pm{background:#fff;border-radius:18px;max-width:680px;width:100%;max-height:88vh;display:flex;flex-direction:column;box-shadow:0 24px 64px rgba(0,0,0,.28);overflow:hidden}
  .pm-head{display:flex;align-items:center;gap:14px;padding:20px 22px;border-bottom:1px solid var(--line);flex:0 0 auto}
  .pm-ava{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;font-weight:600;flex:0 0 auto}
  .pm-id{flex:1;min-width:0}
  .pm-id h3{margin:0;font-size:18px;font-weight:600;letter-spacing:-.2px}
  .pm-id .meta{font-size:13px;color:var(--muted);margin-top:2px}
  .pm-fit{font-size:13px;font-weight:700;padding:5px 12px;border-radius:999px;white-space:nowrap;flex:0 0 auto}
  .pm-x{flex:0 0 auto;width:32px;height:32px;border-radius:9px;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:17px;color:var(--muted);line-height:1}
  .pm-body{padding:6px 22px 22px;overflow:auto}
  .pm-an{background:#f6f8fc;border:1px solid #e7ebf7;border-radius:13px;padding:15px 17px;margin:14px 0 4px}
  .pm-an .v{font-size:14.5px;font-weight:600;color:var(--ink);line-height:1.5}
  .pm-an .grp{margin-top:11px}
  .pm-an .lab{font-size:11px;font-weight:700;letter-spacing:.5px;margin-bottom:4px}
  .pm-an .lab.s{color:#1a9e57} .pm-an .lab.r{color:#cc342b} .pm-an .lab.p{color:#3257d6}
  .pm-an ul{margin:0;padding-left:17px}
  .pm-an li{font-size:13px;line-height:1.55;color:#3a3a40;margin:1px 0}
  .pm-row{padding:12px 0;border-top:1px solid var(--line)}
  .pm-q{font-size:12px;color:var(--muted);margin-bottom:6px}
  .pm-a{font-size:14px;color:var(--ink);font-weight:500}
  .pm-chips{display:flex;flex-wrap:wrap;gap:6px}
  .pm-chip{background:#eef1fc;color:#3257d6;font-size:12.5px;font-weight:500;padding:4px 10px;border-radius:8px}
  /* tabs */
  .tabbar{display:flex;gap:8px;margin-top:24px;flex-wrap:wrap}
  .tabbtn{font-family:inherit;font-size:14px;font-weight:600;color:#dfe5fb;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:9px 20px;cursor:pointer;transition:all .12s}
  .tabbtn:hover{background:rgba(255,255,255,.18)}
  .tabbtn.active{background:#fff;color:#2f49b8;border-color:#fff}
  .tab{display:none}
  .tab.active{display:block}
  .ometa{display:flex;flex-wrap:wrap;gap:9px;margin:22px 0 2px}
  .ometa .pill{background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 13px;font-size:12.5px;color:var(--muted);box-shadow:var(--shadow)}
  .ometa .pill b{color:var(--ink);font-weight:600}
  /* owner sections */
  section.s{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 26px;box-shadow:var(--shadow);margin-top:16px}
  .sh{display:flex;align-items:baseline;gap:12px;margin:0 0 14px}
  .sh .no{flex:0 0 auto;font-size:13px;font-weight:700;color:#3257d6;background:#eef1fc;border-radius:9px;width:30px;height:26px;display:flex;align-items:center;justify-content:center;font-feature-settings:"tnum" 1}
  .sh h2{font-size:19px;font-weight:600;margin:0;letter-spacing:-.2px}
  .sh .star{color:#3257d6}
  p.lead{margin:0 0 12px;font-size:15px}
  ul.o{list-style:none;margin:0;padding:0}
  ul.o>li{position:relative;padding:8px 0 8px 22px;font-size:15px;line-height:1.55;border-top:1px solid var(--line)}
  ul.o>li:first-child{border-top:0}
  ul.o>li::before{content:"";position:absolute;left:3px;top:16px;width:7px;height:7px;border-radius:2px;background:#3257d6}
  ul.o.metric>li::before{background:#1a9e57}
  .ownwhy{margin-top:8px;background:#f6f8fc;border-left:3px solid #3257d6;border-radius:0 8px 8px 0;padding:9px 13px;font-size:13px;color:#3a3a40}
  .ownwhy b{color:#3257d6}
  .exp{display:flex;flex-direction:column;gap:14px}
  .exprow{display:grid;grid-template-columns:170px 1fr auto;align-items:center;gap:14px}
  .exprow .t{font-size:14.5px;font-weight:600}
  .ebar{height:10px;background:#ececf2;border-radius:999px;overflow:hidden}
  .ebar i{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,#3257d6,#5b7bf0)}
  .etag{font-size:12px;font-weight:700;color:#3257d6;background:#eef1fc;border-radius:999px;padding:4px 11px;white-space:nowrap}
  .scalenote{margin-top:14px;font-size:12.5px;color:var(--muted);text-align:right}
  .ochips{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
  .ochips .c{font-size:13.5px;background:#eef1fc;color:#2f49b8;border-radius:9px;padding:7px 13px;font-weight:500}
  .kv{display:grid;grid-template-columns:auto 1fr;gap:8px 18px;font-size:14.5px}
  .kv .k{color:var(--muted)}
  @media(max-width:620px){.exprow{grid-template-columns:120px 1fr}.exprow .etag{grid-column:2}}
  /* alignment tab */
  .vbanner{background:var(--warn-soft);border:1px solid #f0e0bd;border-radius:14px;padding:18px 20px;margin-bottom:16px}
  .vbanner .b{display:inline-block;font-size:13px;font-weight:700;color:var(--warn);background:#fff;border:1px solid #f0e0bd;border-radius:999px;padding:5px 13px;margin-bottom:10px}
  .vbanner p{margin:0;font-size:15px;line-height:1.6}
  .r2wrap{position:relative;height:420px}
  .r2wrap canvas{position:absolute;inset:0;width:100%!important;height:100%!important}
  .cmp{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--shadow)}
  .cmp th,.cmp td{padding:14px 16px;text-align:left;vertical-align:top;font-size:14px;line-height:1.5;border-top:1px solid var(--line)}
  .cmp thead th{background:#fafafc;font-size:12px;font-weight:600;color:var(--muted);border-top:0}
  .cmp td.dim{font-weight:600;width:22%}
  .cmp td .sm{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
  .atag{display:inline-block;font-size:12px;font-weight:700;padding:5px 11px;border-radius:999px;white-space:nowrap}
  .atag.ok{background:var(--ok-soft);color:var(--ok)} .atag.warn{background:var(--warn-soft);color:var(--warn)} .atag.risk{background:#fdeceb;color:var(--risk)}
  .alegend{display:flex;gap:18px;flex-wrap:wrap;margin-top:12px}
  .alegend span{display:inline-flex;align-items:center;gap:7px;font-size:13px;color:var(--muted)}
  .alegend i{width:11px;height:11px;border-radius:3px;display:inline-block}
  @media(max-width:760px){.cmp,.cmp thead,.cmp tbody,.cmp tr,.cmp td{display:block}.cmp thead{display:none}.cmp tr{border-top:1px solid var(--line);padding:6px 0}.cmp td{border-top:0;padding:5px 16px}.cmp td.dim{padding-top:13px;font-size:15px}}
'''

JS='''
var QDATA = __QDATA__;
var PEOPLE = __PEOPLE__;
var ANALYSIS = __ANALYSIS__;
(function(){
  if(typeof Chart==='undefined') return;
  if(typeof ChartDataLabels!=='undefined') Chart.register(ChartDataLabels);
  Chart.defaults.font.family='IBM Plex Sans, IBM Plex Sans Thai, -apple-system, sans-serif';
  Chart.defaults.font.size=11; Chart.defaults.color='#6e6e73';
  var ACC='#5b62e6';
  var PAL=['#3257d6','#1a9e57','#b5790a','#cc342b','#7b61ff','#0aa2c0','#e8590c','#5b7bf0','#c7c7cc','#16a34a','#9333ea'];
  function pf(v,ans){ if(!ans) return ''; var p=Math.round(v/ans*1000)/10; return v+' ('+p+'%)'; }

  // radar (lazy — render when learner tab shown)
  var radarDone=false;
  function renderRadar(){ if(radarDone)return; var el=document.getElementById('cRadar'); if(!el)return; radarDone=true; new Chart(el,{type:'radar',
    data:{labels:['Claude','ทำเว็บ deploy','ฐานข้อมูล','GitHub','ใช้ AI ทั่วไป'],datasets:[{data:[1.6,1.5,0.9,0.8,2.1],borderColor:'#1a9e57',backgroundColor:'rgba(26,158,87,.16)',borderWidth:2,pointBackgroundColor:'#1a9e57',pointRadius:3}]},
    options:{maintainAspectRatio:false,scales:{r:{min:0,max:3,ticks:{stepSize:1,backdropColor:'transparent'},pointLabels:{font:{size:12,weight:'600'}}}},plugins:{legend:{display:false},datalabels:{display:false}}}}); }
  var radar2Done=false;
  function renderRadar2(){ if(radar2Done)return; var el=document.getElementById('cRadar2'); if(!el)return; radar2Done=true; new Chart(el,{type:'radar',
    data:{labels:['Claude','ทำเว็บ deploy','ฐานข้อมูล','GitHub','ใช้ AI ทั่วไป'],datasets:[
      {label:'เจ้าของคาดหวัง',data:[3,3,3,3,3],borderColor:'#3257d6',backgroundColor:'rgba(50,87,214,.12)',borderWidth:2,pointBackgroundColor:'#3257d6',pointRadius:3},
      {label:'ความพร้อมจริงของผู้เรียน',data:[1.6,1.5,0.9,0.8,2.1],borderColor:'#1a9e57',backgroundColor:'rgba(26,158,87,.14)',borderWidth:2,pointBackgroundColor:'#1a9e57',pointRadius:3}]},
    options:{maintainAspectRatio:false,scales:{r:{min:0,max:3,ticks:{stepSize:1,backdropColor:'transparent'},pointLabels:{font:{size:12,weight:'600'}}}},plugins:{legend:{position:'bottom',labels:{padding:14,usePointStyle:true,pointStyle:'circle'}},datalabels:{display:false}}}}); }

  // lazy question charts
  var DONE={};
  function renderQ(i){
    if(DONE[i]) return; var q=QDATA[i]; var ctx=document.getElementById('q'+i); if(!ctx) return; DONE[i]=1;
    var ans=q.answered;
    if(q.type==='pie'){
      new Chart(ctx,{type:'pie',data:{labels:q.labels,datasets:[{data:q.counts,backgroundColor:PAL,borderColor:'#fff',borderWidth:2}]},
        options:{maintainAspectRatio:false,plugins:{legend:{position:'right',labels:{boxWidth:9,font:{size:11},padding:8,usePointStyle:true,pointStyle:'circle'}},datalabels:{color:'#fff',font:{size:11,weight:'700'},formatter:function(v){return v? Math.round(v/ans*1000)/10+'%':'';}}}}});
    } else {
      var horiz=(q.type==='hbar'); var mx=horiz? ans : Math.max.apply(null,q.counts)+1;
      new Chart(ctx,{type:'bar',data:{labels:q.labels,datasets:[{data:q.counts,backgroundColor:ACC,borderRadius:4,barThickness:horiz?15:34}]},
        options:{maintainAspectRatio:false,indexAxis:horiz?'y':'x',layout:{padding:{right:horiz?52:6,top:horiz?0:18}},
          scales: horiz?{x:{beginAtZero:true,max:ans,ticks:{stepSize:Math.max(1,Math.round(ans/4)),font:{size:10}},grid:{color:'#f0f0f2'}},y:{ticks:{font:{size:11},autoSkip:false},grid:{display:false}}}
                       :{y:{beginAtZero:true,max:mx,ticks:{stepSize:1,font:{size:10}},grid:{color:'#f0f0f2'}},x:{grid:{display:false},ticks:{font:{size:12}}}},
          plugins:{legend:{display:false},datalabels:{anchor:'end',align:'end',clamp:true,color:'#5a5a62',font:{size:10.5,weight:'600'},formatter:function(v){return pf(v,ans);}}}}});
    }
  }
  // accordion
  function openAcc(acc){ acc.classList.add('open'); JSON.parse(acc.getAttribute('data-qs')).forEach(renderQ); }
  document.querySelectorAll('.acc').forEach(function(acc){
    acc.querySelector('.acc-head').addEventListener('click',function(){
      if(acc.classList.contains('open')) acc.classList.remove('open'); else openAcc(acc);
    });
  });
  var eb=document.getElementById('expandAll'), cb=document.getElementById('collapseAll');
  if(eb) eb.addEventListener('click',function(){ document.querySelectorAll('.acc').forEach(openAcc); });
  if(cb) cb.addEventListener('click',function(){ document.querySelectorAll('.acc').forEach(function(a){a.classList.remove('open');}); });

  // person modal
  var ov=document.getElementById('pmOv');
  function tc(t){return t==='top'?['#e6f6ec','#1a9e57']:t==='watch'?['#fdf3e0','#b5790a']:t==='crit'?['#fdeceb','#cc342b']:['#eef1fc','#3257d6'];}
  function ul(items){var u=document.createElement('ul'); items.forEach(function(x){var li=document.createElement('li'); li.textContent=x; u.appendChild(li);}); return u;}
  function grp(cls,label,items){var g=document.createElement('div'); g.className='grp'; var l=document.createElement('div'); l.className='lab '+cls; l.textContent=label; g.appendChild(l); g.appendChild(ul(items)); return g;}
  function openP(key){
    var p=PEOPLE[key]; if(!p) return; var an=ANALYSIS[key];
    var a=document.getElementById('pmAva'); a.textContent=key.charAt(0); a.style.background=p.color;
    document.getElementById('pmName').textContent=p.name+' ('+p.nick+')';
    var dept='',pos=''; p.fields.forEach(function(f){if(f[0]==='แผนก')dept=f[1];if(f[0]==='ตำแหน่ง')pos=f[1];});
    document.getElementById('pmMeta').textContent=[dept,pos].filter(function(x){return x&&x!=='—';}).join(' · ');
    var c=tc(p.tier); var fb=document.getElementById('pmFit'); fb.textContent='ความพร้อม '+p.fit; fb.style.background=c[0]; fb.style.color=c[1];
    var body=document.getElementById('pmBody'); body.innerHTML='';
    if(an){var box=document.createElement('div'); box.className='pm-an'; var v=document.createElement('div'); v.className='v'; v.textContent=an.v; box.appendChild(v);
      if(an.s&&an.s.length)box.appendChild(grp('s','จุดแข็ง',an.s)); if(an.r&&an.r.length)box.appendChild(grp('r','ต้องระวัง',an.r)); if(an.p&&an.p.length)box.appendChild(grp('p','แนวทางในคลาส',an.p)); body.appendChild(box);}
    p.fields.forEach(function(f){var row=document.createElement('div'); row.className='pm-row'; var q=document.createElement('div'); q.className='pm-q'; q.textContent=f[0]; row.appendChild(q); var val=f[1];
      if(Array.isArray(val)){var w=document.createElement('div'); w.className='pm-a pm-chips'; val.forEach(function(x){var s=document.createElement('span'); s.className='pm-chip'; s.textContent=x; w.appendChild(s);}); row.appendChild(w);} else {var av=document.createElement('div'); av.className='pm-a'; av.textContent=val; row.appendChild(av);} body.appendChild(row);});
    ov.classList.add('open');
  }
  function closeP(){ov.classList.remove('open');}
  document.querySelectorAll('.rrow[data-key]').forEach(function(r){r.addEventListener('click',function(){openP(r.getAttribute('data-key'));});});
  document.getElementById('pmX').addEventListener('click',closeP);
  ov.addEventListener('click',function(e){if(e.target===ov)closeP();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')closeP();});

  // tabs
  function showTab(t){
    document.querySelectorAll('.tabbtn').forEach(function(x){x.classList.toggle('active',x.getAttribute('data-tab')===t);});
    var ow=document.getElementById('tab-owner'), le=document.getElementById('tab-learner');
    if(ow) ow.classList.toggle('active',t==='owner');
    if(le) le.classList.toggle('active',t==='learner');
    var al=document.getElementById('tab-align'); if(al) al.classList.toggle('active',t==='align');
    if(t==='learner') renderRadar();
    if(t==='align') renderRadar2();
  }
  document.querySelectorAll('.tabbtn').forEach(function(b){b.addEventListener('click',function(){showTab(b.getAttribute('data-tab'));window.scrollTo({top:0,behavior:'smooth'});});});
  // hash routing
  if(location.hash.indexOf('align')>=0) showTab('align');
  else if(/learner|all|p=/.test(location.hash)) showTab('learner');
  if(location.hash.indexOf('all')>=0){ document.querySelectorAll('.acc').forEach(openAcc); }
  if(location.hash.indexOf('p=')>=0){ try{openP(decodeURIComponent(location.hash.split('p=')[1]));}catch(e){} }
})();
'''
JS=JS.replace('__QDATA__',json.dumps(QDATA,ensure_ascii=False)).replace('__PEOPLE__',json.dumps(PEOPLE,ensure_ascii=False)).replace('__ANALYSIS__',json.dumps(ANALYSIS,ensure_ascii=False))

doc=f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{P('สรุปแบบสำรวจผู้เข้าอบรม (เต็ม) | Claude AI Workshop')}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="hero-band"><div class="hero-inner">
  <span class="eyebrow">Claude AI Workshop</span>
  <h1>บ.ขอนแก่นอิเล็คทริค — สรุป AI Workshop</h1>
  <p class="sub">รวมมุมเจ้าของธุรกิจ (ความคาดหวัง) และมุมผู้เข้าอบรม (ผลสำรวจ) ไว้ที่เดียว · เลือกดูทีละมุม</p>
  <div class="tabbar">
    <button class="tabbtn active" type="button" data-tab="owner">ความคาดหวังเจ้าของธุรกิจ</button>
    <button class="tabbtn" type="button" data-tab="learner">สรุปผู้เข้าอบรม</button>
    <button class="tabbtn" type="button" data-tab="align">ความสอดคล้อง</button>
  </div>
</div></div>
<div class="wrap">
  <div class="tab active" id="tab-owner">
{owner_html}
  </div>
  <div class="tab" id="tab-learner">
  <div class="kpi strip">
    <div class="k acc-blue"><div class="n a">11</div><div class="l">ผู้เข้าอบรม</div></div>
    <div class="k acc-blue"><div class="n">9<span style="font-size:13px;color:var(--muted)">/11</span></div><div class="l">สายการตลาด</div></div>
    <div class="k acc-amber"><div class="n w">2.7<span style="font-size:13px;color:var(--muted)">/5</span></div><div class="l">{P('มั่นใจใช้ AI (เฉลี่ย)')}</div></div>
    <div class="k acc-amber"><div class="n w">6<span style="font-size:13px;color:var(--muted)">/11</span></div><div class="l">ไม่เคยเขียนโค้ด</div></div>
    <div class="k acc-red"><div class="n r">7<span style="font-size:13px;color:var(--muted)">/11</span></div><div class="l">{P('กลัวเรียนไม่ทัน')}</div></div>
    <div class="k acc-green"><div class="n g">1</div><div class="l">{P('ใช้ Claude ประจำ')}</div></div>
  </div>
  <section>
    <div class="sec-head"><h2>ภาพรวมผู้เรียน</h2></div>
    <div class="two">
      <div class="card">
        <h3>{P('อันดับความพร้อม — เรียงจากสูงไปต่ำ')}</h3>
        <div class="rhint">แตะที่ชื่อเพื่อดูสรุป วิเคราะห์ และคำตอบทั้งหมดของคนนั้น</div>
        <div class="rank">
{rank_html}
        </div>
      </div>
      <div class="card">
        <h3>{P('ความพร้อมรายหัวข้อ (0 = ยังไม่พร้อม · 3 = ทำเองได้จริง)')}</h3>
        <div class="exwrap"><canvas id="cRadar"></canvas></div>
      </div>
    </div>
  </section>

  <section>
    <div class="sec-head"><h2>ข้อค้นพบ &amp; รายละเอียด</h2><span class="n">5 กลุ่มข้อค้นพบ · 17 คำถาม</span>
      <div class="tools"><button class="tbtn" id="expandAll" type="button">เปิดทั้งหมด</button><button class="tbtn" id="collapseAll" type="button">ย่อทั้งหมด</button></div>
    </div>
    <p class="rhint" style="margin:-6px 2px 14px">แตะหัวข้อเพื่อเปิดดู — ซ่อนไว้เพื่อให้หน้าแรกกระชับ</p>
    <div class="subgroup-label">ข้อค้นพบสำคัญ</div>
{insight_acc}
    <div class="subgroup-label">รายละเอียดทุกคำถาม (กราฟ)</div>
{acc_html}
  </section>
  </div>

  <div class="tab" id="tab-align">
{align_html}
  </div>

  <footer>{P('ที่มา: แบบสำรวจผู้เข้าอบรม (8 คำตอบ) · กู้คืน 30 มิ.ย. 2026 · เปอร์เซ็นต์คิดจากจำนวนผู้ตอบในแต่ละคำถาม').replace('8 คำตอบ','11 คำตอบ')}</footer>
</div>

<div class="pm-ov" id="pmOv">
  <div class="pm" role="dialog" aria-modal="true">
    <div class="pm-head">
      <div class="pm-ava" id="pmAva"></div>
      <div class="pm-id"><h3 id="pmName"></h3><div class="meta" id="pmMeta"></div></div>
      <div class="pm-fit" id="pmFit"></div>
      <button class="pm-x" id="pmX" aria-label="ปิด">✕</button>
    </div>
    <div class="pm-body" id="pmBody"></div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.min.js"></script>
<script>{JS}</script>
</body>
</html>'''
open(BASE+'/AI-Workshop-รวม.html','w',encoding='utf-8').write(doc)
print("wrote", len(doc),"chars · groups",len(GROUPS),"· highlights",len(HIGHLIGHTS))
