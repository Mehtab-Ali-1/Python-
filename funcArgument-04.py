# Function Arguments and return statement:
# There are four types of arguments that we can provide in a function:
# - Default Arguments
# - Keyword Arguments
# - Various length Arguments
# - Required Arguments

#          (Default Arguments)
def average (a,b=4):
    print("The average of this value is",(a+b)/2)
average(4)

#         (Required Arguments)
def req (a,b):
    print(a+b)
req(b="haseeb",a="Muhammad")    # if i want to write first b then i will write (b = "")

#         (Various length arguments)
def average1 (*numbers):
    sum = 0 
    for i in numbers:
        sum = sum + i 
    # print("Average is: ", sum / len(numbers))
    return  sum / len(numbers)
# average(3,2,6)
c = average1(8,5,2,6)
print(c)