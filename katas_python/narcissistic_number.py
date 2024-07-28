# function to check whether a number is Armstrong(narcissistic) number
def narcissistic(value):
    # convert number to string
    num_str = str(value)
    # get length of number
    num_len = len(num_str)
    # use a generator to calculate each number lifted to the power of num_len then sum the numbers
    sum_num = sum(int(n) ** num_len for n in num_str)
    # Return True or False depending on result
    return sum_num == value


line = input()
print(narcissistic(line))
