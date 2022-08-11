"""
Необходимо реализовать функцию, которая будет делать копирование словаря так,
чтобы после изменения оригинала не изменялась копия.
"""

def copy_dict(origin_dict):
   
    dict_init={}
    for i in origin_dict:
        dict_init[i]=origin_dict[i]
    return(dict_init)    
        

    
"""
Второй вариант реализации с использованием copy():

def copy_dict(origin_dict):
    dict_init=origin_dict.copy()
    return dict_init
"""    



