def descending_order(num: str):
    numbers = []
    for digit in num:
        numbers.append(digit)
    numbers.sort(reverse=True)
    return ''.join(numbers)


number = input()
print(descending_order(number))
