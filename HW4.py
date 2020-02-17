from functools import reduce
from itertools import cycle, count
from math import factorial
def sep(sep, sep2):
    return sep * sep2

print(sep('*', 50))


#Задание1.
def sal():
    time = float(input('Выработка в часах: '))
    salary = int(input('Оплата в час: '))
    bonus = int(input('Премия: '))
    res = time * salary + bonus
    print(f'Заработная плата сотрудника: {res}')
sal()

print(sep('*', 50))

#Задание 2.
my_list = [19, 22, 13, 4, 58, 66, 7, 8]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')

print(sep('*', 50))

#Задание 3.
print(list([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]))

print(sep('*', 50))

#Задание 4.
my_list = [11, 44, 22, 43, 22, 48, 11, 48, 5]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

print(sep('*', 50))

#Задание 5.
def my_func(el_p, el):
    return el_p * el
print(f'Четные числа: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

print(sep('*', 50))

#Задание 6.
def count_list():
    for el in count(11):
        if el > 26:
            break
        else:
            print(el)
print(count_list())

def cycle_list():
    n = 0
    for el in cycle('ABC'):
        if n > 11:
            break
        else:
            print(el)
            n += 1
print(cycle_list())

print(sep('*', 50))

#Задание 7.
def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
print(gen)
