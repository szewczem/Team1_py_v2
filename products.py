#Klasy i metody dla produktów

class Product:

    def __init__(self, name, volume, flavour, zero, price ):
        self.name :str = name # nazwa napoju
        self.volume :int = volume # pojemność w ml
        self.flavour :str = flavour # smak
        self.zero :bool = zero # zero cukru
        self.price :int = price # cena napoju

    def __str__(self): # print klasy pokazuje nazwe/pojemność/smak/ zero cukru czy nie
        if self.zero:
            return f"{self.name} {self.volume} ml {self.flavour} zero cukru"
        else:
            return f"{self.name} {self.volume} ml {self.flavour}"

    # gettery i settery (takie, które mogą się przydać, np. przy promocjach itp.):

    def get_price(self):
        return self.price
    def set_price(self, new_price :int):
        self.price = new_price
    # miejsce na kolejne, jeśli będą potrzebne

# przykładowy energetyk do testów:

energetyk = Product("Energetyk", 250, "cytrynowy",False,5)

