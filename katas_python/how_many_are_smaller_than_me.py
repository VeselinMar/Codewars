from collections import deque


def smaller(arr):
    result = []
    work_list = deque(arr)
    while work_list:
        number = work_list.popleft()
        count = 0
        for n in work_list:
            if n < number:
                count += 1
        result.append(count)

    return result


print(smaller([5, 4, 3, 2, 1]))
print(smaller([1, 2, 0]))
