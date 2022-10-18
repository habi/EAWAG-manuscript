import glob
import os
# Get all the relevant files
files = glob.glob(os.path.join(os.getcwd(), '0*.md'))
word_list = []
for c,f in enumerate(files):
    # Read all files
    input_file = open(f, 'r')
    # Extract words, strip them and add certain words to a list
    words = input_file.read().split()
    for d,word in enumerate(words):
        w = word.strip('*').strip(',').strip('.')
        if len(w) > 5:
            word_list.append(w)
# Only return the unique words
unique_words = set(word_list)
print(sorted(unique_words))