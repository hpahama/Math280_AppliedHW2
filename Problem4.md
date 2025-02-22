import numpy as np

from google.colab import files
uploaded = files.upload()

textfile=open('midsummer.txt', 'r')
text=textfile.read()
text = text.replace('\n',' ')

wordlist = text.split(" ")
wordset= set(wordlist)

numberdictionary = dict()
worddictionary = dict()
for i, word in enumerate(wordset):
  numberdictionary[word]= i
  worddictionary[i]= word

frequencies= dict()
for i in wordset:
  frequencies[i]= dict()
for j in range(len(wordlist)-1):
  if wordlist[j+1] in frequencies[wordlist[j]]:
    frequencies[wordlist[j]][wordlist[j+1]]+=1
  else:
    frequencies[wordlist[j]][wordlist[j+1]]=1

transitionmatrix =np.zeros((len(wordset),len(wordset)))
for i in frequencies:
  ptotal = sum(frequencies[i].values())
  for j in frequencies[i]:
    transitionmatrix[numberdictionary[j]][numberdictionary[i]]=frequencies[i][j]/ptotal

def predict(word, length):
  string = word
  for i in range(0,length-1):
    probability = transitionmatrix[:, numberdictionary[word]]
    nextwordindex =np.random.choice(range(0, len(wordset)), p= probability)
    word = worddictionary[nextwordindex]
    string = string + " " + word
  return(string)

predict('ACT', 200)

