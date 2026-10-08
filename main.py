from datetime import datetime
from games.roulette import play_roulette

DIVIDER_LENGTH = 20
TICKET_PRICE = 10
DRINK_PRICE = 3
WARDROBE_PRICE = 2.5
MIN_AGE = 18
STANDARD_COST = TICKET_PRICE + DRINK_PRICE + WARDROBE_PRICE



def main():
    name = input("Vul naam in: ")
    birthdate = check_age(input("Vul geboortedatum in (dd-mm-yyyy): "))
    gender = input("Vul geslacht in (man/vrouw): ").upper()
    budget = float(input("Startbudget in euro's: "))

    saldo = budget - STANDARD_COST

    show_welcome_message(budget, saldo, determine_salutation(name, gender))

    while True:
        choice = show_main_menu()

        match choice:
            case n if 0 > choice > 3:
                print("Ongeldige keuze.")
                continue
            case 1:
                game_choice = show_game_menu()
                if game_choice == 1:
                    print("Fruitgame")
                #     TODO: IMPLEMENT FRUIT GAME
                elif game_choice == 2:
                    saldo = play_roulette(saldo)
                elif game_choice == 0:
                    continue
                else:
                    print("Ongeldige keuze.")
                    continue
            case 2:
                show_balance(saldo)
                continue
            case 3:
                show_account(name, gender, birthdate, calculate_age(birthdate))
                continue
            case 0:
                break

    print(f"Eindsaldo is {saldo}")



def check_age(birthdate):
    age = calculate_age(birthdate)
    if age >= 18:
        return birthdate
    else:
        print("Je bent niet oud genoeg voor het casino.")
        exit(1)

def calculate_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")

    age = datetime.now().year - int(birth_year)
    return age

def determine_salutation(name, gender):
    if gender == "MAN":
        return f"Welkom meneer {name} \n"
    elif gender == "VROUW":
        return f"Welkom mevrouw {name} \n"
    else:
        return f"Welkom {name} \n"

def show_welcome_message(startbudget, saldo, salutation):

    print("Casino de gouden driehoek")
    print("-" * DIVIDER_LENGTH)
    print(salutation)

    print(f"Startbudget: € {startbudget:.2f}")
    print(f"vaste kosten: € {STANDARD_COST:.2f}")
    print(f"Saldo: € {saldo:.2f} \n")

    if saldo <= 0:
        print("Je hebt niet genoeg geld voor het casino")

def show_balance(balance):
    print(f"Je huidige saldo is {balance}")

def show_account(name, gender, birthdate, age):
    print(f"Naam:          {name}")
    print(f"Gender:        {gender}")
    print(f"Geboortedatum: {birthdate}")
    print(f"Leeftijd:      {age}")

def show_main_menu():
    print("1. Spellen")
    print("2. Saldo")
    print("3. Account")
    print("0. Stop")

    choice = int(input("keuze: "))
    return choice

def show_game_menu():
    print("1. Fruitmachine")
    print("2. Roulette")
    print("0. Terug")

    choice = int(input("Keuze: "))
    return choice


main()