def rectangle():
    length = int(input('please enter rectangle length: '))
    width = int(input('please enter rectangle width: '))
    area = print('the area is ', str(length * width), '.')
    return area

def circle():
    radius = int(input('please enter circle radius: '))
    circum = 3.14159 * (radius ** 2)
    area = 2* 3.14159 * radius
    area = str(round(area, 2))
    circum = str( round (circum , 2))
    return print('youre circle area is ', area, ', youre circumference is ', circum, '.')

#rectangle()
circle()