def high_and_low(numbers):
    # Split the input string into a list of integers
    numbers_list = list(map(int, numbers.split()))
    # Find the maximum and minimum values
    highest = max(numbers_list)
    lowest = min(numbers_list)
    # Return them as a formatted string
    return f"{highest} {lowest}"


line = input()
print(high_and_low(line))
