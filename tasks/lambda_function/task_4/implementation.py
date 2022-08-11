"""

Требуется получить список res_list_product, который будет содержать
продукты со стоимостью больше 10.
"""

class Product:
    def __init__(self, value):
        self.value = value
   
    

a = Product(12)
b = Product(7)
c = Product(10)
my_list_product = [a, b, c]



res_list_product = str(filter(lambda x: (x>10), my_list_product))
print(res_list_product)


