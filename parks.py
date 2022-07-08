import requests

API_BASE_URL = 'https://developer.nps.gov/api/v1'
key = 'b5SPZ9bRhqC2LZDBW0bvZjLlojSTZXCDSTctBS54'

res = requests.get(
    'https://developer.nps.gov/api/v1/activities', params={'id':'7779241FA70B49BC86F0829AE332C7080', 'limit': 25, 'api_key': key}
    )

data = res.json()

for result in data['data']:
    print(result['name'], result['id'])
    
    