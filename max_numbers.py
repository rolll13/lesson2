try:
    n = int(input("Input count of numbers? "))
except ValueError:
    print("Wrong number")
else:
    arr = []
    while n > 0:
        try:
            number = int(input("Number? "))
        except ValueError:
            print("Wrong value, try again")
        else:
            n = n - 1
            arr.append(number)
    max_number = -2 ** 31
    for value in arr:
        if value > max_number:
            max_number = value

    print(max_number)

# https://git-scm.com
# tkinter
# PyQt
print("new line")