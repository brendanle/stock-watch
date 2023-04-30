import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def economic_indicator(indicator, api_key):
    url = f"https://www.alphavantage.co/query?function={indicator}&interval=annual&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def economic_indicator_treasury_yield(maturity, api_key):
    url = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity={maturity}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def plot_economic_indicator(indicator, api_key):
    valid_ticker = True
    try:
        economic_indicator_data = economic_indicator(indicator, api_key)
        df = pd.DataFrame.from_dict(economic_indicator_data["data"])
        df = df.set_index("date")
        df.index = pd.to_datetime(df.index)
        df["value"] = df["value"].replace(".", np.nan)
        df = df.dropna()
        prices = df["value"].astype(float).resample("M").last()
        axis = prices.plot(title=economic_indicator_data["name"])
        axis.set_xlabel("Year")
        axis.set_ylabel(economic_indicator_data["unit"])
    except KeyError as e:
        print(f"encountered error (economic_indicator): {e}")
        valid_ticker = False

    if valid_ticker:
        plt.savefig("image.png")
        plt.show()
    else:
        print("Couldn't plot.")

def plot_economic_indicator_treasury_yield(maturity, api_key):
    valid_ticker = True
    try:
        treasury_yield_data = economic_indicator_treasury_yield(maturity, api_key)
        df = pd.DataFrame.from_dict(treasury_yield_data["data"])
        df = df.set_index("date")
        df.index = pd.to_datetime(df.index)
        df["value"] = df["value"].replace(".", np.nan)
        df = df.dropna()
        prices = df["value"].astype(float).resample("M").last()
        axis = prices.plot(title=treasury_yield_data["name"])
        axis.set_xlabel("Year")
        axis.set_ylabel(treasury_yield_data["unit"])
    except KeyError as e:
        print(f"encountered error (plot_economic_indicator_treasury_yield): {e}")
        valid_ticker = False

    if valid_ticker:
        plt.savefig("image.png")
        plt.show()
    else:
        print("Couldn't plot.")