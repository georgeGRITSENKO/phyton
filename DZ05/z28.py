def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b-1)

a = int(input('Введите число 1-ое: '))
b = int(input('Введите число 2-ое: '))
print(sum(a, b))