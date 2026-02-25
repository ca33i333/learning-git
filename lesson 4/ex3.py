names = ["book", "pen", "notebook", "pencil", "eraser"]
quantities = [10, 20, 30, 40, 50]
prices = [10000, 20000, 30000, 40000, 50000]

def buyProduct(name, quantity, price):
    global names, quantities, prices
    # thêm thông tin trên vào danh sách.
    names.append(name)
    quantities.append(quantity)
    prices.append(price)
    return names, quantities, prices

def customerQuestion(name, quantity):
    global names, quantities, prices
    # kiểm tra xem sản phẩm có trong danh sách còn có để bán hay không.

print(buyProduct("apple", 3, 10000))