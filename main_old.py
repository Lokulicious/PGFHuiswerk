import random
from operator import truediv

name = input("Vul naam in: ")
birthdate = input("Vul geboortedatum in (dd-mm-yyyy): ")
gender = input("Vul geslacht in (man/vrouw): ").upper()

birth_day, birth_month, birth_year = birthdate.split("-")
min_age = 18
current_year = 2026

budget = float(input("Startbudget in euro's: "))

ticket_price = 10
drink_price = 3
wardrobe_price = 2.5

standard_costs = float(ticket_price + drink_price + wardrobe_price)
saldo = budget - standard_costs

has_budget = saldo >= 0

options = ("Kies een optie: \n"
           "1. rood \n"
           "2. zwart \n"
           "3. even \n"
           "4. oneven \n"
           "0. stop \n")



if current_year - int(birth_year) < min_age:
    print("Je bent niet oud genoeg voor het casino")
    exit(1)

print("Casino de gouden driehoek")
print("-" * 20)

if gender == "MAN":
    print(f"Welkom meneer {name} \n")
elif gender == "VROUW":
    print(f"Wekom mevrouw {name} \n")


print(f"Startbudget: € {budget:.2f}")
print(f"vaste kosten: € {standard_costs:.2f}")
print(f"Saldo: € {saldo:.2f} \n")

if has_budget:
    print("Je hebt genoeg budget voor het casino")
else:
    print("Je hebt niet genoeg budget voor het casino")

while True:
    print(options)
    choice = int(input("keuze: "))

    if choice != 0:
        amount = float(input("Hoeveel zet je in?: "))

        if amount > saldo:
            print("Je hebt niet genoeg saldo voor deze actie.")
            continue
        elif amount <= 0:
            print("Inzet moet boven de 0 zijn")
            continue
        else:
            saldo -= amount


    spin = random.randint(0, 36)

    color = ""
    odd_even = ""

    has_won = False

    if spin % 2 == 0:
        odd_even = "even"
        if spin <= 18:
            color = "zwart"
        else:
            color = "rood"
    elif spin % 2 != 0:
        odd_even = "odd"
        if spin <= 18:
            color = "rood"
        else:
            color = "zwart"

    match choice:
        case 1:
            if color == "rood":
                has_won = True
            else:
                has_won = False
        case 2:
            if color == "zwart":
                has_won = True
            else:
                has_won = False
        case 3:
            if odd_even == "even":
                has_won = True
            else:
                has_won = False
        case 4:
            if odd_even == "odd":
                has_won = True
            else:
                has_won = False
        case 0:
            break

    print(f"De kleur was {color} en het nummer {spin}")

    if has_won:
        saldo += (amount * 2)
        print(f"je hebt €{amount * 2:.2f} gewonnen. je saldo is nu €{saldo:.2f}")
    else:
        print(f"Je hebt niet gewonnen, je saldo is nu €{saldo:.2f}")


print(f"Eindsaldo is €{saldo:.2f}")