# main.py

# --- Импорт библиотек ---
import uvicorn
from fastapi import FastAPI

# --- Инициализация приложения ---
app = FastAPI(
    title="Simple FastAPI App",
    description="Первое приложение на FastAPI",
    version="1.0.0"
)

# --- Роуты ---
@app.get("/", summary="Главная страница", tags=["Root"])
async def root():
    """
    Возвращает приветственное сообщение.
    """
    return {"message": "Hello World 🌍"}


# --- Точка входа ---
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

"""
📌 Инструкция по запуску:

1. Установи зависимости (если ещё не установлены):
    pip install fastapi uvicorn

2. Запусти приложение:
    uvicorn main:app --reload 
    python main.py
    fastapi dev main.py

3. Открой в браузере:
    🌐 Главная:         http://127.0.0.1:8000/
    📚 Документация:    http://127.0.0.1:8000/docs
    📘 ReDoc:           http://127.0.0.1:8000/redoc

🔁 Параметр --reload позволяет перезапускать сервер при изменении кода (удобно для разработки).
"""
