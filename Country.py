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

wybierz_kraj()

#zrobione analogicznie do pliku z pytaniem o plec
#to jest na razie proste rozwiazanie do rozbudowania, na przyklad potrzebne jest uzupelnienie walidacji

#UWAGA!
#pozostaje do rozwiazania kwestia wieku pelnoletnosci w Polsce i USA (18/21 lat)
