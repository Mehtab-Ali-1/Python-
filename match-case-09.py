x = int(input("Enter your x value: "))
match x:
    case 0:
        print("Your value is zero")
    case _ if x % 2==0:
        print("This value can divide by 2")
    case _ if x % 3==0:
        print("This value can divide by 3")    
    case _ if x != 90:
        print(x,"is not 90") 
    case _ if (x !=70):
        print(x,"is not 70")
    case _:                #   this is for defualt value
        print(x)
