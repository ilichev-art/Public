per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))

a = money / 100 * per_cent['ТКБ']
b = money / 100 * per_cent['СКБ']
c = money / 100 * per_cent['ВТБ']
d = money / 100 * per_cent['СБЕР']
deposit = []
deposit.append(a)
deposit.append(b)
deposit.append(c)
deposit.append(d)

deposit_round = list(map(round, deposit))
print('Накопленные средства за год составят:')
print(deposit_round)
print('Максимальная сумма составит:')
print(max(deposit_round))





