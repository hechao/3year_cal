from yahoo_historical import Fetcher

data = Fetcher("AAPL", [2007,1,1], [2017,1,1])

df = data.getHistorical()

print(df)
