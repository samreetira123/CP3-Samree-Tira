print("Welcome, please login. ^^")
username = input("Username : ")
password = input("Password : ")

if username == "Samree" and password == "Tira" :
    print("Welcome to Fruit Shop",username,"!")
    print("------------------- Menu Fruit --------------------")
    print("1.pumpkin",30,"THB/kilogram")
    print("2.Bananas",20,"THB/kilogram")
    print("3.Coconat",26,"THB/kilogram")
    print("4.kiwi"   ,80,"THB/kilogram")
    print("5.melon"  ,45,"THB/kilogram")
    print("6.mango"  ,20,"THB/kilogram")
    print("------------------------------------------------")
    pumpkin = int(input("How many pumpkin would you like?"))
    Bananas = int(input("How many Bananas would you like?"))
    Coconat = int(input("How many Coconat would you like?"))
    kiwi  = int(input("How many kiwi would you like?"))
    melon  = int(input("How many melon would you like?"))
    mango  = int(input("How many mango would you like?"))
    totals = pumpkin*30 + Bananas*20 + Coconat*26 + kiwi*80 + melon*45 + mango*20
    print("Total",totals,"THB")
else :
    print("Wrong !!! Please try again.")

