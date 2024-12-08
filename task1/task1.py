import sys


def calculate_path(n, m):
    start = 1
    path = []

    while True:
        path.append(start)
        start = 1 + (start + m - 2) % n
        if start == 1:
            break

    return ''.join(map(str, path))

if len(sys.argv) != 3:
    print("usage: python3 task1.py 'n' 'm'")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

print(calculate_path(n, m))
