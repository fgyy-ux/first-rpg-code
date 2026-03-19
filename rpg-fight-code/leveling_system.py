player_xp = 0
player_level = 1
def check_xp(player_xp, player_level):
    needed_xp = player_xp * 10
    if needed_xp >= player_level:
        player_level += 1
        player_xp -= needed_xp
        print(f'You leveled UP! You are now level {player_level}')
        return player_xp, player_level