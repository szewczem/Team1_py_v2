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
    
 
def wiek_60 (wiek):
    if wiek >= 60:
        print("Energetyki nie są rekomendowane dla osób 60+.")
    else:
        pass

def wiek_50(wiek):
    if wiek >= 50:
        print("Osoby 50+ powinny dbać o swoje zdrowie i zwracać szczególną uwagę na produkty, które spożywają.")



########## APP ##########

wiek = input("Podaj wiek uzytkownika: ")
# sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)

if wiek>=18 and wiek<120:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
    wiek_50(wiek)
    wiek_60 (wiek)
    game_gratis_drink()    
    
# naprawa błędów i braków walidacji
if wiek <18:
    print ("Przepraszamy, nie sprzedajemy energetyków niepełnoletnim")
elif wiek>120:
    print("Podany wiek przekracza 120 lat, na pewno masz tyle?")
else:
    pass

if wiek>=18:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
    wiek_50(wiek)

