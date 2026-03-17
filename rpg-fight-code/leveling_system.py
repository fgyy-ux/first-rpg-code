def check_xp(player_xp, player_level):
    player_level = player_xp * 10
    if player_xp >= player_level:
        player_level += 1
        player_xp -= player_level
        print(f'You leveled UP! You are now level {player_level}')
        return player_xp, player_level