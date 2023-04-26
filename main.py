# documentation: https://www.alphavantage.co/documentation/

import requests

api_key = "N20TDIL2VOIJS399"

print("\nSelect an option \n ==== MENU ====")

menu_items = ["Stocks", "Forex", "Crypto", "Commodities", "Economic Indicators"]

for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

choice = input("Enter your choice (1-5): ")

if choice == "1":

    stock_ticker = input("Type your desired stock ticker and return. ")

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_ticker}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    price = data['Global Quote']['05. price']

    print(f"The current price of {stock_ticker} as of {data['Global Quote']['07. latest trading day']} is: {price}")

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


