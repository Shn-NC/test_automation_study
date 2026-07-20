# 02_Kod\M1\L1_3_kolejka.py - Zarządzanie kolejką testów regresji

surowe = "logowanie;koszyk;platnosc;wylogowanie;koszyk"
testy = surowe.split(";")           # podzielenie wartości zmiennej 'surowe', używając średnika jako separatora, tworząc w ten sposób listę 'testy'
print(f"Testy: {testy} ({len(testy)} testów)")          # potwierdzenie utworzenia listy 'testy' i policzenie ilości elementów na liście
print(f"Czy jest 'płatność'? {'platnosc' in testy}")            # sprawdzenie czy element 'płatność' jest przypisana do listy 'testy' - rezultat: True/False (True w tym przypadku)
print(f"Ilość wystąpień 'koszyk': {testy.count('koszyk')}")             # policzenie wystąpnień wartości 'koszyk' na liście 'testy'. 
testy.append("rejestracja")             # użycie metody .append(x) aby dodać wartość 'rejestracja' na końcu listy
print(f"Testy po dodaniu 'rejestracja': {testy} ({len(testy)} testów)")             # potwierdzenie dodania 'rejestracja' na końcu listy metodą .append(x)
testy.insert(0, "smoke")            # użycie metody .insert(i, x) aby dodać wartość 'smoke' na początku listy, gdzie '0' to numer indeksu (i), 'smoke' to element listy (x)
print(f"Testy po dodaniu 'smoke': {testy} ({len(testy)} testów)")           # potwierdzenie dodania 'smoke' na pierwszym miejscu listy metodą .insert(i, x)
pierwszy = testy.pop(0)             # wyjęcie z listy elementu na pozycji indeksu: 0 (w naszym przypadku 'smoke')
print(f"Wykonuję jako pierwszy: {pierwszy}")            # potwierdzenie jaki element wyjęliśmy z listy 'testy' i przypisaliśmy do zmiennej 'pierwszy'
print(f"Lista po użyciu metody .pop(x): {testy}")          # Upewnienie się, że metoda .pop(x) usunęła z listy 'testy' element z indeksu x
print(f"Oryginalna nieposortowana lista: {testy}")          # lista jest taka sama jak wiersz wyżej, ale pokazuję, dla przejrzystości i spełnienia warunków zadania
print(f"Lista posortowana alfabetycznie: {sorted(testy)}")          # pokazanie listy posortowanej alfabetycznie metodą sorted(lista). Dla klarownosci, utworzenie nowej listy nowa_lista = stara_lista.sort() zaaplikuje sortowanie do starej listy
polaczone = ";".join(testy)         # metoda .join() - łączy elementy listy (testy) po separatorze ";" i przypisuje do zmiennej 'polaczone'
print(f"Sklejone elementy listy (z powrotem zmienna): {polaczone}")           # potwierdzenie, że lista została prawidłowo sklejona. Nowa wartość została przypisana do zmiennej 'polaczone'

# BONUS
srodowisko = ("staging", "https://staging.sklep.pl")            # utworzenie krotki (tuple) poprzez zastosowanie nawiasów okrągłych
nazwa_srod, url = srodowisko            # przypisanie zmiennych dla krotki
print(f"Nazwa środowiska: {nazwa_srod}; URL: {url}")            # wypisanie wartości zmiennych w krotce