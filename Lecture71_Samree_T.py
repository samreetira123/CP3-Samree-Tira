menuList = []
priceList = []
def showBill():
    print("------ ร้านยายตุ๋ย ------")
    for number in range(len(menuList)) :
        print(menuList[number],priceList[number])
def checkBill():
    print("--------------------")
    Total = 0
    for x in range(len(priceList)):
            Total += int(priceList[x])
    print("รวม :",Total,"บาท")

while True :
    menuName = input("โปรดใส่เมนูอาหาร : ")
    if menuName.lower() == "exit" :
        break
    else :
        menuPrice = input("ราคา : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
checkBill()