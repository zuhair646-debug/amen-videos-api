from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)

# ✅ تفعيل CORS لكل النطاقات (أو حدد نطاقات معينة)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://zenrex.ai",
            "https://catalog.cloudflarestorage.com",
            "http://localhost:*",
            "*"  # للتطوير - احذفها في الإنتاج
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# 🎬 بيانات الفيديوهات (مثال - استبدلها ببياناتك الحقيقية)
VIDEOS = [
    {
        "id": 1,
        "title": "فيديو تعليمي للأطفال - الحروف العربية",
        "description": "تعلم الحروف العربية بطريقة ممتعة وآمنة",
        "thumbnail": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=400",
        "url": "https://example.com/video1.mp4",
        "duration": "5:30",
        "category": "تعليمي",
        "views": 1250,
        "uploadDate": "2024-01-15"
    },
    {
        "id": 2,
        "title": "قصة قبل النوم - الأرنب الصغير",
        "description": "قصة هادفة ومسلية للأطفال",
        "thumbnail": "https://images.unsplash.com/photo-1585435557343-3b092031a831?w=400",
        "url": "https://example.com/video2.mp4",
        "duration": "8:45",
        "category": "ترفيهي",
        "views": 3420,
        "uploadDate": "2024-01-20"
    },
    {
        "id": 3,
        "title": "تجارب علمية بسيطة للأطفال",
        "description": "تجارب آمنة يمكن تنفيذها في المنزل",
        "thumbnail": "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=400",
        "url": "https://example.com/video3.mp4",
        "duration": "6:15",
        "category": "علمي",
        "views": 2100,
        "uploadDate": "2024-01-25"
    }
]

SHORTS = [
    {
        "id": 101,
        "title": "نصيحة اليوم",
        "thumbnail": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=400",
        "url": "https://example.com/short1.mp4",
        "duration": "0:45",
        "views": 5200
    },
    {
        "id": 102,
        "title": "لغز ممتع",
        "thumbnail": "https://images.unsplash.com/photo-1606326608606-aa0b62935f2b?w=400",
        "url": "https://example.com/short2.mp4",
        "duration": "0:30",
        "views": 4100
    }
]

# 🏠 الصفحة الرئيسية
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "مرحباً بك في API منصة آمِن",
        "version": "1.0.0",
        "endpoints": {
            "/api/videos": "جلب جميع الفيديوهات",
            "/api/videos/<id>": "جلب فيديو محدد",
            "/api/shorts": "جلب الفيديوهات القصيرة",
            "/api/search": "البحث في الفيديوهات"
        }
    })

# 📹 جلب جميع الفيديوهات
@app.route('/api/videos', methods=['GET'])
def get_videos():
    category = request.args.get('category')
    
    if category:
        filtered = [v for v in VIDEOS if v['category'] == category]
        return jsonify({
            "status": "success",
            "count": len(filtered),
            "data": filtered
        })
    
    return jsonify({
        "status": "success",
        "count": len(VIDEOS),
        "data": VIDEOS
    })

# 📹 جلب فيديو محدد
@app.route('/api/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = next((v for v in VIDEOS if v['id'] == video_id), None)
    
    if video:
        return jsonify({
            "status": "success",
            "data": video
        })
    else:
        return jsonify({
            "status": "error",
            "message": "الفيديو غير موجود"
        }), 404

# 🎬 جلب الفيديوهات القصيرة
@app.route('/api/shorts', methods=['GET'])
def get_shorts():
    return jsonify({
        "status": "success",
        "count": len(SHORTS),
        "data": SHORTS
    })

# 🔍 البحث
@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    
    results = [
        v for v in VIDEOS 
        if query in v['title'].lower() or query in v['description'].lower()
    ]
    
    return jsonify({
        "status": "success",
        "query": query,
        "count": len(results),
        "data": results
    })

# 🏥 فحص الصحة
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "amen-api"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
