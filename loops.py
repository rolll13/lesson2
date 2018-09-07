print('WHILE')
i = 10
while i > 0:
    i = i - 1
    if i == 5:
        continue
    print(i)
else:
    print('Else')

print('FOR')
for var in "123":
    print(var)
else:
    print('Else')

    # print("Exception", 1 / 0)
try:
    byte1 = b"123"
except (TypeError, ZeroDivisionError, ValueError):
    print('Wrong bytes')
else:
    print('Try else')
finally:
    pass

try:
    a = 1 / 0
except ZeroDivisionError:
    pass

try:
    a = 1
finally:
    pass

byte1 = b"123"
try:
    byte1[1] = 12

    try:
        1 / 0
    except:
        pass
except TypeError:
    pass

a = [1, 2, 3] #  list
print(a[0], a[-1], a[0] == a[-3])
b = (1, 2, 3) #  tuple
c = {1: 2, 3: 4}  # dict

c = {
    (1, 2): 3,
    "123": 4,
    b"123": 5
}
c[(1,2)]
c["123"]
c[b"123"]

c["123"] = 44

a = {}
a[1] = 1
a[1.0] = 2
a[True] = 3
{
    1: 3
}









