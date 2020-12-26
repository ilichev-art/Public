quantity_ticket = int(input('Введите количество билетов:\n'))
age = int(input('Введите возраст:\n'))
price = 0

if quantity_ticket <= 3:
    if 18 <= age <= 25:
        price = 990
    elif age > 25:
        price = 1390
    print('Сумма: ', quantity_ticket * price)
elif quantity_ticket > 3:
    if 18 <= age <= 25:
        price = 990
    elif age > 25:
        price = 1390
    print('Сумма со скидкой: ', int((quantity_ticket * price) * 0.9))
else:
    price = 0
