
from pathlib import Path

# BƯỚC 1: Xác định đường dẫn
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# BƯỚC 2: Đọc tất cả tài liệu Markdown
documents = []

for file_path in sorted(DATA_DIR.glob("*.md")):
    document = {
        "filename": file_path.name,
        "content": file_path.read_text(encoding="utf-8")
    }
    documents.append(document)

print(f"Đã nạp {len(documents)} tài liệu")

# BƯỚC 3: Tạo danh sách lưu chunks
chunks = []

# BƯỚC 4: Duyệt từng tài liệu
for doc in documents:
    text = doc["content"]

    # Chia tài liệu theo heading cấp 2
    sections = text.split("\n## ")

    # Lấy tiêu đề tài liệu
    document_title = sections[0].strip()

    # BƯỚC 5: Duyệt các phần nội dung
    for index, section in enumerate(sections[1:], start=1):

        # Xóa khoảng trắng thừa
        cleaned_section = section.strip()

        # Bỏ qua section rỗng
        if not cleaned_section:
            continue

        # BƯỚC 6: Tạo chunk
        chunk = {
            "filename": doc["filename"],
            "document_title": document_title,
            "chunk_id": index,
            "content": cleaned_section
        }

        chunks.append(chunk)

# BƯỚC 7: In kết quả
print(f"\nTổng số chunks: {len(chunks)}")

for chunk in chunks:
    print("\n---------------------")
    print(f"File: {chunk['filename']}")
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Tiêu đề: {chunk['document_title']}")
    print(f"Nội dung: {chunk['content']}")
