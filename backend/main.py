from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Crypto Price API!"}

@app.get("/prices")
async def get_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    # Filter for specific trading pairs
    pairs_of_interest = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    filtered_prices = {
        item["symbol"]: item["price"]
        for item in data
        if item["symbol"] in pairs_of_interest
    }

    return {"prices": filtered_prices}
