#import requests

#URL = "https://api"
#HEADER = {
 #   "Content-Type": "application/json",
  #  "trainer_token": "0e1f9cd8d97622f436805822daac440f"
   # "trainer_id": "2978"
#}

# body = {
  #  "trainer_token": "0e1f9cd8d97622f436805822daac440f",
   # "email": "",
   # "password": ""
#  }

#response = requests.post(url=f"{URL}/v2/trainers/reg", json=body, headers=HEADER, timeout=5)
#print("Статус код:", response.status_code, ". Сообщение:", response.json()["message"])

#body = {
    #"name": "generate",
    #"photo": "generate"
#}

#response = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')

#body = {
    #"pokemon_id": "18350",
    #"name": "Boris12",
    #"photo": "https://dolnikov.ru/pokemons/albums/008.png"
#}

#response = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')

#body = {
    #"pokemon_id": "18351"
#}

#response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')
#json_data = response.json()

#response = requests.get(url=f'{URL}/v2/trainers', headers=HEADER, json=body)
#print(f'Статус код: {response.status_code}.')


#json_data = response.json()

import random
import tqdm
import time

users = []

for i in tqdm.trange(1, 10001):
    user = {}
    user['id'] = i
    user['name'] = f'Name_{i}'
    user['age'] = random.randint(25, 60)
    user['email'] = f'sample_{i}@mail.ru'
    users.append(user)
    time.sleep(0.01)

print('Ok')
