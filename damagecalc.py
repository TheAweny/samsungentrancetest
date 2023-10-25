def calculate_damage(enchanted_sword, bow_damage, spell_damage, physical_defense, magical_defense):
    max_damage = 0

    # Рассчитываем урон от атаки зачарованным мечом
    physical_damage = max(0, enchanted_sword[0] - physical_defense)
    magical_damage = max(0, enchanted_sword[1] - magical_defense)
    total_damage = physical_damage + magical_damage
    max_damage = max(max_damage, total_damage)

    # Рассчитываем урон от атаки из лука
    physical_damage = max(0, bow_damage - physical_defense)
    max_damage = max(max_damage, physical_damage)

    # Рассчитываем урон от заклинания
    magical_damage = max(0, spell_damage - magical_defense)
    max_damage = max(max_damage, magical_damage)

    return max_damage

# Ввод данных
enchanted_sword = list(map(int, input().split()))
bow_damage = list(map(int, input().split()))
defenses = list(map(int, input().split()))

# Вычисляем максимальный урон
max_damage = calculate_damage(enchanted_sword, bow_damage[0], bow_damage[1], defenses[0], defenses[1])

# Вывод результата
print(max_damage)