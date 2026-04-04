import random
class Enemy:
    def __init__(self):
        Enemy.hp = 100
        Enemy.counter_chance = 70
        Enemy.damage = random.randint (10, 15)
        Enemy.fix_damage = 0
        Enemy.protection_effectiveness = 2
        Enemy.critical_impact_multiplier = 2