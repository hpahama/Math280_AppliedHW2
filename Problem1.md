# Applied Homework Assignment 2: 
(Markov Chains and Predictive Text)

## Problem 1

### Task
1. Find the 7x7 transition matrix for the guard's movements.
2. Determine the proportion of time the guard spends in each room over hours or days.

### Step 1
The transition matrix will have 7 rows and 7 columns. Each element (i, j) will represent the probability of moving from room \(i\) to room \(j\). Since the guard moves randomly, the probabilities will be equal among all neighboring rooms.

### Step 2
I will write a Python program to simulate the guard's movements over a long period and calculate the proportion of time spent in each room.

### Code Breakdown
```python
import numpy as np

# Function to create the transition matrix
def create_transition_matrix():
    return np.array([
        [0, 1/2, 0, 1/2, 0, 0, 0],   # R1
        [1/3, 0, 1/3, 0, 1/3, 0, 0], # R2
        [0, 1/2, 0, 0, 0, 1/2, 0],   # R3
        [1/2, 0, 0, 0, 1/2, 0, 0],   # R4
        [0, 1/4, 0, 1/4, 0, 1/4, 1/4], # R5
        [0, 0, 1/3, 0, 1/3, 0, 1/3], # R6
        [0, 0, 0, 0, 1/2, 1/2, 0]    # R7
    ])

# Function to simulate the guard's movement
def simulate_guard_movement(transition_matrix, num_steps):
    current_room = 0
    time_spent = np.zeros(7)

    for _ in range(num_steps):
        time_spent[current_room] += 1
        current_room = np.random.choice(7, p=transition_matrix[current_room])

    return time_spent

# Main function
def main():
    transition_matrix = create_transition_matrix()
    num_steps = 100000
    time_spent = simulate_guard_movement(transition_matrix, num_steps)

    # Calculate the proportion of time spent in each room
    proportion_of_time = time_spent / num_steps
    
    # Print the results in a readable format
    print("Proportion of Time Spent in Each Room:")
    for room in range(7):
        print(f"Room {room + 1}: {proportion_of_time[room]:.2%}")

if __name__ == "__main__":
    main()
```

## Definition
This Python code simulates the movements of a guard patrolling an art gallery with seven interconnected rooms. The guard starts in room 1 (R1) and moves to neighboring rooms at random based on predefined probabilities. The simulation runs for 100,000 steps, and the code calculates the proportion of time the guard spends in each room. The code is organized into three main functions: `create_transition_matrix` to define the probabilities of moving between rooms, `simulate_guard_movement` to simulate the guard's movements and count the time spent in each room, and `main` to execute the simulation and print the results.

## Answer
**Proportion of Time Spent in Each Room:**
- Room 1: 11.16%
- Room 2: 16.71%
- Room 3: 11.07%
- Room 4: 11.12%
- Room 5: 22.21%
- Room 6: 16.62%
- Room 7: 11.11%