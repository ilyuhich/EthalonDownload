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


new_look = (
    f'{bcolors.WARNING}Getting system ready to fetch data from{bcolors.ENDC}',
    f'{bcolors.WARNING}Checking paths, files and route to host {bcolors.ENDC}',
    f'{bcolors.WARNING}Wait please...\n\nConnecting to host {bcolors.ENDC}',

)


def wait_for(text, url, laps):  # "scanning" wait_for
    for j in range(randint(15, 50)):
        for i in range(10):
            system('cls')
            print(f'{text} {url} {i * "."}')
            print("X" * j)
            time.sleep(laps / 20)
    time.sleep(laps)


start_time = time.time()

url = 'http://192.168.34.8:8080/etalon/'
cam_list_downloaded = []
laps = 1

for text in new_look:
    wait_for(text, url, laps / 10)

system('cls')
print(
    f'{bcolors.WARNING}Need to to fetch{bcolors.FAIL} {len(cam_list) - len(cam_list_downloaded)} {bcolors.WARNING}files from {url}{bcolors.ENDC}')
cowsay.daemon(f"{bcolors.WARNING}All is ready to start downloading files.\nPlease press Enter to START.{bcolors.ENDC}")
input()
system('cls')

laps = laps
for camera in cam_list:
    print(f"\n\n{bcolors.FAIL}DON'T CLOSE APPLICATION OR SHUTDOWN THE COMPUTER{bcolors.ENDC}")
    print(f"Elapsed to fetch {len(cam_list) - len(cam_list_downloaded)} files")
    print('.' * (len(cam_list) - len(cam_list_downloaded)))
    file = camera + '.jpg'
    full_path = url + file
    source = 'C:/Users/coordinator2/Desktop/Чудаков/Эксперименты Таблицы/Python/EthalonDownload/' + file
    destination = 'C:/Users/coordinator2/Desktop/Чудаков/Эксперименты Таблицы/Python/EthalonDownload/downloaded/' + file
    print(f'\nFetching {file}\n')
    filereq = requests.get(full_path, stream=True)
    with open(destination, "wb") as receive:
        shutil.copyfileobj(filereq.raw, receive)
    del filereq
    cam_list_downloaded.append(camera)

    print('Succesful! \nWill process next file...')
    time.sleep(laps/5)
    system('cls')

print(f'\nDownloaded {len(cam_list_downloaded)} from {len(cam_list)} files.')
print(f'I have wasted {(time.time() - start_time)} seconds to do this work')

