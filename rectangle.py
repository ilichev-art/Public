# quantity_ticket = int(input('Введите количество билетов:\n'))
# age = int(input('Введите возраст посетителя:\n'))
# price = 0
#
# if 18 <= age <= 25 and quantity_ticket <= 3:
#     price = 990
# elif age > 25 and quantity_ticket <= 3:
#     price = 1390
#     print('Сумма: ', quantity_ticket * price)
# elif 18 <= age <= 25 and quantity_ticket > 3:
#     price = 990
# elif age > 25 and quantity_ticket >= 3:
#     price = 1390
#     print('Сумма: ', quantity_ticket * price * 0.9)
# else:
#     price = 0

# Количество бесплатных чашек кофе за каждую 6-ю чашку
# cup = int(input('Введите количество чашек:'))
# free_cup = int(cup / 6)
# print('Вы заказали ', cup, 'чашек кофе')
# print('Вы получаете ', free_cup, ' бесплатно чашек кофе')


# Четное-не четное
# x = int(input('введите число:\n'))
# for i in range(x + 1):
#     if i % 2 == 0:
#         print(f'число {i} четное')
#     else:
#         print(f'число {i} не четное')

# x = int(input('Введите число:'))
# a = [n for n in range(0, x + 1) if n % 3 == 0 or n % 5 == 0]
#
# print(sum(a))

# list1 = [1,2,3,4,5,6]
# list2 = [4,5,6,7,8,10]
# a = [n for n in list1 if n % 2 == 0]
# b = [x for x in list2 if x % 2 != 0]
# c = a + b
# print(c)



# Посчиталь сумму "руки" в покере
# current_hand = [5,3,4,10,'Q',5]
# dict = {
#     2:1,
#     3:1,
#     4:1,
#     5:1,
#     6:1,
#     7:0,
#     8:0,
#     9:0,
#     10:-1,
#     'J':-1,
#     'Q':-1,
#     'K':-1,
#     'A':-1
# }
# card_sum = sum([dict[x] for x in current_hand])
# print(card_sum)

# Является ли число палиндромом?
# number = int(input('Введите число:'))
# reversed_number = 0
# tmp_original = number
# while tmp_original > 0:
#     reversed_number = (reversed_number * 10)+ tmp_original % 10
#     tmp_original = tmp_original // 10
#
# if number == reversed_number:
#     print('Palindrome!')
# else:
#     print('No Palindrome')


# Игра Камень-Ножницы-Бумага
# import random
#
# while True:
#     user = input('Enter choice [r/s/p]:').lower()
#     number = random.choice(['r', 's', 'p'])
#     print('Компьютер выбрал:', number)
#
#     winning_combinations = [('r','s'), ('s','p'), ('p','r')]
#     if user == number:
#         print('A draw')
#     elif (user, number) in winning_combinations:
#         print( 'User win!')
#     else:
#         print('Comp win!')
#     print(user, number)

# Игра орел-решка
# import random
#
# tries = 0
# cast = random.choice(['орел', 'решка'])
# while tries <= 100:
#     cast = random.choice(['орел', 'решка'])
#     tries += 1
#     print(str(cast))

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a **2

class Round:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area_round(self):
        return (self.a * 0 + 3.14) * self.b **2





