def health_bar(hp, total = 100, chars = ("#", "-"), bar_length = 20):
    total = max(1, total)
    hp = max(0, min(hp, total))
    filled_length = int(round(hp / total * bar_length))
    empty_length = int(bar_length - hp / total * bar_length)
    filled_bar = chars[0] * filled_length
    empty_bar = chars[1] * empty_length
    return f"[{filled_bar}{empty_bar}]"
import random
player_hp = 100
player_max_hp = 100
enemy_hp = 100
turn = 1
counter_chance = 0
player_defense = False
emeny_defense = False
heal_cooldown = 0
fireball_cooldown = 0
#player turn
while player_hp > 0 and enemy_hp > 0:
    print (f'------Turn {turn}------')
    print(health_bar(player_hp), player_hp)
    print(health_bar(enemy_hp), enemy_hp)
    move = input('Choose 1-Slash, 2-Fireball, 3-Defense or 4-Heal: ')
    if move == "1":
        player_damage = 10
        enemy_hp -= player_damage
        print (f'Enemy Got HIT by {player_damage} HP!')
    elif move == "2":
        if fireball_cooldown > 0:
            print('Fireball is on Cooldown!')
        else:
            player_damage = 25
            enemy_hp -= player_damage
            print(f'Enemy Got HIT by {player_damage} HP!')
            fireball_cooldown = 2
            crit_chance = 0.15
            if random.random() < crit_chance:
                print(f'Critical HIT {player_damage} Damage!')
                player_damage *= 2
    elif move == "3":           
            player_defense = True
            enemy_damage = random.randint (4, 10)
            player_hp = (max(0, player_hp - 3))
            print('You defended yourself')
            player_hp -= enemy_damage
    elif move == "4":
        if heal_cooldown > 0:
            print('Healing is on Cooldown!')
        else:
            heal = random.randint (5, 15)
            player_hp += heal
            if player_hp > player_max_hp:
                player_hp = player_max_hp
                print(f'You heal for {heal} HP!')
                heal_cooldown = 2
    else:
     player_damage = 0
     print ('You missed')
    if enemy_hp <= 0:
     break
      #player turn ends
      #enemy turn
    enemy_damage = random.randint (10, 15)
    enemy_defense = False
    player_hp -= enemy_damage
    print (f'You are HIT {enemy_damage}!')
    if random.random() < 0.12:
        print (f'Enemy Critical Hit {enemy_damage}!')
        enemy_damage *= 2
        if random.random() < counter_chance:
            random.randint (1, 5)
        else:
            enemy_defense = True
            enemy_hp = (max(0, enemy_hp - 3))
            print('Enemy has defended')
            #double damage on critical hit
                 #enemy turn ends
    #print turn number 
    if fireball_cooldown > 0:
        fireball_cooldown -= 1
    if heal_cooldown > 0:
        heal_cooldown -= 1
    print()
    turn += 1
#determine winner    
if player_hp <= 0:
    print('You lose!')
elif enemy_hp <= 0:
    print('You win!')