# L1_2_parser.py — Parser danych logowania

surowe = "   UserName: Szymon_QA | ID: 100742 | kraj: PL   "

surowe = surowe.strip()
pierwszy_dwukropek = surowe.find("UserName:") # indeks pierwszego dwukropka
drugi_dwukropek = surowe.find("ID:") # indeks drugiego dwukropka
trzeci_dwukropek = surowe.find("kraj:") # indeks trzeciego dwukropka
login = surowe[pierwszy_dwukropek + 10:surowe.find("|", pierwszy_dwukropek)].strip() # login
print(f"Login: {login} ({len(login)} znaków)") # Szymon_QA (9 znaków)
ladny_login = login.replace("_", " ") # zamiana podkreślnika na spację
print(f"Ładny login: {ladny_login}") # Ładny login: Szymon QA
id = surowe[drugi_dwukropek + 3:surowe.find("|", drugi_dwukropek)].strip() # ID
id = int(id) # konwersja na liczbę całkowitą
print(f"ID: {id} | Następne ID: {id + 1}") # ID: 100742 | Następne ID: 100743
id = str(id) # konwersja z powrotem na tekst
print(f"ID to same cyfry? {id.isdigit()}") # Czy ID jest liczbą: True
kod_kraju = surowe[trzeci_dwukropek + 5:].strip() # kod kraju
print(f"Kod kraju: {kod_kraju}") # Kod kraju: PL