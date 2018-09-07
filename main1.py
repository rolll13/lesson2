# n1 = int(input("Введите первое число? "))
# n2 = int(input("n2? "))
# n3 = int(input("n3? "))
#
# r = None
# if n1 > n2 and n1 > n3:
#     r = n1
# elif n2 > n1 and n2 > n3:
#     r = n2
# elif n3 > n1 and n3 > n2:
#     r = n3
# else:
#     r = n1
#
# print("Max", r)

# Вводятся два целых числа.
# Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом,
# а также остаток (если он есть) и
# частное (в любом случае).

n1 = int(input("n1 "))
n2 = int(input("n2 "))
print(not bool(n1 % n2), n1 % n2)

if n1 % n2 == 0:
    print(True)
else:
    print(False)











