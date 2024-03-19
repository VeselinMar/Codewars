def xo(s):
    s = s.lower()
    count_x = 0
    count_o = 0
    for l in s:
        if l == 'x':
            count_x += 1
        elif l == 'o':
            count_o += 1
    if count_o == count_x:
        return True
    else:
        return False


line = 'ooxx'
print(xo(line))
