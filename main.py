import os


# first Task
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


# print(cook_book)

# Second task
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return shop_list




def merge_files(directory):
    files = os.listdir(directory)

    file_contents = {}

    for filename in files:
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.readlines()
            file_contents[filename] = content

    sorted_files = sorted(file_contents.items(), key=lambda x: len(x[1]))

    with open('merged.txt', 'w', encoding='utf-8') as file:
        for filename, content in sorted_files:
            file.write(f'{filename}\n')
            file.write(f'{len(content)}\n')
            file.writelines(content)


def main():
    merge_files('some_txt')
    cook_book = read_recipes('receipts.txt')


if __name__ == '__main__':
    main()


