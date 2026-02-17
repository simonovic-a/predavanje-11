import json
import sys

user = None
max_budget = 100000

with open("data/users.json", 'r') as file:
    user = json.load(file)

user_budget = int(user['budget']) + int(user['credit'])


if user_budget >= max_budget:
    print("Imate veći budžet od maksimalnog dozvoljenog")
    sys.exit()
elif user_budget < 0:
    print("Nedovoljan iznos budžeta")
    sys.exit()

print(f"Dobar dan, dobrodošli nazad! Iznos Vašeg budžeta je {user_budget}")

expense = 0

while expense <= 0 or expense > user_budget:
    expense = int(input("Molim Vas unesite želejeni iznos troška: "))