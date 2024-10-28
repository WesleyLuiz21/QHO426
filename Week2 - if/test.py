# Python Conditions and if statements

a = 222
b = 222

if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")


a2 = 200
b2 = 33
c2 = 500

if a2 > b2 and c2 > a2:
    print("\nBoth conditions are True")
else:
    print("\n Not Applicable")

x = 41

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("print less or equal to 10")

print("test")