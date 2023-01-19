'''#Problem-2: Write a program in python to swap two variables without using temporary variable.'''

x = int(input("Enter the value of x?"))
y = int(input("Enter the value of y?"))
print("before swapping numbers: %d   %d\n" %(x,y))

#swapping-concept---

x = x + y
y = x - y
x = x - y
print("After swapping: %d   %d\n"%(x,y))