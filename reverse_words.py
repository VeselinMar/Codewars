def reverse_words(text: str):
    if text:
        text = text.split(' ')
        rev_text = [word[::-1] for word in text]
        text = ' '.join(rev_text)
    return text


line = input()
print(reverse_words(line))
