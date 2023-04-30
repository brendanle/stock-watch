from functions import commodities
from functions import economic_indicators
from functions import forex
from functions import stocks
from functions import cryptocurrency

# Free to use, but limited. Register for an API Key here https://www.alphavantage.co/support/#api-key
api_key = "N20TDIL2VOIJS399"

def main():

    print("\nSelect an option \n ==== MENU ====")
    menu_items = ["Stocks", "Forex", "Commodities", "Economic Indicators", "Cryptocurrencies"]

    for i in range(len(menu_items)):
        print(f"{i+1}. {menu_items[i]}")

    choice = input(f"Enter your choice (1-{len(menu_items)}): ")

    if choice == "1":
        stock_ticker = input("Enter the stock ticker: ")
        stocks.plot_stock_data(stock_ticker, api_key)

    elif choice == "2":
        first_currency = input("Enter the first currency index you would like to see the exchange rate for. ")
        second_currency = input("Enter the second currency index you would like to see the exchange rate for. ")
        forex.plot_forex_data(first_currency, second_currency, api_key)

    elif choice == "3":
        commodity = input("[WTI, BRENT, NATURAL_GAS, COPPER, ALUMINUM, WHEAT, CORN, COTTON, SUGAR, COFFEE, ALL_COMMODITIES]\nEnter a commodity. ")
        commodities.plot_commodities(commodity, api_key)

    elif choice == "4":
        indicator = input("[REAL_GDP, REAL_GDP_PER_CAPITA, TREASURY_YIELD, CPI, INFLATION, RETAIL_SALES, DURABLES, UNEMPLOYMENT, NONFARM_PAYROLL]\nEnter an economic indicator: ")
        if indicator == "TREASURY_YIELD":
            maturity = input("\n[3month, 2year, 5year, 7year, 10year, 30year]\nEnter the time stamp you would like to access. ")
            economic_indicators.plot_economic_indicator_treasury_yield(maturity, api_key)
        else:
            economic_indicators.plot_economic_indicator(indicator, api_key)

    elif choice == "5":
        first_currency = input("Enter the first currency index you would like to see the exchange rate for. ")
        second_currency = input("Enter the second currency index you would like to see the exchange rate for. ")
        cryptocurrency.cryptocurrency_exchange(first_currency, second_currency, api_key)

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()