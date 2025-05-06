
import yfinance as yf
from datetime import datetime
import json

symbol = "1810.HK"
today = datetime.now().strftime("%Y-%m-%d")

data = yf.download(symbol, period="2d", interval="1d")
if len(data) < 2:
    raise ValueError("Failed to fetch Xiaomi stock data")

latest = data.iloc[-1]
json_data = {
    "date": today,
    "symbol": "01810.HK",
    "open": round(latest["Open"], 2),
    "high": round(latest["High"], 2),
    "low": round(latest["Low"], 2),
    "close": round(latest["Close"], 2)
}

filename = f"xiaomi-{today}.json"
with open(filename, "w") as f:
    json.dump(json_data, f, indent=2)

print(f"Saved {filename}")
