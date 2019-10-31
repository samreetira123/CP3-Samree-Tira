userinput = int(input())
sum = 0
for x in range(userinput):
        print(" "*(userinput-x)+"*"*(sum+1))
        sum = sum + 2