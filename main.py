from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def root() :
    return {"status": "ok"}

@app.get("/assets")
def get_assets(ticker: str) :
    symbols = ticker.split(",")
    result = {}

    for symbol in symbols :
        try :
            stock = yf.Ticker(symbol)
            info = stock.info

            result[symbol] = {
                "symbol": symbol,
                "name": info.get["shortName"],
                "currency": info.get["currency"],
                "price": info.get["currentPrice"],
                "previous_price": info.get["previousClose"],    
            }
        except Exception as e:
            result[symbol] = {
                "symbol": symbol,
                "error": str(e)
            }
    return result
