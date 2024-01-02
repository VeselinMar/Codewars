def narcissistic(value):
    num_str = str(value)
    sum_num = 0
    for n in num_str:
        sum_num += int(n) ** len(num_str)
    if sum_num == int(value):
        return True
    return False


line = input()
print(narcissistic(line))
