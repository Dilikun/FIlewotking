def read_recipes(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            num_ingredients = int(file.readline())
            ingredients_list = []
            for _ in range(num_ingredients):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()})
            cook_book[dish_name] = ingredients_list
            file.readline()  # пропускаем пустую строку
    return cook_book

cook_book = read_recipes('receipts.txt')
print(cook_book)