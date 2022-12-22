import math


def addition(a, b):
    result = a + b
    return result

def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    result = a / b
    return result

def quadratic_equation(a, b, c):
    # рассчитываем дискриминант
    if a == 0:
        raise ZeroDivisionError
    discriminant = b ** 2 - 4 * a * c
    return discriminant

def find_roots(a, b, c):
    # рассчитываем дискриминант
    if a == 0:
        raise ZeroDivisionError
    discriminant = b ** 2 - 4 * a * c
    # если дискриминант больше нуля, уравнение имеет два решения
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    # если дискриминант равен нулю, уравнение имеет одно решение
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return x1
    # иначе уравнение не имеет решений в действительных числах
    else:
        return "Уравнение не имеет решений в действительных числах"

def distance_between_points(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result
