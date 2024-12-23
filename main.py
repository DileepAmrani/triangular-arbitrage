import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()


templates = Jinja2Templates(directory="templates")


def get_binance_prices(pairs):
    url = "https://api.binance.com/api/v3/ticker/price"
    prices = {}
    for pair in pairs:
        response = requests.get(url, params={"symbol": pair})
        data = response.json()
        if 'price' in data:
            prices[pair] = data['price']
    return prices

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    pairs = ["BTCUSDT", "ETHUSDT", "BTCETH"] 
    prices = get_binance_prices(pairs)
    return templates.TemplateResponse("index.html", {"request": request, "prices": prices})
