"""

Реализовать класс MathClock, который поддерживает следующие операции:

-сложение с числом увеличивает количество минут на входящее значение
-вычитание числа уменьшает количество минут на входящее значение
-умножение на число увеличивает количество часов на входящее значение
-деление на число уменьшает количество часов на входящее значение

Также реализовать метод get_time, который возвращает время в формате 'hh:mm'.

"""


from datetime import time, datetime


class MathClock:
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def __add__(self, value):
        res=self.value1+value
        self.value1=res
        return(self.value1)
    def __sub__(self, value):
        res=self.value1-value
        self.value1=res
        return(self.value1)
        
    def __mul__(self, value):
        res=self.value2+value
        self.value2=res
        return(self.value2)
        
    def __truediv__(self, value):
        res=self.value2-value
        self.value2=res
        return(self.value2)
       

    def get_time(self):
        txth=int(self.value2)
        txtm=int(self.value1)
        t=time(txth,txtm)
        print(t.strftime('%H:%M'))
        
a=MathClock()
a*5
a.get_time()


