import math


# simple math problems

# Area of a circle:
def ex1(r):
    area = math.pi * r ** 2
    print(round(area))


# Factorial of a number:
def ex2(numar):
    result = 1
    for i in range(numar):
        i += 1
        result = result * i
    print(result)


# Sum of two numbers:
def ex9(a, b):
    sum = a + b
    print(f"suma este {sum}")


# Average of a list of numbers:
def ex10(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    result = sum / len(numbers)
    print(result)


# Even or odd number:
def ex12(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Check if number is divisible by another number:
def ex15(n1, n2):
    if n1 % n2 == 0:
        print("Este divizibil")
    else:
        print("Nu este divizibil")


# Distance between two points:
def ex21(px1, py1, px2, py2):
    px = (px2 - px1) ** 2
    py = (py2 - py1) ** 2
    result = math.sqrt(px + py)
    print(result)


ex1(5)
ex2(3)
ex9(2, 3)
ex10([1, 2, 3, 4])
ex12(3)
ex15(6, 3)
ex21(5, 7, 4, 8)

