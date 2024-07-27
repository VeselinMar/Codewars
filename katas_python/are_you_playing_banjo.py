def are_you_playing_banjo(name):
    # only names starting with 'r' or 'R' play the banjo
    # therefore we lower the first symbol and compare with 'r' if equal -> he plays the banjo
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    return name + ' does not play banjo'


line = input()
print(are_you_playing_banjo(line))
