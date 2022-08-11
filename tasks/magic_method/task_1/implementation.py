"""
Реализовать классы: Multiplier, Hundred, Thousand, Million.
Прямое взаимодействие будет происходить только с дочерними классами Multiplier.
Дочерние классы должны поддерживать арифметические операции между собой.
Для получения текущего значения реализовать метод get_value -> int.
Например:

a = Hundred(10)

b = Thousand(1)

c = a + b # c.get_value() -> 2000
"""

class Multiplier:
    def __init__(self):
        pass


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self):
        pass


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self):
        pass


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self):
        pass
