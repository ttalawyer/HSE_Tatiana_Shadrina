# Функция для проверки монотонности
def is_monotonic(nums):
    # если в списке меньше 2 элементов — он точно монотонный
    if len(nums) < 2:
        return True

    # сначала определим направление
    i = 0
    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
        i += 1

    # если все элементы равны — True
    if i == len(nums) - 1:
        return True

    # определяем, растёт ли последовательность
    increasing = nums[i] < nums[i + 1]

    # теперь проверяем всю последовательность
    while i < len(nums) - 1:
        if increasing:
            if nums[i] > nums[i + 1]:
                return False
        else:
            if nums[i] < nums[i + 1]:
                return False
        i += 1

    return True


# --- Основная часть программы ---
# Запрашиваем у пользователя ввод
user_input = input("Введите числа через запятую: ")

# Преобразуем строку в список чисел
nums = [int(x.strip()) for x in user_input.split(",")]

# Проверяем и выводим результат
if is_monotonic(nums):
    print("Последовательность является монотонной.")
else:
    print("Не является монотонной.")
