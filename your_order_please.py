def order(sentence: str):
    if sentence:
        words = sentence.split()
        final = ['a'] * len(words)  # initialize with filled positions
        for part in words:
            for digit in '123456789':
                if digit in part:
                    index = int(digit) - 1
                    final[index] = part
                    break  # Exit the loop once the digit is found
        return ' '.join(final)
    return sentence


line = input()
print(order(line))
