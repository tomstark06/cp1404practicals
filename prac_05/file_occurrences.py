"""
Word occurrences exercise
Estimate: 25 minutes
Actual: 20 minutes
"""

word_to_count_of_word = {}
text = input("Text: ")
words = text.split()
for word in words:
    count_of_word = word_to_count_of_word.get(word, 0)
    word_to_count_of_word[word] = count_of_word + 1
max_length = max(len(word) for word in words)
for word, count_of_word in sorted(word_to_count_of_word.items()):
    print(f"{word:{max_length}} : {count_of_word}")
