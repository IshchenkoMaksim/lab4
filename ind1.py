#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    m = int(input('Введите число времени года от 1 до 4: '))

    if m == 1:
        print('Декабрь, Январь, Февраль,')
    elif m == 2:
        print('Март, Апрель, Май')
    elif m == 3:
        print('Июнь, Июль, Август')
    elif m == 4:
        print('Сентябрь, Октябрь, Ноябрь')
    else:
        print('Неверное число', file=sys.stderr)
        exit(1)
