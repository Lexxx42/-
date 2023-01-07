# Давайте для начала напишем самый простой объект для итератора.
# Наш объект, каждый раз когда мы будем запрашивать элемент, будет возвращать случайное число из
# диапазона от 0 до 1.
# from random import random
#
#
# class RandomIterator:
#     def __next__(self):
#         return random()
#
#
# x = RandomIterator()
# print(next(x))

# Чтобы экземпляр нашего класса стал итератором необходимо внутри нашего класса определить
# метод next().

# Когда мы вызываем функцию next(x) - это эквивалентно записи
# x.__next__(), таким образом, мы считаем, что х -- iterator тогда, когда у него есть
# данный метод.

# Теперь давайте определим нужную нам функциональность: мы хотим, чтобы вместо ноля
# у нас возвращалось случайное значение из диапазона 0, 1.

# Мы будем использовать функцию random() из библиотеки random.

# Теперь при каждом вызове метода next() нашего класса,
# возвращается случайное число в диапазоне от 0 до 1.

# Давайте обратим внимание на то, что в данный момент данный итератор будет генерировать бесконечную
# последовательность, потому что мы определили у него поведение,
# когда он должен бросать ошибку StopIteration.

# Давайте напишем конструктор у нашего класса.

# from random import random
#
#
# class RandomIterator:
#     def __init__(self, k):  # Наш конструктор будет принимать один дополнительный аргумент
#         self.k = k  # к - это именно то количество случ-х чисел, которое бы мы хотели,
#         # чтобы перебирал наш итератор. Давайте заполним его в качестве атрибута нашего экземпляра.
#         # А также в качестве атрибута нашего экземпляра инициализируем число i - это
#         # число уже перечисленных нашим итератором случайных чисел.
#         self.i = 0
#         # Инициализируем его нулем.
#
#     def __next__(self):  # Модифицируем наш метод __next__(). В том случае, если счетчик уже выведенных
#         # элементов меньше числа запланированного числа (того числа, которое мы передали в конструктор),
#         if self.i < self.k:
#             self.i += 1
#             return random()  # то мы должны вернуть случайное следующий элемент.
#         # При этом мы должны запомнить, что мы его вывели. Т.е. увеличить счетчик.
#         else:  # В том случае, если наш счетчик уже равен счетчику элементов, который мы планировали
#             # перечислить с помощью нашего итератора, то мы должны бросить ошибку
#             raise StopIteration
#
#
# # Чтобы данный код успешно запустить, мы должны передать число k в конструктор.
# x = RandomIterator(3)
# print(next(x))
# print(next(x))
# print(next(x))  # ок
# print(next(x))  # StopIteration

# Хорошо мы написали итератор, который перечисляет случайные элементы до тех пор, пока
# не выведет нужное нам число элементов.
# Однако можем ли мы его сразу использовать в цикле for?

# Для того чтобы мы могли использовать наш итератор в цикле for мы должны уметь вызывать
# функцию iter() от нашего объекта х.
# iter(x)  # object is not iterable

# Чтобы мы могли вызвать функцию iter(x) от объекта х, т.е. чтобы мы могли посчитать, что
# по нашему объекту можно итерироваться, мы решаем проблему подобным образом, как с
# методом __next__(). Мы на самом деле определяем внутри нашего класса метод __iter__().


# from random import random
#
#
# class RandomIterator:
#     def __iter__(self):  # Как мы помним, функция iter() должна возвращать экземпляр итератора.
#         return self
#
#     # Поэтому в случае с итераторами чаще всего метод итер возвращает именно self.
#     # А в случае с классами, которые мы хотим перебирать мы возвращаем экземпляр итератора.
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
#
#
# # Теперь когда мы описали метод __iter__() внутри нашего класса RandomIterator мы можем
# # его использовать в цикле for.
#
# for x in RandomIterator(10):
#     print(x)
# Увидим, что мы действительно перебрали 10 случайных чисел из диапазона 0-1.

# Мы с вами разобрались, что для того, чтобы объект можно было проитерировать, т.е. перебрать
# его элементы, у него должен быть определенный метод __iter__(), который возвращает нам итератор.
# А для того, чтобы объект являлся итератором у него должен быть определенный метод __next__().

# Давайте попробуем определить как себя ведет метод __iter__() для какого-нибудь нашего класса.

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


# Напишем класс MyList отнаследовав его от list.
# Таким образом, чтобы каждый раз, когда мы итерировались по объекту класса MyList мы бы перебирали
# элементы парами.
# Прежде всего стоит отметить, что метод __iter__() уже определен в нашем классе list, поэтому
# если бы мы использовали наследование, но при этом не определили наш метод __итер__()
# внутри класса MyList, а написали бы pass.
# То перебирая элементы внутри нашего экземпляра класса MyList([1,2,3,4]), то этот перебор вел бы себя
# в точности как перебор экземпляра класса лист.

# Поэтому у нас возникает необходимость определять свой собственный метод __итер__(),
# который бы возвращал нам итератор.

# Давайте напишем класс итератора, который принимает список элементов, который мы хотим перебирать
# парами в конструктор.

for pair in MyList([1, 2, 3, 4]):
    print(pair)

# Однако у итератора, который мы написали есть очевидный недостаток: если передать в конструктор
# MyList() нечетное число элементов, наш итератор сломается,
# когда попытается вывести последнюю пару.

# Однако несмотря на то, что данный код исполняется неправильно при последовательностях
# нечетной длины, мы решили именно ту задачу, которую себе ставили.
# Мы хотели выводить элементы списка парами, т.е. мы смогли сами определить свое поведение для
# своего класса, если мы перебираем в нем элементы с помощью цикла for.
