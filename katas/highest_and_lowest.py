def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    numbers_string = f'{max(numbers)} {min(numbers)}'
    return numbers_string


line = input()
print(high_and_low(line))
