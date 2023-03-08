import math


# simple math problems

# Area of a circle:
def circle_area(r):
    if r == 0:
        raise ValueError("Can't use 0 ar the radius")
    else:
        area = math.pi * r ** 2
        print(round(area))
        return round(area)


# Factorial of a number:
def factorial(numar):
    result = 1
    for i in range(abs(numar)):
        i += 1
        result = result * i
        if numar < 0:
            result = result * -1
        elif numar ==0:
            result = 0
    print(result)
    return result


# Sum of two numbers:
def sum(a, b):
    sum = a + b
    print(f"suma este {sum}")
    return sum


# Average of a list of numbers:
def average(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    result = sum / len(numbers)
    print(result)
    return result


# Even or odd number:
def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Check if number is divisible by another number:
def divisible(n1, n2):
    if n2 == 0:
        raise ValueError("Can't divide by 0")
    if n1 % n2 == 0:
        return "It is divisible"
    else:
        return "Not divisible"


# Distance between two points:
def distance_points(px1, py1, px2, py2):
    px = (px2 - px1) ** 2
    py = (py2 - py1) ** 2
    result = math.sqrt(px + py)
    print(result)
    return round(result)


circle_area(5)
factorial(-3)
sum(2, 3)
average([1, 2, 3, 4])
print(even_odd(3))
divisible(5, 3)
distance_points(5, 7, 4, 8)

