import numpy as np

#funkcje do obliczania EMA, MACD i SIGNAL
def calculate_ema(prices, period):
    alpha = 2 / (period + 1)
    ema = np.zeros_like(prices)
    ema[0] = prices[0]  #początkowa wartość EMA
    for i in range(1, len(prices)):
        ema[i] = alpha * prices[i] + (1 - alpha) * ema[i - 1]
    return ema

def calculate_macd(prices, short_period=12, long_period=26):
    ema_short = calculate_ema(prices, short_period)
    ema_long = calculate_ema(prices, long_period)
    macd = ema_short - ema_long
    return macd

def calculate_signal(macd, signal_period=9):
    signal = calculate_ema(macd, signal_period)
    return signal