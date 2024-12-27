from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://triangular-arbitrage-eight.vercel.app"],  # React app URL during development
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
        if response.status_code != 200:
            return {"error": f"Failed to fetch data from Binance. Status Code: {response.status_code}"}

        try:
            data = response.json()  # This should be a list based on your response
        except ValueError:
            return {"error": "Failed to parse response from Binance"}

    # Log data for debugging (optional)
    print("Binance Response:", data)

    # Filter for specific trading pairs
    pairs_of_interest = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    filtered_prices = {
        item["symbol"]: item["price"]
        for item in data
        if item["symbol"] in pairs_of_interest
    }

    return {"prices": filtered_prices}
