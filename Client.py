class Client:
    def __init__(self, wiek, plec, kraj, czy_moze_kupic, czy_wygral, czy_bez_cukru):
        self.wiek = wiek #na podstawie finalnego wyniku z zapytania o wiek
        self.plec = plec #na podstawie finalnego wyniku z zapytania o plec
        self.kraj = kraj #na podstawie wyniku z zapytania o kraj, nie pytalismy o to, dodalem wybor kraju jako oddzielny plik, na razie proste rozwiazanie do rozbudowania
        self.czy_moze_kupic :bool = czy_moze_kupic #na podstawie wyniku sprawdzenia wieku
        self.czy_wygral :bool = czy_wygral #na podstawie wyniku z funkcji numbers_game
        self.czy_bez_cukru: bool = czy_bez_cukru #na podstawie wyniku z funkcji promocja_zero

    def czy_moze_kupic(self):
        if self.wiek >= 18:
            return True
        else:
            return False

    def czy_wygral(self):
        if ...:
            return True
        else:
            return False

    def czy_bez_cukru(self):
        if ...:
            return True
        else:
            return False

