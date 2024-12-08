import numpy as np


def get_user_input():
    user_input = input("Введите числа, разделенные запятыми: ")
    numbers = []
    try:
        for item in user_input.split(','):
            number = float(item.strip())
            numbers.append(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числа, разделенные запятыми.")
        return
    return numbers

def calculate_statistics(numbers):
    mean_num = sum(numbers) / len(numbers)
    std_devl = np.std(numbers)
    return mean_num, std_devl


user_numbers = get_user_input()
if user_numbers is not None:
    mean, std_dev = calculate_statistics(user_numbers)
    print("Среднее значение:", mean)
    print("Стандартное отклонение:", std_dev)



# def is_nan_or_inf(value) -> True|False:
#    return math.isnan(value) or math.isinf(value)
