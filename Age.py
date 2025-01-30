wiek = input("Podaj wiek użytkownika: ")

#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")

#brak walidacji dla niepełnoletnich, wiek powyżej 120 lat wykluczony
def check_age (wiek):
    try:
        wiek = int(wiek)
        if wiek < 18:
            return "Przykro nam, jesteś jeszcze na to za młody. Odwiedź nas później"
        elif 18 <= wiek <= 120:
            if 18 <= wiek <= 25:
                return "Czy na pewno masz 18 lat? Czy możesz pokazac dowod osobisty?"
            elif wiek >= 60:
                return "Energetyki nie są rekomendowane dla osób 60+."
            elif wiek >= 50:
                return "Osoby 50+ powinny dbać o swoje zdrowie i zwracać szczególną uwagę na produkty, które spożywają."
            else:
                return ("Witamy w aplikacji. Możesz kupować u nas napoje energetyczne. "
                        "Pamiętaj, że energetyki nie sa zdrowe! Może wybierzesz sok owocowy?")
        else:
            return "Podany liczba przekracza 120 lat. Spróbuj ponownie."
    except ValueError:
        return "Podana wartość nie jest prawidłową liczbą."



# Wywołanie funkcji

print(check_age(wiek))
