import os
from os.path import expanduser

os.chdir(expanduser("~"))
for dir_path, dir_names, filenames in os.walk('Lab2'):  #  смотрим что лежит 
    for file in filenames:
        os.remove(os.path.join(dir_path, file))  #  стираем путь к файлам
    for name in dir_names:
        os.removedirs(os.path.join(dir_path, name))  #  рекурсивно удаляем каталоги
        os.rmdir('/Lab2')  #  удляем путь к каталогу
print("You uninstalled a program")
