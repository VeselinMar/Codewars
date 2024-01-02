def square_sum(numbers):
    squared = [pow(num, 2) for num in numbers]
    return sum(squared)


number = [1, 2, 2]

print(square_sum(number))
