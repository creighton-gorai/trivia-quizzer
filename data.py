import requests

'''
You can change your data by changing the parameters
Read API from https://opentdb.com/api.php to change accordingly
'''

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
