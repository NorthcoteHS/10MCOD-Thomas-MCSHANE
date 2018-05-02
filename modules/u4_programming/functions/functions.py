import time
import random
def hello():
    print("Hello World!")
hello()

def subtract(x,y,z):
    print ("Welcome to the number subtracter!"), time.sleep(1)
    x = input ("What is your first value?")
    z = input("Is, ", x , " your first value? (Yes or No)")
    while z == "No":
        x = input ("What is your first value?")
    if z == "Yes":
        y = input ("What is your second value?")
        a = x - y
        print ("The answer is, ", a)
    elif z == "No":
        done
subtract(x,y)
