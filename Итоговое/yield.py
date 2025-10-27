#Запрос числа
number = int(input("Ведите желаемое количество чисел: "))

# Генератор чисел Фибоначчи
def fib_generator(n):
    a, b = 0, 1
    count = 0

    while count < n:
        yield a  # отдаём текущее значение, но не выходим из функции
        a, b = b, a + b
        count += 1

# Используем генератор
for num in fib_generator(number):
    print(num) 