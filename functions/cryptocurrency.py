import requests

def currency_exchange_rates(first_currency, second_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={first_currency}&to_currency={second_currency}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def cryptocurrency_exchange(first_currency, second_currency, api_key):
    valid_ticker = True
    if valid_ticker:
        try:
            cryptocurrency_data = currency_exchange_rates(first_currency, second_currency, api_key)
            from_currency_code = cryptocurrency_data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
            to_currency_code = cryptocurrency_data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
            exchange_rate = cryptocurrency_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

        except KeyError as e:
            print(f"encountered error (cryptocurrency): {e}")
            valid_ticker = False
    if valid_ticker:
        try:
            print("\n----------------------------")
            print("\n" + "The current exchange rate between " + first_currency + "/" + second_currency + " is " + exchange_rate + ".\n")
            print("----------------------------")
        except:
            print("Error printing out the details!")