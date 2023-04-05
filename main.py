# Импортировать модуль shutil
import shutil
import os
# Импортировать модуль пути из ОС
from os import path

my_data = ("Data")

if not os.path.isdir("Data"):#Проверка наличия каталога
    os.mkdir("Data")#Создание каталога

SpeedLimit_20 = ["00000_0000"]
SpeedLimit_30 = ["00001_"]
SpeedLimit_50 = ["00002_"]
SpeedLimit_60 = ["00003_"]
SpeedLimit_70 = ["00004_"]
SpeedLimit_80 = ["00005_"]
SpeedLimit_Off_80 = ["00006_"]
SpeedLimit_100 = ["00007_"]
SpeedLimit_120 = ["00008_"]
No_overtaking = ["00009_"]
Trucks_are_not_allowed_to_overtake = ["00010_"]
Intersection_with_secondary_road = ["00011_"]
The_main_road = ["00012_"]
Give_way = ["00013_"]
Stop = ["00014_"]
Movement_Prohibition = ["00015_"]
Truck_traffic_is_prohibited = ["00016_"]
No_entry = ["00017_"]
Other_hazards = ["00018_"]
Dangerous_bend_in_left = ["00019_"]
Dangerous_bend_in_rigth = ["00020_"]
Dangerous_turns = ["00021_"]
Rough_road = ["00022_"]
Slippery_road = ["00023_"]
Road_narrows_in_left = ["00024_"]
Road_repair = ["00025_"]
Traffic_light = ["00026_"]
No_Pedestrians = ["00027_"]
Kids = ["00028_"]
Bicycles_are_prohibited = ["00029_"]
Icing_Hazard = ["00030_"]
Wild_animals = ["00031_"]
End_of_the_zone_of_all_restrictions = ["00032_"]
Mandatory_direction_of_travel_in_rigth = ["00033_"]
Mandatory_direction_of_travel_in_left= ["00034_"]
Mandatory_direction_of_travel_in_ahead = ["00035_"]
Mandatory_direction_of_travel_in_ahead_and_rigth = ["00036_"]
Mandatory_direction_of_travel_in_ahead_and_left = ["00037_"]
Obstacle_Avoidance_Direction_in_rigth =  ["00038_"]
Obstacle_Avoidance_Direction_in_left =  ["00039_"]
Roundabout_Circulation = ["00040_"]
End_of_no_overtaking_zone = ["00041_"]
End_of_no_overtaking_zone_for_trucks = ["00042_"]

def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')







# Проверьте, существует ли файл
if path.exists(my_data):
    destination_path = "C:\Users\TEMP.KVANTORIUM69.001\PycharmProjects\pythonProject1\List of characters\1. SpeedLimit 20" # Задайте путь к каталогу, в который будет перемещен файл
    new_location = shutil.move(my_data, destination_path)# Переместите файл в новое место
else:
    print("Файл не существует.") # Распечатать сообщение, если файл не существует

print("% s перемещен в указанное место,% s" % (my_data , new_location))# Распечатать новое расположение файла




