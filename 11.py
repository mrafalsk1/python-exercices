import math


def circle_cal(radius):
    area = math.pi *(radius ** 2)
    circ = 2 * math.pi * radius
    diameter = radius * 2

    return area, circ, diameter


if  __name__ == "__main__":
    radius = float(input("Radius"))

    area, circ, diameter = circle_cal(radius)

    print(f'{area} {circ} {diameter}')