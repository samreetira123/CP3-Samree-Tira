def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice * 7 /100)
    return  result

totalPrice = int(input("Total Price : "))
print(vatCalculator(totalPrice))
