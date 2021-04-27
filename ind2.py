#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = float(input('Введите числа: a, b и c через Enter: a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    if a < b < c or a == b < c or a < b == c or a == b == c:
        print(a, b, c)

    elif a < c < b or a == c < b:
        print(a, c, b)

    elif b < a < c or b < a == c:
        print(b, a, c)

    elif b < c < a or b == c < a:
        print(b, c, a)

    elif c < a < b or c < a == b:
        print(c, a, b)

    elif c < b < a:
        print(c, b, a)

    if a > b > c or a == b > c or a > b == c or a == b == c:
        print(a, b, c)

    elif a > c > b or a == c > b:
        print(a, c, b)

    elif b > a > c or b > a == c:
        print(b, a, c)

    elif b > c > a or b == c > a:
        print(b, c, a)

    elif c > a > b or c > a == b:
        print(c, a, b)

    elif c > b > a:
        print(c, b, a)
