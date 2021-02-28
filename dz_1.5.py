revenue = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
if revenue > expenses:
    print('Фирма работает с прибылью')
    profitability = (revenue - expenses) / revenue
    print('Рентабельность: ', profitability)

    count = int(input('Введите число сотрудников: '))
    print('Прибыль на одного сотрудника: ', (revenue - expenses) / count)

else:
    print('Фирма работает в убыток или в 0')
