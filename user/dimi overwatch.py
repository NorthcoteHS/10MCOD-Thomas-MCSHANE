import time
import os
x = int(input('Time until launch? ' ))
print ('1. Overwatch')
y = input('Game Name? ' )
while x > 0:
    x=x-1
    print (x), time.sleep(1),
if x == 0 and y == ('Overwatch'):
    print ('done')
    os.system("start C:/Program Files (x86)/Overwatch/Overwatch.exe")
if x == 0 and y == ('1'):
    print ('done')
    os.system("start C:/Program Files (x86)/Overwatch/Overwatch.exe")
