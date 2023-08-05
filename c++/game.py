import random

# Player character stats
player_classes = {
    1: {"class_name": "Fighter", "health": 25, "damage_min": 1, "damage_max": 10, "hit_chance": 0.7},
    2: {"class_name": "Mage/Ranged", "health": 18, "damage_min": 1, "damage_max": 14, "hit_chance": 0.6},
    3: {"class_name": "Stealth/Thief", "health": 18, "damage_min": 1, "damage_max": 10, "hit_chance": 0.5},
    4: {"class_name": "Tinkerer/Gnome/Engineer", "health": 16, "damage_min": 1, "damage_max": 18, "hit_chance": 0.65},
}

# Computer monster stats
monster_health = 33
monster_damage_min = 1
monster_damage_max = 4
monster_dodge_chance = 0.1

def die_roll(x):
    return random.randint(1, x)

def computer_turn_damage():
    return die_roll(monster_damage_max)

def user_turn_damage(x):
    return die_roll(x)

def hit_check(hit_chance):
    return random.random() < hit_chance

def check_for_winner(player_health, monster_health):
    if player_health <= 0:
        return "Monster"
    elif monster_health <= 0:
        return "Player"
    else:
        return None

def player_generator():
    print("Welcome to World of Yourcraft")
    print("1. Fighter 2. Mage/Ranged 3. Stealth/Thief 4. Tinkerer/Gnome/Engineer")
    player_choice = int(input("Choose your character class (1, 2, 3, or 4): "))
    player_class = player_classes.get(player_choice)
    if not player_class:
        print("Invalid choice. Exiting.")
        exit()

    print(f"You have chosen {player_class['class_name']}. Get ready for the battle!")
    return player_class["health"], player_class["damage_min"], player_class["damage_max"], player_class["hit_chance"]

def main():
    player_health, player_damage_min, player_damage_max, player_hit_chance = player_generator()
    rounds = 0

    while True:
        rounds += 1
        print(f"Round {rounds}:")
        
        # Player turn
        player_damage = user_turn_damage(player_damage_max)
        print(f"Your character hits the Monster for {player_damage} points of damage.")
        
        # Monster turn
        monster_damage = computer_turn_damage()
        if hit_check(player_hit_chance):
            player_health -= monster_damage
            print(f"The Monster hits your character for {monster_damage} points of damage.")
        else:
            print("The Monster missed your character this turn.")
        
        # Check for winner
        winner = check_for_winner(player_health, monster_health)
        if winner:
            print(f"\nYour {player_classes[player_choice]['class_name']} has won the battle! Congratulations!")
            break

        print(f"\nResults: {player_classes[player_choice]['class_name']} {player_health} health, Monster {monster_health} health\n")

if __name__ == "__main__":
    main()
