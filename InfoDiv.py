#creator: Kingslayer
import os
import sys

#поиск директорий и прочих процессов
print("INFODIV (c)Kingslayer")
while True:
    print("[sysinfo] - информация о системе\n[home] - перейти в директорию /home\n[image] - просмотр директории с изображениями\n[downloads] - перейти в директорию Загрузки\n[documents] - перейти в директорию Документы\n[usernow] - информация о пользователе который сейчас в терминале\n[dirnow] - показывает в какой в директории сейчас\n[editdir] -  навигация по директориям\n[hashinfo] - - информация о параметрах хэширования\n[clearcache] - очистка внутреннего кэша\n")
    x = input(": ")
    if x == "sysinfo":
        print(">>>>>>"," OC", sys.platform)
        print(">>>>>>", os.name)
        print(">>>>>>", os.getpid())
        print(">>>>>>", os.uname())
    if x == "home":
        print(">>>>>>", os.listdir(path="/home"))
    if x == "image":
        username = input("user: ")
        print(">>>>>>", os.listdir(path="/home/" + username +"/Изображения/"))
    if x == "downloads":
        username = input("user: ")
        print(">>>>>>", os.listdir(path="/home/" + username +"/Загрузки"))
    if x == "documents":
        username = input("user: ")
        print(">>>>>>", os.listdir(path="/home/" + username + "/Документы"))
    if x == "usernow":
        print(">>>>>>", os.getlogin())
    if x == "dirnow":
        print(">>>>>>", os.getcwd())
    if x == "editdir":
        path = input("dir: ")
        os.chdir(path)
    if x == "hashinfo":
        print(sys.hash_info)
    if x == "clearcache":
        print(sys._clear_type_cache())
