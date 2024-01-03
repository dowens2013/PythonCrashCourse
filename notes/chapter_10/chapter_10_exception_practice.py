# write a program to a missing file to work with this error
# i converted the program to count for number of words. change path string to simulate error.
from pathlib import Path
from word_count import count_words

file_names = ['alice.txt', 'moby_dicdk.txt', 'little_women.txt']

for x in file_names:
    path = Path(x)
    count_words(path)






