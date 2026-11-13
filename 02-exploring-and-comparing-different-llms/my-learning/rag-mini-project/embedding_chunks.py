
from pathlib import Path
from sentence_transformers import SentenceTransformer

# 1. Xác định thư mục dữ liệu
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# 2. Nạp và chia tài liệu thành chunks
chunks = []

for file_path in sorted(DATA_DIR.glob("*.md")):
    text = file_path.read_text(encoding="utf-8")
    sections = text.split("\n## ")

    document_title = sections[0].strip()

    for index, section in enumerate(sections[1:], start=1):
        content = section.strip()

        if not content:
            continue

        chunks.append({
            "filename": file_path.name,
            "document_title": document_title,
            "chunk_id": index,
            "content": content
        })

# 3. Tải mô hình
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# 4. Lấy nội dung của từng chunk
texts = [chunk["content"] for chunk in chunks]

# 5. Tạo Embedding
embeddings = model.encode(texts)

# 6. Kiểm tra kết quả
print("Tổng số chunks:", len(chunks))
print("Kích thước embeddings:", embeddings.shape)
for index, chunk in enumerate(chunks):
    print(f"\nChunk {index + 1}")
    print("File:", chunk["filename"])
    print("Chunk ID:", chunk["chunk_id"])
    print("Vector shape:", embeddings[index].shape)
