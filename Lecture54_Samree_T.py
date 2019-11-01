def userLogin():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234" :
        ShowMenu()
    else :
        print("Wrong !!!")
        userLogin()

def ShowMenu():
    print("-------------- SKL Shop -----------")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    print("-----------------------------------")
    menuSelect()

def menuSelect():
    menu = int(input("Pressed Menu 1-2 :"))
    if menu == 1 :
        print(vatCalculator(int(input("TotalPrice : "))))
    elif menu == 2 :
        print(priceCalcultor())
    return menu

def vatCalculator(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return  "TotalPrice[VAT] "+str(result)+" THB"

def priceCalcultor():
    price1 = int(input("Price 1 : "))
    price2 = int(input("Price 2 : "))
    totalPrice = price1+price2
    return vatCalculator(totalPrice)

print(userLogin())