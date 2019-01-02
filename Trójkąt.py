# ZADANIE: Napisz program, który na podstawie danych pobranych od użytkownika, czyli długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt prostokątny. Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i pole, w przeciwnym wypadku komunikat, że nie da się utworzyć trójkąta.
# POJĘCIA: pętla for, obiekt, typ danych, metoda, lista, instrukcja warunkowa zagnieżdżona.

import math

operacja = "t" # deklarujemy i inicjujemy zmienną pomocniczą
while operacja != "n":  # dopóki wartość 'operacja' jest inna niż znak 'n'
    while True:
        try:
            dane = input("Podaj 3 boki trojkata (oddzielone przecinkami): ")

            lista = [] # definicja pustej listy
            for x in dane.split(","):
                lista.append(int(x)) # dodanie elementu do listy
            a,b,c = lista # rozpakowanie listy
            # wyrazenie listopwe, które zastępuje kod 10-13:
            # a,b,c = [int(x) for x in dane.split(",")]

            print("Podano boki: ",a,b,c)
            break
        except ValueError:
            print("Wprowadzone dane są niepoprawne. Spróbuj jeszcze raz")
            continue

    if a + b > c and a + c > b and b + c > a:   # warunek złożony
        print("Z podanych boków można zbudować trójkąt.")
        # czy boki spełniają warunki trójkąta prostokątnego?
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Do tego prostokątny!")

        # na wyjściu możemy wyprowadzić wyrażenia
        print("Obwód wynosi:",(a+b+c))
        p = 0.5 * (a+b+c) # obliczamy współczynnik wzoru Herona
        # liczymy pole ze wzoru Herona
        P = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Pole wynosi:",P)
        operacja = 'n' # ustawiamy zmienną na "n", aby wyjść z pętli while
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
        operacja = input("Spróbujesz jeszcze raz (t/n): ")

print("Do zobaczenia...")
    
