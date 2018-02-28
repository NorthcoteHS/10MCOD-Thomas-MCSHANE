import time
import os
x = int(input('Time? ' ))
print ('1. Minecraft')
print ('2. Overwatch')
print ('3. CSGO')
print ('4. GMOD')
y = input('Game Name? ' )
while x > 0:
    x=x-1
    print (x), time.sleep(1),
if x == 0 and y == ('Minecraft'):
    print ('done')
    os.system("start D:\Minecraft\MinecraftLauncher.exe")
if x == 0 and y == ('Overwatch'):
    print ('done')
    os.system("start D:/Overwatch/Overwatch.exe")
if x == 0 and y == ('CSGO'):
    print ('done')
    os.system("start D:/Steam/Steam.exe"), time.sleep(10)
    os.system("start D:/Steam/steamapps/common/CSGO/csgo.exe")
if x == 0 and y == ('GMOD'):
    print ('done')
    os.system("start D:/Steam/Steam.exe"), time.sleep(10)
    
    os.system("start D:/Steam/steamapps/common/GarrysMod/hl2.exe")
if x == 0 and y == ('1'):
    print ('done')
    os.system("start D:\Minecraft\MinecraftLauncher.exe")
if x == 0 and y == ('2'):
    print ('done')
    os.system("start D:/Overwatch/Overwatch.exe")
if x == 0 and y == ('3'):
    print ('done')
    os.system("start D:/Steam/Steam.exe"), time.sleep(10)
    os.system("start D:/Steam/steamapps/common/CSGO/csgo.exe")
if x == 0 and y == ('4'):
    print ('done')
    os.system("start D:/Steam/Steam.exe"), time.sleep(10)
    os.system("start D:/Steam/steamapps/common/GarrysMod/hl2.exe")
