import requests

api_key = 'O4AFG06u.GvQ9NCqn0QXmnfyqSNx3lIYyVAAVAWQO' # VEXT Key

your_query = 'what is machine learning'

#setting header
headers = {
    'Content-Type: application/json',
    'Apikey: Api-Key <API_KEY>',
}

#data playload

data = {
    "playload": your_query
}

#the URL

url = 'https://payload.vextapp.com/hook/WRKTRCB94L/catch/$(ajayverma23)'

response = requests.post(url, json=data, headers=headers)

response = response.text

print(response.text)