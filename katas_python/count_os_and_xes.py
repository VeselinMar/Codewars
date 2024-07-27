# we receive a line containing various symbols
# count whether the number of 'o's equals the number of 'x's
def xo(s):
    # convert the string to lowercase
    s = s.lower()
    # take advantage of the built-in count function and compare the number of 'o's and 'x's
    return s.count('o') == s.count('x')


line = 'ccoo32xxasd'
print(xo(line))
