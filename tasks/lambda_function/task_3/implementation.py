"""
Требуется возвести в квадрат все элементы списка my_list и получить
новый массив *res_list
"""

my_list = [1, 2, 3]
res_list = list(map(lambda x: x*x, my_list))
print(res_list)
