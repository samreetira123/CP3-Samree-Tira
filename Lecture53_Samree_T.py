def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice * 7 /100)
    return  result

print(vatCalculator(int(input("Total Price : "))))