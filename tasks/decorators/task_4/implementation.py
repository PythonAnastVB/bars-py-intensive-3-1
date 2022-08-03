import time
T=0
def decorator_maker_function(times, delay):
    def decorator_maker(function):
    
        def wrapper():
            global T
            base_result=function()
            T+=1
            if base_result==False:
                while T<times:
                    function()
                    T+=1
                    time.sleep(delay)
            else:
                return base_result
            if T==3:
                print("Количество попыток исчерпано")
                
        return wrapper
    return decorator_maker


    
