class Player:
    def __init__(self):
        Player.hp = 100
        Player.max_hp = 100
        Player.heal_cooldown = 0
        Player.fix_heal = 0

        Player.damage = 10
        Player.fireball_damage = 25
        Player.fireball_cooldown = 0
        Player.defense = False

        Player.xp = 0
        Player.level = 1
        Player.xp_needed = 10
        
        Player.ability_points = 0