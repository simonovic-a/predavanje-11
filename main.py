import json

user = None

with open("data/users.json", 'r') as file:
    user = json.load(file)

