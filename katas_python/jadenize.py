def to_jaden_case(string):
    # execute only if string is valid
    if string:
        new_string = ''
        # capitalize each first symbol in string using the built-in function capitalize()
        return ' '.join([word.capitalize() for word in string.split(' ')])
    return ''


sentence = input()
print(to_jaden_case(sentence))
