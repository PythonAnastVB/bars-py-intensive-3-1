"""
Необходимо создать класс своей неизменяемой структуры, похожей на tuple,
с методами count и index:

К элементу объекта должна быть возможность обратиться по индексу.
При передаче в метод index параметра, которого нет внутри вашего объекта,
нужно поднимать ValueError.
При написании ваших методов index и count нельзя использовать методы
index и count из Python tuple.
Внутри структуры можно использовать tuple в качестве хранилища объектов.
"""

class Mytuple():

    def __init__(self, x):
        self.x=x
    
    def counter(self, value):
        count=0
        for i in range(len(self.x)):
            if self.x[i]==value:
                count+=1
        print(count)        

    def indexer(self, value):
        if value in self.x:
            for i in range(len(self.x)):
                if value==self.x[i]:
                    print(i)
                    break
        else:
            raise ValueError
            
           
        

