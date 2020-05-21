from os import system
from random import randint
import requests
import shutil
from cam_list import cam_list
import time
import cowsay

start_time = time.time()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


start_time = time.time()

url = 'http://192.168.34.8:8080/etalon/'
cam_list_downloaded = []
cam_list_not_loaded = []
laps = 1/100


system('cls')
print(
    f'\n\n\n\n{bcolors.WARNING}Need to to fetch{bcolors.FAIL} {len(cam_list) - len(cam_list_downloaded)} {bcolors.WARNING}files from {url}{bcolors.ENDC}')
cowsay.daemon(f"{bcolors.WARNING}All is ready to start downloading files.\nPlease press Enter to START.{bcolors.ENDC}")
input()
system('cls')

laps = laps
check = 0

for camera in cam_list:
    file = camera + '.jpg'
    full_path = url + file
    destination = 'C:/downloaded/' + file
    print(f"\n\n{bcolors.FAIL}DON'T CLOSE THE APPLICATION OR SHUTDOWN THE COMPUTER{bcolors.ENDC}\n")
    print(f"Elapsed to fetch {len(cam_list) - len(cam_list_downloaded)} files. \nFetching {file}\n ")
    print('.' * (len(cam_list) - len(cam_list_downloaded)))

    filereq = requests.get(full_path, stream=True)
    if filereq.status_code == 200:  #check status page
        check += 1
        with open(destination, "wb") as receive:
            shutil.copyfileobj(filereq.raw, receive)
    else:
        cam_list_not_loaded.append(camera)
    del filereq
    cam_list_downloaded.append(camera)
    system('cls')

print(f"Available {check} from {str(len(cam_list))}")
print(f'I wasted {(time.time() - start_time)} seconds to check')
print("Files with report also saved in output directory.")


file = ('C:/downloaded/!Отсутствуют.txt', 'w+')
with open('C:/downloaded/!Отсутствуют.txt', 'w') as f:
    for item in cam_list_not_loaded:
        f.write("%s\n" % item)

file = ('C:/downloaded/!Скачано.txt', 'w+')
with open('C:/downloaded/!Скачано.txt', 'w') as f:
    for item in cam_list_downloaded:
        f.write("%s\n" % item)


