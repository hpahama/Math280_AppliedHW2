# Applied Homework Assignment 2: 
(Markov Chains and Predictive Text)

## Problem 2

### Task
Some lines I found hilarious:
“How is it that I cannot hear you? You, with your boasting about how he sweet-talked her feeble dreams and cunningly maneuvered like a sly fox! That same flaw, 'Ladies,' or 'Fair-ladies,' makes me want to shriek! Oh, and my very gentle friends, you’re a delightful bunch!”

## How This Predictive Text Generator Works

### 1. Reading and Preprocessing the Text
```python
textfile=open('midsummer.txt', 'r')
text=textfile.read()
text = text.replace('\n',' ')
```
- Read the text file: Opens and reads the contents of `'midsummer.txt'`.
- Replace newline characters: Replaces newline characters with spaces to create a continuous string.

### 2. Creating Word Lists and Sets
```python
wordlist = text.split(" ")
wordset= set(wordlist)
```
- Split the text: Splits the text into a list of words.
- Create a unique set of words: Creates a set of unique words from the word list.

### 3. Creating Dictionaries for Words and Indices
```python
numberdictionary = dict()
worddictionary = dict()
for i, word in enumerate(wordset):
  numberdictionary[word]= i
  worddictionary[i]= word
```
- Enumerate words: Assigns a unique index to each word.
- Dictionaries: Creates two dictionaries:
  - `numberdictionary`: Maps each word to a unique index.
  - `worddictionary`: Maps each index back to the corresponding word.

### 4. Counting Word Frequencies
```python
frequencies= dict()
for i in wordset:
  frequencies[i]= dict()
for j in range(len(wordlist)-1):
  if wordlist[j+1] in frequencies[wordlist[j]]:
    frequencies[wordlist[j]][wordlist[j+1]]+=1
  else:
    frequencies[wordlist[j]][wordlist[j+1]]=1
```
- Initialize frequency dictionaries: Initializes a dictionary to count how often each word follows another word.
- Count occurrences: Counts how often each word follows another in the text, updating the frequency dictionaries.

### 5. Building the Transition Matrix
```python
transitionmatrix =np.zeros((len(wordset),len(wordset)))
for i in frequencies:
  ptotal = sum(frequencies[i].values())
  for j in frequencies[i]:
    transitionmatrix[numberdictionary[j]][numberdictionary[i]]=frequencies[i][j]/ptotal
```
- Initialize the matrix: Creates a square matrix of size `number of unique words x number of unique words` with zeros.
- Calculate probabilities: For each word, calculates the probability of transitioning to each following word and updates the matrix accordingly.

### 6. Predictive Text Function
```python
def predict(word, length):
  string = word
  for i in range(0,length-1):
    probability = transitionmatrix[:, numberdictionary[word]]
    nextwordindex =np.random.choice(range(0, len(wordset)), p= probability)
    word = worddictionary[nextwordindex]
    string = string + " " + word
  return(string)
```
- Initialize: Takes a starting word and the desired length of the generated text.
- Generate text: Uses the transition matrix to predict and append the next word based on the current word's probabilities, repeating until the desired length is reached.
- Return generated text: Returns the generated string.

### Summary
This predictive text generator reads a text file, preprocesses the text, and creates a transition matrix based on word frequencies. It then uses this matrix to generate new text based on the probabilities of word transitions.