from head import *

client = Client()
date = datetime.today().strftime('%Y')
paircoin = "BTCUSDT"

klinesT = client.get_historical_klines(paircoin, Client.KLINE_INTERVAL_1HOUR, "01 january 2017")

df = pd.DataFrame(klinesT, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
df['close'] = pd.to_numeric(df['close'])
df['high'] = pd.to_numeric(df['high'])
df['low'] = pd.to_numeric(df['low'])
df['open'] = pd.to_numeric(df['open'])

df.drop(df.columns.difference(['open','high','low','close','volume', 'timestamp']), 1, inplace=True)

df = df.set_index(df['timestamp'])
df.index = pd.to_datetime(df.index, unit='ms')
del df['timestamp']
#print(df)

result = df.to_json(orient="index")
parsed = json.loads(result) 
with open(str(paircoin) + '_DATA_' + str(date) + '.json', 'w') as json_file:
    json.dump(parsed, json_file)

file = str(paircoin) + '_DATA_' + str(date) + '.json'
print(file)
os.system("mv " + file + " ../data/")