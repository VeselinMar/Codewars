def solution(roman: str) -> int:
    extra = 0
    if "CM" in roman:
        extra += 900
        roman = roman.replace("CM", "")
    if "CD" in roman:
        extra += 400
        roman = roman.replace("CD", "")
    if "XC" in roman:
        extra += 90
        roman = roman.replace("XC", "")
    if "XL" in roman:
        extra += 40
        roman = roman.replace("XL", "")
    if "IX" in roman:
        extra += 9
        roman = roman.replace("IX", "")
    if "IV" in roman:
        extra += 4
        roman = roman.replace("IV", "")
    legend = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    modern_year = [legend[letter] for letter in roman]
    return sum(modern_year) + extra


roman_year = input()
print(solution(roman_year))
