# Assignment 01: AI Travel Guide

## Problem

Khi khám phá Huế, du khách thường lúng túng trước hệ thống di tích rải rác và giàu chiều sâu lịch sử. Việc tự tìm hiểu qua sách hướng dẫn, tờ rơi hay bảng chỉ dẫn tĩnh buộc họ phải tự chắt lọc thông tin rời rạc từ nhiều nguồn. Các công cụ này thiếu tính cá nhân hóa, không thể gợi ý điểm đến hay lập lịch trình theo quỹ thời gian và sở thích riêng. Hệ quả là du khách tốn nhiều thời gian tra cứu, di chuyển thiếu tối ưu và dễ bỏ lỡ những giá trị văn hóa cốt lõi của cố đô.

## How I Would Use AI

Để khắc phục hạn chế trên, tôi đề xuất ứng dụng AI Travel Guide vận hành theo quy trình ba bước. Ở bước Input, du khách cung cấp các yêu cầu cá nhân như quỹ thời gian, ngân sách, phương tiện và sở thích. Trong giai đoạn Processing, thay vì để mô hình ngôn ngữ lớn (LLM) tự suy đoán, hệ thống tích hợp dữ liệu cập nhật theo thời gian thực (giờ mở cửa, giá vé, thời gian di chuyển) kết hợp cùng công cụ bản đồ để sắp xếp hành trình hợp lý. Đồng thời, cơ chế RAG (Retrieval-Augmented Generation) sẽ truy xuất ngữ cảnh từ tài liệu di sản Huế uy tín trước khi LLM tạo phản hồi, giúp giảm thiểu đáng kể rủi ro sai lệch thông tin. Cuối cùng, Output mang đến cho du khách lịch trình chi tiết theo khung giờ, lời thuyết minh văn hóa sinh động và khả năng hỏi – đáp linh hoạt ngay tại điểm đến.

## Impact

So với sách hướng dẫn tĩnh hay các lịch trình cố định vốn khó điều chỉnh tức thì theo nhu cầu cá nhân, AI Travel Guide mang lại sự linh hoạt cao và hỗ trợ rút ngắn thời gian tra cứu. Du khách dễ dàng tiếp cận những câu chuyện văn hóa Huế được cá nhân hóa và tương tác trực tiếp tại điểm đến. Với địa phương, ứng dụng mở ra cơ hội quảng bá di sản, ẩm thực cùng các điểm tham quan ít phổ biến. Để duy trì giá trị bền vững, nguồn dữ liệu cần được kiểm chứng và cập nhật thường xuyên nhằm nâng cao độ tin cậy.
