bilets = int(input('Введите количество билетов:'))
summa = 0

for ticket in range(bilets):
    age = int(input('Введите Ваш возраст:'))
    if age < 18:
        summa += 0
        print('Бесплатно')
    if 18 <= age <= 25:
        summa += 990
        print('Cумма за билет:990')
    if age > 25:
        summa += 1390
        print('Cумма за билет:1390')
        
if bilets >= 3:
    summa = summa - (summa//100*10)
print('Сумма за все выбранные билеты:',int(summa))
