stores = [
    {
        "name" : "apple",
        "quantity" : 10,
        "price" : 10000
    },
    {
        "name" : "banana",
        "quantity" : 4,
        "price" : 15000
    }
]

for item in stores:
    if item["quantity"] < 5:
        print(item["name"])