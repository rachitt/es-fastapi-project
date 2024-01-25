import pickle
import json
import requests

url= 'http://127.0.0.1:8000/spaceship_ss'

input_model= {
    'HomePlanet': 1,
    'CryoSleep': 0,
    'Cabin': 149,
    'Destination': 2,
    'Age': 39.0 ,
    'VIP': False,
    'RoomService': 0.0,
    'FoodCourt': 0.0,
    'ShoppingMall': 0.0,
    'Spa': 0.0,
    'VRDeck': 0.0
}

input_data_json= json.dumps(input_model)

response= requests.post(url, data=input_data_json)
print(response.text)
