marks = [1,2,3,"hello",True,"why",34,434,32,56]
print(marks)
print(marks[-2])          # negative index
print(len(marks)-2)       # convert positive index

if 3 in marks:
    print("Yes")
else:
    print("No")
if "hel" in "hello":
    print("YES")
else:
    print("NO")
    
print(marks)
print(marks[1:9])         # from Starting & ending index
print(marks[1:9:3])       # the third value is jumping index
print(marks[:])           # default python:    print(marks[0:len(marks)])
print(marks[2:])          # default from ython: print(marks[2:len(marks)])
print(marks[:4])          # default from python: print(marks[0:4])