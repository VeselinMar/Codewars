from collections import deque


def smaller(arr):
    # we save our result in a list
    result = []
    # we define a work list(deque) and fill it with our numbers
    # we use a deque because we want to start from the left
    work_list = deque(arr)
    for _ in range(len(arr)):
        number = work_list.popleft()
        count = 0
        for n in work_list:
            if n < number:
                count += 1
        result.append(count)
        # we added the popped number to the end of the list because we need to count
        # whether the number is smaller than the following numbers
        work_list.append(number)

    return result


print(smaller([5, 4, 3, 2, 1]))
print(smaller([1, 2, 0]))
print(smaller([1, 4, 0, 7]))
