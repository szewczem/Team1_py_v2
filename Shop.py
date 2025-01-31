from products import product_list
from app import ostrzezenie

class Shop:
    def __init__(self):
        self.wiek = self.pobierz_wiek()  # Pobranie wieku z walidacją
        self.sprawdz_wiek()  # Automatyczne sprawdzenie wieku po wprowadzeniu danych
        self.wyswietl_produkty()

    def pobierz_wiek(self):
        while True:
            wiek = input("Zanim rozpoczniesz zakupy w naszym sklepie, proszę podaj wiek kupującego: ")

            # Sprawdzamy, czy liczba jest całkowita
            if wiek.isdigit():
                wiek = int(wiek)

                # Jeśli wiek przekracza 100 lat, prosimy o ponowne podanie
                if wiek > 100:
                    print("Podany wiek przekracza 100 lat. Na pewno masz tyle?")
                    decyzja = input("Jeśli się pomyliłeś, wpisz swój wiek jeszcze raz. Jeśli nie, wpisz 'tak': ")
                    if decyzja.lower() != "tak":
                        try:
                            wiek = int(decyzja)  # Próbujemy zamienić nową wartość na liczbę całkowitą
                            return wiek  # Jeśli się udało, przyjmujemy nowy wiek
                        except ValueError:
                            print("Niepoprawna wartość. Wiek musi być liczbą całkowitą. Spróbuj ponownie.")
                            continue  # Powtarzamy pętlę

                return wiek  # Jeśli wiek jest OK, zwracamy go

            # Sprawdzamy, czy liczba jest niecałkowita (np. 18.5)
            try:
                if float(wiek) and not float(wiek).is_integer():
                    print("Podano liczbę niecałkowitą! Proszę podać wiek jako liczbę całkowitą.")
                    continue
            except ValueError:
                pass  # Jeśli nie można zamienić na float, to nie jest liczba

            print("Wiek musi być liczbą całkowitą. Spróbuj ponownie.")

    def sprawdz_wiek(self):

        if self.wiek < 18:
            print("Przykro nam, jesteś jeszcze na to za młody. Odwiedź nas później.")
        else:
            print("Witamy w naszym sklepie. Możesz kupować u nas energetyki.")

        ostrzezenie(self.wiek)


    def wyswietl_produkty(self):
        if self.wiek >= 18:
            print("Dostępne są następujące produkty: ")
            print(product_list)

