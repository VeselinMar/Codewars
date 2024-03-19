def neutralise(s1, s2):
    s_final = ''
    for s in range(len(s1)):
        if s1[s] == s2[s]:
            s_final += s1[s]
        else:
            s_final += '0'
    return s_final


first = input()
second = input()

print(neutralise(first, second))
