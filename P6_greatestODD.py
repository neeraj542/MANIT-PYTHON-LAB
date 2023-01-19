'''#Problem-6:   Write a program which will allow user to enter 10 numbers and display largest odd
number from them. It will display appropriate message in case if no odd number is
found.'''
import array

numbers = [int(input("Enter a number: ")) for x in range(10)]
odds = [x for x in numbers if x % 2 == 1]
if len(odds) == 0:
    print("No odd numbers")
else:
    print("The largest odd number is", max(odds))