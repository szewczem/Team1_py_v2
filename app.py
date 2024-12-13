wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba calkowitą
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18:
    print("Witamy w apce. Mozesz kupować u nas energetyki")



# Alicja aprzychodzka // alicja.przychodzka@gmail.com  odradzenie dla osób +60 prozdrowotne

def wiek_60 (wiek):
    if wiek >= 60:
        print("Energetyki nie są rekomendowane dla osób 60+.")
    else:
        pass

wiek_60 (wiek) # wywołanie funkcji
