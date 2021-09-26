import os  # подкдючаем модули
import stat

while 1:  # бесконечный цикл
    with open('template.tbl', 'r') as f:  # открываем и возвращаем как файл на чтение
        temps = f.read().splitlines()  # читаем файл и возвращаем список со всеми строками
    for fname in temps:  # для списка
        check = os.path.exists(fname)  # переменная = проверка существования/открыт ли файл
        if not check:
            closing = open(fname, 'tw', encoding='utf-8')  # открываем файл в текстовом режиме для записи
            closing.close()  # закрываем
            os.chmod(fname, stat.S_IROTH)  # изменяем право доступа к fname на У других есть разрешение на чтение.
