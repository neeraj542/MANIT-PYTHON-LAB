'''#Problem-3: Write a Python Program to Convert Decimal to Binary, Octal and Hexadecima'''

dec = int(input("Enter decimal: "))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")