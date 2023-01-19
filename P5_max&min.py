'''#Problem-5:  Write a program in python to find out maximum and minimum number out of three
user entered number.'''

x = int(input("Enter 1st no: "))
y = int(input("Enter Second no: "))
z = int(input("Enter third no: "))

if (x>y):
    if (x>z):
        print("x is greatest number.")
    else:
        print("z is greatest number.")
elif (y>z):
    print("y is greatest number.")
else:
    print("z is greatest number.")
