import random
import time
import ctypes
import os
import webbrowser
from colorama import Fore
from colorama import Style
# open webbrowser and run music (example) and use alt-tab to return to the program
webbrowser.open('https://www.youtube.com/watch?v=VBlFHuCzPgY'), time.sleep(1)
user32 = ctypes.windll.user32
user32.keybd_event(0x12, 0, 0, 0)
time.sleep(1)
user32.keybd_event(0x09, 0, 0, 0)
time.sleep(1)
user32.keybd_event(0x09, 0, 2, 0)
time.sleep(0.1)
user32.keybd_event(0x12, 0, 2, 0)
c = ["black", "white", "blue", "green", "yellow", "red"]
i = input ("Welcome to the sorting hat quiz! Would you like to play? (N for no) ")
if i == "Y" or "y":
    print ("For each answer type 'A', 'B', 'C', or 'D'")
    q = ["What is your age? <25 (A), 26 - 50 (B), 51- 75 (C), 76+ (D) ", "How would your friends describe you? Smart (A), Cunning (B), Courageous (C), Loyal (D) ", "Which element best suits you? Water (A), Earth (B), Fire (C), Hufflepuff (D) ", "Which animals do you prefer? Birds (A), Reptiles (B), Cats (C), Dogs (D) ", "Which of these places would you want to live in? U.K (A), Japan (B), Ausralia (C), Other (D) ", ]
    random.shuffle(q)
    a = 0
    b = 0
    c = 0
    d = 0
    for i,item in enumerate (q):
        ask = input(item)
        if ask == "A":
            a = a + 1
        elif ask == "B":
            b = b + 1
        elif ask == "C":
            c = c + 1
        elif ask == "D":
            d = d + 1
        del q[i]
    if a > b and a > c and a > d:
        print ("You are a Ravenclaw!")
        print ("You are intelligent and seek knowledge, this is the same house as me,well done!")
    elif b > a and b > c and b > d:
        print ("You are a Slytherin!")
        print ("You are cunning, and will do anything to achieve your goals, most dark wizards have been Slytherin.")
    elif c > a and c > b and c > d:
        print ("You are Gryffindor!")
        print ("You are brave and aren't afraid to help those in need, though you can be a bit foolish at times.")
    elif d > a and d > b and d > c:
        print ("You are a Hufflepuff!")
        print ("You are a hard worker, and are dedicated to your tasks. You are also totally loyal to your friends!")
    else:
        print ("You are divergent!")
        print ("You have gotten one or more other houses! Meaning you have the qualities of two to four houses!")
    time.sleep(10)
    print ("Bye!")
else:
    print ("Goodbye! :(")
