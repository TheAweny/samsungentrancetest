def binary_search_spell(book, spell_name):
    low = 0
    high = len(book) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_spell = book[mid]

        if mid_spell == spell_name:
            return mid  # Нашли заклинание, возвращаем индекс страницы
        elif mid_spell < spell_name:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Заклинание не найдено


#   Пример использования:

book = [
    "Acid Splash",
    "Acid Stream",
    "Acid Spray",
    "Acid Cloud",
    "Acid Fog",
    "Acidic Spray",
    "Acidic Stream",
    "Acidic Splash",
    "Acidic Cloud",
    "Acidic Fog",
    "Acid Storm",
    "Acid Torrent",
    "Acid Wave",
    "Acidic Wave",
    "Acid Tornado",
    "Acidic Tornado",
    "Acid Storm",
    "Acid Blizzard",
    "Acidic Blizzard",
    "Acid Rain",
    "Acidic Rain",
    "Acid Spray",
    "Acid Stream",
    "Acid Spray"
]
print(f"Список заклинаний: {book}")
# book = [str(i) for i in range(1, 6522794)]  # Раскомментируйте, если поиск должен проходить по номеру)
spell_name = input("Введите название заклинания в книге: ")  # Заклинание, которое нужно найти

result = binary_search_spell(book, spell_name)
if result != -1:
    print(f"Заклинание '{spell_name}' найдено на странице {result + 1}")
else:
    print(f"Заклинание '{spell_name}' не найдено в книге.")