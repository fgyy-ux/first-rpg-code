import random
# скажу честно, я заюзал нейронку и поэтому враг теперь то-же ходит с игроком и на 4 магия исцеления на 5-10 хп
#и что на счет шанса оглушения при блокировании или шанс контр удара и добавления кд на магию
# Функция для рисования полоски здоровья
def health_bar(hp, total=100, chars=("#", "-"), bar_length=20):
    hp = max(0, min(hp, total)) # Чтобы полоска не уходила в минус или за предел
    filled_length = int(round(hp / total * bar_length))
    empty_length = bar_length - filled_length
    return f"[{chars[0] * filled_length}{chars[1] * empty_length}]"

# Начальные данные
player_hp = 100
player_max_hp = 100
enemy_hp = 100
turn = 1

print("--- Бой начинается! ---")

# Основной игровой цикл
while player_hp > 0 and enemy_hp > 0:
    print(f'\n------ Ход {turn} ------')
    print(f"Игрок: {health_bar(player_hp)} {player_hp}/{player_max_hp}")
    print(f"Враг:  {health_bar(enemy_hp)} {enemy_hp}/100")
    
    # --- ХОД ИГРОКА ---
    move = input('Выбери: 1-Удар, 2-Файербол, 3-Защита, 4-Исцеление: ')
    
    if move == "1":
        damage = 10
        enemy_hp -= damage
        print(f'Ты нанес {damage} урона мечом!')
        
    elif move == "2":
        damage = 20
        enemy_hp -= damage
        print(f'Огненный шар сжигает врага на {damage} HP!')
        
    elif move == "3":
        print('Ты встал в защитную стойку! (Урон врага в этом ходу будет снижен)')
        # Логику защиты можно усложнить, но пока просто пометим флаг
        
    elif move == "4":
        heal = random.randint(5, 10) # Магия исцеления
        player_hp += heal
        if player_hp > player_max_hp:
            player_hp = player_max_hp
        print(f'Магия исцеления! Ты восстановил {heal} HP.')
        
    else:
        print('Ты замешкался и пропустил ход!')

    # Проверка: не погиб ли враг после хода игрока?
    if enemy_hp <= 0:
        break

    # --- ХОД ВРАГА ---
    print("\nХод врага...")
    enemy_damage = random.randint(5, 15)
    
    # Если игрок выбрал защиту (кнопка 3), уменьшаем урон врага в 2 раза
    if move == "3":
        enemy_damage //= 2
        
    player_hp -= enemy_damage
    print(f'Враг атакует и наносит {enemy_damage} урона!')

    turn += 1

# --- ФИНАЛ ---
print('\n------------------------------')
if player_hp <= 0:
    print(f'Твое здоровье: 0. Ты проиграл...')
elif enemy_hp <= 0:
    print(f'Здоровье врага: 0. Победа!')