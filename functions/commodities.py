import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def commodities(commodity, api_key):
    url = f"https://www.alphavantage.co/query?function={commodity}&interval=monthly&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def plot_commodities(commodity, api_key):
    valid_ticker = True
    if valid_ticker:
        try:
            commodity_data = commodities(commodity, api_key)
            df = pd.DataFrame.from_dict(commodity_data["data"])
            df = df.set_index("date")
            df.index = pd.to_datetime(df.index)
            df["value"] = df["value"].replace(".", np.nan)
            df = df.dropna()
            prices = df["value"].astype(float).resample("M").last()
            axis = prices.plot(title=commodity_data["name"])
            axis.set_xlabel("Year")
            axis.set_ylabel(commodity_data["unit"])
        except KeyError as e:
            print(f"encountered error (commodities): {e}")
            valid_ticker = False

    if valid_ticker:
        plt.savefig("image.png")
        plt.show()
    else:
        print("Couldn't plot.")