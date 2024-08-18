print("Hello World");
# if i want to write seperate text...
print("Hello",3,6,sep="-");
# if i want to write some text in new line...
print("Hello, Friends\n how are you");
print("I\'m good");
# if you want that when statement is end then print some text or numbers...
print("hey everyone, what are you doing",end="0099\n");  # if i don't write \n in this line the next line also start with this line...
print("next line");

# Variable & dataTypes
a = "Hello";
print(type(a));
b = 123;
print(type(b));
c = True;
print(type(c));
d = None;
print(type(d));

# Arithematic Operators
print(2+1);      # Addition 
print(2-1);      # Substraction
print(2*1);      # Multiplication
print(16/3);     # division
print(14//3);    # Floor division operator
print(5%3);      # Modulus
print(3**3)      # Exponential

# Data Types
#convert data type str to int...
aa = "3";
bb = "5";
# add = int(aa) + int(bb);  (OR)
print(int(aa)+ int(bb));

# Input
inpu = input("Enter your name: ");
print("My name is ",inpu);
# Input calculate with data types
x = input("Enter your first number: ");
y = input("Enter your second number");
addi = int(x)+int(y);
print("Your total is" ,addi);