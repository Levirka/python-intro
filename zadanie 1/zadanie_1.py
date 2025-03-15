#opis funkcji wbudowanej z()
#Funkcja zip() łączy elementy z kilku iterowalnych obiektów (np. list, krotek) w pary, trójki itd., aż do wyczerpania najkrótszej sekwencji.

#opis modułu z biblioteki standardowej math
#Moduł math zawiera funkcje matematyczne, takie jak pierwiastki, logarytmy, trygonometrię i stałe matematyczne.

#opis wyjątku ValueError

import math  # Moduł matematyczny: https://docs.python.org/3/library/math.html

# Tworzenie dwóch list
numbers = [1, 2, 3, 4, 5]
names = ["Ala", "Bartek", "Celina", "Dawid", "Ewa"]

# Łączenie list funkcją zip(): https://docs.python.org/3/library/functions.html#zip
zipped_list = list(zip(numbers, names))
print("Połączone listy:", zipped_list)

# Wykorzystanie funkcji sqrt() z modułu math
try:
    num = int(input("Podaj liczbę do obliczenia pierwiastka: "))
    result = math.sqrt(num)  # Obliczanie pierwiastka kwadratowego
    print(f"Pierwiastek kwadratowy z {num} wynosi {result}")
except ValueError:
    print("Błąd: Podana wartość nie jest liczbą lub jest ujemna!")  # Obsługa wyjątku

# Dokumentacja wyjątku ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
