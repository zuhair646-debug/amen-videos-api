# 🎬 API منصة آمِن للفيديوهات العائلية

## 📋 الوصف
Backend API كامل لمنصة آمِن، مبني بـ Flask مع دعم CORS كامل.

---

## 🚀 النشر على Railway

### الطريقة 1: من GitHub (الأسرع) ✅
1. افتح Railway → **New Project**
2. اختر **Deploy from GitHub repo**
3. اختر **zuhair646-debug/amen-videos-api**
4. Railway سيكتشف Flask تلقائياً ✅
5. انتظر حتى يكتمل النشر (~2 دقيقة)

### الطريقة 2: من CLI
```bash
railway login
railway init
railway link
railway up
```

---

## 🌐 Endpoints

| Endpoint | الوصف | مثال |
|---------|-------|------|
| `GET /` | معلومات API | `/` |
| `GET /api/videos` | جلب جميع الفيديوهات | `/api/videos` |
| `GET /api/videos?category=تعليمي` | تصفية حسب الفئة | `/api/videos?category=تعليمي` |
| `GET /api/videos/<id>` | جلب فيديو محدد | `/api/videos/1` |
| `GET /api/shorts` | الفيديوهات القصيرة | `/api/shorts` |
| `GET /api/search?q=كلمة` | البحث | `/api/search?q=تعليمي` |
| `GET /health` | فحص الصحة | `/health` |

---

## ✅ CORS مفعّل لـ:
- ✅ `https://zenrex.ai`
- ✅ `https://catalog.cloudflarestorage.com`
- ✅ `localhost` (للتطوير)
- ✅ جميع النطاقات (`*` - للتطوير فقط)

---

## 🔧 متغيرات البيئة (اختيارية)

Railway يضبط `PORT` تلقائياً. لو تبي تعدّل:

```env
PORT=5000
FLASK_ENV=production
```

---

## 🧪 اختبار محلي

```bash
# تثبيت المكتبات
pip install -r requirements.txt

# تشغيل السيرفر
python app.py
```

افتح: http://localhost:5000

---

## 📦 الملفات
- `app.py` — الـ API الرئيسي مع جميع الـ routes
- `requirements.txt` — المكتبات المطلوبة
- `Procfile` — أمر تشغيل Gunicorn
- `runtime.txt` — إصدار Python 3.11.7
- `.gitignore` — استثناءات Git

---

## 🎯 الخطوات بعد النشر

### 1️⃣ انسخ URL السيرفر من Railway
مثال: `https://amen-videos-api-production.up.railway.app`

### 2️⃣ عدّل الموقع في Zenrex
افتح `current_html` وابحث عن:
```javascript
const API_BASE = 'https://amen-bot.up.railway.app';
```

استبدلها بـ:
```javascript
const API_BASE = 'https://amen-videos-api-production.up.railway.app';
```

### 3️⃣ اختبر الموقع
افتح `https://zenrex.ai/s/amen-videos` وتأكد أن الفيديوهات تظهر ✅

---

## 🛠️ تخصيص البيانات

لإضافة فيديوهاتك الحقيقية، عدّل القوائم `VIDEOS` و `SHORTS` في `app.py`:

```python
VIDEOS = [
    {
        "id": 1,
        "title": "عنوان الفيديو",
        "description": "الوصف",
        "thumbnail": "رابط الصورة",
        "url": "رابط الفيديو",
        "duration": "5:30",
        "category": "تعليمي",
        "views": 1250,
        "uploadDate": "2024-01-15"
    }
]
```

---

## 📊 إضافة قاعدة بيانات (مستقبلاً)

لو تبي تخزن الفيديوهات في database بدل list:
1. أضف PostgreSQL من Railway Dashboard
2. ثبّت `psycopg2-binary` في requirements.txt
3. عدّل `app.py` لاستخدام SQLAlchemy

---

## 🔒 الأمان

⚠️ **مهم:** 
- CORS مفتوح حالياً (`*`) للتطوير
- لما تجهز للإنتاج، احذف `"*"` من قائمة `origins` في `app.py`
- أضف authentication للـ endpoints الحساسة

---

## 🐛 استكشاف الأخطاء

### المشكلة: CORS blocked
✅ **الحل:** تأكد أن نطاقك موجود في قائمة `origins` في `app.py`

### المشكلة: 404 Not Found
✅ **الحل:** تأكد أن الـ URL صحيح ويبدأ بـ `/api/`

### المشكلة: فشل النشر
✅ **الحل:** تأكد أن جميع الملفات موجودة:
- `app.py`
- `requirements.txt`
- `Procfile`
- `runtime.txt`

---

**🚀 صُنع بواسطة Zenrex AI - التحديث الأخير: 2026**

للدعم: https://zenrex.ai
