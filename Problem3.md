# Applied Homework Assignment 2: 
(Markov Chains and Predictive Text)

## Problem 3

### Step 1:
I created a code that counts the most repeated words in a text/paragraph. I used the generated phrase I had worked on in problem 2.

```python
from collections import Counter
import re

text = """ACT III SCENE I. MOTH Hail! MOTH Hail! MOTH And run away this case, let him And stolen unto this purple grapes, green For I hear without the deep, And so foolish Fates. This is certain. This princess of Egypt: The one word of any sucking dove; I was a most cruel pray. Lysander! speak most, to call them thanks for with his face by what visions have you should be called Bottom's house triumphantly, And 'tailor' cries, and wound The sun was a single life. Come, now is thy sweet eyes. HELENA You are these? EGEUS My gentle lady dear!' QUINCE A crew of man By some satire, keen and cawing at once this injury. HERMIA ACT III SCENE I. The deepest loathing to a murderer look, so proud Demetrius? O, why so? TITANIA Music, still thou mistakest, Or in the temple by daylight, From lovers' flights doth behold the counsel that parted eye, Steal me that they that he that were only thine. QUINCE Well, I pray you; for your cheek so That I Upon that do estate unto this business Against my side, And sleep, that she upon my daughter's heart, Turn'd her charmed eye his hairy temples then did these things The more better assurance, tell true, tell he waked, of odious savours sweet: So the moon. But, room, fairy! here awhile, And that the brakes, And bootless speed, When I would my consent that love turn'd true. PUCK Come not a sword to so proud Demetrius? speak troth, you are you must be blamed. Marry, our minds till death or by moonlight into Lysander's eye; Whose note so rich with little flower, Both on hill, in their elves come by moonlight at his seat on my daughter's heart, In Hermia's sphery eyne? But that, one sampler, sitting on pipes of their wormy beds are invisible within his sprite, In number more the night Than thine, thou art, That we meet by us follow you. DEMETRIUS Not so, my insufficiency? Good troth, A lion-fell, nor else the stomach brings, Or else the lion's dam; For, if I assure you; for our law Immediately provided in love thee and swear to try whose right, Of our dreams. Exeunt Thisbe PUCK Ho, ho, ho! Coward, why so? Lay breath so grow to it, And then end loyalty! Here comes Oberon. Fairy And here, and all the creeping fowler eye, Lysander, look to make my good to tremble: my modesty, no more true love have I must love. HELENA The wren with briers, I then I speak not made me as you. DEMETRIUS HELENA Enter PEASEBLOSSOM, COBWEB, MOTH, and let me leave, Unworthy as any sucking dove; I can I desire your fancies to it. THESEUS His eyes I will answer: my breast imbrue: Stabs himself in government. THESEUS What say what you have but chide; but Pyramus; Ay, there create Ever shall be to Athens calls. Their wonted sight. When we come not:"""

# Clean text: remove punctuation and convert to lowercase
words = re.findall(r'\b\w+\b', text.lower())

# Count words
word_counts = Counter(words)

# Get the top 3 most common words
top_3 = word_counts.most_common(3)

# Print results
for word, count in top_3:
    print(f"{word}: {count}")
```

The result was: 'i', 'and', and 'the'

### Step 2:

```python
import numpy as np

# Define the words we're tracking
words = ["i", "and", "the"]

# Define the transition matrix based on given probabilities
# Each row must sum to 1!
transition_matrix = np.array([
    [0.33, 0.33, 0.34],  # "i" → "i" (33%), "i" → "and" (33%), "i" → "the" (34%)
    [0.40, 0.30, 0.30],  # "and" → "i" (40%), "and" → "and" (30%), "and" → "the" (30%)
    [0.25, 0.25, 0.50]   # "the" → "i" (25%), "the" → "and" (25%), "the" → "the" (50%)
])

# Function to simulate word transitions
def simulate_word_sequence(start_word, num_steps=10):
    if start_word not in words:
        raise ValueError("Word not in list!")

    current_idx = words.index(start_word)
    sequence = [start_word]

    for _ in range(num_steps - 1):
        next_idx = np.random.choice(len(words), p=transition_matrix[current_idx])
        sequence.append(words[next_idx])
        current_idx = next_idx

    return sequence

# Function to print transition probabilities in a readable way
def print_transition_matrix():
    print("\n Word Transition Probabilities:\n")
    print(f"{'':<10}{'i':<10}{'and':<10}{'the':<10}")
    for i, word in enumerate(words):
        probs = "  ".join(f"{p:.2f}" for p in transition_matrix[i])
        print(f"{word:<10}{probs}")

# Run the simulation and print results
if __name__ == "__main__":
    print_transition_matrix()

    # Example: Generate a sequence starting with "i"
    generated_sequence = simulate_word_sequence("i", num_steps=5)
    print("\n Generated Word Sequence:", " → ".join(generated_sequence))
```
