stores = {
    "apple" : 7,
    "banana" : 3,
    "orange" : 10,
    "mango" : 4
}

for item, count in stores.items():
    if count < 5:
        print(item)