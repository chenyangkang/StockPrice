# StockPrice

This is a package for downloading NASDAQ stock price data at day-level. Each day 00:00 AM New York time it updates all 3000+ stock data of NASDAQ from `alpaca` trading API, and save it into `stock_historical_prices` folder. The latest data, that is the data of today, will not be available, as I did not subscribe.

User should store their alpaca API key and secret key in the settings of the repository.

It could be used as a submodule for downstream data analysis.