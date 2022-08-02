def check_value():
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(number):
        if type(number) is int and number>0:
            base_result=function(number)
            return base_result
            
        else:
            print('В функцию передано невалидное значение')
    return wrapper

"""
Кэширование результата на примере моей функции
"""
from functools import lru_cache

@lru_cache(maxsize=30)
def foo(number):
    s=number+1
    return s
print(foo(1000))

    
    
    
    
    
    
