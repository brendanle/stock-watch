# documentation: https://www.alphavantage.co/documentation/

import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "N20TDIL2VOIJS399"
valid_ticker = True

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

def currency_exchange_rate(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={first_currency}&to_currency={second_currency}&apikey=demo"
    response = requests.get(url)
    return response.json()

print("\nSelect an option \n ==== MENU ====")

menu_items = ["Stocks", "Forex", "Crypto", "Commodities", "Economic Indicators"]

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

choice = input(f"Enter your choice (1-{len(menu_items)}): ")

if choice == "1":

    stock_ticker = input("Type your desired stock ticker and return. ")

    # Overview
    if valid_ticker:
        try:
            # overview_data = get_overview(stock_ticker, "demo")
            overview_data = get_overview(stock_ticker, api_key)
            symbol = overview_data["Symbol"]
            name = overview_data["Name"]
            description = overview_data["Description"]
            exchange = overview_data["Exchange"]
        except KeyError as e:
            print(f"encountered error (overview): {e}")
            valid_ticker = False

    # Global Quote
    if valid_ticker:
        try:
            # global_quote_data = get_global_quote_data(stock_ticker, "demo")
            global_quote_data = get_global_quote_data(stock_ticker, api_key)
            day = global_quote_data["07. latest trading day"]
            price = global_quote_data["05. price"]
        except KeyError as e:
            print(f"encountered error (global quote): {e}")
            valid_ticker = False

    # Chart
    if valid_ticker:
        try:
            # time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, "demo")
            time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, api_key)
            df = pd.DataFrame.from_dict(time_series_monthly_adjusted_data, orient="index")
            df.index = pd.to_datetime(df.index)
            prices = df["5. adjusted close"].astype(float).resample("M").last()
            axis = prices.plot(title=f"{stock_ticker} Historical Monthly Adjusted Close Prices")
            axis.set_xlabel("Year")
            axis.set_ylabel("PRice")
        except KeyError as e:
            print(f"encountered error (chart): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "[" + day + "] " + symbol + " - " + price + "\n\n" + description + "\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")

    # Save & Show
    if valid_ticker:
        plt.savefig("stockimage.png")
        plt.show()
    else:
        print("Couldn't plot.")

elif choice == "2":

    #forex
    first_currency = input("Enter the first currency index you would like to see the exchange rate for. ")
    second_currency = input("Enter the second currency index you would like to see the exchange rate for. ")

    if valid_ticker:
        try:
            currency_exchange_rate_data = currency_exchange_rate(first_currency, second_currency, "demo")
            from_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
            to_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
            exchange_rate = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        except KeyError as e:
            print(f"encountered error (currency exchange rate): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "The current exchange rate between " + first_currency + " and " + second_currency + " is " + exchange_rate + ".\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")

elif choice == "3":
    print("You selected Option 3.")
elif choice == "4":
    print("You selected Option 4.")
elif choice == "5":
    print("You selected Option 5.")
else:
    print("Invalid choice. Please enter a number between 1 and 5.")