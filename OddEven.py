#creating own exception from main exception class

class OddEvenException(Exception):
    pass

try:
    userchoice = int(input("Enter number"))
    if userchoice % 2 ==0:
        print(str(userchoice) + " is an EVEN number")

    else:
        print(str(userchoice) + "is an ODD number")

except OddEvenException:
    print("sORRY! Not valid integer value")