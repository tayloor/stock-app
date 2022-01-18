import yfinance as yf

# this is how you get all the data on a stock.
# MSFT is the ticker name for Microsoft
msft = yf.Ticker("MSFT")


# by calling msft.info, you get a dictionary of information about Microsoft.
# stuff like the number of employees in the company and the debt to equity ratio are included.
print('--- MICROSOFT INFO ---')
msft_info = msft.info

# here I just iterate through all values in the dictionary to print them
for key, value in msft_info.items():
    print(key, ' : ', value)



# you can also query the price action history with the history function.
# I specify a period of 1 month to view the history for the past month.
print('--- MICROSOFT STOCK HISTORY OVER PAST MONTH ---')
msft_history = msft.history(period="1mo")
print(msft_history)