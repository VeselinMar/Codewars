def my_languages(results):
    # filter the languages whose scores are above 60
    filtered_languages = {language: score for language, score in results.items() if score >= 60}
    # sort the filtered languages by score in reverse order
    sorted_languages = sorted(filtered_languages.items(), key=lambda x: x[1], reverse=True)
    # add the sorted languages to a list
    certificates = [language for language, score in sorted_languages]

    return certificates


print(my_languages({"Java": 10, "Ruby": 80, "Python": 66}))
print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}))
print(my_languages({"C++": 50, "ASM": 10, "Haskell": 20}))
