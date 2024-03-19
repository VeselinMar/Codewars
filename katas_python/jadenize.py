def to_jaden_case(string):
    new_string = ''
    string_to_list = string.split(' ')
    if string:  # execute only if string is valid
        for item in range(len(string_to_list)):  # capitalize each first symbol in string
            new_string += string_to_list[item][0].upper() + string_to_list[item][1::].lower()
            if item != len(string_to_list) - 1:  # each item is followed by a space char except the last one
                new_string += ' '
        return new_string
    return ''


sentence = input()
print(to_jaden_case(sentence))
