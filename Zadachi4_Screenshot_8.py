import random
import pandas as pd

words = ['python', 'crossword', 'code', 'program', 'solution', 'puzzle']

def generate_crossword(words):
    crossword_df = pd.DataFrame(index=range(10), columns=range(10))
    for word in words:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, 9 - len(word))
            y = random.randint(0, 9)
            for i, letter in enumerate(word):
                crossword_df.iloc[y, x + i] = letter
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - len(word))
            for i, letter in enumerate(word):
                crossword_df.iloc[y + i, x] = letter
    crossword_df = crossword_df.fillna(value=lambda _: chr(random.randint(65, 90)))
    return crossword_df

def solve_crossword(crossword_df, words):
    solved_crossword = crossword_df.copy()
    for word in words:
        for i in range(10):
            for j in range(10):
                if solved_crossword.iloc[i, j] == word[0]:
                    if ''.join(solved_crossword.iloc[i, j:j + len(word)]) == word:
                        solved_crossword.iloc[i, j:j + len(word)] = list(word)
                    elif ''.join(solved_crossword.iloc[i:i + len(word), j]) == word:
                        solved_crossword.iloc[i:i + len(word), j] = list(word)
    return solved_crossword

crossword = generate_crossword(words)
print("Сгенерированный кроссворд:")
print(crossword)
solved_crossword = solve_crossword(crossword, words)
print("Решенный кроссворд:")
print(solved_crossword)
