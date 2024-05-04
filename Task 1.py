import math


mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]


def is_square(num):
    if num < 0:
        return False  
    sqrt = math.sqrt(num)
    return sqrt == int(sqrt) 


square_numbers = [num for num in mylist if is_square(num)]


print("Kvadratı olanededler:", square_numbers)
