# ZADANIE: Pobierz od użytkownika imię, wiek i powitaj go komunikatem: “Mów mi Python, mam x lat. Witaj w moim świecie imie. Jesteś starszy(młodszy) ode mnie.”
# POJĘCIA: zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz.

# deklarujemy i inicjalizujemy zmienne
aktRok = 2019
pythonRok = 1989
# obliczamy wiek Pythona
wiekPython = aktRok - pythonRok

# pobieramy dane
imie = input("Jak się zazywasz?\n")
wiek = int(input("Ile masz lat?\n"))

# wyświetlamy komunikat
print("Witaj!", imie)
print("Mów mi Python, mam", wiekPython, "lat.")

# instrukcja warunkowa
if wiek > wiekPython:
    print("Jesteś starszy ode mnie.")
else:
    print("Jesteś młodszy ode mnie.")
    
                 
