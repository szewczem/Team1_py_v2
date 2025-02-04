from functions import ostrzezenie
from products import product_list

class Shop:
    def __init__(self):
        self.wiek = input("Zanim rozpoczniesz zakupy w naszym sklepie, proszę podaj wiek kupującego: ")
        self.enter = False
        self.pobierz_wiek(self.wiek, self.enter)  # Pobranie wieku z walidacją
                

    def pobierz_wiek(self, wiek, enter):
        while True:
            # Sprawdzamy, czy liczba jest całkowita
            if wiek.isdigit():
                wiek = int(wiek)    
                if wiek > 0:            
                    self.sprawdz_wiek(wiek, enter)
                    break
            # Sprawdzamy, czy liczba jest niecałkowita (np. 18.5)
            try:
                if float(wiek) and not float(wiek).is_integer():
                    wiek = input("Podano liczbę niecałkowitą! Proszę podać wiek jako liczbę całkowitą: ")
                    continue
            except ValueError:
                # Jeśli nie można zamienić na float, to nie jest liczba
                wiek = input("Podawany wiek musi być liczbą całkowitą. Proszę podać swój wiek ponownie: ")
                self.pobierz_wiek(wiek, enter)
                break
            else:
                wiek = input("Wprowadzono niepoprawną wartość. Proszę podać swój wiek: ")
                continue


    def sprawdz_wiek(self, wiek, enter):
        if wiek < 18:
            print("Przykro nam, jesteś jeszcze na to za młody. Odwiedź nas później.")        
        # Jeśli wiek przekracza 100 lat, prosimy o ponowne podanie
        elif wiek > 100:
            decyzja = input("\nPodany wiek przekracza 100 lat. Na pewno masz tyle? [y/n]: ")
            if decyzja != "y":
                try:
                    wiek = int(input("Proszę podać swój wiek: "))  # Próbujemy zamienić nową wartość na liczbę całkowitą                      
                    self.sprawdz_wiek(wiek, enter)
                except ValueError:
                    wiek = input("Niepoprawna wartość. Wiek musi być liczbą całkowitą. Proszę podać swój wiek: ")
                    self.pobierz_wiek(wiek, enter)
            else:
                print("\nWitamy w naszym sklepie. Możesz kupować u nas energetyki.")       
                self.welcome(wiek, enter)
        else:
            print("\nWitamy w naszym sklepie. Możesz kupować u nas energetyki.")                
            self.welcome(wiek, enter)


    def wyswietl_produkty(self):
        print("\nDostępne są następujące produkty: ")
        for i in range(1,product_list.number_of_product()):
            print(f"{i}:  {product_list.product_number(i)}")

    
    def welcome(self, wiek, enter):
        self.enter = True         
        ostrzezenie(wiek) 
        self.wyswietl_produkty() 



