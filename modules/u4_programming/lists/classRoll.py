import random
roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
print (roll[2])
enrolment = len(roll)
roll.append('James')
del roll[2]
roll[5] = 'Mike'
list.sort(roll)
print (roll)
list.reverse(roll)
print (roll)
print(random.choice(roll))
y = len(roll)
x = y//2
xx = x+1
firsthalf = roll[0:x]
secondhalf = roll[xx:y]
print (firsthalf)
print (secondhalf)
