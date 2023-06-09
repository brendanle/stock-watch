# documentation: https://www.alphavantage.co/documentation/

import requests
import numpy as np
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
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def currency_exchange_rate(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={first_currency}&to_currency={second_currency}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def fx_monthly(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={first_currency}&to_symbol={second_currency}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def commodities(commodity, api_key):
    url = f"https://www.alphavantage.co/query?function={commodity}&interval=monthly&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def economic_indicator(indicator, api_key):
    url = f"https://www.alphavantage.co/query?function={indicator}&interval=annual&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def economic_indicator_treasury_yield(maturity, api_key):
    url = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity={maturity}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

print("\nSelect an option \n ==== MENU ====")

menu_items = ["Stocks", "Forex/Crypto", "Commodities", "Economic Indicators"]

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

choice = input(f"Enter your choice (1-{len(menu_items)}): ")

if choice == "1":

    stock_ticker = input("Type your desired stock ticker and return. ")

    # Overview
    if valid_ticker:
        try:
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
            global_quote_data = get_global_quote_data(stock_ticker, api_key)
            day = global_quote_data["07. latest trading day"]
            price = global_quote_data["05. price"]
        except KeyError as e:
            print(f"encountered error (global quote): {e}")
            valid_ticker = False

    # Chart
    if valid_ticker:
        try:
            time_series_monthly_adjusted_data = get_monthly_adjusted_data(stock_ticker, api_key)
            df = pd.DataFrame.from_dict(time_series_monthly_adjusted_data, orient="index")
            df.index = pd.to_datetime(df.index)
            prices = df["5. adjusted close"].astype(float).resample("M").last()
            axis = prices.plot(title=f"{stock_ticker} Historical Monthly Adjusted Close Prices")
            axis.set_xlabel("Year")
            axis.set_ylabel("Price")
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

    first_currency = input("Enter the first currency index you would like to see the exchange rate for. ")
    second_currency = input("Enter the second currency index you would like to see the exchange rate for. ")

    if valid_ticker:
        try:
            currency_exchange_rate_data = currency_exchange_rate(first_currency, second_currency, api_key)
            from_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
            to_currency_code = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
            exchange_rate = currency_exchange_rate_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        except KeyError as e:
            print(f"encountered error (currency exchange rate): {e}")
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
            print(f"encountered error (chart): {e}")
            valid_ticker = False

    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "The current exchange rate between " + first_currency + "/" + second_currency + " is " + exchange_rate + ".\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")

    if valid_ticker:
        plt.savefig("stockimage.png")
        plt.show()
    else:
        print("Couldn't plot.")

elif choice == "3":

    commodity = input("[WTI, BRENT, NATURAL_GAS, COPPER, ALUMINUM, WHEAT, CORN, COTTON, SUGAR, COFFEE, ALL_COMMODITIES]\nEnter a commodity. ")

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
            print(f"encountered error (chart): {e}")
            valid_ticker = False

    if valid_ticker:
        plt.savefig("stockimage.png")
        plt.show()
    else:
        print("Couldn't plot.")

elif choice == "4":

    indicator = input("[REAL_GDP, REAL_GDP_PER_CAPITA, TREASURY_YIELD, CPI, INFLATION, RETAIL_SALES, DURABLES, UNEMPLOYMENT, NONFARM_PAYROLL\nEnter a commodity. ")

    if indicator == "TREASURY_YIELD":

        #By default, maturity=10year. Strings 3month, 2year, 5year, 7year, 10year, and 30year are accepted.
        maturity = input("\n[3month, 2year, 5year, 7year, 10year, 30year]\nEnter the time stamp you would like to access. ")

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
            print(f"encountered error (chart): {e}")
            valid_ticker = False

        if valid_ticker:
            plt.savefig("stockimage.png")
            plt.show()
        else:
            print("Couldn't plot.")
    else:
        if valid_ticker:
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
                print(f"encountered error (chart): {e}")
                valid_ticker = False

        if valid_ticker:
            plt.savefig("stockimage.png")
            plt.show()
        else:
            print("Couldn't plot.")

else:
    print("Invalid choice. Please enter a number between 1 and 5.")