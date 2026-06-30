---
name: reference-clasp-apps-script-webapp
description: วิธี deploy Apps Script ผ่าน clasp + ใช้ Web App doGet เป็น workaround เพราะ clasp run ติด GCP project linking
metadata: 
  node_type: memory
  type: reference
  originSessionId: ee3243ee-719d-43e0-bff1-37e9a5221f48
---

# Deploy Apps Script standalone ผ่าน clasp — ทำได้แค่ไหน

ทดสอบจริง 2026-06-30 บน macOS ใช้ bobbysomporn@gmail.com

## Setup (ครั้งแรก)
1. `npm install -g @google/clasp`
2. User ต้อง toggle ON "Google Apps Script API" ที่ `https://script.google.com/home/usersettings` (Google บังคับ — automate ไม่ได้)
3. `clasp login` (ใช้ default OAuth client ของ clasp — เปิด browser, user click Allow ครั้งเดียว) → token เก็บที่ `~/.clasprc.json`
4. `clasp create --type standalone --title "..."` → ได้ Script ID + dir มี `.clasp.json` + `appsscript.json`
5. วาง code เป็น `Code.gs` → `clasp push -f`

## ❌ clasp run ใช้ไม่ได้ตรงๆ
- ต้อง link GCP project + create OAuth client ใน console + deploy as API executable + scope ตรงทุกอย่าง — friction สูงมาก
- เรียก `script.googleapis.com/v1/scripts/{id}:run` ด้วย token clasp → ได้ 403 PERMISSION_DENIED (caller != script owner via correct OAuth client)
- `clasp logs` ต้อง GCP project ID — ไม่ได้ตั้ง = "GCP project ID is not set"

## ✅ Workaround: Web App + doGet
**ใช้แทน clasp run ได้เกือบทุกกรณีที่ต้องการ trigger function**

`appsscript.json`:
```json
{
  "timeZone": "Asia/Bangkok",
  "runtimeVersion": "V8",
  "webapp": { "executeAs": "USER_DEPLOYING", "access": "MYSELF" },
  "oauthScopes": [
    "https://www.googleapis.com/auth/forms",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/script.external_request"
  ]
}
```

`Code.gs`:
```javascript
function doGet() {
  var result = mainFunction();  // ฟังก์ชันจริงที่อยากรัน
  return HtmlService.createHtmlOutput('<h1>เสร็จ</h1>...' + result.url);
}
```

แล้ว:
- `clasp push -f && clasp deploy --description "v1"` → ได้ deployment ID
- Web App URL: `https://script.google.com/macros/s/{DEPLOYMENT_ID}/exec`
- User เปิด URL ครั้งแรก → consent ครั้งเดียว (advance → Go to ... unsafe → Allow) → doGet รัน → HTML กลับมาพร้อมผลลัพธ์
- Redeploy ทุกครั้งหลังแก้ code → deployment ID ใหม่ทุกรอบ → ต้องเปิด URL ใหม่

## ✅ Drive API ผ่าน clasp token ใช้ได้
- `scope drive.file` ของ clasp token list/อ่าน metadata ของไฟล์ที่ Web App สร้างได้
- DELETE: ❌ มัก 403 (`appNotAuthorizedToFile`) เพราะไฟล์สร้างด้วย user authorization คนละ app กับ clasp — user ต้องลบเองที่ drive.google.com

## Pitfalls
- ทุก `FormApp.create()` สร้างใหม่ทุกรอบ → duplicate ทุกครั้งที่ doGet ถูกเรียก (browser preload/refresh ก็เป็น) → ใช้ `FormApp.openById(ID) + clearAllItems` แทน หรือเก็บ ID ใน `PropertiesService.getScriptProperties()`
- เนื้อหาภาษาไทยใน `.gs` ใช้ single-quoted string ปลอดภัยกว่า — `"` ภายในข้อความเลี่ยง escape ได้
- Syntax check: copy `Code.gs` → `/tmp/x.js` แล้ว `node -c` (Apps Script V8 ใกล้เคียง Node ES2015+ พอเช็คได้)

## Reference paths
- Project ตัวอย่าง: `~/Documents/Claude/Projects/AI Workshop Management/clasp-deploy/`
- Related: [[AI Workshop — บ.ขอนแก่นอิเล็คทริค|project-ai-workshop-khonkaen]]
