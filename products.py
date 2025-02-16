#Klasy i metody dla produktów

import json

class Product:
    def __init__(self, id, name, flavour, zero, price):
        self.id :int = id
        self.name :str = name
        self.flavour :str = flavour
        self.zero :bool = zero    # zero cukru
        self.price :int = price

    # data serialization
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "flavour": self.flavour,
            "zero": self.zero,
            "price": self.price
        }

    # data deserialization
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            name = data["name"],
            flavour = data["flavour"],
            zero = data["zero"],
            price = data["price"]
        )

    def __str__(self):    # print klasy pokazuje nazwe/smak/zawartość cukru/cene
        sugar_status = "bez cukru" if self.zero else "z cukrem"
        return f"{self.name:10} {self.flavour:13} {sugar_status:10} {self.price} PLN/szt."

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name and self.flavour == other.flavour and
                self.zero == other.zero and self.price == other.price)

    # gettery i settery (takie, które mogą się przydać, np. przy promocjach itp.):
    def get_price(self):
        return self.price
    
    def set_price(self, new_price :int):
        self.price = new_price

    # miejsce na kolejne, jeśli będą potrzebne


class ProductList:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.product_list = []

    def __str__(self):    # wyświetlanie listy dla usera
        return "\n".join(str(product) for product in self.product_list)
    
    def add_product(self, new_product):    # dodanie jednego produktu do listy
        self.product_list.append(new_product)
    
    def add_products(self, new_products):    # dodanie kilku produktów na raz do listy
        self.product_list.extend(new_products)
    
    def remove_product(self, product_name):    # usuniecie produktu z listy
        self.product_list.remove(product_name)

    def save_products(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([product.to_dict() for product in self.product_list], file, indent=4)

    def load_products(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

                if "Products" in json_data:
                    self.product_list = [Product.from_dict(product) for product in json_data["Products"]]
                else:
                    print("Error: 'Products key not found in JSON!")
                    self.product_list = []
        except FileNotFoundError:
            self.product_list = []

    def number_of_product(self):
        return len(self.product_list)
    
    def product_number(self, i):
        return self.product_list[i]


# przykładowy energetyk do testów:
#gratis = Product("BlackScorpion","Cola", True, 0)


product_list = ProductList()
product_list.load_products()


