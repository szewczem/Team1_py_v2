from products import product_list, Product

class Cart:
    def __init__(self):
        self.cart_list = []

    def __str__(self):
        return "\n".join(str(product) for product in self.cart_list)

    # dodanie jednego produktu do listy
    def add_to_cart(self, i):
        self.cart_list.append(product_list.product_number(i))

    # usuniecie produktu z listy
    def remove_from_cart(self, i):
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

