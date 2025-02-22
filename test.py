import numpy as np
from collections import Counter

# Step 1: Read the text and preprocess
file_path = 'C:\\Users\\paham\\Documents\\Classes2025\\midsummer.txt'
textfile = open(file_path, 'r')
text = textfile.read()
text = text.replace('\n',' ')

# Step 2: Create word lists and sets
wordlist = text.split(" ")
wordset = set(wordlist)

# Step 3: Create dictionaries for words and indices
numberdictionary = {word: i for i, word in enumerate(wordset)}
worddictionary = {i: word for i, word in enumerate(wordset)}

# Step 4: Count word frequencies
frequencies = {word: {} for word in wordset}
for i in range(len(wordlist) - 1):
    current_word, next_word = wordlist[i], wordlist[i + 1]
    if next_word in frequencies[current_word]:
        frequencies[current_word][next_word] += 1
    else:
        frequencies[current_word][next_word] = 1

# Step 5: Build the transition matrix
transitionmatrix = np.zeros((len(wordset), len(wordset)))
for word, next_words in frequencies.items():
    total = sum(next_words.values())
    for next_word, count in next_words.items():
        transitionmatrix[numberdictionary[next_word]][numberdictionary[word]] = count / total

# Step 6: Find the top 3 most frequent words
top_words = [word for word, count in Counter(wordlist).most_common(3)]

# Step 7: Calculate the probabilities
probabilities = {}
for word in top_words:
    probabilities[word] = {next_word: transitionmatrix[numberdictionary[next_word]][numberdictionary[word]] for next_word in top_words}

# Output the results
print(f"Top 3 most frequent words: {top_words}")
for word, next_words in probabilities.items():
    for next_word, prob in next_words.items():
        if prob > 0:
            print(f"The word '{next_word}' follows the word '{word}' with probability {prob:.4f}")

# Print the file location
print(f"The file is located at: {os.path.abspath(file_path)}")
