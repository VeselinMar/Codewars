def duplicate_encode(word):
    duplication_checker = 0
    new_word = ''
    for char in word:
        for ind in range(len(word)):
            if char.lower() == word[ind].lower():
                duplication_checker += 1
                if duplication_checker > 1:
                    new_word += ')'
                    break
        if duplication_checker == 1:
            new_word += '('
        duplication_checker = 0

    return new_word


check = input()
print(duplicate_encode(check))
