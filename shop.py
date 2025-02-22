from functions import ostrzezenie
from products import product_list
from client import Client, ClientsList
from cart import Cart

class Shop:         
    def __init__(self, enter=False, clients_list="clients_list.txt"):
        self.enter = enter
        self.clients_list = ClientsList(clients_list)

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
                continue
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
                # print("\nWitamy w naszym sklepie. Możesz kupować u nas energetyki.")  
                self.enter = True     
                return self.enter
        else:
            # print("\nWitamy w naszym sklepie. Możesz kupować u nas energetyki.")                
            self.enter = True     
            return self.enter

    def wyswietl_produkty(self):
        print("\nDostępne są następujące produkty: ")
        for i in range(product_list.number_of_product()):
            print(f"{i + 1}:  {product_list.product_number(i)}")
    
    def welcome(self):        
        print("Zanim rozpoczniesz zakupy w naszym sklepie, proszę wprowadzić następujące dane: ")
        client_name = input("Podaj swoje imię bądź nick: ")
        client_age = input("Podaj swój wiek: ")        
        self.pobierz_wiek(client_age, self.enter)  # Pobranie wieku z walidacją
        if self.enter == True:
            client_gender = input("Podaj swoją płeć [F/M]: ")
            client = Client(client_name, client_age, client_gender)
            self.clients_list.add_to_clients_list(client)           
            ostrzezenie(int(client_age))             

    def shopping(self):
        self.wyswietl_produkty()
        item_num = int(input('\nPodaj numer produktu który chcesz dodać do koszyka: '))
        cart = Cart()
        cart.add_to_cart(item_num)

        while True:
            shopping = int(input('\nJeśli chcesz kontynuwać zakupy wpisz [1], jeśli chcesz edytować koszyk wpisz [2], jeśli chcesz zakończyć zakupy wpisz [3]: '))
            print("\033[H\033[J", end="")
            if shopping == 1:
                self.wyswietl_produkty()
                item_num = int(input('\nPodaj numer produktu który chcesz dodać do koszyka: '))
                cart.add_to_cart(item_num)
                continue
            elif shopping == 2:
                cart.show_cart()
                remove = int(input("\nWpisz [1] aby usunąć produkt z koszyka, wpisz [2] aby wrócić do sklepu: "))
                if remove == 1:
                    remove_num = int(input("Podaj numer produktu który chcesz usunąć z koszyka: "))
                    cart.remove_from_cart(remove_num-1)
                    cart.show_cart()
                    continue
            elif shopping == 3:
                cart.game_gratis_drink()                
                print(f"\nLiczba przedmiotów w koszyku: {cart.number_of_product()}, całkowita cena koszyka {cart.total_price()} PLN.")
                print("Dziękujemy za zakupy. Zapraszamy ponownie!\n")
                break
            else:
                print("Podano nieprawidłową wartość. Wpisz jedną z liczb dostępnych do wyboru.")