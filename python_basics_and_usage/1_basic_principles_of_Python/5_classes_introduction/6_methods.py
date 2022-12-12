# Также язык Python поддерживает методы

# Методы - это по сути такие атрибуты внутри созданного экземпляра, которые
# на самом деле являются функциями и чаще всего делают что-то полезное

# Рассмотрим на примере списков и, допустим, метод sort()
# если бы мы создали список
x = [2, 3, 1]
# и затем бы запустили у нашего экземпляра (инстанса)
x.sort()  #
print(x)  # [1, 2, 3]
# х изменился и теперь элементы в нем расположены по возрастанию

# правильнее всего использовать методы ровно тогда, когда мы хотим объект изменить
# или что-нибудь о нем узнать
# далеко за примерами ходить не надо
# посмотрим на те же самые списки

# у списков также есть метод append
x.append(4)
print(x)  # [1, 2, 3, 4]

# метода append() дописывает элемент, который мы передаем аргументом в конец списка
# А метод pop является в свою очередь методом, который не просто объект меняет,
# но еще и позволяет нам, что-то о нем узнать
top = x.pop()
# потому что метод pop() убирает последний элемент списка и его возвращает
print(top)  # 4

# таким образом, раз метод является атрибутом экземпляра и при этом поведение самого метода
# не сильно меняется от экземпляра к экземпляру внутри всех экземпляров одного класса
# логичнее всего описать методы было бы именно внутри классов

# именно таким механизмом пользуется язык Python,
# давайте посмотрим пример
# вернемся к нашему классу
print('****')


class Counter:
    def __init__(self):  # конструктор
        self.count = 0

    def inc(self):  # 1й метод: инкремент
        self.count += 1

    def reset(self):  # 2й метод: обнуление счетчика
        self.count = 0


x = Counter()  # вызов конструктора
x.inc()  # вызов метода инкремента

# Как мы нашли имя inc() в неймспейсе нашего экземпляра?
# Ведь в неймспейсе нашего экземпляра было только имя count, который мы создали внутри конструктора,
# правильным ответом будет тот механизм, которым интерпретатор пытается найти атрибуты внутри
# экземпляра. Он сначала ищет в неймспейсе самого экземпляра, а затем пытается найти этот
# атрибут в неймспейсе класса.

# Давайте покажем, что было в оперативной памяти на момент исполнения x.inc():

# Когда мы определяли класс у нас создался объект для нашего класса Counter.
# И в его неймспейсе были имена: __init__, имя inc, имя reset.
# Затем мы создали сам объект х у которого класс Counter.
# Когда мы вызывали конструктор мы заранее установили атрибут нашего икса count = 0
# т.е. где-то в неймспейсе нашего икса у нас есть имя count, которое изначально = 0

# Когда мы вызываем x.inc(), чтобы понять, что же нужно ему исполнить,
# Интерпретатор сначала пытается найти имя инк внутри неймспейса экземпляра х

# Однако там оказалось только имя count и поэтому он пошел дальше и начал
# смотреть в неймспейсе класса.

# когда интерпретатор в процессе имени доходит до самого класса
# и если это имя внутри класса является еще и функцией - он считает, что это
# имя для нашего экземпляра является методом.

# И по аналогии с конструктором, когда мы вызываем метод себя в качестве
# первого аргумента функции.

# Таким образом, когда мы вызываем функцию x.inc() мы на самом деле вызываем
# функцию Counter.inc() и подставляем икс в качестве аргумента self.

# Таким образом, мы увеличиваем атрибут count нашего экземпляра x на 1
# Т.е. когда мы запустим x.inc(), и выведем print(x.count) мы увидим, что
# на самом деле это теперь 1.
print(x.count)
# Важно понимать, что вызов метода абсолютно эквивалентен вызову функции, если бы мы передали
# внутрь тот же самый объект.
# т.е. наш вызов метода x.count абсолютно эквивалентен вызову функции Counter.inc(x)
Counter.inc(x)
print(x.count)
# Давайте исполним наш код до конца
x.reset()  # сброс счетчика
print(x.count)

# Единственная тонкость и деталь, которая осталась, что же такое x.inc()
# любому атрибуту и имени внутри неймспейса экземпляра должен соответствовать какой-то объект
# так какой это объект?

# Это так называемый связанный метод или Bound method
# связанные методы в языке Python - это такие специальные объекты
# мы сначала находим функцию, которая соответствует x.inc()
# а затем связываем ее с объектом.

# Таким образом, мы сначала найдем функцию Counter.inc
# и свяжем ее с объектом х
# Таким образом, когда мы вызовем x.inc() этот вызов будет абсолютно
# эквивалентен вызову функции Counter.inc(x)

print(type(x.inc()))
