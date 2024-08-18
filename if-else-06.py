#            if else statements

age = int(input("Enter your age:    "))
print("Your age is /",age)
if(age>=18):
    print("You can drive")
else:
    print("You can't drive.")
print(" ********************************************************************")
budget = 100
applePrice = 110
if (applePrice <= budget):
    print("Give me 1kg apple")
else:
    print("Don't give me apple")
print(" ********************************************************************")
value = int(input("Enter the value of number: "))
if (value > 0):
    print("The value is positive.")
elif (value == 0):
    print("The value is zero.")
elif (value < 0):
    print("The value is negative.")
print(" ********************************************************************")
age1 = int(input("Enter your age: "))
edu = int(input("Enter your education :"))
if (age1>=15):
    if(edu>=10):
        print("You can learn programing")
    else:
        print("You can't learn programming because you have not matric certificate.")
else:
    print("You can't programming because your age is < 15")