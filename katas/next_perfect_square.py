import math


def find_next_square(sq):
    root = math.sqrt(int(sq))
    if int(root) == root:
        return int((root + 1) ** 2)
    return -1


line = input()
print(find_next_square(line))
