from products import product_list, Product
from random import randrange    # BlackScorpion Energy Drink GRATIS after guessing the number (shop event)


class Cart:
    def __init__(self):
        self.cart_list = []

    def __str__(self):
        return "\n".join(str(product) for product in self.cart_list)
    
    def add_to_cart(self, i):    # dodanie jednego produktu do listy
        self.cart_list.append(product_list.product_number(i))
        self.show_cart()
    
    def remove_from_cart(self, i):    # usuniecie produktu z listy
        self.cart_list.remove(self.product_number(i))
    
    def number_of_product(self):
        return len(self.cart_list)    

    def product_number(self, i):
        return self.cart_list[i]    

    def show_cart(self):
        print('\nTwój koszyk:')
        for i in range(self.number_of_product()):
            print(f"{i+1}:  {self.product_number(i)}")

    def total_price(self):
        total = 0
        for i in range(self.number_of_product()):
            total += self.product_number(i).price
        return total

    def game_gratis_drink(self):
        print('\nJako pełnoletni klient masz możliwość wygrania nagrody. Wygraj grę i odbierz gratis do zakupów!')

        def start_game(self):
            answer = input(
                'Zgadnij poprawną liczbę w maksymalnie 5 próbach, aby wygrać nagrodę. Czy chcesz zagrać w grę? [y/n]? ')
            if answer == 'y':
                numbers_game(self)
            else:
                print('Wyzwanie odrzucone.')

        def numbers_game(self):
            number = randrange(0, 101)
            # print(number)
            count = 1
            guess = int(input(
                f'\nZgadnij wylosowaną liczbę z przedziału od 0 do 100. Masz tylko 5 prób, powodzenia!\nPróba {count}: '))
            while count <= 5:
                if guess == number:
                    print('Zgadłeś! Wygrywasz BlackScorpion Energy Drink!')
                    self.add_to_cart(0)
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
        start_game(self)  