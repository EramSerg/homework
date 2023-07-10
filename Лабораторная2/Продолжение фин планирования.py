salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = spend - salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

#print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)
for i in range(1, months):
    spend = spend + spend * increase
    money_capital = money_capital + spend - salary



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
