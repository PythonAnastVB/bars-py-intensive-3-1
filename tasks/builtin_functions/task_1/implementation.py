"""
Реализовать класс Value, которое принимает числовое значение.
Класс Value должен уметь быть частью простейших арифметических
действий (сложение/вычитание, умножение/деление).
В случае невозможности выполнения действий - выбрасывать исключение
MyException(tasks/common).

"""


class Value:
    def __init__(self, number):
        self.number=number
    def __str__(self):
        txt=str(self.number)
        return txt
    def __add__(self, x):
        y=self.number+x
        tmp=Value(y)
        return tmp
    def __sub__(self, x):
        number=self.number - x
        tmp3=Value(number)
        return tmp3
    def __truediv__(self, x):
        number=self.number/ x
        tmp2=Value(number)
        return tmp2
    def __mul__(self, x):
        number=self.number*x
        tmp4=Value(number)
        return tmp4
    


