# lstm_model.py     
            #   final

# import yfinance as yf
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# def forecast_next_7_days(ticker):
#     df = yf.Ticker(ticker).history(period="1y")[['Close']]w
#     df.dropna(inplace=True)

#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(df.values)

#     look_back = 60
#     X_train, y_train = [], []
#     for i in range(look_back, len(scaled_data)):
#         X_train.append(scaled_data[i - look_back:i, 0])
#         y_train.append(scaled_data[i, 0])

#     X_train, y_train = np.array(X_train), np.array(y_train)
#     X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

#     model = Sequential()
#     model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
#     model.add(LSTM(units=50))
#     model.add(Dense(1))
#     model.compile(optimizer='adam', loss='mean_squared_error')
#     model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

#     future_input = scaled_data[-look_back:].reshape(1, look_back, 1)
#     predictions = []
#     for _ in range(7):
#         pred = model.predict(future_input, verbose=0)[0][0]
#         predictions.append(pred)
#         future_input = np.append(future_input[:, 1:, :], [[[pred]]], axis=1)

#     predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

#     last_date = df.index[-1]
#     future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)

#     return df, future_dates, predicted_prices.flatten()








# import yfinance as yf
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# def forecast_next_7_days(ticker):
#     df = yf.Ticker(ticker).history(period="1y")[['Close']]  # ✅ Fixed line
#     df.dropna(inplace=True)

#     # Normalize
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(df.values)

#     # Create sequences
#     look_back = 60
#     X_train, y_train = [], []
#     for i in range(look_back, len(scaled_data)):
#         X_train.append(scaled_data[i - look_back:i, 0])
#         y_train.append(scaled_data[i, 0])

#     X_train, y_train = np.array(X_train), np.array(y_train)
#     X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

#     # Build model
#     model = Sequential()
#     model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
#     model.add(LSTM(units=50))
#     model.add(Dense(1))
#     model.compile(optimizer='adam', loss='mean_squared_error')
#     model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

#     # Predict next 7 days
#     future_input = scaled_data[-look_back:].reshape(1, look_back, 1)
#     predictions = []
#     for _ in range(7):
#         pred = model.predict(future_input, verbose=0)[0][0]
#         predictions.append(pred)
#         future_input = np.append(future_input[:, 1:, :], [[[pred]]], axis=1)

#     predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).flatten()

#     last_date = df.index[-1]
#     future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)

#     return df, future_dates, predicted_prices








# final
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
# from sklearn.preprocessing import MinMaxScaler
# import yfinance as yf

# def forecast_next_7_days(ticker="META"):
#     # Load data
#     df = yf.Ticker(ticker).history(period="1y")[['Close']]
#     df.dropna(inplace=True)

#     # Scale data
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_data = scaler.fit_transform(df.values)

#     # Prepare training data
#     look_back = 60
#     X_train, y_train = [], []
#     for i in range(look_back, len(scaled_data)):
#         X_train.append(scaled_data[i - look_back:i, 0])
#         y_train.append(scaled_data[i, 0])
#     X_train, y_train = np.array(X_train), np.array(y_train)
#     X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))

#     # Build LSTM model
#     model = Sequential()
#     model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
#     model.add(LSTM(units=50))
#     model.add(Dense(1))
#     model.compile(optimizer='adam', loss='mean_squared_error')
#     model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

#     # Predict next 7 days
#     future_input = scaled_data[-look_back:].reshape(1, look_back, 1)
#     predictions = []
#     for _ in range(7):
#         pred = model.predict(future_input, verbose=0)[0][0]
#         predictions.append(pred)
#         future_input = np.append(future_input[:, 1:, :], [[[pred]]], axis=1)

#     predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

#     # Create future dates
#     last_date = df.index[-1]
#     future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)

#     # -------------------
#     # 📊 PLOT 1: Full chart with historical and forecasted data
#     plt.figure(figsize=(12, 5))
#     plt.plot(df.index, df['Close'], label='Historical')
#     plt.plot(future_dates, predicted_prices, label='LSTM 7-Day Forecast', color='orange', marker='o')
#     plt.title(f'{ticker} LSTM Forecast (Full View)')
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.grid(True)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

#     # -------------------
#     # 📊 PLOT 2: Zoomed chart for only 7-day prediction
#     plt.figure(figsize=(10, 6))
#     plt.plot(future_dates, predicted_prices, marker='o', color='green', label='Predicted')
    
#     # Annotate each point with the predicted value
#     for i, (date, price) in enumerate(zip(future_dates, predicted_prices)):
#         plt.text(date, price + 1, f"${price[0]:.2f}", ha='center', fontsize=9, color='black')

#     plt.title(f'{ticker} - 7 Day LSTM Forecast (Zoomed)')
#     plt.xlabel('Date')
#     plt.ylabel('Predicted Price')
#     plt.grid(True)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()


#     return df, future_dates, predicted_prices






import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import datetime

def forecast_next_7_days(ticker):
    # Load historical data for the past 1 year
    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=365)
    df = yf.download(ticker, start=start, end=end)

    if df.empty:
        raise ValueError("No data found for ticker:", ticker)

    df = df[['Close']].dropna()

    # Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)

    sequence_length = 60
    x = []
    y = []

    for i in range(sequence_length, len(scaled_data)):
        x.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i])

    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))

    # Build an optimized LSTM model for better accuracy
    model = Sequential()
    model.add(LSTM(units=128, return_sequences=True, input_shape=(x.shape[1], 1)))
    model.add(LSTM(units=128, return_sequences=True))
    model.add(LSTM(units=64, return_sequences=False))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    # Train the model with increased epochs and a smaller batch size for better accuracy
    model.fit(x, y, epochs=50, batch_size=16, verbose=1)

    # Forecast the next 7 days
    forecast_input = scaled_data[-sequence_length:]
    forecast_input = forecast_input.reshape(1, sequence_length, 1)

    future_predictions = []
    for _ in range(7):
        pred = model.predict(forecast_input, verbose=0)
        future_predictions.append(pred[0][0])
        # Correct reshaping and appending
        forecast_input = np.append(forecast_input[:, 1:, :], [[[pred[0][0]]]], axis=1)

    future_prices = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1)).flatten()
    future_dates = [df.index[-1] + datetime.timedelta(days=i) for i in range(1, 8)]

    return df, future_dates, future_prices
