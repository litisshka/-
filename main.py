# Вводим 5 целых чисел
numbers = []

for _ in range(5):
    value = int(input("Введите число: "))
    numbers.append(value)

# Выводим введённые числа
print("Исходный массив:", numbers)

# Начальные значения
maximum = numbers[0]
minimum = numbers[0]
total = 0

# За один цикл находим максимум, минимум и сумму
for value in numbers:
    if value > maximum:
        maximum = value

    if value < minimum:
        minimum = value

    total += value

# Выводим результат
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Сумма:", total)