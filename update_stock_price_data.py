import os
import pandas as pd
import yfinance as yf
import datetime
import os
# import my_secrets
from tqdm.auto import tqdm
import requests

stock_list = list(pd.read_csv('nasdaq_stock_info/stock_info.csv')['code'])
start_date = '2015-01-01'
end_date = str((datetime.datetime.now() - pd.to_timedelta('1d')).date())

ALPACA_API_KEY = os.environ.get("ALPACA_API_KEY", "<unknown")
ALPACA_SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY", "<unknown")

for stock in tqdm(stock_list):
    url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={stock}&timeframe=1Day&start={start_date}&end={end_date}&limit=10000&adjustment=all&feed=sip&sort=asc"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
    }
    
    # print(headers)

    response = requests.get(url, headers=headers)
    
    # print(response)
    
    # print(response.text)

    import json
    response_dict = json.loads(response.text)
    
    data = pd.DataFrame(response_dict['bars'][stock])
    data.to_csv(f'stock_historical_prices/{stock}.csv', index=False)

