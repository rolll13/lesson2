print('Exc_1')


def task1():
    try:
        unit = int(input("Что во что переводим: байты в килобайты - 1,"
                         " килобайты в байты - 2 "))
    except ValueError:
        print('Неверный выбор, попробуй еще')
    else:
        if unit != 1 and unit != 2:
            print('Неверный выбор, попробуй еще')
        else:
            num = int(input('Введите число: '))
            if unit == 1:
                return num / 1024
            else:
                return num * 1024


print(task1())

print("Exc_2")


def task2():
    number = input("Введите число: ")
    mult = 1
    _sum = 0
    for num in number:
        _sum += int(num)
        if num != 0:
            mult *= int(num)
        else:
            mult = 0
    return 'Сумма: ', _sum, 'Произведение: ', mult


print(task2())

print('Exc_3')


def task3():
    min_x = float(input('Минимальное значение x: '))
    max_x = float(input('максимальное значение х: '))
    step = float(input('Шаг: '))
    x = min_x

    while x <= max_x:
        y = -1.24 * x ** 2 + x
        print('Y = ', y, ' X = ', x)
        x += step
    else:
        return 'Конец'


print(task3())

print('Exc_4')


def task4():
    num = input('Введите число: ')
    pos_end = len(num) - 1
    pos_start = 0
    palindrome = True

    while pos_start < pos_end:
        if num[pos_start] == num[pos_end]:
            pos_start += 1
            pos_end -= 1
            palindrome = True
        else:
            return 'Не палиндром'
    if palindrome:
        return 'Палиндром'


print(task4())
print('Exc_5')


def task5():
    l = [1, -5, 8, 13]
    len_l = len(l)
    _sum = 0

    for num in l:
        if num > 0:
            _sum += num
        else:
            len_l -= 1
            continue
    return _sum / len_l


print(task5())
