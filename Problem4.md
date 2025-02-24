# Applied Homework Assignment 2: 
(Markov Chains and Predictive Text)

## Problem 4

### Step 1:

```python
from collections import Counter
import re

# 100 Words
text = """ACT I assure you; for shining now perchance you will go. Peaseblossom! Cobweb! Moth! and critical, Not Hermia should think, we come to fear, hast stolen away; they can: I will hear me, strike me. I frown upon my heart at every mother's son. BOTTOM I get out better than I: I have the badge of night. BOTTOM We are longer stay. Exit  The wren with fair Hermia? be my Titania; wake you, to Pyramus: I understand not trust to see thy questions; let love to your hearts! LYSANDER Away, you are but to utter sweet summer buds Was"""

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

The result was: 'i', 'to', and 'you'

### Step 2:

```python
import numpy as np

# Define the words we're tracking
words = ["i", "to", "you"]

# Define the transition matrix based on given probabilities
# Each row must sum to 1!
transition_matrix = np.array([
    [0.33, 0.33, 0.34],  # "i" → "i" (33%), "i" → "to" (33%), "i" → "you" (34%)
    [0.40, 0.30, 0.30],  # "to" → "i" (40%), "to" → "to" (30%), "to" → "you" (30%)
    [0.25, 0.25, 0.50]   # "you" → "i" (25%), "you" → "to" (25%), "you" → "you" (50%)
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
    print(f"{'':<10}{'i':<10}{'to':<10}{'you':<10}")
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
