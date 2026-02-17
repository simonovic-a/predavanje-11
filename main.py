import json
import sys

user = None
max_budget = 100000

with open("data/users.json", 'r') as file:
    user = json.load(file)


if user['budget'] >= max_budget:
    print("Imate veći budžet od maksimalnog dozvoljenog")
    sys.exit()
elif user['budget'] < 0:
    print("Nedovoljan iznos budžeta")
    sys.exit()