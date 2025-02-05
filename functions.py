def ostrzezenie(wiek):
    if wiek >= 60:
        print("\nEnergetyki nie są rekomendowane dla osób 60+.")
    elif wiek >= 50:
        print("\nOsoby 50+ powinny dbać o swoje zdrowie i zwracać szczególną uwagę na produkty, które spożywają.")

def wybierz_plec():
    print("Wybierz rodzaj płci:")
    print("1. Mężczyzna")
    print("2. Kobieta")
    print("3. Inna")

    wybor = input("Wprowadź numer (1, 2, 3): ")

    if wybor == "1":
        plec = "Mężczyzna"
    elif wybor == "2":
        plec = "Kobieta"
    elif wybor == "3":
        plec = "Inna"
    else:
        plec = "Nieznana"

    print(f"Wybrałeś płeć: {plec}")

def wybierz_kraj():
    print("Wybierz kraj z ktorego pochodzisz:")
    print("1. Polska")
    print("2. USA")
    print("3. Inny")

    wybor = input("Wprowadź numer (1, 2, 3): ")

    if wybor == "1":
        kraj = "Polska"
    elif wybor == "2":
        kraj = "USA"
    elif wybor == "3":
        kraj = "Inny"
    else:
        kraj = "brak danych"

    print(f"Wybrałeś kraj: {kraj}")

