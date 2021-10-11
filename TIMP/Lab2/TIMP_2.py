import time
import sys
import os
from os.path import expanduser

WHAT_LIMITED = 1  # 1 - ограничено по времени, 2 - по пользователям
TIME_LIMIT = 75  # ограничение времени
USER_LIMIT = 3  # ограничение пользователей

reached = 0
if WHAT_LIMITED == 1:  #  если лимит по времени
    file_limit = open(os.path.join(expanduser("~"), '.none/time_limit'))  #  отправляем .none в home
    time_limit = float(file_limit.read())  #  преобразуем число из строки в float
    now_time = time.time()  #  смотрим текущее время
    if (now_time - time_limit) > TIME_LIMIT:  #  если мы превышаем лимит
        print("The trial version is over. Buy the full version.")
        sys.exit()  #  закрываем
    print("Time limit: " + str(TIME_LIMIT - now_time + time_limit))  #  если нет то пишем сколько осталось
    file_limit.close()
else:  #  если лимит по пользователям
    file_limit = open(os.path.join(expanduser("~"), '.none/use_limit'))
    use_limit = float(file_limit.read())
    if use_limit >= USER_LIMIT:  #  смотри привысили ли мы лимит
        print("The trial version is over. Buy the full version")
        sys.exit()
    print("Trial use left to go: ", str(USER_LIMIT - use_limit - 1))   #   если не привысили сколько осталось
    file_limit.close()
    file_limit = open(os.path.join(expanduser("~"), '.none/use_limit'), 'w')
    file_limit.write(str(use_limit + 1))  #  увеличиваем счетчик пользователей 
    file_limit.close()

f = open('list', 'r+')   #  открываем файл для записи пользователей
list = [line for line in f]
name = input("Enter your name: ")
try:
    list.index(name + '\n')  #  узнаем индекс имени
except ValueError:
    f.write(name + '\n')  #  записываем имя
else:
    print("This name is already taken")
