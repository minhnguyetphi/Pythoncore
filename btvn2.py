# -*- coding: utf-8 -*-
"""BTVN2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kkU8Pqf5-RrYWc2hdY13QSb8_plzWRSy
"""

#Bài 1
age = int(input('Nhập tuổi: '))
income = float(input('Nhập thu nhập: '))
print(f'age > 18 and income >=2500 is', age >=18 and income >=2500)

#Bài 2
import math
x = float(input('Nhập giá trị: '))
y = float(input('Nhập giá trị: '))
z = float(input('Nhập giá trị: '))
F = (x + y + z)/(x**2 + y**2 +1) - math.fabs(x-z*math.cos(y))
print(f'Giá trị của F = {F}')

#Bài 3
a = float(input('Nhập giá trị: '))
b = float(input('Nhập giá trị: '))
print(a//b)
print(a%b)

a = float(input('Nhập giá trị: '))
b = float(input('Nhập giá trị: '))
print(a//b)
print(a%b)

a = float(input('Nhập giá trị: '))
b = float(input('Nhập giá trị: '))
print(a//b)
print(a%b)