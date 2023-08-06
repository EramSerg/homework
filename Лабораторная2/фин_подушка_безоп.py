money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    raznica = spend - salary
    if raznica > money_capital:
        break

    money_capital = money_capital - raznica
    spend = spend * (1 + increase)
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
#print("Количество месяцев, которое можно протянуть без долгов:", ...)

