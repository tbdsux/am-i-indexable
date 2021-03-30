from fastapi import FastAPI

from api.handler import search, validate

app = FastAPI()

@app.get("/api/search/{search_engine}")
async def index(search_engine: str, q: str):
	# strip trailing slashes
	q = q.strip('/')

	# get search results
	res = search(search_engine, q)

	# check
	return validate(q, res)