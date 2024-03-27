def generate_combinations(word, current = ''):
    if len(word) == 0:
        print(current)
    else:
        for i in range(len(word)):
            generate_combinations(word[:i] + word[i+1:], current + word[i])

word = "abc"
generate_combinations(word)
