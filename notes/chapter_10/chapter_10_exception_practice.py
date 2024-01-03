# write a program to a missing file to work with this error
# i converted the program to count for number of words. change path string to simulate error.
from pathlib import Path
from word_count import count_words

path = Path('alice.txt')

count_words(path)



