import random


def play_roulette(saldo):
    while True:
        gamble_choice = show_options()
        if 0 > gamble_choice > 4:
            print("invalid choice")
            continue
        elif gamble_choice == 0:
            break

        amount = choose_amount(saldo)
        if not validate_amount(amount, saldo):
            continue
        saldo -= amount

        if get_result(gamble_choice, spin()):
            win_amount = amount * 2
            saldo += win_amount
            print(f"You won {win_amount}, your new saldo is now {saldo}!")
        else:
            print(f"You lost, new saldo is now {saldo}.")

    return saldo




def show_options():
    print("Kies een optie: \n"
               "1. rood \n"
               "2. zwart \n"
               "3. even \n"
               "4. oneven \n"
               "0. stop \n")
    return int(input("Keuze: "))



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
    return random.randint(0, 36)

def get_color(spin_result):
    color = ""
    if spin_result % 2 == 0:
        if spin_result <= 18:
            color = "zwart"
        else:
            color = "rood"
    elif spin_result % 2 != 0:
        if spin_result <= 18:
            color = "rood"
        else:
            color = "zwart"
    return color

def get_result(gamble_choice, spin_result):
    has_won = False
    match gamble_choice:
        case 1:
            if get_color(spin_result) == "rood":
                has_won = True
        case 2:
            if get_color(spin_result) == "zwart":
                has_won = True
        case 3:
            if spin_result % 2 == 0:
                has_won = True
        case 4:
            if spin_result % 2 != 0:
                has_won = True
    return has_won
