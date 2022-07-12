import csv
most_volatile_stock = {'NFLX': {'c': 177.34, 'd': -9.635, 'dp': -5.1531, 'h': 184.99, 'l': 176.89, 'o': 184.73, 'pc': 186.975, 't': 1657569602}}
with open('csv_file.csv', 'w') as f:
    writer = csv.writer(f)

    header = ["stock_symbol","percentage_change","current_price","last_close_price"]
    writer.writerow(header)
    for key, value in most_volatile_stock.items():
        writer.writerow([key, value['dp'], value['c'], value['pc']])