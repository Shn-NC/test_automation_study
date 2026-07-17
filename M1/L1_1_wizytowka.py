imie = input("Podaj swoje imię: ")
wiek_text = input("Podaj swój wiek: ")
wiek = int(wiek_text)  # konwersja tekstu na liczbę całkowitą
wzrost_text = input("Podaj swój wzrost w metrach (np. 1.75): ")
wzrost = float(wzrost_text)  # konwersja tekstu na liczbę zmiennoprzecinkową
czy_pelnoletni = True
wiek_za_10_lat = wiek + 10

print("--- Wizytówka ---")
print(f"Imię: {imie}")
print(f"Wiek: {wiek} (za 10 lat): {wiek_za_10_lat}")
print(f"Wzrost: {wzrost} metrów")
print(f"Czy pełnoletni: {czy_pelnoletni}")

print("Typ zmiennej 'wiek' to:", type(wiek))
print("Typ zmiennej 'wzrost' to:", type(wzrost))