from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
app = FastAPI()

# load model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=model_name)

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {
        "project": "API Phân loại cảm xúc văn bản",
        "model": model_name,
        "description": "Phân loại văn bản tiếng Anh thành POSITIVE hoặc NEGATIVE"
    }

@app.get("/health")
async def health():
    return {"status": "OK"}

@app.post("/predict")
async def predict(request: TextRequest):
    input_text = request.text.strip()

    # validate
    if not input_text:
        raise HTTPException(status_code=400, detail="Văn bản không được để trống")
    
    if len(input_text.split()) < 3:
        raise HTTPException(status_code=400, detail="Văn bản quá ngắn")

    if len(input_text) > 1000:
        raise HTTPException(status_code=400, detail="Văn bản quá dài")

    try:
        result = classifier(input_text)

        label = result[0]["label"]
        score = result[0]["score"]

        # chuyển sang tiếng Việt cho đẹp
        sentiment_vi = "Tích cực" if label == "POSITIVE" else "Tiêu cực"

        return {
            "input": input_text,
            "label": label,
            "sentiment_vi": sentiment_vi,
            "confidence": round(score, 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hệ thống: {str(e)}")