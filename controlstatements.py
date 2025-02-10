# A python that checks for room temperature
from oparators import number

temperature = 23
if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")


# A program that returns  the largest number

first = 87
second = 50
third = 99

if first >second and first > third :
    print(first, "is the largest number")

elif second > first and second > third :
    print(second, "is the largest number")
else :
    print(third, " is the largest number")

# Program to check a number and return whether is odd or even

number = 56
if number == 0:
    print(number, "is a neutral number")

elif number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")