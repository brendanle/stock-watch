
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def currency_exchange_rate(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={first_currency}&to_currency={second_currency}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def fx_monthly(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={first_currency}&to_symbol={second_currency}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def plot_forex_data(first_currency, second_currency, api_key):
    valid_ticker = True
    if valid_ticker:
        try:
            currency_exchange_rate_data = currency_exchange_rate(first_currency, second_currency, api_key)
            from_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
            to_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
            exchange_rate = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        except KeyError as e:
            print(f"encountered error (currency_exchange_rate): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            fx_monthly_data = fx_monthly(first_currency, second_currency, api_key)
            df = pd.DataFrame.from_dict(fx_monthly_data["Time Series FX (Monthly)"], orient="index")
            df.index = pd.to_datetime(df.index)
            prices = df["4. close"].astype(float).resample("M").last()
            axis = prices.plot(title=f"{first_currency}/{second_currency} Time Series FX")
            axis.set_xlabel("Year")
            axis.set_ylabel("Price")
        except KeyError as e:
            print(f"encountered error (fx_monthly): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "The current exchange rate between " + first_currency + "/" + second_currency + " is " + exchange_rate + ".\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")

        plt.savefig("image.png")
        plt.show()
    else:
        print("Couldn't plot.")