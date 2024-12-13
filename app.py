wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<120:
    print("Witamy w apce. Mozesz kupować u nas energetyki")

# naprawa błędów i braków walidacji
if wiek <18:
    print ("Przepraszamy, nie sprzedajemy energetyków niepełnoletnim")
elif wiek>120:
    print("Podany wiek przekracza 120 lat, na pewno masz tyle?")
else:
    pass