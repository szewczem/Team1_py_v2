def wybierz_smak():
    print("Wybierz smak napoju energetycznego jaki chcesz kupić:")
    print("1. Cytrynowy")
    print("2. Truskawowy")
    print("3. Arbuzowy")
    print("4. Pomarańczowy")

    wybor = input("Wprowadź numer (1, 2, 3, 4): ")

    if wybor == "1":
        smak = "Cytrynowy"
    elif wybor == "2":
        smak = "Truskawowy"
    elif wybor == "3":
        smak = "Arbuzowy"
    elif wybor == "4":
        smak = "Pomarańczowy"
    else:
        return "Nie wybrano smaku. Zapraszamy ponownie."

    return f"Wybrałeś smak: {smak}. Przejdź dalej do wybrania ilości do zamówienia."

