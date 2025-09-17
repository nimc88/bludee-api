from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Bludee API")

# Servir archivos estáticos (tu HTML y futuros CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta principal: abre tu index.html
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Endpoint de prueba
@app.get("/health")
def health():
    return {"ok": True}

# Endpoint del chatbot (por ahora simulado)
@app.post("/chat")
async def chat(payload: dict):
    q = payload.get("q", "")
    return {
        "answer": f"Recibí tu pregunta: '{q}'. (Pronto: motor experto BB)",
        "sources": []
    }

