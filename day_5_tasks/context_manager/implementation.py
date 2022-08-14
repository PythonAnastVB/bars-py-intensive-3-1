"""
Реализовать свой менеджер контекста, который при чтении текстового файла
сначала всегда по умолчанию печатает количество строк в этом файле.
Можно использовать класс или декоратор @contextmanager
"""
@contextmanager
def open_file(name):
    f=open(name, w)
    count=0
    for line in f:
        count+=1
    yield f
    yield count
    f.close
