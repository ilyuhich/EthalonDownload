from os import system
import requests
import shutil
from cam_list import cam_list
import time

url = 'http://192.168.34.8:8080/etalon/'
cam_list_downloaded = []

laps = 5
system('cls')
print(f'Getting system to fetch data from {url}\n')
time.sleep(laps)
print(f'Ready to fetch data from {url}')
laps = 1
for i in range(10):
    system('cls')
    print(f'Scanning the path {url}...')
    print("X" * i)
    time.sleep(laps)
laps = 3
print(f'Need to to fetch {len(cam_list) - len(cam_list_downloaded)} files from {url}')
time.sleep(laps)
system('cls')

#print('\n'.join(cam_list))
#system('cls')

laps = 0.01
for camera in cam_list:
    print(f"Elapsed to fetch {len(cam_list) - len(cam_list_downloaded)} files\n")
    file = camera + '.jpg'
    full_path = url + file
    print(f'Fetching {file}\n')
    filereq = requests.get(full_path, stream=True)
    with open(file, "wb") as receive:
        shutil.copyfileobj(filereq.raw, receive)
    del filereq
    time.sleep(laps)
    print(f'Moving the file {file} to downloaded ...\n')
    source =      'C:/Users/coordinator2/Desktop/Чудаков/Эксперименты Таблицы/Python/EthalonDownload/' + file
    destination = 'C:/Users/coordinator2/Desktop/Чудаков/Эксперименты Таблицы/Python/EthalonDownload/downloaded/' + file
    print(f"From {source}")
    print(f"to   {destination} \n")
    shutil.move(source, destination)
    cam_list_downloaded.append(camera)
    time.sleep(laps)
    print('Succesful!')
    time.sleep(laps)
    system('cls')

print(f'\nDownloaded {len(cam_list_downloaded)} from {len(cam_list)} files.')