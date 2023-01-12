# В языке python действительно важно закрывать файлы.

# Однако от момента, где мы файл открыли и до момента, где мы должны были его закрыть
# могла бы произойти ошибка.
# Если ошибка действительно произошла, то интерпретатор мог просто не дойти до метода
# close().
# Чтобы обезопасить себя от такой ситуации, чтобы перестать писать метод
# close() самим, мы можем использовать open() вместе с конструкцией with.

with open("test.txt") as f, open("test_copy", "w") as w:
    for line in f:
        w.write(line)
        print(line)

# Такая конструкция гарантирует нам, что когда мы выйдем и блока with, вне зависимости от того произошла
# ли там ошибка или исполнение кода прошло нормально, то интерпретатор закроет наш файл.
# Поэтому такая конструкция является рекомендованной для того, чтобы работать с файлами.

# Так же в конструкции with мы можем открыть сразу несколько файлов, для этого
# их можно перечислить через запятую.
