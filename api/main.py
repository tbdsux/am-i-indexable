from fastapi import FastAPI

from api.handler import search, validate

app = FastAPI()

@app.get("/api/search/{search_engine}")
async def index(search_engine: str, q: str):
	res = search(search_engine, q)

	return validate(q, res)