# K14 · Hook Model — สร้าง Habit จาก Customer

> **TL;DR (EN):** Nir Eyal's Hook Model (Hooked, 2014) explains how products like Instagram and Slack create habits — through a cycle of Trigger → Action → Variable Reward → Investment. The more cycles a customer completes, the harder it is to leave. Loyalty programs are habit-engineering machines: each point earned, tier climbed, or coupon redeemed is one loop of the Hook.
>
> **สรุป (TH):** Hook Model ของ Nir Eyal อธิบายว่า product แบบ Instagram/Slack สร้าง habit ยังไง — วงจร Trigger → Action → Variable Reward → Investment ทำซ้ำมากเท่าไหร่ ยิ่งเลิกใช้ยาก Loyalty program = เครื่องสร้าง habit ทุกแต้มที่ได้ ทุก tier ที่เลื่อน ทุก coupon ที่แลก = 1 รอบ Hook

---

## 1. Hook Model 4 ขั้น

```
       ┌──────────────────────────────────┐
       │                                  │
       ▼                                  │
   1. TRIGGER ─▶ 2. ACTION ─▶ 3. REWARD ─▶ 4. INVESTMENT
       │           (ทำอะไร)    (Variable)     (ลงทุน)
       │              ▲                          │
       │              │                          │
       └──────────────┴──────────────────────────┘
                       Loops back to Trigger
```

---

## 2. ขั้น 1 — Trigger (ตัวกระตุ้น)

### 🔔 External Trigger (จากภายนอก)
- Push notification
- LINE message
- Email
- Ad
- คนแนะนำ

### 💭 Internal Trigger (จากภายใน — กำหนดเอง)
- ความรู้สึก: เบื่อ, เหงา, หิว, อยากดื่มกาแฟ
- สถานการณ์: ช่วงเช้า, ก่อนนอน, เช็คอินทำงาน

> **เป้าหมายสูงสุด:** ลูกค้าเลิกต้องการ external trigger — ใช้ product เพราะ internal trigger เอง
> เช่น "หิว → คิดถึง Café Amazon" (ไม่ต้องดูโฆษณา)

### ใน Loyalty Context
| Trigger | EasyCRM ใช้ได้ |
|---|---|
| LINE message | "แต้มจะหมดอายุ 30 วัน" |
| Push from rich menu | "Reward ใหม่!" |
| Internal: ซื้อกาแฟ | "ส่งสลิปเลย เก็บแต้ม" |

---

## 3. ขั้น 2 — Action (การกระทำ)

> **Fogg Behavior Model:** B = MAT (Behavior = Motivation × Ability × Trigger)
> — BJ Fogg, Stanford

### ทำให้ Action ง่ายที่สุด

| ดี | ไม่ดี |
|---|---|
| 1 ปุ่ม | ฟอร์มยาว |
| Auto-fill | คีย์เอง |
| LINE ID | ลงทะเบียนใหม่ |
| สแกน QR | กรอกโค้ด |

### ใน EasyCRM
- ✅ ส่งสลิป → ระบบอ่านเอง → ได้แต้ม (1 step!)
- ✅ Add LINE OA → สมัครเสร็จ (Login เก่ามา)
- ✅ Rich menu 1-tap → ดูแต้ม

---

## 4. ขั้น 3 — Variable Reward (รางวัลที่คาดเดาไม่ได้)

### 🎰 ทำไม Variable สำคัญ?
- Brain ปล่อย dopamine **ตอนคาด** ไม่ใช่ตอนได้
- รางวัล "predictable" → boring
- รางวัล "variable" → addictive (slot machine effect)

### 3 ประเภทของ Variable Reward

#### 🌍 Tribe (สังคม)
- Like, comment, share
- Status update (เลื่อน tier → คนอื่นเห็น)
- Leaderboard

#### 🎁 Hunt (ของรางวัล)
- Mystery box
- Lucky draw
- Surprise discount

#### 🧠 Self (ตัวเอง)
- ความรู้สึก mastery
- Achievement, badge
- Progress complete

### ใน Loyalty Context
| Reward Type | EasyCRM examples |
|---|---|
| Tribe | Share tier badge บน LINE Profile |
| Hunt | Mystery reward wheel หลังครบ 1,000 แต้ม |
| Self | Tier progress bar, achievement "1st ปี" |

> **Killer combo:** ตัวอย่างจริง — Starbucks "Bonus Star Challenge"
> "ซื้อ 5 ครั้งใน 7 วัน อาจได้ 50-200 stars (random)"
> = Tribe (compete with friends) + Hunt (random) + Self (achievement)

---

## 5. ขั้น 4 — Investment (การลงทุน)

### 💎 ลูกค้าลงทุนอะไรในระบบ?
- **เวลา** (กรอกข้อมูล, setup profile)
- **ข้อมูล** (preference, history)
- **เงิน** (top-up, subscription)
- **ความสัมพันธ์** (referral, follow)
- **ชื่อเสียง** (rating, review)

### ทำไมสำคัญ?
- Investment = **sunk cost** → switch ออกยาก
- Investment = **store value** → product ดีขึ้นเรื่อย ๆ (more data → better recommend)
- Investment = **set up next trigger** → "เก็บ 10 แก้วแล้ว เก็บอีก 2 จะฟรี" → bring back

### ใน Loyalty Context
| Investment | EasyCRM ตัวอย่าง |
|---|---|
| Time | สะสมแต้ม 2,000 แต้ม |
| Data | กรอก preference (เครื่องดื่มที่ชอบ) |
| Relationship | Refer friend |
| Reputation | Review/rating หลังแลกของรางวัล |

---

## 6. Hook ที่สมบูรณ์ — Walking Through (EasyCRM)

```
1. TRIGGER:    LINE message "เพื่อนสมัครสมาชิกแล้ว — สมัครฟรีรับ 100 แต้ม"
                   ↓
2. ACTION:     คลิกลิ้งก์ → กรอกชื่อ+เบอร์ → "สมัคร" (10 วินาที)
                   ↓
3. REWARD:     "🎉 ยินดีต้อนรับ! รับ 100 แต้ม + Mystery gift"
                   ↓
4. INVESTMENT: กรอก preference เครื่องดื่ม, สาขาประจำ
                   ↓
   (Internal trigger ครั้งถัดไป)
   ลูกค้าซื้อกาแฟ → คิดเอง "เปิด LINE ส่งสลิป"
                   ↓
1. TRIGGER (internal): หิวกาแฟ
2. ACTION: สั่ง + ส่งสลิป
3. REWARD: ได้แต้ม + "ครบ 500 แต้มแล้ว! แลกของรางวัลได้"
4. INVESTMENT: เลือก reward → reserve → กลับมารับสาขา
                   ↓
   Hook continues...
```

→ หลัง 10 รอบ Hook ลูกค้ามี habit เปิดแอปทุกครั้งที่ซื้อ

---

## 7. Anti-pattern — Manipulation vs Habit-building

### ⚠️ Hook ที่ใช้ผิด = manipulation

| ✅ Healthy Habit | ❌ Manipulation |
|---|---|
| ทำให้ user ดีขึ้น | ทำให้ user แย่ลง |
| Transparent | Hidden mechanics |
| Easy to leave | Trap |
| User feels good after | User feels regret after |

### ตัวอย่าง manipulation ใน loyalty
- Point ที่หมดอายุเร็วเกินไปจน user รู้สึกถูกเอาเปรียบ
- Tier downgrade แบบไม่แจ้ง
- Reward catalog ที่ "ขาย" สูงเกิน point earn
- Dark pattern ใน cancellation flow

> **Nir Eyal's "Manipulation Matrix":**
> 1. **Facilitator** (ดี) — ทำให้ user ดีขึ้น + ตัวเอง use product
> 2. **Peddler** (gray) — ดีสำหรับ user แต่ตัวเองไม่ใช้
> 3. **Entertainer** (กลาง) — ตัวเอง use แต่ user ไม่ได้ดีขึ้น
> 4. **Dealer** (แย่) — manipulation ล้วน ๆ
>
> → Loyalty ที่ดีควรอยู่ในกล่อง **Facilitator**

---

## 8. วัด Hook Strength

### Metric: Habit Strength
```
Habit Strength = Frequency × Perceived Utility
```

### Question
> "ถ้า product นี้หายไป — user รู้สึกยังไง?"

| Response | Habit Strength |
|---|---|
| "เฉย ๆ" | ไม่มี habit |
| "เสียดาย" | กำลังก่อตัว |
| "ลำบาก" | habit ชัดเจน |
| "ขาดไม่ได้" | habit เทพ |

### Behavior Frequency Test
- ใช้ < 1 ครั้ง/สัปดาห์ = ยังไม่ใช่ habit
- ใช้ ≥ 1 ครั้ง/สัปดาห์ = habit กำลังก่อ
- ใช้ ≥ 1 ครั้ง/วัน = habit แข็งแกร่ง

---

## 9. ใช้ Hook Model กับ EasyCRM อย่างไร

### Tactical Checklist
- [ ] **Trigger:** LINE message timing ตรง daily routine
- [ ] **Action:** ส่งสลิป → ได้แต้มใน 5 วินาที (ไม่เกิน)
- [ ] **Variable Reward:** Mystery gift, double-point days, surprise upgrades
- [ ] **Investment:** Tier progress, preference profile, referral
- [ ] **Internal trigger formed within 14 days** (track via cohort)

---

## 🔗 อ่านต่อ

- Retention ที่เกี่ยวข้อง → [[K13-Retention-Churn]]
- Gamification (Octalysis ใช้ similar principles) → [[K07-Gamification-Octalysis]]
- Tier system สร้าง investment → [[K05-Tier-System-Design]]

## 📚 Resources

- *Hooked: How to Build Habit-Forming Products* — Nir Eyal (2014)
- *Atomic Habits* — James Clear (related: habit stacking)
- BJ Fogg Behavior Model — Stanford
