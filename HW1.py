#Задание 1
a = 'Привет '
b = 'я Алексей.'
print(a,b)
d = input('Как тебя зовут? ')
c = int(input('Сколько тебе лет? '))
e = input('Чем ты занимаешься? ')

#Задание 2
sec = int(input('Введите количество секунд: '))
h = sec//3600
m = (sec-h*3600)//60
s = sec % 60
print(h, 'час', m, 'минут', s, 'сек')

#Задание 3
def sum(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)
sum(int(input("Введите число: ")))

#Задание 4
i = str(input("Введите число: "))
m = max(i)
print(m)

#Задание 5
revenue = int(input('Введите Вашу выручку за месяц: '))
cost = int(input('Введите Ваши расходы за месяц: '))
profit = revenue - cost
expenses = cost - revenue
profitability = (profit/revenue)
if revenue > cost:
    print('Ваша чиста прибыль: ' + str(profit))
    print("Рентабельность составила: " + str(profitability))
elif revenue < cost:
    print('Ваши расходы составили: ' + str(expenses))
else:
    print('В этом месяце Вы не заработали, но и ничего не потеряли.')
workers = int(input('Сколько у Вас сотрудников: '))
one_worker = profit / workers
print('Ваша прибыль, в расчете на одного сотрудника: ' + str('%.1f'%one_worker))

#задание 6
a = int(input("Сколько Вы пробежали сегодня км: "))
b = int(input("Сколько бы Вы хотели бегать в день км: "))
days = 1
while a < b:
    a = a + a * 0.1
    days += 1
print("Вы достигнете своей цели на " + str(days) + " день.")


