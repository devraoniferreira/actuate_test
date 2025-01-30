import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.payload import ShortRequest, LongRequest, ClickCountRequest
from src.shortener import generate_short_url, retrieve_long_url, increment_click_count, get_click_count

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/short")
def short(short_request: ShortRequest):
    logging.info(f"Received short request: {short_request}")
    short_url = generate_short_url(short_request.url)
    long_request: LongRequest = LongRequest(short_url=short_url)
    return long_request

@app.post("/long")
def long(long_request: LongRequest):
    logging.info(f"Received long request: {long_request}")
    url = retrieve_long_url(long_request.short_url)
    short_request: ShortRequest = ShortRequest(url=url)
    return short_request

@app.get("/{short_url}")
def redirect(short_url: str):
    logging.info(f"Received redirect request: {short_url}")
    url = retrieve_long_url(short_url)
    increment_click_count(short_url)
    return RedirectResponse(url=url, status_code=302)

@app.get("/count/{short_url}")
def count(short_url: str):
    logging.info(f"Received count request: {short_url}")
    count = get_click_count(short_url)
    click_count_request: ClickCountRequest = ClickCountRequest(click_count=count)
    return click_count_request

