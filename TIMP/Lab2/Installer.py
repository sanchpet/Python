import tarfile  #  модуль для создания .tar
import os  #  модуль оси
from os.path import expanduser  #  модуль для ~ для HOME
import time

arch = tarfile.open("archive.tar")  # открываем архив и сохраняем в перменную 
os.chdir(expanduser("~"))  #  изменяем текущий рабочий каталог на заданный путь ~
arch.extractall("./Lab2")  #  извлекаем все содержимое в текущий рабочий каталог
arch.close() 

if not os.path.isdir('.none'):  # если не существует .none то
    os.mkdir('.none')  #  создаем .none
    time_limit = open('.none/time_limit', 'w')  #  открываем для записи
    time_limit.write(str(time.time()))  #  записываем время текущее
    time_limit.close()
    use_limit = open('.none/use_limit', 'w')  #  открываем для записи
    use_limit.write('0')  #  записываем нолик
    print("You have installed the program")
else:
    print("You installed the program before")
