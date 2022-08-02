"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
"""
После выполнения кода будет выведено:
Test message
None - так как функция data_transmitter() не принимает на вход параметры,
это не задано в ее описании.

"""
