def duplicate_encode(word):
    # Create a dictionary to count occurrences of each character, ignoring case.
    counts = {}
    for char in word.lower():
        counts[char] = counts.get(char, 0) + 1

    # Construct new word using the counts
    new_word = ''
    for char in word:
        if counts[char.lower()] > 1:
            new_word += ')'
        else:
            new_word += '('

    return new_word


check = input()
print(duplicate_encode(check))
