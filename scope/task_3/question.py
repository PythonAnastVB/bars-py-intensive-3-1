"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)
"""
после выполнения кода будет выведено:
3 - так как переменная number переопределена благодаря инструкции nonlocal
3

"""
