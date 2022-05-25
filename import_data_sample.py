from engine.head import *

filename = 'data/' + 'BTCUSDT_DATA_2022_INTERVAL_5m.json'

if os.path.exists(filename):
    df = pd.read_json(path_or_buf=filename, orient='index')
    # df = df['2020-01-01':]
    # df = df['2021-01-01':'2021-05-01']
    print("\nData pandas loaded 100%...\n")
else:
    print("Pas de JSON à charger..")
    exit()

print(df)