def func_a(a, b):
    if a > b:
        return a
    if a < b:
        return b

# print(func_a(5, 6))


'''
Завдання a,b,c не потребують виведення результату на екран,
але я їх залишив для перевірки роботи функції.
Можу видалити якщо потрібно
'''


def func_b(a, b, c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < a and c < b:
        return c

# print(func_b(a=3, b=3, c=1))


def func_c(a):
    if a >= 0:
        return a
    if a < 0:
        return a * -1

# print(func_c(-2))


def func_d(a, b):
    return a + b

print(func_d(2, 3))


def func_e(a):
    if a > 0:
        return "The value is positive"
    elif a < 0:
        return "The value is negative"
    elif a == 0:
        return "The value is zero"
    else:
        return "Please use numbers only"

print(func_e(3))
