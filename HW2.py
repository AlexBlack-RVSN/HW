#Задание 1.
a_list = [1, 5, 'Hello!', True, 12.256]
def type(a_list):
    for element in a_list:
        if isinstance(element, int):
            print('Число.')
        if isinstance(element, str):
            print('Строка.')
        if isinstance(element, float):
            print('Число с запятой.')
        if isinstance(element, bool):
            print('Булевый тип.')
type(a_list)

#Задание 2.
el_count = int(input("Введите количество элементов списка:"))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

#Задание 3.
months = int(input('Введите номер месяца: '))
months_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
months_dict = {12: "зима",  1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
               10: "осень", 11: "осень"}
if 1 <= months <= 2:
    print(f"Сейчас {months_list[months - 1]}. Бррр, холодно, {months_dict.get(months)} ведь.")
elif 3 <= months <= 5:
    print(f"Сейчас {months_list[months - 1]}. Мммм, все цветет {months_dict.get(months)} ведь.")
elif 6 <= months <= 8:
    print(f"Сейчас {months_list[months - 1]}. Ухх, лето. Зажжем, {months_dict.get(months)} ведь.")
elif 9 <= months <= 11:
    print(f"Сейчас {months_list[months - 1]}. Фуу, {months_dict.get(months)} ведь.")
elif months == 12:
    print(f"Сейчас {months_list[months - 1]}. Бррр, холодно, {months_dict.get(months)} ведь.")
else:
    print(f"В году 12 месяцев, месяца № {months} не существует.")

#Задание 4.
my_str = input('Введите предложение: ')
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f' {num} {my_word [el]}')
        num += 1
    else:
        print(f' {num} {my_word [el] [0:10]}')
        num += 1

#Задание 5.
my_list = [1, 2, 3, 5, 7, 7]
print(f'Рейтинг - {my_list}')
number = int(input('Введите число (-1 - выход): '))
while number != -1:
    for el in range(len(my_list)):
        if my_list[el] == number:
            my_list.insert(el + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[el] > number and my_list[el + 1] < number:
            my_list.insert(el + 1, number)
    print(f'текущий список - {my_list}')
    number = int(input('Введите число: '))

#Задание 6.
product = []
property_product = {'Название': '', 'Цена': '', 'Кол-во': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Кол-во': [], 'Единица измерения': []}
num = 0
feature = None
control = None
while True:
    control = input('Для создания списка нажмите "Enter", для аналитики списка введите "A", для выхода нажмите "Q".'
                    '').upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print('Аналитика ваших товаров: ')
        for key, value in analytics.items():
            print(f'{key[:25]}: {value}')
    for f in property_product.keys():
        feature = input(f'Введите данные: {f} ')
        property_product[f] = int(feature) if (f == 'Цена' or f == 'Кол-во') else feature
        analytics[f].append(property_product[f])
    product.append((num, property_product))








