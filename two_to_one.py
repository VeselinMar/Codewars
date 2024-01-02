def longest(a1, a2):
    result = ''
    for letter in (a1 + a2):
        if letter not in result:
            result += letter
    return ''.join(sorted(result))


line_1 = input()
line_2 = input()
print(longest(line_1, line_2))
