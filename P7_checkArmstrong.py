'''#Problem-7: Write a Python program to check if the number provided by the user is an Armstrong
number.'''

x = int(input("Check number is armstrong or not? \n Enter number: "))
sum = 0
temp = x

while x>0:
    remainder = x % 10
    sum = sum + pow(remainder, 3)
    x = x/10

if sum==temp:
    print("Yes, Armstrong")
else:
    print("No")
