import glob
import os
import string
# Get all the relevant files
files = glob.glob(os.path.join(os.getcwd(), '0*.md'))
word_list = []
for c, f in enumerate(files):
    # Read all files
    input_file = open(f, 'r')
    # Extract words, strip them and add certain words to a list
    words = input_file.read().split()
    for d, word in enumerate(words):
        for e, punctuation in enumerate(string.punctuation):
            word = word.replace(punctuation,'')
        if len(word) > 5 and not word.startswith('doi') and not word.startswith('https'):
            word_list.append(word.lower())
# Only return the unique words
unique_words = set(word_list)
print(sorted(unique_words))