# documentation: https://www.alphavantage.co/documentation/

import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "N20TDIL2VOIJS399"

def get_global_quote_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()["Global Quote"]

def get_monthly_adjusted_data(stock_ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()["Monthly Adjusted Time Series"]

print("\nSelect an option \n ==== MENU ====")

menu_items = ["Stocks", "Forex", "Crypto", "Commodities", "Economic Indicators"]

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

choice = input("Enter your choice (1-5): ")

if choice == "1":

    stock_ticker = input("Type your desired stock ticker and return. ")

    # Stock Daily Quote
    global_quote_data = get_global_quote_data(stock_ticker, api_key)
    day = global_quote_data["07. latest trading day"]
    price = global_quote_data["05. price"]
    print(f"The current price of {stock_ticker} as of {day} is: {price}")

    # Stock Full Chart
    time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, api_key)
    df = pd.DataFrame.from_dict(time_series_monthly_adjusted_data, orient="index")
    df.index = pd.to_datetime(df.index)
    prices = df["5. adjusted close"].astype(float).resample("M").last()
    axis = prices.plot(title=f"{stock_ticker} Historical Monthly Adjusted Close Prices")
    axis.set_xlabel("Year")
    axis.set_ylabel("PRice")

    # Save & Show
    plt.savefig("stockimage.png")
    plt.show()

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