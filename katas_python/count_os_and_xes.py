# we receive a line containing various symbols
# count whether the number of 'o's equals the number of 'x's
def xo(s):
    s = s.lower()
    return s.count('o') == s.count('x')


line = 'ccoo32xxasd'
print(xo(line))
