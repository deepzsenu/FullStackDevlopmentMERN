import random

def simulate_monty_hall(num_games):
    switch_wins = 0
    stick_wins = 0

    for _ in range(num_games):
        doors = [0, 0, 0]
        prize_index = random.randint(0, 2)
        doors[prize_index] = 1

        initial_choice = random.randint(0, 2)

        # Host reveals a goat
        revealed_door = random.choice([i for i in range(3) if i != initial_choice and doors[i] == 0])

        # Switch strategy
        switch_choice = next(i for i in range(3) if i != initial_choice and i != revealed_door)

        if doors[switch_choice] == 1:
            switch_wins += 1

        # Stick strategy
        if doors[initial_choice] == 1:
            stick_wins += 1

    return switch_wins, stick_wins

# Simulate 1000 games
num_games = 1000
switch_wins, stick_wins = simulate_monty_hall(num_games)

# Print the results
print(f"Switch wins: {switch_wins} out of {num_games}")
print(f"Stick wins: {stick_wins} out of {num_games}")
