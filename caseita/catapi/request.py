import requests

headers = {'x-api-key':'5d30f84c-3874-4ad7-9449-4deea044fdf1'}
url = 'https://api.thecatapi.com/v1/breeds?limit=5'

getBreeds = requests.get(headers=headers, url=url)
for breed in getBreeds.json():
    print(breed['origin'])
    print(breed['temperament'])
    print(breed['description'])

