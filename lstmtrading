import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import requests

# Obtém os dados históricos do preço da criptomoeda
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d"
data = requests.get(url).json()
data = pd.DataFrame(data, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

# Prepara os dados
scaler = MinMaxScaler()
data[['open', 'high', 'low', 'close']] = scaler.fit_transform(data[['open', 'high', 'low', 'close']])

# Divide os dados em conjunto de treinamento e teste
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Cria o modelo de rede neural
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(train_data.shape[1], 4)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Treina o modelo
model.fit(train_data, epochs=100, batch_size=32)

# Faz previsões com o conjunto de teste
predictions = model.predict(test_data)

# Decide se comprar ou vender com base nas previsões
if predictions[-1] > data['close'].iloc[-1]:
    print("Comprar")
else:
    print("Vender")
