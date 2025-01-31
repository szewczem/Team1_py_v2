# BlackScorpion Energy Drink GRATIS after guessing the number (shop event)
from random import randrange

def game_gratis_drink():
    print('Jako pełnoletni klient masz możliwość wygrania nagrody. Wygraj grę i odbierz gratis do zakupów!')

    def start_game():
        answer = input(
            'Zgadnij poprawną liczbę w maksymalnie 5 próbach, aby wygrać nagrodę. Czy chcesz zagrać w grę? [y/n]? ')
        if answer == 'y':
            numbers_game()
        else:
            print('Wyzwanie odrzucone.')

    def numbers_game():
        number = randrange(0, 101)
        # print(number)
        count = 1
        guess = int(input(
            f'\nZgadnij wylosowaną liczbę z przedziału od 0 do 100. Masz tylko 5 prób, powodzenia!\nPróba {count}: '))

        while count <= 5:
            if guess == number:
                print('Zgadłeś! Wygrywasz BlackScorpion Energy Drink!')
                break
            elif count == 5 and guess != number:
                print(f"Nie masz więcej prób do wykorzystania. Wylosowaną liczbą była liczba: {number}.")
                break
            elif guess > number:
                count += 1
                guess = int(input(f'Wylosowana liczba jest niższa, spróbuj ponownie.\nPróba {count}: '))
            elif guess < number:
                count += 1
                guess = int(input(f'Wylosowana liczba jest wyższa, spróbuj ponownie.\nPróba {count}: '))

    start_game()  

def promocja_zero():
    promo_question = input("Czy preferujesz energetyki bez cukru? [y/n]")
    if promo_question == "y":
        print("Tylko dziś promocja 2+1 na napoje eneregetyczne o dowolnym smaku!")
    else:
        print("Zastanów się nad wypróbowaniem nowych smaków zero, przygotowaliśmy atrakcyjne promocje ;)")
 
def ostrzezenie(wiek):
    if wiek >= 60:
        print("Energetyki nie są rekomendowane dla osób 60+.")
    elif wiek >= 50:
        print("Osoby 50+ powinny dbać o swoje zdrowie i zwracać szczególną uwagę na produkty, które spożywają.")

def sok_owocowy(wiek):
    if wiek>=18 and wiek<120:
        print("Energetyki nie sa zdrowe, moze wolisz sok owocowy?")

def wiek_1825(wiek):
    if wiek>=18 and wiek<25:
        print("Czy na pewno masz 18 lat? Czy mozesz pokazac dowod osobisty?")



########## APP ##########
if __name__ == "__main__":
    wiek = input("Podaj wiek uzytkownika: ")
    # sprawdzenie czy wiek jest liczba calkowitą
    if wiek.isdigit() == False:
        exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
    wiek=int(wiek)

    if wiek>=18 and wiek<120:
        print("Witamy w apce. Mozesz kupować u nas energetyki")
        sok_owocowy(wiek)
        wiek_1825(wiek)
        ostrzezenie(wiek)
        game_gratis_drink()
        promocja_zero()

