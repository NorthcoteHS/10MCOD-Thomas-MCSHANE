import time
import os
x = int(input('Time for (seconds)? ' ))
while x > 0:
    x=x-1
    print (x), time.sleep(1),
if x == 0:
    print ('done')
    os.system("start C:/Users/Tom/Downloads/Ghoul.mp3")
    

    

