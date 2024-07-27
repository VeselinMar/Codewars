# basic calculator whose functionality is implemented through elif functions
# operations or performed when the user provides the following form:
# operator(+, -, /, *), first number, second number
def basic_op(operator, value1, value2):
    if '+' in operator:
        return value1 + value2
    elif '-' in operator:
        return value1 - value2
    elif '*' in operator:
        return value1 * value2
    elif '/' in operator:
        return round(value1 / value2)


line = (input().strip('()')).split(',')
print(basic_op(line[0], int(line[1].strip(' ')), int(line[2].strip(' '))))
