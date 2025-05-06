import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funkcje import calculate_macd, calculate_signal

#wczytanie danych
data = pd.read_csv('dane/Dogecoin Historical Data.csv', quotechar='"') #quotechar-obsluga cudzysłowów

prices = data['Price'].values
dates = pd.to_datetime(data['Date'])

#MACD i SIGNAL
macd = calculate_macd(prices)
signal = calculate_signal(macd)

#wykresy
plt.figure(figsize=(14, 10))

#1.ceny zamknięcia
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label='Cena zamknięcia Dogecoin', color='blue')
plt.title('Notowania Dogecoin')
plt.xlabel('Data')
plt.ylabel('Cena zamknięcia')
plt.legend()
plt.show()

#2,3.MACD i SIGNAL
plt.figure(figsize=(10, 5))
plt.plot(dates, macd, label='MACD', color='blue')
plt.plot(dates, signal, label='SIGNAL', color='red')
plt.title('MACD i SIGNAL dla Dogecoin')
plt.xlabel('Data')
plt.ylabel('Wartość')
plt.legend()
plt.tight_layout()
plt.savefig("wykresy/ms_dogecoin.png", dpi=300)

#sygnały kupna i sprzedaży
buy_signals = []
sell_signals = []

for i in range(1, len(macd)):
    if macd[i - 1] < signal[i - 1] and macd[i] > signal[i]:
        buy_signals.append(i)
    elif macd[i - 1] > signal[i - 1] and macd[i] < signal[i]:
        sell_signals.append(i)

#wykres z sygnałami kupna i sprzedaży
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label='Cena zamknięcia Dogecoin', alpha=0.5, color='blue')
plt.scatter(dates.iloc[buy_signals], prices[buy_signals], label='Sygnał kupna', marker='^', color='green', s=100)
plt.scatter(dates.iloc[sell_signals], prices[sell_signals], label='Sygnał sprzedaży', marker='v', color='red', s=100)
plt.title('Sygnały kupna i sprzedaży na podstawie MACD')
plt.xlabel('Data')
plt.ylabel('Cena zamknięcia')
plt.legend()
plt.tight_layout()
plt.savefig("wykresy/sygnaly_dogecoin.png", dpi=300)

#wykresy - pierwsze 100 wartości
first_n = 100
end_idx = min(first_n, len(dates))

#sygnały KUPNA/SPRZEDAŻY dla pierwszych 100 dni
buy_signals_first100 = []
sell_signals_first100 = []

for i in range(1, end_idx):
    if macd[i - 1] < signal[i - 1] and macd[i] > signal[i]:
        buy_signals_first100.append(i)
    elif macd[i - 1] > signal[i - 1] and macd[i] < signal[i]:
        sell_signals_first100.append(i)

#1.ceny zamknięcia - pierwsze 100
plt.subplot(3, 1, 1)
plt.plot(dates[:end_idx], prices[:end_idx], label='Cena zamknięcia Dogecoin', color='blue')
plt.title('Notowania Dogecoin (ostatnie 100 dni)')
plt.xlabel('Data')
plt.ylabel('Cena zamknięcia')
plt.legend()

#2,3.MACD i SIGNAL - pierwsze 100
plt.figure(figsize=(10, 5))
plt.plot(dates[:end_idx], macd[:end_idx], label='MACD', color='blue')
plt.plot(dates[:end_idx], signal[:end_idx], label='SIGNAL', color='red')
plt.title('MACD i SIGNAL dla Dogecoin (ostatnie 100 dni)')
plt.xlabel('Data')
plt.ylabel('Wartość')
plt.legend()
plt.tight_layout()
plt.savefig("wykresy/ms_dogecoin_100dni.png", dpi=300)

# wykres z sygnałami kupna i sprzedaży - pierwsze 100 dni
plt.figure(figsize=(10, 5))
plt.plot(dates[:end_idx], prices[:end_idx], label='Cena zamknięcia Dogecoin', alpha=0.5, color='blue')
plt.scatter(dates.iloc[buy_signals_first100], prices[buy_signals_first100],
            label='Sygnał kupna', marker='^', color='green', s=100)
plt.scatter(dates.iloc[sell_signals_first100], prices[sell_signals_first100],
            label='Sygnał sprzedaży', marker='v', color='red', s=100)
plt.title('Sygnały kupna i sprzedaży na podstawie MACD (ostatnie 100 dni)')
plt.xlabel('Data')
plt.ylabel('Cena zamknięcia')
plt.legend()
plt.tight_layout()
plt.savefig("wykresy/sygnaly_dogecoin_100dni.png", dpi=300)

print("Sygnały kupna (pierwsze 100 dni):")
for idx in buy_signals_first100:
    print(f"Data: {dates.iloc[idx].date()}, Cena: {prices[idx]:.4f}")

print("\nSygnały sprzedaży (pierwsze 100 dni):")
for idx in sell_signals_first100:
    print(f"Data: {dates.iloc[idx].date()}, Cena: {prices[idx]:.4f}")

#symulacja automatycznego handlu
capital = 1000  #kapitał początkowy
position = 0  #liczba posiadanych jednostek Dogecoin
portfolio_value = []  #wartość portfela po każdej transakcji

for i in range(len(prices)):
    if i in buy_signals and capital > 0:
        position = capital / prices[i]
        capital = 0
    elif i in sell_signals and position > 0:
        capital = position * prices[i]
        position = 0
    portfolio_value.append(capital + position * prices[i])

#wykres wartości portfela
plt.figure(figsize=(12, 6))
plt.plot(dates, portfolio_value[::-1], label='Wartość portfela', color='purple')
plt.title('Wartość portfela inwestycyjnego')
plt.xlabel('Data')
plt.ylabel('Wartość portfela')
plt.legend()
plt.savefig("wykresy/portfel_dogecoin.png")

print(f'\nPoczątkowy kapitał: 1000')

#końcowy kapitał
final_capital = capital + position * prices[-1]
print(f'Końcowy kapitał: {final_capital:.2f}')

#skutecznosc wskaźnika MACD
num_buy_signals = len(buy_signals)
num_sell_signals = len(sell_signals)
print(f'\nLiczba sygnałów kupna: {num_buy_signals}')
print(f'Liczba sygnałów sprzedaży: {num_sell_signals}')

#zyski/straty dla każdej transakcji
profits = []
for i in range(len(buy_signals)):
    buy_price = prices[buy_signals[i]]
    sell_price = prices[sell_signals[i]] if i < len(sell_signals) else prices[-1]
    profit = (sell_price - buy_price) / buy_price * 100
    profits.append(profit)

#średnia
average_profit = np.mean(profits)
print(f'\nŚredni zysk na transakcję: {average_profit:.2f}%')

#min
min_profit = np.min(profits)
print(f'Największa strata na transakcję: {min_profit:.2f}%')

#max
max_profit = np.max(profits)
print(f'Maksymalny zysk na transakcję: {max_profit:.2f}%')

#liczba transakcji z zyskiem i stratą
positive_trades = sum(1 for p in profits if p > 0)
negative_trades = sum(1 for p in profits if p < 0)
print(f'\nLiczba transakcji z zyskiem: {positive_trades}')
print(f'Liczba transakcji ze stratą: {negative_trades}')