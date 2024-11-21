def check_50(wiek):
    if wiek > 50:
        print("Masz ponad 50 lat, uważaj na swoje zdrowie.")

wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
    check_50(wiek)
