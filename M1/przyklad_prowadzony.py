# przyklad_prowadzony.py — kalkulator zamówienia

nazwa_produktu = "Klawiatura"     # str
cena_jednostkowa = 149.99         # float
sztuki = 3                        # int

wartosc = cena_jednostkowa * sztuki   # float * int = float

print(f"Produkt: {nazwa_produktu}")
print(f"Cena jednostkowa: {cena_jednostkowa} PLN")
print(f"Liczba sztuk: {sztuki}")
print(f"Wartość zamówienia: {wartosc} PLN")

print("Typ zmiennej 'wartosc' to:", type(wartosc))