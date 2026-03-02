import random

# --- 1. Variables ---
player_hp = 100
enemy_hp = 100

# --- 2. HP bar function ---
def hp_bar(current_hp, max_hp):
    bar_length = 20
    filled = int(current_hp / max_hp * bar_length)
    empty = bar_length - filled
    bar = "█" * filled + "-" * empty
    print(f"[{bar}] {current_hp}/{max_hp}")

# --- 3. Fight loop ---
turn = 1
while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Turn {turn} ---")

    # Player attack
    move = input("Choose 1-Slash or 2-Fireball: ")
    if move == "1":
        damage = 10
        enemy_hp -= damage
        print(f"You hit enemy for {damage} HP!")
    elif move == "2":
        damage = 15
        enemy_hp -= damage
        print(f"You hit enemy for {damage} HP!")
    else:
        print("You missed your turn!")

    # Enemy attack (random)
    if enemy_hp > 0:
        enemy_damage = random.randint(5, 12)
        player_hp -= enemy_damage
        print(f"Enemy hits you for {enemy_damage} HP!")

    # Show HP bars after both attacks
    print("Player HP:")
    hp_bar(player_hp, 100)
    print("Enemy HP:")
    hp_bar(enemy_hp, 100)

    turn += 1

# --- 4. Result ---
if player_hp <= 0:
    print("\nYou lost!")
elif enemy_hp <= 0:
    print("\nYou won!")