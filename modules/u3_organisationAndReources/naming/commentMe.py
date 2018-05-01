"""
Prog: circCalc.py
Name: Tom
Date: 2018/05/01
Desc: Calculate area and perimeter of a circle
"""
# Welcome User
print('Welcome to the Circle Calculator!')
# Ask User for Radius
r = input('Enter a radius: ')
r = int(r)
# Calculate and print are
area = 3.14 * r * r
print('The area is', area)
# Calculate and print perimeter
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
