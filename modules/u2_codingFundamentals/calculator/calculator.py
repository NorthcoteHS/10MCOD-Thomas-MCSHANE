import random
import time
print("Welcome to the calculator!"), time.sleep(1)
x = int(input("What is your first number?"))
y = int(input("What is your second number?"))
z = input("Would you like to times, add, subtract, or divide?")
if z == "times":
    a = x*y
    print("The answer is, ", a), time.sleep(3)
if z == "add":
    a = x+y
    print("The answer is, ", a), time.sleep(3)
if z == "subtract":
    a = x-y
    print("The answer is, ", a), time.sleep(3)
if z == "divide":
    a = x/y
    print("The answer is, ", a), time.sleep(3)
print("Goodbye")
