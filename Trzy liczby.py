# ZADANIE: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.
# POJĘCIA: pętla while, obiekt, typ danych, metoda, instrukcja warunkowa zagnieżdżona.

operacja = "t"
while operacja == "t":  
    
    while True:
        try:
            a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").replace(',',' ').split(" ")
            print("Wprowadzono liczby: ", a,b,c)
            print("\nNajmniejsza: ")
            break
        except ValueError:
            print("Błędne dane! Spróbuj jeszcze raz...")
            continue

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    operacja = input("Jeszcze raz(t/n)? ")

print("Koniec!")
