# przyklad_l1_3.py — kolejka przypadków testowych

testy = ["logowanie", "koszyk", "płatność"]
print(f"Start: {testy} ({len(testy)} testów)")

testy.append("wylogowanie")        # dodaj na koniec (zwraca None, zmienia w miejscu)
testy.insert(0, "rejestracja")     # wstaw na początek
print(f"Po dodaniu: {testy}")

wykonany = testy.pop(0)            # zdejmij pierwszy I zapamiętaj, co to było
print(f"Wykonuję: {wykonany}")
print(f"Zostało: {testy}")

print(f"Czy jest 'koszyk'? {'koszyk' in testy}")   # membership -> bool

posortowane = sorted(testy)        # NOWA lista, oryginał nietknięty
print(f"Alfabetycznie: {posortowane}")
print(f"Oryginał bez zmian: {testy}")

# krotka + unpacking
konfiguracja = ("saucedemo.com", 443)
host, port = konfiguracja
print(f"Host: {host}, port: {port}")