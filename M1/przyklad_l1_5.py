# Walidator pojedynczego wpisu z raportu wykonania testów

wpis = "TC-107;FAIL;12.4"

# 1. Rozbicie na części (L1.2/L1.3)
czesci = wpis.split(";")
print("Części:", czesci, "| liczba pól:", len(czesci))

# 2. Walidacja strukturalna — sprawdzamy ZANIM sięgniemy po indeksy
if len(czesci) != 3:
    print("BŁĄD: wpis musi mieć dokładnie 3 pola")
else:
    tc_id = czesci[0].strip()
    status = czesci[1].strip().upper()
    czas_txt = czesci[2].strip()

    # 3. Walidacja ID — dwa warunki połączone AND
    if tc_id.startswith("TC-") and tc_id[3:].isdigit():
        print(f"ID poprawne: {tc_id}")
    else:
        print(f"ID niepoprawne: {tc_id}")

    # 4. Walidacja statusu — przynależność do zbioru dopuszczalnych wartości
    dozwolone = {"PASS", "FAIL", "SKIP"}
    if status in dozwolone:
        print(f"Status poprawny: {status}")
    else:
        print(f"Status spoza słownika: {status}")

    # 5. Konwersja czasu z zabezpieczeniem (short-circuit chroni float())
    if czas_txt.replace(".", "", 1).isdigit():
        czas = float(czas_txt)

        # 6. Kaskada elif — kolejność OD NAJWĘŻSZEGO warunku
        if czas < 1:
            kategoria = "szybki"
        elif czas < 10:
            kategoria = "normalny"
        elif czas < 60:
            kategoria = "wolny"
        else:
            kategoria = "krytycznie wolny"

        print(f"Czas: {czas}s -> {kategoria}")

        # 7. Ternary
        flaga = "DO ANALIZY" if status == "FAIL" or czas >= 60 else "OK"
        print(f"Flaga: {flaga}")
    else:
        print(f"Czas nie jest liczbą: {czas_txt}")    