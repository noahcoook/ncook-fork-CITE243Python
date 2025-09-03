import sys

def rectangle():
    length = int(input('please enter rectangle length: '))
    width = int(input('please enter rectangle width: '))
    area = print('the area is ', str(length * width), '.')
    return area

def circle():
    radius = int(input('please enter circle radius: '))
    circum = 3.14159 * (radius ** 2)
    area = 2* 3.14159 * radius
    area = str(round(area, 2)) #rounds down area to 2 places, also converts that value into a str
    circum = str( round (circum , 2)) #same but for circum
    return print('youre circle area is ', area, ', youre circumference is ', circum, '.')

user_input = input("would you like to find area of rectangle or circle? ")

if user_input == 'circle' or user_input == 'Circle':
    circle()
    sys.exit()
 
if user_input == 'rectangle' or user_input == 'Rectangle':
    rectangle()
    sys.exit
    