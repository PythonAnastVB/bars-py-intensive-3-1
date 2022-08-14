"""
Представим, что у нас есть огромный файл log.txt.
Нужно вернуть все строки файла, которые содержат слово „error“
"""
import io

word=u'error'
with io.open('log.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, and='')
