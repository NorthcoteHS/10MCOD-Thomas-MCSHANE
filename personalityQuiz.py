import random
import time
welcome = input("Welcome to the hogwarts house quiz, would you like to play? (1 for yes, 2 for no)")
if welcome == 2:
    print ("Goodbye")
else:
    questions = ["How old are you? >14 (1), 15-24(2), 25-34(3), 35-44(4), 45+(5)", "What is your favourite colour? Green (1), Red (2), Yellow (3), Blue (4)"]
    answers = ["Ravenclaw", "Gryffindor", "Hufflepuff", "Slytherin"]
    for i,item in enumerate (questions):
        n=0
        ask = input(item)
        if ask == 1:
            n = n + 0
        if ask == 2:
            n = n + 1
        if ask == 3:
            n = n + 2
        if ask == 4:
            n = n + 3
        if ask == 5:
            n = n + 4
        del questions[i]
        print (n)
