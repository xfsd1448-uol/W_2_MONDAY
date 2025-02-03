import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

print(distance(1,2,3,4))


def sum_even_numbers(list_of_numbers):
    total = 0
    for i in list_of_numbers:
        if i % 2 == 0:
            total += i
    return total

print(sum_even_numbers([1,2,3,4,5,6]))