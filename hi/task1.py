# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

numb = input('Введите дробное число: ')
some_str = str(numb).replace('.', '')
some_str2 = list(map(int, some_str))
summ = 0
for number in some_str2:
    summ += number
print(summ)


