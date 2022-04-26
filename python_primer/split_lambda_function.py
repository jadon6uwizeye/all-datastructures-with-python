items = {
    "price" : 10,
    "price2": 15,
    "price3":9
}

        
print(list(filter(lambda item: items[item] > 10, items)))