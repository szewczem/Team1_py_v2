from shop import Shop
from cart import Cart
from client import Client, ClientsList


def main():
    shop = Shop()
    shop.welcome()
    shop.shopping()


if __name__ == "__main__":
    main()
