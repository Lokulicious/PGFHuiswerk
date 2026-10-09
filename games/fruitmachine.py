import random


def play_fruitmachine(saldo):

    while True:
        print(f"je huidige saldo is: {saldo}")
        start_input =  input("Druk op enter om te spelen, typ stop om te stoppen. ")

        if start_input == "stop":
            break

        amount = choose_amount(saldo)
        if not validate_amount(amount, saldo):
            continue
        saldo -= amount

        rolls = spin()
        show_icons(rolls)
        win_amount = get_results(rolls, amount)
        saldo += win_amount

    return saldo


def choose_amount(saldo):
    amount = float(input("Hoeveel zet je in? "))
    return amount


def validate_amount(amount, saldo):
    if amount > saldo:
        print("Je hebt niet genoeg saldo voor deze actie.")
        return False
    elif amount <= 0:
        print("Inzet moet boven de 0 zijn")
        return False
    else:
        return True

def spin():
    roll1 = random.randint(1, 3)
    roll2 = random.randint(1, 3)
    roll3 = random.randint(1, 3)
    rolls =  [roll1, roll2, roll3]

    return rolls



def get_results(rolls, amount):
    if rolls[0] == rolls[1] == rolls[2]:
        print(f"3 dezelfde! je hebt {amount * 3} gewonnen!")
        return amount * 3
    elif rolls[0] == rolls[1] or rolls[0] == rolls[2] or rolls[1] == rolls[2]:
        print(f"2 Dezelfde, je hebt {amount * 2} gewonnen!")
        return amount * 2
    else:
        return 0

def show_icons(rolls):
    roll_options = ["kers", "citroen", "ster"]
    icons = ["", "", ""]

    i = 0
    while i < len(rolls):
        icons[i] = roll_options[rolls[i] - 1]
        i += 1

    print(f"Rollen: {icons[0]} | {icons[1]} | {icons[2]}")