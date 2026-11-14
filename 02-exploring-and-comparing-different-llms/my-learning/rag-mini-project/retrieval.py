
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

# =====================================
# BƯỚC 1: DOCUMENT LOADING
# =====================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

chunks = []

# Đọc tất cả file Markdown
for file_path in sorted(DATA_DIR.glob("*.md")):

    text = file_path.read_text(encoding="utf-8")

    # =====================================
    # BƯỚC 2: DOCUMENT CHUNKING
    # =====================================

    sections = text.split("\n## ")
    document_title = sections[0].strip()

    for index, section in enumerate(sections[1:], start=1):

        content = section.strip()

        if not content:
            continue

        chunk = {
            "filename": file_path.name,
            "document_title": document_title,
            "chunk_id": index,
            "content": content
        }

        chunks.append(chunk)

print("Tổng số chunks:", len(chunks))

if not chunks:
    raise ValueError("Không tìm thấy chunks. Kiểm tra thư mục data.")

# =====================================
# BƯỚC 3: EMBEDDING
# =====================================

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

texts = [chunk["content"] for chunk in chunks]

chunk_embeddings = model.encode(texts)

print("Kích thước embeddings:", chunk_embeddings.shape)

# =====================================
# BƯỚC 4: RETRIEVAL
# =====================================

query = input("Nhập câu hỏi du lịch Huế: ").strip()

if not query:
    raise ValueError("Câu hỏi không được để trống.")
# query = "Lăng Minh Mạng có những công trình kiến trúc nổi bật nào?"

print("\nCâu hỏi:", query)

# Chuyển câu hỏi thành vector
query_embedding = model.encode(query)

# Tính độ tương đồng với tất cả chunks
scores = util.cos_sim(
    query_embedding,
    chunk_embeddings
)[0]

# Chọn 2 chunks có điểm cao nhất
top_results = sorted(
    range(len(chunks)),
    key=lambda i: scores[i].item(),
    reverse=True
)[:2]

# =====================================
# BƯỚC 5: HIỂN THỊ KẾT QUẢ
# =====================================

for rank, index in enumerate(top_results, start=1):

    chunk = chunks[index]

    print(f"\nTOP {rank}")
    print("File:", chunk["filename"])
    print("Chunk ID:", chunk["chunk_id"])
    print("Similarity:", round(scores[index].item(), 4))
    print("Nội dung:", chunk["content"])
