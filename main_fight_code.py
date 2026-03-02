def health_bar(hp, total = 100, chars = ("#", "-"), bar_length = 20):
    total = max(1, total)
    filled_length = int(round(hp / total * bar_length))
    empty_length = int(bar_length - hp / total * bar_length)
    filled_bar = chars[0] * filled_length
    empty_bar = chars[1] * empty_length
    return f"[{filled_bar}{empty_bar}]"
import random
player_hp = 100
enemy_hp = 100
turn = 1
counter_chance = 0.5
player_defense = False
enemy_defense = False
#player turn
enemy_damage = 0
player_defense = False
while player_hp > 0 and enemy_hp > 0:
    print (f'------Turn {turn}------')
    print(health_bar(player_hp), player_hp)
    print(health_bar(enemy_hp), enemy_hp)
    move = input('Choose 1-Slash, 2-Fireball or 3-Defense')
    player_damage = 0
    if random.random() < 0.15: #15% chance to miss
        player_damage = 0
        print('You missed!')
        if random.random() < 0.15:
            print ('Critical HIT!')
            player_damage *= 2
        elif random.random() < 0.85:
            print ('No damage dealt')
        move = input('Choose 1-Slash or 2-Fireball')
    if move == "1":
        enemy_hp -= 5
        print ('Enemy HIT!')
    elif move == "2":
        enemy_hp -= 10
        print ('Enemy HIT!')
        while:
           move = "3"
           player_defense = True
           player_hp = (max(0, enemy_damage - 3))
           player_hp -= enemy_damage
           print('You defended yourself')
else:
 print('Turn missed')
if random.random() < counter_chance:
            random.randint (1, 5)
            enemy_damage -= player_damage
            print ('You counterattack!') #player turn ends
    #enemy turn
if enemy_hp > 0:
         enemy_damage = 0
         if random.random() < 0.2:
            enemy_damage = 0
            print('Enemy missed!')
         else:
            enemy_damage = random.randint (1, 10)
            player_hp -= enemy_damage
            print (f'You are HIT!')
            if random.random() < 0.12:
                print ('Enemy Critical Hit!')
                enemy_damage *= 2
                if random.random() < counter_chance:
                    random.randint (1, 5)
                else:
                    enemy_defense = True
                    enemy_hp = (max(0, player_damage - 3))
                    enemy_hp -= player_damage
                    print('Enemy has defended')  #double damage on critical hit
                 #enemy turn ends
    #print turn number 
print ('Turn:', turn)
print ('------------------------------')
turn += 1
#determine winner    
if player_hp <= 0:
    print('You lose!')
elif enemy_hp <= 0:
    print('You win!')