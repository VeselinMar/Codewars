from collections import deque


def smaller(arr):
    # save our result in a list
    result = []
    # define a work list(deque) and fill it with our numbers
    # use a deque because we want to start from the left
    work_list = deque(arr)
    for _ in range(len(arr)):
        number = work_list.popleft()
        count = 0
        for n in work_list:
            if n < number:
                count += 1
        result.append(count)
        # add the popped number to the end of the list still needs to be used in further counts
        work_list.append(number)

    return result


print(smaller([5, 4, 3, 2, 1]))
print(smaller([1, 2, 0]))
print(smaller([1, 4, 0, 7]))
