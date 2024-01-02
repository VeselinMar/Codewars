def is_pangram(s: str):
    count = 0
    found = ''
    for symbol in s:
        if symbol.isalpha() and symbol.lower() not in found:
            count += 1
            found += symbol.lower()
            if count == 26:
                return True
    return False


string = input()
print(is_pangram(string))
