class Index(Exception):
    def __init__(self, a):
        self.a = a


class Name(Exception):
    def __init__(self, b):
        self.b = b


w = [1, 2, 3, 4, 5]


def sum_(www, total):
    summ = 0
    if not isinstance(total, int):
        raise Name(f'аргумент {total} не является числом')
    www.append(total)
    for i in range(len(www)):
        if i == len(www) - 1:
            raise Index('Дальше поймаешь IndexError')
        if www[i] > www[i + 1]:
            summ += 1
    print(summ)


try:
    print(sum_(w, 6))
except Index:
    print('Придумай что-то другое')
except Name:
    print('Нужно написать число')
finally:
    print('поздравляю, вы написали изначально нерабочий код)))')
print()
try:
    print(sum_(w, 'шесть'))
except Index:
    print('Придумай что-то другое')
except Name:
    print('Нужно написать число')
