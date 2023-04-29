import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_global_quote_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def get_monthly_adjusted_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def get_overview(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def plot_stock_data(stock_ticker, api_key):
    valid_ticker = True

    # Overview
    try:
        overview_data = get_overview(stock_ticker, api_key)
        symbol = overview_data["Symbol"]
        name = overview_data["Name"]
        description = overview_data["Description"]
        exchange = overview_data["Exchange"]
    except KeyError as e:
        print(f"encountered error (get_overview): {e}")
        valid_ticker = False

    # Global Quote
    if valid_ticker:
        try:
            global_quote_data = get_global_quote_data(stock_ticker, api_key)
            day = global_quote_data["Global Quote"]["07. latest trading day"]
            price = global_quote_data["Global Quote"]["05. price"]
        except KeyError as e:
            print(f"encountered error (get_global_quote_data): {e}")
            valid_ticker = False

    # Chart
    if valid_ticker:
        try:
            time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, api_key)
            df = pd.DataFrame.from_dict(time_series_monthly_adjusted_data["Monthly Adjusted Time Series"], orient="index")
            df.index = pd.to_datetime(df.index)
            prices = df["5. adjusted close"].astype(float).resample("M").last()
            axis = prices.plot(title=f"{stock_ticker} Historical Monthly Adjusted Close Prices")
            axis.set_xlabel("Year")
            axis.set_ylabel("Price")
        except KeyError as e:
            print(f"encountered error (get_monthly_adjusted_data): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "[" + day + "] " + symbol + " - " + price + "\n\n" + description + "\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")

        plt.savefig("image.png")
        plt.show()
    else:
        print("Couldn't plot.")
