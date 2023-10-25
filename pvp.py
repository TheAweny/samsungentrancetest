time = 18
attack_per_second = 2
first_damage = 112

# Вычисление количества атак
attacks = time * attack_per_second

# Вычисление суммарного урона
total_damage = (attacks / 2) * (2 * first_damage + (attacks - 1) * -1)

print("Суммарный урон рыцаря:", total_damage)