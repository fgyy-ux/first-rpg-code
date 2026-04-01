def end_of_battle(player):
    if player.ability_points > 0:
        move = input('Do you want to spend you Ability Points? ' \
        '1-Yes, 2-No')
        if move == "1":
            print('Choose what ability to boost')
            spend_ability(player)

def spend_ability(player):
    print('1-Increase HP')
    choice = input(''> '')
    if choice == "1":
        player.max_hp += 10
        player.hp = player.max_hp
        player.ability_points -= 1