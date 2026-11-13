import os
import json
import urllib.request

# Lấy chính xác đường dẫn thư mục chứa file main.py hiện tại
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# 1. DOCUMENT LOADING
file_filenames = ["dai-noi.md", "lang-minh-mang.md"]
documents = []

for filename in file_filenames:
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            documents.append({"content": f.read(), "source": filename})
        print(f"Đã nạp thành công: {filename}")
    else:
        print(f"Không tìm thấy file tại: {path}")

print(f"\nTổng số tài liệu đã nạp: {len(documents)}\n")

# 2. DOCUMENT CHUNKING
chunks = []
for doc in documents:
    text = doc["content"]
    sections = text.split("\n## ")
    for sec in sections:
        chunks.append({
            "content": sec.strip(),
            "source": doc["source"]
        })

print(f"Tổng số chunks sau khi chia nhỏ: {len(chunks)}")

# 3. RETRIEVAL
def retrieve(query, top_k=2):
    query_words = set(query.lower().split())
    scored = []
    for c in chunks:
        score = sum(1 for w in query_words if w in c["content"].lower())
        scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:top_k]]

# 4. GENERATION (Tích hợp gọi API Gemini thực tế bằng urllib thuần)
def ask_travel_guide(query, api_key=""):
    relevant_docs = retrieve(query)
    context = "\n---\n".join([f"[{d['source']}]: {d['content']}" for d in relevant_docs])
    
    prompt = f"""Bạn là AI Travel Guide Huế. Hãy trả lời câu hỏi của du khách dựa hoàn toàn vào dữ liệu được cung cấp dưới đây. Tuyệt đối không tự bịa đặt thông tin.

[DỮ LIỆU THAM KHẢO]:
{context}

[CÂU HỎI]: {query}"""

    if not api_key:
        print("\n=== [CHƯA CÓ API KEY] KHUÔN MẪU PROMPT HOÀN CHỈNH ===")
        print(prompt)
        print("\n(Hãy nhập API Key của bạn vào hàm ask_travel_guide để nhận câu trả lời thực tế từ Gemini!)")
        return

    # Gọi REST API Gemini trực tiếp qua urllib (vượt qua mọi lỗi Windows Security/pydantic)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            print("\n=== AI TRAVEL GUIDE HUẾ TRẢ LỜI ===")
            print(result["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:
        print(f"Lỗi khi gọi API Gemini: {e}")

# --- THỰC THI ---
# Nếu bạn đã có Google Gemini API Key, hãy điền vào chuỗi bên dưới (ví dụ: api_key="AIzaSy...")
# Nếu chưa có, chương trình sẽ in ra khuôn mẫu Prompt chuẩn xác để bạn kiểm tra.
MY_API_KEY = "" 

ask_travel_guide("Lăng Minh Mạng có đặc điểm kiến trúc gì?", api_key=MY_API_KEY)