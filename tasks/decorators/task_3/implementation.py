
count =0
def counter():
    """
    Обертка для подсчёта количества вызовов обернутой функции.
    Returns:
        int - количество вызовов функции.
    """
    def wrapper():
        global count
        base_result=function()
        count+=1
        return count
    
    return wrapper
    print(count)

    
