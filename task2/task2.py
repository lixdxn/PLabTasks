import math
import sys


def main():
    if len(sys.argv) != 3:
        print("usage: python3 task2.py circle.txt dot.txt")
        sys.exit(1)

    circle_file_path = sys.argv[1]
    dot_file_path = sys.argv[2]

    with open(circle_file_path, 'r') as circle_file:
        x_centre = float(circle_file.readline())
        y_centre = float(circle_file.readline())
        radius = float(circle_file.readline())

    with open(dot_file_path, 'r') as dot_file:
        dot = [tuple(map(float, line.split())) for line in dot_file]

    for (x, y) in dot:
        distance = math.sqrt((x - x_centre) ** 2 + (y - y_centre) ** 2) # формула расстояния
        if abs(distance - radius) < 1e-9:  # точка на окружности
            print(0)
        elif distance < radius:  # точка внутри окружности
            print(1)
        else:  # точка за пределами окружности
            print(2)

main()