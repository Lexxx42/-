# Библиотеки анализа данных
# NumPy - работа с числовыми массивами | pip install numpy
# matplotlib - построение графиков | pip install matplotlib


from numpy import *

# [2 3 4] - создание одномерного массива из списка целых чисел
a = array([2, 3, 4])
print(a)

print(a.ndim)  # 1 - посмотреть размерность массива (1-одномерный, 2 - двумерный)

print(a.shape)  # (3,) - размер массива (число строк, столбцов и т.д.)

# создание 2-мерного массива из двух последовательностей чисел
b = array([(1.5, 2, 3), (4, 5, 6)])
print(b)  # [[1.5 2.  3. ]
# [4.  5.  6. ]]
# Все числа имеют тип с плавающей точкой
print(b.ndim)  # 2
print(b.shape)  # (2, 3) - 2 строки, 3 столбца
print(b.size)  # 6 - количество элементов

z = zeros((3, 2))  # массив заполненный нулями, 3 строки, 2 столбца
print(z)
# [[0. 0.]
# [0. 0.]
# [0. 0.]]

# [10 15 20 25] - генерация массива, (нач знач, кон знач, шаг)
print(arange(10, 30, 5))

print(linspace(0, 2, 9))  # [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ] -
# генерирует 9 чисел на отрезке от 0 до 2 с равным шагом (нач, кон, кол-во точек). Конец включен!

# одномерный массив можно превратить в двумерный
b = arange(12).reshape(4, 3)
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

a = array([10, 20, 30])
b = arange(3)
print(a)  # [10 20 30]
print(b)  # [0 1 2]

# Арифметические операции на массивах выполняются поэлементно
print(a+b)  # [10 21 32]
print(a-b)  # [10 19 28]

print(a**2)  # [100 400 900]


print(2*sin(a))  # [-1.08804222  1.8258905  -1.97606325]

print(a < 20)  # [ True False False]
