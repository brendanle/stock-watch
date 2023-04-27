# documentation: https://www.alphavantage.co/documentation/

import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "N20TDIL2VOIJS399"
valid_stock_ticker = True

def get_global_quote_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()["Global Quote"]

def get_monthly_adjusted_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()["Monthly Adjusted Time Series"]

def get_overview(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_ticker}&apikey=${api_key}"
    response = requests.get(url)
    return response.json()

print("\nSelect an option \n ==== MENU ====")

menu_items = ["Stocks", "Forex", "Crypto", "Commodities", "Economic Indicators"]

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

choice = input("Enter your choice (1-5): ")

if choice == "1":

    stock_ticker = input("Type your desired stock ticker and return. ")

    # Overview
    if valid_stock_ticker:
        try:
            overview_data = get_overview(stock_ticker, "demo")
            symbol = overview_data["Symbol"]
            name = overview_data["Name"]
            description = overview_data["Description"]
            exchange = overview_data["Exchange"]
        except KeyError as e:
            print(f"encountered error (overview): {e}")
            valid_stock_ticker = False

    # Global Quote
    if valid_stock_ticker:
        try:
            global_quote_data = get_global_quote_data(stock_ticker, "demo")
            day = global_quote_data["07. latest trading day"]
            price = global_quote_data["05. price"]
        except KeyError as e:
            print(f"encountered error (global quote): {e}")
            valid_stock_ticker = False

    # Chart
    if valid_stock_ticker:
        try:
            time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, "demo")
            df = pd.DataFrame.from_dict(time_series_monthly_adjusted_data, orient="index")
            df.index = pd.to_datetime(df.index)
            prices = df["5. adjusted close"].astype(float).resample("M").last()
            axis = prices.plot(title=f"{stock_ticker} Historical Monthly Adjusted Close Prices")
            axis.set_xlabel("Year")
            axis.set_ylabel("PRice")
        except KeyError as e:
            print(f"encountered error (chart): {e}")
            valid_stock_ticker = False

    if valid_stock_ticker:
        try:
            print("\n" + "[" + day + "] " + symbol + " - " + price + "\n\n" + description)
        except:
            print("Error printing out the details!")

    # Save & Show
    if valid_stock_ticker:
        plt.savefig("stockimage.png")
        plt.show()
    else:
        print("Couldn't plot.")

elif choice == "2":
    print("You selected Option 2.")
elif choice == "3":
    print("You selected Option 3.")
elif choice == "4":
    print("You selected Option 4.")
elif choice == "5":
    print("You selected Option 5.")
else:
    print("Invalid choice. Please enter a number between 1 and 5.")