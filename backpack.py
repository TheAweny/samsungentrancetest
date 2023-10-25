class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Main:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_heaviest_item(self):
        if not self.items:
            return None  # Рюкзак пустой

        heaviest_item = self.items[0]

        for item in self.items:
            if item.weight > heaviest_item.weight:
                heaviest_item = item

        return heaviest_item


if __name__ == "__main__":
    backpack = Main()

    # Добавляем предметы в рюкзак
    backpack.add_item(Item("Меч", 5))
    backpack.add_item(Item("Щит", 7))
    backpack.add_item(Item("Зелье здоровья", 1))

    # Находим самый тяжелый предмет
    heaviest_item = backpack.find_heaviest_item()

    if heaviest_item:
        print("Самый тяжелый предмет в рюкзаке:", heaviest_item.name)
    else:
        print("Рюкзак пустой")