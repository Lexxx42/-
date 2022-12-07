# Что такое стек вызовов?
# Стек вызовов хранит прежде всего функции, которые мы вызвали.
# Если мы исполняли какой-то код и интерпретатор видит, что нужно исполнить какую-то функцию, он кладет эту
# функцию на стек. Если эта функция завершает свое исполнение, то он снимает ее со стека.

# Посмотрим на примере, как это происходит:

def g():  # определение
    print('i am in function g')


def f():  # определение
    print('i am in function f')
    g()
    print('i am in function f')


print('i am in outside of any function')  # вызов
f()  # вызов
print('i am in outside of any function')  # вызов

# 2 определения функции и 3 вызова функции.
# будем рисовать содержимое стека

#           #
#           #
#           #
#           #
#           #
#           #
#   print   #
#   module  #
#############

# функция module - эта функция занимается тем, что исполняет наши запросы
# каждый раз,когда мы построчно вводим какие-то инструкции - это именно она складывает числа, именно она
# определяет для нас функции. Создает объекты g() и f() при прочтении функций.

# Когда мы вызываем функцию - мы кладем функцию на стек.
# А когда функция завершает свое исполнение, она со стека снимается.
# Интерпретатор всегда выполняет самую верхнюю функцию на стеке.

# Когда интерпретатор закончит исполнение функции print() и выведет то, что мы его попросили он снимет функцию
# print() со стека и продолжит исполнение с того места, где мы до этого исполнялись.



#           #
#           #
#           #
#           #
#           #
#  print()  #
#    f()    #
#   module  #
#############

# Теперь он увидит функцию f() и для ее исполнения положит ее на стек.
# так как первая строка функции f() это функция print(), то он положит ее на стек
# выведет сообщение на экран и снимет принт со стека

#           #
#           #
#           #
#           #
#  print()  #
#    g()    #
#    f()    #
#   module  #
#############

# Далее он начнет исполнение функции g() и кладет ее на стек
# Первой строкой функции g() является функция принт()
# мы снова положим функцию принт() на стек

# Остановимся на данный конкретный момент, чтобы понять фундаментальный принцип стека вызовов.
# Все функции внутри стека вызовов на самом деле исполняются, но одна из них исполняется реально, та функция, которая
# лежит на верхушке стека. А остальные функции ждут соседа сверху, пока он исполнится. Таким образом, функция
# module() ждет, пока исполнится функция f(), функция f() ждет пока исполнится функция g(), и функция g() ждет
# пока исполнится принт()

# Реально исполняемая функция инструкция за инструкцией - это функция принт()

# Таким образом, стек вызовов отражает все функции, которые исполняются в данный момент и кто кого на самом деле ждет.


#           #
#           #
#           #
#           #
#           #   # Когда заканчивается выполнение функции принт() внутри функции g() она снимается со стека
#           #   мы заканчиваем исполнение инструкций g() т.к. принт() был последней инструкцией
#    f()    #   в функции f() еще есть функция принт() и мы кладем ее на стек
#   module  #
#############

#           #
#           #
#           #
#           #
#           #
#  print()  #   функция принт() выводит, что ее просят и снимается со стека
#    f()    #
#   module  #
#############

#           #
#           #
#           #
#           #
#           #
#           #
#           #   функция f() закончила свое исполнение и снимается со стека
#   module  #
#############

#           #
#           #
#           #
#           #
#           #
#           #
#  print()  #   исполняется последняя функция принт()
#   module  #
#############

#           #
#           #
#           #
#           #
#           #
#           #
#           #   выводится сообщение и снимается функция и возвращается управление интерпретатору
#   module  #
#############

# Чтобы лучше понять стек, мы можем реализовать стек на основе списка в языке python

# Стек

x = [1, 2, 3]

x.append(4)
x.append(5)

print(x)  # [1, 2, 3, 4, 5]

top = x.pop()
print(top)
print(x)  # [1, 2, 3, 4]

top = x.pop()
print(top)
print(x)  # [1, 2, 3]


