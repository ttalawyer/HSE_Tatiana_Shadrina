def roman_to_int_generator(s):
    # таблица римских чисел
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    # идём по строке, пока не закончатся символы
    while i < len(s):
        # проверяем: если не последний символ и текущее число меньше следующего — вычитаем
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            step_value = values[s[i + 1]] - values[s[i]]
            total += step_value
            yield f"{s[i]}{s[i + 1]} = {step_value}, сумма = {total}"
            i += 2
        else:
            step_value = values[s[i]]
            total += step_value
            yield f"{s[i]} = {step_value}, сумма = {total}"
            i += 1

    # после цикла отдаём итог
    yield f"Итоговое число: {total}"

roman_number = input("Введите римское число: ")

for step in roman_to_int_generator(roman_number):
    print(step)