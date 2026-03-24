import random
import leveling_system
def health_bar(hp, total = 100, chars = ("#", "-"), bar_length = 20):
    total = max(1, total)
    hp = max(0, min(hp, total))
    filled_length = int(round(hp / total * bar_length))
    empty_length = int(bar_length - hp / total * bar_length)
    filled_bar = chars[0] * filled_length
    empty_bar = chars[1] * empty_length
    return f"[{filled_bar}{empty_bar}]"

player_hp = 100
player_max_hp = 100
enemy_hp = 100
turn = 1
counter_chance = 70
player_defense = False
enemy_defense = False
enemy_crit_attack = False
heal_cooldown = 0
fireball_cooldown = 0
player_damage = 10
fireball_damage = 25
heal_random = 0
enemy_damage_random = 0
player_level_before_the_fight = 1
level_points = 1

#player turn
while player_hp > 0 and enemy_hp > 0:
    print (f'------Turn {turn}------')
    print(health_bar(player_hp), player_hp)
    print(health_bar(enemy_hp), enemy_hp)
    move = input('Choose 1-Slash, 2-Fireball, 3-Defense or 4-Heal: ')
    if move == "1":
        enemy_hp -= player_damage
        print (f'Enemy Got HIT by {player_damage} HP!')
    elif move == "2":
        if fireball_cooldown > 0:
            print('Fireball is on Cooldown!')
        else:
            enemy_hp -= fireball_damage
            print(f'Enemy Got HIT by {fireball_damage} HP!')
            fireball_cooldown = 2
            crit_chance = 0.15
            if random.random() < crit_chance:
                print(f'Critical HIT {fireball_damage} Damage!')
                fireball_damage *= 2
    elif move == "3":           
            player_defense = True
    elif move == "4":
        if heal_cooldown > 0:
            print('Healing is on Cooldown!')
        else:
            heal = random.randint (15, 20)
            heal += heal_random
            player_hp = min(player_max_hp, player_hp + heal) 
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
    enemy_damage += enemy_damage_random
    enemy_defense = False
    if random.random() < 0.12:
        enemey_crit_atack = True
        enemy_damage *= 2
        if random.random() < counter_chance:
            random.randint (1, 5)
        else:
            enemy_defense = True
            enemy_hp = (max(0, enemy_hp - 3))
            print('Enemy has defended')
    if player_defense == True:
        enemy_damage /= 2
        enemy_damage = round (enemy_damage)
        print('You defended yourself')  
        player_defense = False
    if enemy_crit_attack == False:
        player_hp -= enemy_damage
        print (f'You are HIT {enemy_damage}!')
    if enemy_crit_attack == True:
        print (f'Enemy Critical Hit {enemy_damage}!')
        enemy_crit_attack = False
        player_hp -= enemy_damage

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
    player_xp = 0

    #gain xp
    leveling_system.player_xp += 5
    leveling_system.player_level, leveling_system.player_xp = leveling_system.check_xp(leveling_system.player_level, leveling_system.player_xp)

     #gain level points
    level_points += leveling_system.player_level 
    level_points -= player_level_before_the_fight
    player_level_before_the_fight = leveling_system.player_level
    print(f'You have {level_points} level points')