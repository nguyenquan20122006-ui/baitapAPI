# API Phân Loại Cảm Xúc Văn Bản (Text Sentiment Analysis API)

Video Demo: [Video Demo](https://your-video-link-here)

---

## Giới thiệu dự án
Dự án này xây dựng một RESTful API dùng để **phân loại cảm xúc văn bản tiếng Anh** thành hai loại:

- POSITIVE (Tích cực)
- NEGATIVE (Tiêu cực)

Hệ thống được phát triển bằng **FastAPI** và sử dụng mô hình AI  
**distilbert-base-uncased-finetuned-sst-2-english** từ thư viện Hugging Face Transformers.

---

## Thông tin sinh viên
- **Họ và tên:** Nguyễn Hữu Nghĩa  
- **Mã số sinh viên:** 24120104  
- **Môn học:** Tư duy tính toán  

---

## Mô hình sử dụng
Mô hình từ Hugging Face:  
https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

---

## Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.x  
- **Web Framework:** FastAPI, Uvicorn  
- **AI/Machine Learning:**  
  - PyTorch (`torch`)  
  - Transformers (`transformers`)  

---

## Hướng dẫn cài đặt & chạy

### 1. Yêu cầu hệ thống
- Python >= 3.10  
- Kết nối Internet (để tải model lần đầu)

---

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt