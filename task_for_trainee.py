#  task 1
# Составить алгоритм: если введенное число больше 7, то вывести “Привет”
number = int(input('Пожалуйста, введите число: '))
print('Привет' if number > 7 else '')


def task_check_number(check_number):
    print('Привет' if check_number > 7 else '')


# task 2
# Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”,
# если нет, то вывести "Нет такого имени"
name = input('Пожалуйста, введите свое имя: ')
print('Привет, Вячеслав' if name == 'Вячеслав' else 'Нет такого имени')


def task_check_name(check_name):
    print('Привет, Вячеслав' if check_name == 'Вячеслав' else 'Нет такого имени')


# task 3
# Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
lst = list(map(int, input("Введите числовой массив (целые числа через пробел): ").split()))
print('Элементы массива кратные 3: ', list(filter(lambda x: x % 3 == 0, lst)))


def task_array(array: list):
    print('Элементы массива кратные 3: ', list(filter(lambda x: x % 3 == 0, array)))


if __name__ == "__main__":
    task_check_number(8)
    task_check_name('Вячеслав')
    task_array([3, 5, 8, 12])
