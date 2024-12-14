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
# Wywołanie funkcji
wybierz_plec()

