"""
Реализовать класс для кофе, у которого будут методы-конструкторы,
возвращающие объект кофе с ингредиентами капучино,
латте и глясе соответственно.
"""

class Coffe:
    def __init__(self, ingredients):
        self.ingredients=ingredients
    def __repr__(self):
        return f'Coffe({self.ingredients!r})'
    @classmethod
    def kapuchino(cls):
        return cls(['capuchino'])
    @classmethod
    def latte(cls):
        return cls(['latte'])
    @classmethod
    def glyasse(cls):
        return cls(['glyasse'])



