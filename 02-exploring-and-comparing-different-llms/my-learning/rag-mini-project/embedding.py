from sentence_transformers import SentenceTransformer
# Bước 1: Tải mô hình Embedding đa ngôn ngữ
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
# Bước 2: Chuẩn bị dữ liệu mẫu
sentences = [
    "Lăng Minh Mạng có kiến trúc hài hòa với thiên nhiên.",
    "Kiến trúc lăng Minh Mạng kết hợp với cảnh quan sông núi.",
    "Du khách có thể tham quan Đại Nội Huế."
]
# Bước 3: Chuyển văn bản thành vector
embeddings = model.encode(sentences)

# Bước 4: Kiểm tra kết quả
print("Số câu:", len(sentences))
print("Kích thước embeddings:", embeddings.shape)
print("Vector đầu tiên (10 giá trị):")
print(embeddings[0][:10])

