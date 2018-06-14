"""
"""
import os
import time
import datetime
x=50
positive = ["good", "great", "ok", "fine", "pretty good"]
negative = ["trash", "bad", "not good", "tired", "bored", "shit"]
tips = ["The average adult needs about 9 cups of water a day!", "The beat of the music you listen to subconsiously effects your running speed!", "Working out at night can make it harder to sleep! Make sure you exercise during the day, especially in the morning!", "The healthy amount of exercise for the average adult is 7-9 Hours."]
print ("Welcome to the fitness planner!")
day = input ("How are you going on this fine " + datetime.date.today().strftime("%A") + "? : ")
if day in positive:
    print ("Thats good!"), time.sleep(1)
elif day in negative:
    print ("Well thats not good!"), time.sleep(1)
welcome = input("Would you like to enter? (Y or N) : ")
if welcome == "Y" or "y":
    while x>0:
        print (" ")
        x=x-1
    x = 50
    print ("Let's get started!")
    a = input("So firstly, how old are you? A. -18, B. 18-64, C. 65+ : ")
    if a == "A":
        ae = ("at least an hour of exercise a day")
        aeee = (" child")
        ree = (" you should have lots of everything, like meats, carbohydrates, dairy, and focus on having vitamin rich foods such as fruit of vegetables!")
    elif a =="B":
        ae = ("three to four hours of intensive exercise a week, but you should be active every daY")
        aeee = ("n adult")
        ree = ("you should eat lots of vegetables, legumes and fruit, as well as a lot of cerealsl, preferably wholegrain. And also other things such as poultry and lean meats")
    elif a =="C":
        ae = ("about half an hour a day, if possible")
        aeee = (" senior")
        ree = ("you should have a lot of lean meat, fruit and vegetables, as well as low-fat dairy.")
    h = int(input("Next, how tall are you? (in centimetres and a whole number) : "))
    w = int(input("Now, how much do you weigh? (in kilograms and a whole number) : "))
    bmi = w / h * 100 / h * 100
    while x>0:
        print (" ")
        x=x-1
    x = 50
    print ("So your BMI is ", bmi, "!"), time.sleep(3)
    print ("A healthy BMI is from 18.5 to 24.9"), time.sleep(1)
    if bmi < 18.5:
        print ("Because your BMI is ", bmi, " you are underweight"), time.sleep(1)
        r = "underweight"
        aee = "you need to make sure you don't overexercise."
    elif bmi > 18.5 and bmi < 24.9:
        print ("Your BMI is in the healthy range! You are neither under nor overweight!"), time.sleep(1)
        r = "healthy"
        aee = "this is a good amount."
    elif bmi > 24.9:
        print ("Because your BMI is ", bmi, " you are overweight"), time.sleep(10)
        r = "overweight"
        aee = "you may need a bit more.", time.sleep(1)
    while x>0:
        print (" ")
        x=x-1
    x = 50
    welcome = input ("Would you like to continue? (Y/N) : ")
    while welcome == "Y":
        facts = int(input("Would you like to learn about: 1. Exercise or 2. Diet : "))
        if facts == 1:
                print ("So you'd like to learn more about exercise!"), time.sleep(1)
                print ("The healthy amount of exercise for someone of your age is ", ae, " although being underweight and overeweight can affect this."), time.sleep(10)
                print ("Because you are ", r + " " + aee), time.sleep(10)
        elif facts == 2:
            print ("So you'd like to learn more about diet!"), time.sleep(1)
            print ("Because you are a" + aeee + " " + ree), time.sleep(5)
            print ("However because you are " + r + " " + re)
            
       