# Импортировать модуль shutil

import shutil

# Импортировать модуль пути из ОС

from os import path


# Задайте имя файла с путем

source_path = "fruit.txt"


# Проверьте, существует ли файл

if path.exists(source_path):

# Задайте путь к каталогу, в который будет перемещен файл

destination_path = "Files"

# Переместите файл в новое место

new_location = shutil.move(source_path, destination_path)

# Распечатать новое расположение файла

print("% s перемещен в указанное место,% s" % (source_path , new_location))

else :

# Распечатать сообщение, если файл не существует

print ("Файл не существует.")