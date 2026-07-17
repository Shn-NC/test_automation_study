# przyklad_l1_2.py — parsowanie e-maila

email = "  Jan.Testowy@Example.COM  "

email = email.strip().lower()          # sprzątamy: spacje + małe litery
print(f"Znormalizowany: {email}")      # jan.testowy@example.com

pozycja_malpy = email.find("@")        # indeks znaku @
login = email[:pozycja_malpy]          # wszystko PRZED @
domena = email[pozycja_malpy + 1:]     # wszystko PO @

print(f"Login:  {login}")              # jan.testowy
print(f"Domena: {domena}")             # example.com
print(f"Długość loginu: {len(login)} znaków")
print(f"Czy to firmowy Example? {domena.startswith('example')}")