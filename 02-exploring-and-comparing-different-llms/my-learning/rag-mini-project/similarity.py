
from sentence_transformers import SentenceTransformer, util

# 1. Tải mô hình Embedding
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# 2. Chuẩn bị dữ liệu
sentences = [
    "Lăng Minh Mạng có kiến trúc hài hòa với thiên nhiên.",
    "Kiến trúc lăng Minh Mạng kết hợp với cảnh quan sông núi.",
    "Du khách có thể tham quan Đại Nội Huế."
]

# 3. Chuyển câu thành vector
embeddings = model.encode(sentences)

# 4. Tính độ tương đồng
score_1_2 = util.cos_sim(
    embeddings[0], embeddings[1]
).item()
# util.cos_sim() : tính độ tương đồng giữa hai vector
score_1_3 = util.cos_sim(
    embeddings[0], embeddings[2]
).item()

# 5. In kết quả
print(f"Câu 1 và câu 2: {score_1_2:.4f}")
print(f"Câu 1 và câu 3: {score_1_3:.4f}")

# 6. So sánh
if score_1_2 > score_1_3:
    print("Kết luận: Câu 1 gần nghĩa với câu 2 hơn.")
else:
    print("Kết luận: Câu 1 gần nghĩa với câu 3 hơn.")
