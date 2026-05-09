from fastapi import FastAPI
from routes.ai import router as ai_router
from typing import Union

app = FastAPI()

app.include_router(ai_router,prefix='/v1',tags=['v1'])


@app.get("/")
def read_root(obtained_marks: int = 600, total_marks: int = 1000):
    percentage=(obtained_marks/total_marks)*100
    return{'percentage': percentage}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}