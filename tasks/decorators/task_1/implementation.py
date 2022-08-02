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
    
