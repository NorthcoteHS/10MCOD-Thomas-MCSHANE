"""
Program: Helloworld.py
Name:    Thomas Mcshane
Date:    22-02-2018
Desc:    Ask user about their day
"""
name = input('What is your name? ' )
print(name)

    # Ask what users name is
    
print('Hello' + " " + name + '! My name is Thomas!')
print('1. good')
print('2. bad')
print('3. ok')
print('4. great!')
print('5. dead')

    # Provide options for next question
    
you = input('So' + " " + name + "? " 'How are you? ' )
print(you + '?')

    # Ask user how they are
    
if you == ("good"):
    print ('Thats Good')
if you == ("1"):
    print ('Thats Good')
if you == ("bad"):
    print ('Thats Unfortunate')
if you == ("2"):
    print ('Thats Unfortunate')
if you == ("ok"):
    print ('Thats Pretty Good')
if you == ("3"):
    print ('Thats Pretty Good')
if you == ("great!"):
    print ('Awesome!')
if you == ("4"):
    print ('Awesome!')
if you == ("dead"):
    print ('R I P' + " " + name + " " + 'x_x')
if you == ("5"):
    print ('R I P' + " " + name + " " + 'x_x')
    
    # Provide if statements to reply to users answer

print('1. cats')
print('2. dogs')
print('3. dolphins')
print('4. birds')
print('5. reptiles')
print('6. fish')
print('7. insects')
print('8. sea creatures')
print('9. dinosaurs')
print('10. none of these')
animals = input('Which animal do you prefer out of these? ' )
print(animals)

    # Ask what animal the user likes
    
if animals == ("cats"):
    print('Aww, I prefer dogs but cats are ok')
if animals == ("dogs"):
    print('Ayyy, Dogs are awesome!')
if animals == ("birds"):
    print('Birds are cool, but magpies are annoying')
if animals == ("dolphins"):
    print('Dolphins are my favourite animal as well!')
if animals == ("reptiles"):
    print('I like snakes the most, but other reptiles are awesome as well')
if animals == ("fish"):
    print('Fish are the best!')
if animals == ("insects"):
    print('Insects can be annoying at times, but theyre really interesting')
if animals == ("sea creatures"):
    print('damn us humans for warming the oceans and killing sea creatures!')
if animals == ("dinosaurs"):
    print('Sorry to break it to you, but dinos are extinct xD')
if animals == ("none of these"):
    print('Hmm,Id like to know what animal you like, but we dont have time for that!')
if animals == ("1"):
    print('Aww, I prefer dogs but cats are ok')
if animals == ("2"):
    print('Ayyy, Dogs are awesome!')
if animals == ("3"):
    print('Birds are cool, but magpies are annoying')
if animals == ("4"):
    print('Dolphins are my favourite animal as well!')
if animals == ("5"):
    print('I like snakes the most, but other reptiles are awesome as well')
if animals == ("6"):
    print('Fish are the best!')
if animals == ("7"):
    print('Insects can be annoying at times, but theyre really interesting')
if animals == ("8"):
    print('damn us humans for warming the oceans and killing sea creatures!')
if animals == ("9"):
    print('Sorry to break it to you, but dinos are extinct xD')
if animals == ("10"):
    print('Hmm,Id like to know what animal you like, but we dont have time for that!')

    # If statements for the users replies

print('1. bye')
print('2. cya')
day = input('Bye' + " " + name + '!' ' ' 'Have a good day!')
print(day)

    # Say goodbye to user

