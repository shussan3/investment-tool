# import yfinance as yf #financial data source
# import json #saving data to file 

# def fetch_stock_info(ticker):
#     """ Fetch and organize key metrics for a given ticker.
#     Return error message if problem with retreiving data from API"""
#     try:
#         stock = yf.Ticker(ticker)
#         info = stock.info
#         metrics = {
#             "Valuation Metrics": {
#                 "Name": info.get("longName"),
#                 "Sector": info.get("sector"),
#                 "Industry": info.get("industry"),
#                 "Market Cap": info.get("marketCap"),
#                 "Current Price": info.get("currentPrice"),
#                 "52-Week High": info.get("fiftyTwoWeekHigh"),
#                 "52-Week Low": info.get("fiftyTwoWeekLow"),
#                 "Price-to-Book Ratio": info.get("priceToBook"),
#                 "Dividend Yield": info.get("dividendYield"),
#                 "Revenue Growth": info.get("revenueGrowth"),
#                 },
#             "Performance Metrics": {
#                 "Revenue Growth (YoY)": info.get("revenueGrowth"),
#                 "Profit Margin": info.get("profitMargins"),
#                 "Gross Margin": info.get("grossMargins"),
#                 "Operating Margin": info.get("operatingMargins"),
#                 "Return on Assets (ROA)": info.get("returnOnAssets"),
#                 "Return on Equity (ROE)": info.get("returnOnEquity"),
#             },        
#         }
#         return metrics
#     except Exception as e: 
#         print(f"Error fetching data for {ticker}: {e}")
#         return {}

# def validate_ticker(ticker):
#     try:
#         stock = yf.Ticker(ticker)

# def display_metrics(metrics):
#     """Display grouped metrics in a readable format"""
#     for category, category_metrics in metrics.items(): 
#         print(f"\n{category}:")
#         for key, value in category_metrics.items():
#             print(f" {key}: {value}")


# # def save_metrics_to_file(metrics, filename = "stock_metrics.json"):
# #     """Save metrics to JSON file"""
# #     try: 
# #         with open(filename, "w") as file: 
# #             json.dump(metrics, file, indent=4)
# #         print(f"Metrics saaved to {filename}")
# #     except Exception as e:
# #         print(f"Error saving metrics to file: {e}")



# if __name__ == "__main__":
#     ticker = input("Enter one or more stock tickers separated by commas").strip().split(",") 
#     tickers = [ticker.strip().upper() for ticker in tickers] #cleaning input
#     for ticker in tickers:
#         if validate_tickers(ticker)
#         metrics = fetch_stock_info(ticker)
#         display_metrics(metrics)


import yfinance as yf
import json
import pandas as pd

def get_tickers():
    # get user input
    user_input = input("enter stock tickers separated by commas: ")

    # split and edit inputs for processing 
    tickers = [ticker.strip().upper() for ticker in user_input.split(",")]

    # validate tickers
    valid_tickers = []
    for ticker in tickers:
        if ticker.isalnum(): #alpha numeric
            valid_tickers.append(ticker)
        else:
            print(f"invalid ticker: {ticker}")

    return valid_tickers

def fetch_multiple_stocks(valid_tickers):
    all_data = {} #initialize a dictionary to store the data

    for ticker in valid_tickers:
        try: 
            stock = yf.Ticker(ticker)
            info = stock.info
            all_data[ticker] = {
                "Name": info.get("longName"),
                "Sector": info.get("sector"),
                "Industry": info.get("industry"),
                "Market Cap": info.get("marketCap"),
                "Current Price": info.get("currentPrice"),
                "52-Week High": info.get("fiftyTwoWeekHigh"),
                "52-Week Low": info.get("fiftyTwoWeekLow"),
                "Price-to-Book Ratio": info.get("priceToBook"),
                "Dividend Yield": info.get("dividendYield"),
                "Revenue Growth": info.get("revenueGrowth"),
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return all_data


if __name__ == "__main__":
    valid_tickers = get_tickers()       #storing tickers that are valid
    stock_data = fetch_multiple_stocks(valid_tickers)   #run valid tickers through info gathering function
    print(f"Validated Tickers: {valid_tickers}")
    print(json.dumps(stock_data, indent=4))
