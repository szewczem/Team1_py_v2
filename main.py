from shop import Shop
from cart import Cart

# funkcja walidacyjna na podanie numeru produktu innego niż lista ale nie wiem jak zastosować...
def validate_product_nr():
    while True:
        try:
            item_num = int(input('\nPodaj numer produktu który chcesz dodać do koszyka: '))

            if item_num < 1 or item_num >= 5:
                print("Podano nieprawidłową wartość. Wpisz jedną z liczb dostępnych do wyboru.")
                continue

            else:
                break

        except ValueError:
            print("Podano nieprawidłową wartość. Wpisz jedną z liczb dostępnych do wyboru.")

def main():
    shop = Shop()
    if shop.enter == True:
        item_num = int(input('\nPodaj numer produktu który chcesz dodać do koszyka: '))
        cart = Cart()
        cart.add_to_cart(item_num)    
        cart.show_cart()

        while True:
            shopping = int(input('\nJeśli chcesz kontynuwać zakupy wpisz [1], jeśli chcesz edytować koszyk wpisz [2], jeśli chcesz zakończyć zakupy wpisz [3]: '))
            if shopping == 1:
                shop.wyswietl_produkty()
                item_num = int(input('\nPodaj numer produktu który chcesz dodać do koszyka: '))
                cart.add_to_cart(item_num)   
                cart.show_cart()
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

    else:
        pass


if __name__ == "__main__":
    main()