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
    def __init__(self,number):
        self.value=number

    def __str__(self):
        txt=""
        txt+=str(self.value)
        return(txt)

    def __add__(self, other):
        res=self.value+other
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
    def __radd__(self, other):
        res=self.value+other
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
    def __iadd__(self, other):
        res=other+self.value
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
    def __sub__(self, other):
        res=self.value-other
        self.value=res
        return(self.value)
    
    def __rsub__(self, other):
        res=other-self.value
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
    def __isub__(self, other):
        res=self.value-other
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
        
    def __mul__(self, other):
        res=self.value*other
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
    def __rmul__(self, other):
        res=other*self.value
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)
    
        
    def __truediv__(self, other):
        res=self.value/other
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)

    def __rtruediv__(self, other):
        res=other/self.value
        tmp=Multiplier(res)
        self.value=tmp
        return(self.value)

    def get_value(self):
        itog=self.value
        print(itog)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.value=value*100

        
class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.value=value*1000
        
class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.value=value*1000000
