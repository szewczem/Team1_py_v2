wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18:
    print("Witamy w apce. Mozesz kupować u nas energetyki")

#task 1 wiek powyzej 120 lat
#dodatkowo wiek ponizej 18 lat

wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<=120:
    print("Witamy w apce. Mozesz kupować u nas energetyki")
elif wiek<18:
    print("Nie masz jeszcze 18 lat, nie kupisz u nas energetykow")
else:
    print("Masz ponad 120 lat, juz nie zyjesz")

