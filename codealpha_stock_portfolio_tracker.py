import pandas as pd
import requests
API_KEY = 'WZ0DHK1EWS8ZO3L3'
BASE_URL = 'https://www.alphavantage.co/query'
class StockPortfolio:
    def __init__(self):
        self.stocks = {}
    def add_stock(self, sym, quant):
        if sym in self.stocks:
            self.stocks[sym]['quant'] += quant
        else:
            self.stocks[sym] = {'quant': quant, 'price': 0.0, 'value': 0.0}
        print(f"Added {quant} shares of {sym}.")

    def remove_stock(self, sym, quant):
        if sym in self.stocks:
            if self.stocks[sym]['quant'] >= quant:
                self.stocks[sym]['quant'] -= quant
                if self.stocks[sym]['quant'] == 0:
                    del self.stocks[sym]
                print(f"Removed {quant} shares of {sym}.")
            else:
                print("Not enough shares to remove.")
        else:
            print(f"{sym} not found in portfolio.")

    def fetch_stock_price(self, sym):
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'sym': sym,
            'interval': '1min',
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        try:
            latest_time = list(data['Time Series (1min)'].keys())[0]
            latest_price = float(data['Time Series (1min)'][latest_time]['4. close'])
            return latest_price
        except KeyError:
            print(f"Error fetching data for {sym}. Check the symbol or API key.")
            return None

    def update_portfolio(self):
        total_value = 0.0
        for sym, info in self.stocks.items():
            price = self.fetch_stock_price(sym)
            if price:
                info['price'] = price
                info['value'] = info['quant'] * price
                total_value += info['value']
        print(f"Total portfolio value: ${total_value:.2f}")

    def display_portfolio(self):
        df = pd.DataFrame.from_dict(self.stocks, orient='index')
        print("\nCurrent Portfolio:")
        print(df)

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock('AAPL', 10)
    portfolio.add_stock('GOOGL', 5)
    portfolio.display_portfolio()
    portfolio.update_portfolio()
    portfolio.display_portfolio()
    portfolio.remove_stock('AAPL', 5)
    portfolio.display_portfolio()
