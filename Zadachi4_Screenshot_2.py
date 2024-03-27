from collections import Counter
import re

def count_words(file_name, num_words):
    with open(file_name, 'r') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())
        word_count = Counter(words)
        top_words = word_count.most_common(num_words)
        
        for word, count in top_words:
            print(word, count)

file_name = 'sample.txt'  
num_words = 10
count_words(file_name, num_words)
