import requests
import csv

quotes = {}
quotes['AAPL'] = requests.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=cb68d8iad3i70tu610c0").json()

quotes['AMZN'] = requests.get("https://finnhub.io/api/v1/quote?symbol=AMZN&token=cb68d8iad3i70tu610c0").json()

quotes['NFLX'] = requests.get("https://finnhub.io/api/v1/quote?symbol=NFLX&token=cb68d8iad3i70tu610c0").json()

quotes['META'] = requests.get("https://finnhub.io/api/v1/quote?symbol=META&token=cb68d8iad3i70tu610c0").json()

quotes['GOOGL'] = requests.get("https://finnhub.io/api/v1/quote?symbol=GOOGL&token=cb68d8iad3i70tu610c0").json()

most_volatile_stock = {}
for quote in quotes:
    
    #initialize the most_volatile_stock variable to the first quote
    if len(most_volatile_stock)==0:
        most_volatile_stock_symbol = quote
        most_volatile_stock[quote]= quotes[quote]
      
    # check for the one with high percentage change    
    if(abs(most_volatile_stock[most_volatile_stock_symbol]['dp'])<abs(quotes[quote]['dp'])):
        most_volatile_stock.clear()
        most_volatile_stock_symbol = quote
        most_volatile_stock[quote] = quotes[quote]
    
with open('csv_file.csv', 'w') as f:
    writer = csv.writer(f)
    
    #the header for the CSV file
    header = ["stock_symbol","percentage_change","current_price","last_close_price"]
    writer.writerow(header)
    
    #loop through most_volatile_stock to get needed data
    for key, value in most_volatile_stock.items():
        writer.writerow([key, value['dp'], value['c'], value['pc']])
    