import requests
import pandas as pd

# Obtém os dados históricos do preço da criptomoeda
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h"
data = requests.get(url).json()
data = pd.DataFrame(data, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data['close'] = data['close'].astype(float)

# Adiciona colunas de médias móveis
data['MA20'] = data['close'].rolling(window=20).mean()
data['MA9'] = data['close'].rolling(window=9).mean()

# Loop para negociar
for i in range(len(data) - 21):
    # Verifica se o preço atual está acima da média móvel de 20 períodos e se a média móvel de 9 períodos está subindo
    if data['close'].iloc[i] > data['MA20'].iloc[i] and data['MA9'].iloc[i] < data['MA9'].iloc[i + 1]:
        print("Comprar")
    # Verifica se o preço atual está abaixo da média móvel de 20 períodos e se a média móvel de 9 períodos está caindo
    elif data['close'].iloc[i] < data['MA20'].iloc[i] and data['MA9'].iloc[i] > data['MA9'].iloc[i + 1]:
        print("Vender")
    else:
        print("Manter")
