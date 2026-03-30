import leveling_system
from leveling_system import check_xp
check_xp()
def end_of_battle(player):
    level_up = leveling_system.check_xp(player)
    if level_up and player.xp > 0:
        move = input('Do you want to spend you Ability Points? ' \
        '1-Yes, 2-No')
        if move == "1":
            print('Choose what ability to boost')
            spend_ability(player)
        else:
            return move