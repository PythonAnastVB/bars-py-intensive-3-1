import time
def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(number):
        start=time.time()
        function(number)
        end=time.time()
        final_result=end-start
        return final_result
    return wrapper
    
@time_execution
def factorial(number):
    """
    Возвращает факториал переданного числа
    Args:
        number: число, для которого надо посчитать факториал
    Returns:
        product - int - факториал от number
    """
    product = 1
    for element in range(1, number+1):
        product *= element

    return product
print(factorial(10000))
