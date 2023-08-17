import requests
import pytest

token = 'd1d7276f6b778534e39320546a54dbfe'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 2034})
    assert response.status_code == 200
    
def test_have_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 2034})
    assert response.json()['trainer_name'] == 'Killue'