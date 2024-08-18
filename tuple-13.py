# in tuple we can't change his value or length...

tup = (1,2,3,True,"hello",54,23)
print(len(tup))
print(tup[3])
print(tup[-1])

if "hello" in tup:
    print("Yes present")
print(tup[1:6:2])
#  startIndes: endIndex: jumpIndex

