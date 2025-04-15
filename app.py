from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from model import analyzer
import uvicorn

app = FastAPI(title="Sentiment Analysis API")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class TextRequest(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/api/analyze")
async def analyze(text_request: TextRequest):
    return analyzer.analyze_sentiment(text_request.text)

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_web(request: Request, text: str = Form(...)):
    result = analyzer.analyze_sentiment(text)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "text": text
        }
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)