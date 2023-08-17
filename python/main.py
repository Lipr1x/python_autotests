import requests

token = 'd1d7276f6b778534e39320546a54dbfe'
host = 'https://api.pokemonbattle.me:9104'

# response_post = requests.post(f'{host}/pokemons', json = {
#     "name": "Kirik",
#     "photo": "https://dolnikov.ru/pokemons/albums/001.png"
# }, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

# print(response_post.json())

# response_put = requests.put(f'{host}/pokemons', json = {
#     "pokemon_id": "6216",
#     "name": "NewName",
#     "photo": "https://dolnikov.ru/pokemons/albums/008.png"
# }, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

# print(response_put.json())

response_post_in = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6214"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_post_in.json())