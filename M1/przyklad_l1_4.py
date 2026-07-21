# przyklad_l1_4.py — raport z testów

wynik = {
    "suite": "regresja",
    "passed": 18,
    "failed": 3,
    "srodowisko": {"nazwa": "staging", "url": "https://staging.sklep.pl"}
}

print(f"Suite: {wynik['suite']}")                     # dostęp po kluczu
print(f"Środowisko: {wynik['srodowisko']['nazwa']}")  # zagnieżdżenie (JSON-owo)

total = wynik["passed"] + wynik["failed"]             # arytmetyka (L1.1)
print(f"Wykonano {total} testów, zdanych {wynik['passed']}")

# bezpieczny dostęp do klucza, którego może nie być
print(f"Czas trwania: {wynik.get('czas', 'nie zmierzono')}")

# zbiór: jakie różne statusy HTTP zaobserwowano
statusy_z_logu = [200, 200, 404, 500, 200, 404]
unikalne = set(statusy_z_logu)                        # {200, 404, 500}
print(f"Różne statusy: {unikalne} ({len(unikalne)} różnych)")
print(f"Czy był 500? {500 in unikalne}")