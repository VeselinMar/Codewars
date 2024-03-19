def basic_op(operator, value1, value2):
    if '+' in operator:
        return value1 + value2
    elif '-' in operator:
        return value1 - value2
    elif '*' in operator:
        return value1 * value2
    elif '/' in operator:
        return value1 / value2


line = (input().strip('()')).split(',')
print(basic_op(line[0], int(line[1].strip(' ')), int(line[2].strip(' '))))
