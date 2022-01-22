# import ccxt
# import sys
# sys.path.append( '../utilities' )
# from data_engine import DataEngine
# from engine.function import Helpers as hlp
# import pandas as pd
# import numpy as np

# pair = 'BTC/USDT'
# timeframe = '15m'
# startDate = '2017-01-01T00:00:00'

# dataEngine = DataEngine(session=ccxt.binance(), path_to_data='../database/')
# df = dataEngine.get_historical_from_db(pair, timeframe, startDate)

from engine.head import *
from engine.function import Helpers as hlp

pair_name = 'BTC/USDT'
filename = 'data/' + 'BTCUSDT_DATA_2022.json'

if os.path.exists(filename):
    df = pd.read_json(path_or_buf=filename, orient='index')
    df = df['2021-01-01':] # date de début uniquement
    #df = df['2021-01-01':'2021-05-01'] # date de début et de fin
    print("\nData pandas loaded 100%...\n")
else:
    print("Pas de JSON à charger..")
    exit()

dfSupAndRes = df
lows = pd.DataFrame(data=dfSupAndRes, index=dfSupAndRes.index, columns=["low"])
highs = pd.DataFrame(data=dfSupAndRes, index=dfSupAndRes.index, columns=["high"])
low_centers = hlp.get_optimum_clusters(lows)
low_centers = sorted(low_centers)
high_centers = hlp.get_optimum_clusters(highs)
high_centers = sorted(high_centers)

print(low_centers)
print(high_centers)