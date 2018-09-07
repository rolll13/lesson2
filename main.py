print("Hello, world")
# VARIABLES
variable1 = 1
variable2 = 2

# print(variable1, variable2)
buffer = variable2
variable2 = variable1
variable1 = buffer
# print(variable1, variable2)

# NUMBERS
big_value = 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
print(big_value)

float_number = 123.1
complex_number = 123 + 123j

# STRINGS
string1 = "Double quote"
string2 = 'Single quote'
string3 = """Triple quote"""
string4 = '''Triple quote'''

string5 = '"""""""""'
string6 = '\''

# OPERATORS
a = 324234
b = 23543234
# print('Numbers', a, b)
# print('+', a + b)
# print('-', a - b)
# print('*', a * b)
# print('/', a / b)
# print('//', a // b)
# print('%', a % b)
#
# print('Swap', a, b)
a = a + b
b = a - b
a = a - b
# print(a, b)

variable3 = 0b10101
variable4 = 0x12345


a = 4
b = 5

print('&', a & b)
print('|', a | b)
print('^', a ^ b)
print('>>', a >> 3)
print('<<', a << 3)

byte1 = b"123"
print(byte1)
byte2 = bytes("123", 'utf8')
byte3 = bytearray("""123""", 'utf8')
print(byte2)
print(byte3, byte3[0], byte3[1])
byte3[2] = 56
print(byte3)

CONST_VARIABLE = 1
default_value = 1

# OPERATORS

a = 3453
b = 3453
print(a, b)
print('<', a < b)
print('<=', a <= b)
print('>', a > b)
print('>=', a >= b)
print('==', a == b)
print('!=', a != b)

print(True, False)
print(None)
print('Compare string with False', '' == False)
print('Empty string', not '')
print(True and True, True and False)
print(False or True or False)

if True:
    a = 1

if False:
    a = 1
elif False or True:
    c = 1
elif False or True or False:
    d = 1
else:
    b = 1

if True:
    if True:
        if True:
            a = 1
        else:
            c = 1
    else:
        d = 1
else:
    z = 1

print("Information")
a = input("Your name?")
print(a)










