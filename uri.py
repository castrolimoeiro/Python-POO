# -*- coding: utf-8 -*-

a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

maior_ab = (a + b + abs(a - b)) / 2
resultado = (maior_ab + c + abs(c - maior_ab)) / 2
print(f'{int(resultado)} eh o maior')
