def check_xp(player):
    player.xp_needed = player.level * 10
    if player.xp >= player.xp_needed:
        player.level += 1
        player.xp -= player.xp_needed
        print(f'You leveled UP! You are now level {player.level}')
        
    return player.xp, player.level