"""
Необходимо проверить, возможно ли создание словаря, ключом которого будет
являться кортеж, содержащий список, и объяснить полученный результат.

"""

"""
Может ли кортеж, содержащий список, быть ключом словаря? Почему?

Ответ:

НЕ может. Так как список - это изменяемый и нехэшируемый объект.
Список, который находится в кортеже, легко изменить (так как кортеж содержит
не сам список, а ссылку на него),а ключи словаря должны оставаться неизменными.
"""

