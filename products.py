#Klasy i metody dla produktów

class Product:

    def __init__(self, name, flavour, zero, price ):
        self.name :str = name # nazwa napoju
        self.flavour :str = flavour # smak
        self.zero :bool = zero # zero cukru
        self.price :int = price # cena napoju


    def __str__(self): # print klasy pokazuje nazwe/smak/zawartość cukru/cene
        sugar_status = "bez cukru" if self.zero else "z cukrem"
        return f"*{self.name:10} {self.flavour:13} {sugar_status:10} {self.price} PLN/szt."

    def __eq__(self, other):
        return (self.name == other.name and self.flavour == other.flavour and
                self.zero == other.zero and self.price == other.price)


    # gettery i settery (takie, które mogą się przydać, np. przy promocjach itp.):

    def get_price(self):
        return self.price
    def set_price(self, new_price :int):
        self.price = new_price
    def get_flavour(self):
        return self.flavour
    # miejsce na kolejne, jeśli będą potrzebne

class ProductList:
    def __init__(self):
        self.product_list = []

    def __str__(self): # wyświetlanie listy dla usera
        return "\n".join(str(product) for product in self.product_list)


    # dodanie jednego produktu do listy
    def add_product(self, new_product):
        self.product_list.append(new_product)

    #dodanie kilku produktów na raz do listy
    def add_products(self, new_products):
        self.product_list.extend(new_products)

    # usuniecie produktu z listy
    def remove_product(self, product_name):
        self.product_list.remove(product_name)


# przykładowy energetyk do testów:

energetyk_cytrynowy = Product("Energetyk","Cytrynowy",True,5)
energetyk_truskawkowy = Product("Energetyk","Truskawkowy",True,5)
energetyk_arbuzowy = Product("Energetyk","Arbuzowy",False,5)
energetyk_pomaranczowy = Product("Energetyk","Pomarańczowy",False,5)


product_list = ProductList()
product_list.add_products([energetyk_cytrynowy, energetyk_truskawkowy,
                              energetyk_arbuzowy, energetyk_pomaranczowy])
